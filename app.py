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
        env = os.environ.copy()
        env["TOKEN"] = env.get("TOKEN", "").strip()
        env["API_ID"] = env.get("API_ID", "").strip()
        env["API_HASH"] = env.get("API_HASH", "").strip()
        env["MONGO_DB_URI"] = env.get("MONGO_DB_URI", "").strip()
        env["OWNER_ID"] = env.get("OWNER_ID", "").strip()

        print("🚀 Starting FallenRobot...", flush=True)
        
        # تشغيل البوت مع عرض كل المخرجات في logs
        process = subprocess.Popen(
            ["python", "-m", "FallenRobot"],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
            universal_newlines=True
        )
        
        # طباعة كل سطر من مخرجات البوت
        for line in process.stdout:
            print(f"[BOT] {line}", end="", flush=True)
        
        process.wait()
        print(f"⚠️ Bot exited with code {process.returncode}", flush=True)
    except Exception as e:
        print(f"❌ Bot error: {e}", flush=True)

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
