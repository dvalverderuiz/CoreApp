# src/report.py
import json
import os
from datetime import datetime

def save_report(result, filename=None):
    if filename is None:
        filename = f"report_{result['hash'][:8]}.json"

    os.makedirs("results", exist_ok=True)
    path = os.path.join("results", filename)

    
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = []
    else:
        data = []

    
    entry = {"timestamp": datetime.now().isoformat(), **result}
    data.append(entry)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return path
