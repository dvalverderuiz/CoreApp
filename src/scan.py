# src/scan.py
import os
import re
import math
import hashlib
from rules import PATTERNS, BLOCKED_EXTENSIONS, MAX_FILE_SIZE_MB

def classify_file(ext: str) -> str:
    if ext in [".txt", ".csv", ".md"]:
        return "Texto"
    if ext in [".pdf", ".docx", ".xlsx"]:
        return "Documento"
    return "Binario"


def calculate_hash(path: str) -> str:
    """Devuelve el hash SHA256 de un archivo."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


def calculate_entropy(data: bytes) -> float:
    """Calcula la entropía Shannon de los datos."""
    if not data:
        return 0.0
    freq = {b: data.count(b) / len(data) for b in set(data)}
    return -sum(p * math.log2(p) for p in freq.values())


def detect_sensitive_data(text: str):
    """Busca patrones sensibles en el texto."""
    detections = []
    for name, pattern in PATTERNS.items():
        if re.search(pattern, text):
            detections.append(name)
    return detections


def analyze_file(path: str) -> dict:
    """
    Analiza un archivo y devuelve un diccionario con los resultados:
    - hash, tamaño, extensión, detecciones, entropía, riesgo
    """
    result = {"file": path}
    try:
        # Hash y tamaño
        result["hash"] = calculate_hash(path)
        size_mb = os.path.getsize(path) / (1024 * 1024)
        result["size_mb"] = round(size_mb, 2)
        ext = os.path.splitext(path)[1].lower()
        result["extension"] = ext
        result["type"] = classify_file(ext)

        # Comprobar tamaño y extensión
        blocked = ext in BLOCKED_EXTENSIONS
        oversize = size_mb > MAX_FILE_SIZE_MB

        # Leer contenido textual (si posible)
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            detections = detect_sensitive_data(text)
            entropy = calculate_entropy(text.encode("utf-8"))
            if entropy > 7.8 and ext in [".txt", ".csv"]:
                detections.append("posible_contenido_cifrado")

        except Exception:
            detections = []
            entropy = 0.0

        result["detections"] = detections
        result["entropy"] = round(entropy, 2)

        # Evaluar riesgo
        score = 0
        if blocked:
            score += 40
        if oversize:
            score += 20
        if entropy > 7.5:
            score += 25
        score += len(detections) * 10
        if size_mb == 0:
            score += 30

        # Riesgo critico (detecciones sensibles)
        if detections:
            score = max(score, 30)

        CRITICAL_DETECTIONS = ["password", "contraseña"]
        if any(d in CRITICAL_DETECTIONS for d in detections):
            score = max(score, 60)

        if len(detections) >= 2:
            score = max(score, 70)

        score = min(score, 100)

        # Evaluar riesgo final
        if score >= 70:
            risk = "Sospechoso"
        elif score >= 30:
            risk = "Revisión necesaria"
        else:
            risk = "Seguro"

        result["risk_score"] = score
        result["risk"] = risk


    except Exception as e:
        result["error"] = str(e)
        result["risk"] = "Error"

    return result
