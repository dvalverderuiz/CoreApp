# SafeSend: Analitzador Preventiu de Seguretat 🛡️

<p align="center">
  <img src="logo_safesend.png" alt="SafeSend Logo" width="300">
</p>

**SafeSend** és una solució de programari modular desenvolupada en Python dissenyada per enfortir la seguretat en entorns corporatius. L'eina se centra a mitigar els riscos derivats de la manipulació de fitxers per part d'usuaris sense formació tècnica específica, proporcionant un diagnòstic clar sobre la perillositat dels documents abans que siguin enviats o executats.

---

> [!IMPORTANT]
> **ESTAT DEL PROJECTE: VERSIÓ ALPHA** ⚠️
> Aquesta versió representa la primera fita funcional del producte. S'ha implementat l'arquitectura modular inicial, l'ús de fitxers de text i la integració de llibreries externes. El codi està sota desenvolupament actiu cap a la versió final (Release).

---

## 📋 Propòsit i Aplicabilitat
L'objectiu principal és oferir una capa de protecció preventiva per evitar la filtració de dades sensibles o l'entrada de programari maliciós. SafeSend transforma dades tècniques complexes (com hashes o entropia) en un veredicte de risc fàcilment comprensible per a qualsevol treballador de l'empresa.

## ✨ Funcionalitats de la Versió Alpha
* **Arquitectura Modular:** Organització del codi en carpetes especialitzades (`src/`, `data/`, `logs/`).
* **Verificació d'Integritat:** Implementació del càlcul de hash per garantir que els fitxers no han estat alterats.
* **Anàlisi de Metadades:** Validació d'extensions i càlcul de mida per detectar suplantacions.
* **Gestió de Registres:** Ús de fitxers de text per emmagatzemar logs d'activitat i configuracions.
* **Integració Externa:** Ús de llibreries especialitzades instal·lades mitjançant `pip` per potenciar l'anàlisi.

## 🚀 Requisits i Instal·lació
El projecte requereix **Python 3.x** i l'ús de l'entorn virtual configurat amb les dependències necessàries.

## 🛠️ Instruccions d'Execució
Per posar en marxa l'analitzador en aquesta fase Alpha, seguiu aquests passos:

1. **Accedir al directori del projecte:** Obriu la terminal a la carpeta arrel del repositori.
2. **Executar el programa:** El fitxer principal d'entrada es troba a la carpeta `src/`. Executar-lo amb la següent comanda:
   ```bash
   python src/main.py
