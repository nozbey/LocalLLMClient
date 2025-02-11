# Flask Chatbot Uygulaması

Bu, NVIDIA'nın yapay zeka modelini entegre eden basit bir Flask tabanlı chatbot uygulamasıdır.

## 🚀 Özellikler
- Kullanıcı mesajlarını alır ve NVIDIA API'sine iletir.
- Yanıtları gerçek zamanlı ve düzgün bir formatta görüntüler.
- Kod blokları içeren yanıtlar kopyalanabilir.

## 📦 Kurulum
1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/your-repo/chatbot-flask.git
   cd chatbot-flask
    ```
2. Bir sanal ortam oluşturun (isteğe bağlı ancak önerilir):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows için: venv\Scripts\activate
     ```
3. .env dosyası oluşturun ve NVIDIA API anahtarınızı ekleyin:
    ```ini
    NVIDIA_API_KEY=your_api_key_here
    ```
## 🛠️ Kullanım
```bash
python app.py
```

## 🛠 API Endpoint
POST /api/chat: Mesaj gönderir ve yanıt alır.
1. İstek:
```json
{
    "message": "Merhaba, nasılsınız?"
}
2. Yanıt:
```json
{
    "response": "Ben bir yapay zeka modeliyim."
}
```


## 📝 Lisans