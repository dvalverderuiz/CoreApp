# 🛡️ SafeSend – Analitzador Preventiu de Seguretat
### *Data Loss Prevention & Malware Pre-Scan Engine*

<p align="center">
  <img src="logo_safesend.png" alt="SafeSend Logo" width="250">
</p>

<p align="center">
  <strong>SafeSend</strong> és una solució avançada de <b>ciberseguretat desenvolupada en Python</b>, dissenyada per actuar com una <i>“duana digital”</i> en entorns corporatius.<br>
  L’eina analitza arxius abans del seu enviament o compartició per <b>mitigar riscos de fuga d’informació (DLP)</b> i <b>entrada de programari maliciós</b>.
</p>

<p align="center">
  🔐 Prevenció DLP · 📊 Risk Scoring · 🧠 Heurístiques · 📄 Informes JSON · 🖥️ GUI Professional
</p>

---

## 🚦 Estat del Projecte

> [!IMPORTANT]
> **VERSIÓ RELEASE – v1.0** ✅  
> Projecte en estat **madur i funcional**, superada la fase Alpha.  
>
> Aquesta versió incorpora un **motor de decisió quantitatiu basat en Risk Scoring**, amb mecanismes d’escalat automàtic per reduir falsos negatius i aproximar el comportament del sistema a solucions **professionals de Data Loss Prevention (DLP)**.

---

## 🧬 Evolució i Millores Tècniques (Post-Alpha)

L’objectiu principal d’aquesta iteració ha estat **incrementar la precisió**, **reduir falsos negatius**, **millorar la interpretabilitat dels resultats** i **apropar el sistema a entorns DLP reals**.

### 🔧 Millores Clau Implementades

- ✅ **Motor de decisió quantitatiu**
  - Substitució de regles booleanes per un **sistema de puntuació de risc (0–100)**.
  - Justificació matemàtica del veredicte final.

- ✅ **Gestió avançada de deteccions sensibles**
  - Escalat automàtic del risc davant credencials, contrasenyes o acumulació d’amenaces.

- ✅ **Heurística d’ofuscació i xifrat**
  - Detecció de contingut potencialment xifrat mitjançant **entropia de Shannon (> 7.5)**.

- ✅ **Classificació per naturalesa d’arxiu**
  - 📄 Arxius de text
  - 📑 Documents (.pdf, .docx)
  - ⚙️ Arxius binaris

- ✅ **Persistència individualitzada**
  - Generació d’informes **JSON independents** identificats pel prefix del **hash SHA-256**.

---

## 📊 Motor d’Anàlisi i Risk Scoring

La puntuació de risc es calcula mitjançant una **suma ponderada de factors**, amb un límit màxim de **100 punts**.

### ⚖️ Taula de Penalitzacions

| 🔍 Factor d’Anàlisi | Impacte | Descripció |
|---|---|---|
| 🧨 Extensió bloquejada | **+40 punts** | Executables o scripts (.exe, .bat, etc.) |
| 📭 Arxiu buit | **+30 punts** | Possible anomalia o evasió |
| 🔐 Entropia elevada | **+25 punts** | Entropia de Shannon > 7.5 |
| 📦 Tamany excedit | **+20 punts** | Fitxers superiors a 25MB |
| 🧾 Dades sensibles | **+10 punts / detecció** | DNI, Email, IBAN, etc. |

---

## 🛡️ Regles de Seguretat d’Escalat (Anti-Falsos Negatius)

1. 🔒 **Penalització mínima**
   - Qualsevol detecció sensible → **mínim 30 punts**

2. 🚨 **Deteccions crítiques**
   - Credencials o contrasenyes → **mínim 60 punts**

3. 🔥 **Acumulació d’amenaces**
   - 2 o més deteccions → **mínim 70 punts (Sospechoso)**

---

## 🔴 Nivells de Classificació Final

| Score | Classificació | Estat |
|---|---|---|
| 0 – 29 | 🟢 **Seguro** | Només si no conté dades sensibles |
| 30 – 69 | 🟠 **Revisión necesaria** | Requereix validació manual |
| 70 – 100 | 🔴 **Sospechoso** | Risc elevat |

---

## 🔍 Gestió Avançada de l’Avaluació

Amb l’objectiu de reduir falsos negatius i augmentar la fiabilitat del sistema, la versió **v1.0 de SafeSend** incorpora un conjunt de mecanismes avançats que permeten contextualitzar millor l’anàlisi, interpretar correctament les deteccions i millorar la traçabilitat dels resultats obtinguts.

### 📂 Classificació del tipus d’arxiu

El sistema incorpora una funcionalitat de **classificació prèvia dels arxius segons la seva naturalesa**, fet que permet aplicar heurístiques adaptades al tipus de contingut analitzat i justificar millor els resultats obtinguts.

Els arxius es classifiquen en les següents categories:

- **Arxius de text** (ex: `.txt`, `.csv`):  
  Analitzats en profunditat mitjançant la detecció de patrons sensibles (regex) i el càlcul de l’entropia de Shannon. Aquest tipus d’arxiu és especialment rellevant en la detecció de dades personals o confidencials en clar.

- **Documents** (ex: `.pdf`, `.docx`):  
  Identificació d’estructures pròpies de documents corporatius. Aquesta classificació permet contextualitzar el contingut i aplicar penalitzacions de forma més coherent amb l’ús habitual d’aquest tipus d’arxius en entorns professionals.

- **Arxius binaris**:  
  Tractament específic orientat a arxius compilats o executables, on l’anàlisi de contingut textual no és fiable. Aquesta distinció evita interpretacions errònies de l’entropia i reforça la detecció d’arxius potencialment perillosos.

Aquesta classificació contribueix a una **avaluació més precisa i realista del risc**, alineada amb bones pràctiques en sistemes de seguretat de la informació.

---

### 🔐 Detecció de contingut potencialment xifrat o ofuscat

Com a millora respecte a la versió inicial, SafeSend incorpora una **heurística avançada per detectar contingut potencialment xifrat o ofuscat** sense recórrer a tècniques criptogràfiques complexes.

En el cas dels **arxius de text**, es calcula el valor de l’**entropia de Shannon**. Quan aquest valor supera el llindar establert (**> 7.5**), el sistema genera una detecció específica que indica la possible presència de contingut xifrat o ofuscat.

Aquest comportament pot ser indicatiu de:
- Intent d’ocultació d’informació sensible
- Dades xifrades prèviament al seu enviament
- Ús de tècniques bàsiques d’ofuscació per evadir mecanismes de detecció

Aquesta heurística aporta un **nivell addicional de seguretat**, reforçant la capacitat del sistema per detectar situacions potencialment anòmales en arxius aparentment inofensius.

---

### 🧾 Persistència i gestió d’informes

La **traçabilitat** és un pilar fonamental de la versió **v1.0** de SafeSend. Com a evolució de la versió alfa, el sistema genera ara **informes JSON individuals per a cada arxiu analitzat**, en lloc d’un únic registre genèric.

Cada informe:
- Es guarda en format **JSON**
- S’identifica mitjançant un **prefix del hash SHA-256** de l’arxiu analitzat
- Inclou totes les dades rellevants de l’anàlisi (deteccions, entropia, puntuació i classificació final)

Aquest enfocament facilita:
- L’**auditoria de seguretat**
- L’**anàlisi històrica** de fitxers
- La traçabilitat d’accions en entorns corporatius
- Futures ampliacions orientades a sistemes de monitorització o SIEM

Aquesta millora apropa el comportament del sistema a solucions professionals de **Data Loss Prevention (DLP)** i reforça la seva utilitat tant en contextos acadèmics com en entorns reals.

---

## 🖥️ Interfície Gràfica (GUI)

La interfície ha estat redissenyada per oferir una experiència **professional i clara**:

1. 📁 Identificació de l’arxiu  
2. 🧮 Característiques tècniques  
3. 🔍 Resultats de l’anàlisi  
4. 📊 Risk Score  
5. 🚦 Veredicte visual per colors  

---

## 🏗️ Arquitectura i Disseny

### 📁 Estructura de Mòduls

- `main.py` → Punt d’entrada
- `gui.py` → Interfície Tkinter
- `scan.py` → Hash i entropia
- `rules.py` → Patrons i constants
- `report.py` → Informes JSON

## 🚀 Instal·lació i Execució
1. Assegureu-vos de tenir instal·lat **Python 3.x**.
2. Cloneu el repositori i instal·leu les dependències necessàries.
3. Executeu el programa des de la terminal:
   ```bash
   python src/main.py

---

## 🧠 Conclusions Finals

Les ampliacions implementades en la versió **v1.0** han permès transformar **SafeSend** d’una eina alfa funcional en una **solució madura i robusta**, alineada amb els principis bàsics de la **seguretat de la informació** i la **prevenció de fuga de dades (DLP)**.

La introducció d’un **sistema de puntuació de risc (Risk Scoring)**, combinat amb regles d’escalat automàtic davant deteccions sensibles i crítiques, ha reduït significativament els **falsos negatius** i ha millorat la **fiabilitat** del veredicte final. Aquest enfocament permet una avaluació **gradual, quantitativa i justificable** del risc associat a cada arxiu analitzat.

A més, la incorporació d’heurístiques avançades com la detecció de **contingut potencialment xifrat mitjançant entropia**, la **classificació per tipus d’arxiu** i la **persistència individualitzada d’informes JSON** reforça la traçabilitat, la interpretabilitat dels resultats i l’auditoria del sistema.

Com a resultat, **SafeSend** es presenta com una eina **coherent, extensible i preparada per futures ampliacions**, adequada tant per a **finalitats acadèmiques** com com a base per a **solucions reals de prevenció de fuga d’informació en entorns corporatius**.

---

*Desenvolupat per l'Equip G11 (Marc Rovira, David Valverde i Miquel Burguera) per a l'assignatura de Productivitat - ENTI UB.*
