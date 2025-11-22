from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # Güvenlik kilidini açar

# --- BASİT YAPAY ZEKA BEYNİ ---
def get_smart_response(msg):
    msg = msg.lower()
    
    if "merhaba" in msg or "selam" in msg:
        return "Merhaba! NanoSynapseTech platformuna hoş geldiniz."
    elif "nano" in msg:
        return "Nanopartikül çalışmalarımız için 'Research' bölümüne bakabilirsiniz."
    elif "kanser" in msg:
        return "Kanser araştırmalarımız tüm hızıyla devam ediyor."
    elif "kimsin" in msg:
        return "Ben senin asistanınım."
    else:
        return "Bu konuyu henüz öğrenmedim ama araştırabilirim."
# ------------------------------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        
        # === İŞTE ÇÖZÜM BURADA ===
        # Hem 'kullanici_mesaji' (yeni kod) hem 'message' (eski kod) kontrol ediliyor.
        # Hangisi gelirse onu kabul edecek.
        user_message = data.get('kullanici_mesaji') or data.get('message')

        # Eğer ikisi de yoksa veya boşsa hata ver
        if not user_message:
            print("UYARI: Boş mesaj geldi!")
            return jsonify({"reply": "Lütfen bir şey yazın.", "cevap": "Lütfen bir şey yazın."}), 400

        print(f"Gelen Mesaj: {user_message}") # Terminalde mesajı görelim

        # Yapay zeka cevabını al
        bot_response = get_smart_response(user_message)

        # Cevabı hem eski hem yeni sisteme uygun gönderiyoruz
        return jsonify({
            "cevap": bot_response,   # Yeni HTML için
            "reply": bot_response    # Eski HTML için
        })

    except Exception as e:
        print(f"HATA OLUŞTU: {e}")
        return jsonify({"cevap": "Sunucu hatası.", "reply": "Sunucu hatası."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)