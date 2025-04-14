import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ==== SETTINGS ====
SESSION_DIR = "chat_logs"
SUMMARY_EXTENSION = ".summary.txt"
MARKDOWN_EXTENSION = ".md"

# ==== GLOBAL SETTINGS (werden durch Einstellungen überschrieben) ====
settings = {
    "max_tokens": 500,
    "summarize_every": 5,
    "enable_summary": True
}


# ==== UTILS ====
def list_sessions():
    if not os.path.exists(SESSION_DIR):
        return []
    return [f.replace(MARKDOWN_EXTENSION, "") for f in os.listdir(SESSION_DIR) if f.endswith(MARKDOWN_EXTENSION)]

def load_file(path):
    return open(path, "r", encoding="utf-8").read() if os.path.exists(path) else ""

def save_file(path, content, mode="a"):
    with open(path, mode, encoding="utf-8") as f:
        f.write(content.strip() + "\n")

def build_messages_from_markdown(md_text):
    lines = md_text.splitlines()
    messages = []
    for line in lines:
        if line.startswith("**User:**"):
            messages.append({"role": "user", "content": line.replace("**User:**", "").strip()})
        elif line.startswith("**GPT:**") or line.startswith("**Gpt:**"):
            messages.append({"role": "assistant", "content": line.replace("**GPT:**", "").strip()})
    return messages


def summarize_conversation(messages, max_tokens=500):
    summary_prompt = [
        {"role": "system", "content": "Fasse das bisherige Gespräch stichpunktartig und kurz zusammen."}
    ] + messages[-10:]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=summary_prompt,
        temperature=0.3,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content.strip()


# ==== SETTINGS MENU ====
def configure_settings():
    while True:
        print("\n[EINSTELLUNGEN]")
        print(f"[1] Maximale Tokens (aktuell: {settings['max_tokens']})")
        print(f"[2] Zusammenfassungen aktivieren (aktuell: {'✅' if settings['enable_summary'] else '❌'})")
        print(f"[3] Zusammenfassung alle X Nachrichten (aktuell: {settings['summarize_every']})")
        print("[4] Zurück")

        choice = input("[EINGABE] Wähle eine Option: ").strip()

        if choice == "1":
            new_tokens = input("Neue maximale Tokens (z.B. 300): ").strip()
            if new_tokens.isdigit():
                settings["max_tokens"] = int(new_tokens)
        elif choice == "2":
            settings["enable_summary"] = not settings["enable_summary"]
        elif choice == "3":
            new_val = input("Zusammenfassen nach wie vielen Nachrichten? ").strip()
            if new_val.isdigit():
                settings["summarize_every"] = int(new_val)
        elif choice == "4":
            break


# ==== INTERACTIVE MENU ====
def choose_model():
    print("\n[GPT] Modell wählen:")
    print("[1] GPT-4")
    print("[2] GPT-3.5")
    print("[3] ⚙️ Einstellungen ändern")

    while True:
        model_choice = input("[EINGABE] Auswahl: ").strip()
        if model_choice == "1":
            return "gpt-4"
        elif model_choice == "2":
            return "gpt-3.5-turbo"
        elif model_choice == "3":
            configure_settings()
            return choose_model()


def choose_session():
    sessions = list_sessions()
    print("\n[GPT] Verfügbare Sessions:")
    for idx, name in enumerate(sessions):
        print(f"[{idx + 1}] {name}")
    print(f"[{len(sessions) + 1}] ➕ Neue Session starten")

    choice = input("[EINGABE] Auswahl: ").strip()
    try:
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(sessions):
            return sessions[choice_idx]
        else:
            return input("[NEU] Gib einen Namen für die neue Session ein: ").strip()
    except:
        return input("[NEU] Gib einen Namen für die neue Session ein: ").strip()


# ==== MAIN CHAT ====
def start_chat(model, session_name, summarize_every, max_summary_tokens, enable_summary):
    os.makedirs(SESSION_DIR, exist_ok=True)

    md_path = os.path.join(SESSION_DIR, session_name + MARKDOWN_EXTENSION)
    sum_path = os.path.join(SESSION_DIR, session_name + SUMMARY_EXTENSION)

    if not os.path.exists(md_path):
        save_file(md_path, f"# Chat Session: {session_name}\n**Datum:** {datetime.now().strftime('%Y-%m-%d')}\n**Modell:** {model}\n\n---", mode="w")

    print(f"\n[GPT] Starte Session: {session_name} (Modell: {model})")
    print("[HINWEIS] Tippe `exit` zum Beenden.\n")

    history_md = load_file(md_path)
    full_messages = build_messages_from_markdown(history_md)
    summary_text = load_file(sum_path) if enable_summary else ""
    interaction_count = 0

    # Nur beim Start: initialen Kontext setzen (Zusammenfassung)
    initial_context = []
    if enable_summary and summary_text:
        initial_context.append({"role": "system", "content": f"Hier ist die Zusammenfassung der bisherigen Unterhaltung:\n{summary_text}"})

    while True:
        user_input = input("[Du]: ")
        if user_input.lower() in ["exit", "quit"]:
            print("[GPT] Chat beendet. Bis zum nächsten Mal!")
            break

        full_messages.append({"role": "user", "content": user_input})
        save_file(md_path, f"\n\n **User:** {user_input}")

        context = initial_context + full_messages[-4:]

        response = client.chat.completions.create(
            model=model,
            messages=context,
            temperature=0.7,
            max_tokens=150
        )

        reply = response.choices[0].message.content.strip()
        print(f"\n[GPT]: {reply}\n")

        save_file(md_path, f"\n\n🤖 **GPT:** {reply}")
        full_messages.append({"role": "assistant", "content": reply})
        interaction_count += 1

        if enable_summary and interaction_count % summarize_every == 0:
            print("[GPT] Erstelle Zusammenfassung...")
            summary_text = summarize_conversation(full_messages, max_summary_tokens)
            print(f"[ZUSAMMENFASSUNG]:\n{summary_text}\n")
            save_file(md_path, f"\n\n📌 **Zusammenfassung:**\n{summary_text}")
            save_file(sum_path, summary_text, mode="w")


# ==== ENTRY ====
if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Kein OPENAI_API_KEY gefunden. Setze ihn mit `export OPENAI_API_KEY=...` oder nutze eine `.env` Datei.")
        exit(1)

    model = choose_model()
    session = choose_session()
    start_chat(model, session, settings["summarize_every"], settings["max_tokens"], settings["enable_summary"])
