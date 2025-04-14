# GPT-Assistant (CLI Tool)

Ein terminalbasiertes CLI-Tool zur Interaktion mit OpenAI GPT-3.5 und GPT-4 – lokal, einfach, effizient.

---

## Funktionen

- **Chat-Verwaltung mit Sessions**  
  Erstelle, öffne und verwalte verschiedene Chat-Sessions direkt im Terminal.

- **Modellwahl**  
  Nutze GPT-3.5 oder GPT-4, je nach Bedarf.

- **Automatische Zusammenfassungen**  
  Nach einer bestimmten Anzahl von Nachrichten wird automatisch eine Zusammenfassung erstellt.

- **Markdown-Speicherung**  
  Alle Gespräche werden lokal als `.md` gespeichert – perfekt zur Archivierung, Nachbearbeitung oder Weitergabe.

- **Einstellbare Parameter**  
  Passe max. Tokens, Zusammenfassungsintervall u.v.m. direkt über das Terminal an.

---

## Datenstruktur

- `chat_logs/session_name.md` → Dein Chatverlauf im Markdown-Format  
- `chat_logs/session_name.summary.txt` → Automatisch generierte Zusammenfassung  
- `.env` → API-Key und andere Umgebungsvariablen (nicht ins Git hochladen!)  

---

## Installation

1. **Repository klonen**

```bash
git clone https://github.com/SyncroAI/gpt-assistant-cli.git
cd gpt-assistant-cli
```

2. **Abhängigkeiten installieren**

```bash
pip install -r requirements.txt
```

3. **API-Key einrichten**

Erstelle eine `.env` Datei mit folgendem Inhalt:

```env
OPENAI_API_KEY=dein-openai-api-key
```

4. **(Optional) Symlink erstellen**

Damit du das Tool von überall mit `gpt` starten kannst:

```bash
sudo ln -s /voller/pfad/zum/script/gpt_chat.py /usr/local/bin/gpt
```

> Beispiel:
> ```bash
> sudo ln -s /home/user/gpt-assistant-cli/gpt_chat.py /usr/local/bin/gpt
> ```

---

## Anwendung

Nach erfolgreicher Einrichtung kannst du einfach im Terminal `gpt` eingeben:

```bash
gpt
```

Dann stehen dir interaktive Menüs zur Verfügung:
- Neue Session starten oder bestehende auswählen
- Modell auswählen (GPT-3.5 oder GPT-4)
- Einstellungen anpassen (Token-Limit, Zusammenfassungen, etc.)

---

## Beispielhafte Nutzung

```bash
# Session starten
> gpt

# Eingabebeispiel
Du: Erkläre mir Quantenverschränkung in einfachen Worten.
GPT: ...

# Zusammenfassung erscheint automatisch nach z. B. 10 Nachrichten
```

---

## To-Do / Ideen für die Zukunft

- Interaktive Session-Verwaltung (z. B. zum Löschen, Umbenennen)
- Erweiterte Konfiguration via YAML oder JSON
- Statistiken über Token-Verbrauch
- Exportfunktionen (PDF, HTML)
- Backup-/Archivierungssystem

---

## Mitmachen & Feedback

Pull Requests, Feature-Ideen und Feedback sind herzlich willkommen!  
Wenn dir das Tool gefällt, gib ihm gerne einen Stern auf GitHub!

---

**Lizenz:** MIT © SyncroAI 

