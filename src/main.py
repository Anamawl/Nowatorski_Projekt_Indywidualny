import requests

OLLAMA_MODEL = "qwen3:14b"

context_window = []
prompt_content = "wiersz o spokoju ducha w 3 zdaniach"

user_name = "User"
model_name = "Ollama"

def ask_ollama(messages):
    prompt_formated_for_ollama = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": OLLAMA_MODEL,
            "messages": messages,
                "stream": False,
        },
    )
    return prompt_formated_for_ollama.json()["message"]["content"]


while True:
    prompt_content = input(f"[{user_name}]: ")
    if prompt_content == "exit":
        break

    context_window.append({"role": "user", "content": prompt_content})

    ollama_says = ask_ollama(context_window)

    context_window.append({"role": "assistant", "content": ollama_says})
    print(f"{model_name}: ", ollama_says)