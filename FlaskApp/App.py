import subprocess
import threading
from flask import Flask

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask!"

def run_flask():
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)

def run_streamlit():
    subprocess.run(["streamlit", "run", "application.py"])

if __name__ == '__main__':
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Start Streamlit in the main thread
    run_streamlit()
