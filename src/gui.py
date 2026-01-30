# src/gui.py
import tkinter as tk
from tkinter import filedialog, messagebox

from scan import analyze_file
from report import save_report

def launch_gui():
    root = tk.Tk()
    root.title("EnvioSeguro – Analizador de archivos")
    root.geometry("1000x400")
    root.resizable(False, False)

    # FUNCIONES INTERFAZ
    def select_file():
        path = filedialog.askopenfilename(title="Selecciona un archivo para analizar")
        if not path:
            return
        result = analyze_file(path)
        update_ui(result)
        save_path = save_report(result)
        messagebox.showinfo("Guardado", f"Informe guardado en:\n{save_path}")

    def update_ui(result):
        txt_output.delete("1.0", tk.END)

        # Identificación del archivo
        txt_output.insert(tk.END, f"📂 Archivo: {result['file']}\n")
        txt_output.insert(tk.END, f"🔢 Hash SHA256: {result['hash']}\n")

        # Características básicas
        txt_output.insert(tk.END, f"📏 Tamaño: {result['size_mb']} MB\n")
        txt_output.insert(tk.END, f"📄 Extensión: {result['extension']}\n")
        txt_output.insert(tk.END, f"📁 Tipo de archivo: {result.get('type', 'Desconocido')}\n")

        # Análisis de contenido
        txt_output.insert(tk.END, f"🎯 Entropía: {result['entropy']}\n")
        txt_output.insert(tk.END, f"🧩 Detecciones: {result['detections']}\n")

        # Evaluación de riesgo
        txt_output.insert(tk.END, f"📊 Puntuación de riesgo: {result.get('risk_score', 0)} / 100\n")
        txt_output.insert(tk.END, f"⚠️ Clasificación final: {result['risk']}\n")

        color = {
            "Seguro": "lightgreen",
            "Revisión necesaria": "orange",
            "Sospechoso": "red",
            "Error": "gray"
        }.get(result["risk"], "lightgray")
        lbl_status.config(text=result["risk"], bg=color)

    
    # INTERFAZ GRÁFICA
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill="both", expand=True)

    btn_select = tk.Button(frame, text="Seleccionar archivo", command=select_file)
    btn_select.pack(pady=10)

    lbl_status = tk.Label(frame, text="Sin análisis", bg="lightgray",
                          font=("Arial", 14), width=20)
    lbl_status.pack(pady=10)

    txt_output = tk.Text(frame, height=12, width=120, wrap="word")
    txt_output.pack()

    root.mainloop()
