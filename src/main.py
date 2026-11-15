import os
import requests
from flask import Flask, request, jsonify, render_template

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = "qwen3:14b"

context_window = []
prompt_content = "wiersz o spokoju ducha w 3 zdaniach"

user_name = "User"
model_name = "Ollama"

def ask_ollama(messages):
    prompt_formated_for_ollama = requests.post(
        f"{OLLAMA_HOST}/api/chat",
        json={
            "model": OLLAMA_MODEL,
            "messages": messages,
                "stream": False,
        },
    )
    return prompt_formated_for_ollama.json()["message"]["content"]


web_app = Flask(__name__)

@web_app.route("/")
def index():
    return render_template("index.html")

@web_app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt_content = data["message"]

    context_window.append({"role": "user", "content": prompt_content})
    ollama_says = ask_ollama(context_window)
    context_window.append({"role": "assistant", "content": ollama_says})

    return jsonify({"response": ollama_says})

if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)




if 0 == 1:
    while True:
        prompt_content = input(f"[{user_name}]: ")
        if prompt_content == "exit":
            break

        context_window.append({"role": "user", "content": prompt_content})

        ollama_says = ask_ollama(context_window)

        context_window.append({"role": "assistant", "content": ollama_says})
        print(f"{model_name}: ", ollama_says)