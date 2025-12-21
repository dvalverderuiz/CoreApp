# rules.py
PATTERNS = {
    "dni": r"\b\d{8}[A-Z]\b",
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "password": r"(?i)(contraseña|password|clave)\s*[:=]\s*\S+",
    "iban": r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b"
}

BLOCKED_EXTENSIONS = [".exe", ".bat", ".cmd", ".sh", ".vbs"]
MAX_FILE_SIZE_MB = 25