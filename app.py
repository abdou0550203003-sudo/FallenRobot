import os
import subprocess
import threading
from flask import Flask

app = Flask(__name__)

@app.route('/')
def health():
    return "OK", 200

def run_bot():
    try:
        subprocess.Popen(["python", "-m", "FallenRobot"])
        print("✅ Bot process started")
    except Exception as e:
        print(f"❌ Bot error: {e}")

if __name__ == "__main__":
    # نشغلو البوت في الخلفية
    threading.Thread(target=run_bot, daemon=True).start()
    
    # نشغلو Flask باش Render يشوف المنفذ
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
