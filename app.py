from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
from openai import OpenAI

# .env dosyasını yükle
load_dotenv()

# Ortam değişkeninden API anahtarını al
nvdia_api_key = os.getenv("NVIDIA_API_KEY")
print(nvdia_api_key)
if not nvdia_api_key:
    raise ValueError("NVIDIA_API_KEY environment variable is not set.")

app = Flask(__name__)

# NVIDIA API istemcisini yapılandırma
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    # api_key="API_KEY_REQUIRED_IF_EXECUTING_OUTSIDE_NGC"  # NVIDIA API anahtarınızı buraya ekleyin
    api_key=nvdia_api_key
)

# Ana sayfa
@app.route('/')
def home():
    return render_template('index.html')  # HTML dosyasını kullanarak bir form göster

# Modelden yanıt almak için API endpoint'i
@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Modelden yanıt al
    completion = client.chat.completions.create(
        model="deepseek-ai/deepseek-r1",
        messages=[{"role": "user", "content": user_input}],
        temperature=0.6,
        top_p=0.7,
        max_tokens=4096,
        stream=True
    )

    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content

    return jsonify({"response": response})

# Uygulamayı çalıştır
if __name__ == '__main__':
    app.run(debug=True)