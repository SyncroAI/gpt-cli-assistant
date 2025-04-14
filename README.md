# 🤖 GPT CLI Assistant

Ein schlanker, lokaler OpenAI-Chat-Assistent für dein Terminal – komplett mit Sessions, Zusammenfassungen & Einstellungsmenü.

## ✨ Features

- 🧠 Lokaler Verlauf in Markdown (`chat_logs/`)
- 🗂️ Beliebig viele Sessions – automatisch gespeichert
- 📝 Automatische Zusammenfassungen deiner Gespräche
- ⚙️ Einstellbares Verhalten direkt im Terminal:
  - Modellwahl (GPT-3.5 oder GPT-4)
  - Max. Tokens für Zusammenfassungen
  - Zusammenfassung an-/ausschalten
- 🖇️ Optional: Symlink-Integration → `gpt` von überall im Terminal starten

---

## 📦 Installation

### 1. Repository klonen

```bash
git clone https://github.com/SyncroAI/gpt-cli-assistant.git
cd gpt-cli-assistant
2. Python-Umgebung & Abhängigkeiten installieren
bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
3. API-Key setzen
Erstelle eine Datei .env mit folgendem Inhalt:

dotenv
Copy
Edit
OPENAI_API_KEY=dein-api-key-hier
🔐 API-Key bekommst du hier: https://platform.openai.com/account/api-keys

🚀 Optional: Als Befehl gpt systemweit nutzen
Erstelle einen Symlink, damit du den Chat einfach mit gpt starten kannst:

bash
Copy
Edit
sudo ln -s /voller/pfad/zum/projekt/script/start.sh /usr/local/bin/gpt
Beispiel:

bash
Copy
Edit
sudo ln -s ~/git/gpt-cli-assistant/script/start.sh /usr/local/bin/gpt
Dann kannst du einfach loslegen:

bash
Copy
Edit
gpt
💬 Nutzung
bash
Copy
Edit
gpt
Dann erscheint das Menü:

csharp
Copy
Edit
[GPT] Modell wählen:
[1] GPT-4
[2] GPT-3.5
[3] ⚙️ Einstellungen ändern
Nach Modellwahl:

csharp
Copy
Edit
[GPT] Verfügbare Sessions:
[1] letzte-session
[2] ➕ Neue Session starten
Beispielhafte Unterhaltung:

text
Copy
Edit
[Du]: Wie baue ich eine PostgreSQL-Abfrage?
[GPT]: Du kannst z. B. folgendes nutzen: ...
⚙️ Einstellungen ändern
Über [3] ⚙️ Einstellungen ändern kannst du während der Session:

maximale Tokens für Zusammenfassungen setzen

Zusammenfassungen deaktivieren

Intervall der Zusammenfassungen ändern

📁 Verläufe & Zusammenfassungen
Alle Chats werden im Ordner chat_logs/ gespeichert:

text
Copy
Edit
chat_logs/
├── mein_chat.md              # Vollständiger Chatverlauf (Markdown)
└── mein_chat.summary.txt     # Letzte Zusammenfassung (reine Textdatei)
🧨 Kommende Features (optional)
Du kannst bald nutzen:

bash
Copy
Edit
gpt --list      # zeigt alle gespeicherten Sessions
gpt --delete xy # löscht Session xy
✅ Voraussetzungen
Python 3.7+

OpenAI API-Key

Linux/macOS-Terminal

🧠 Idee & Umsetzung
Dieses Projekt entstand aus einer Idee für einen persönlichen, schnellen Terminal-Assistenten – ohne Chat-Verlauf bei OpenAI, lokal speichernd & flexibel.

Built with Liebe, Terminal-Hackerei & ein bisschen Wahnsinn 🧪

📜 Lizenz
MIT License – feel free to fork, verbessern, teilen.

💖 Support & Mitmachen
Wenn du’s nützlich findest:

⭐ Star da lassen
🍴 Forken & erweitern
📢 Spread the Word

Made with ❤️ by SyncroAI
