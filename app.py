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
        # تجهيز المتغيرات البيئية بشكل صريح مع إزالة الفراغات
        env = os.environ.copy()
        env["TOKEN"] = env.get("TOKEN", "").strip()
        env["API_ID"] = env.get("API_ID", "").strip()
        env["API_HASH"] = env.get("API_HASH", "").strip()
        env["MONGO_DB_URI"] = env.get("MONGO_DB_URI", "").strip()
        env["OWNER_ID"] = env.get("OWNER_ID", "").strip()

        print(f"🔑 Token length: {len(env['TOKEN'])}")
        print(f"🔑 Token starts with: {env['TOKEN'][:10]}...")

        # تشغيل البوت مع تمرير المتغيرات النظيفة
        subprocess.Popen(
            ["python", "-m", "FallenRobot"],
            env=env
        )
        print("✅ Bot process started")
    except Exception as e:
        print(f"❌ Bot error: {e}")

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
