import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Citim variabila 'MESAJ'. Daca nu exista, folosim un default.
    mesaj_custom = os.getenv('MESAJ', 'Mesaj Default')
    return f"{mesaj_custom} | Rulez pe: {os.getenv('HOSTNAME')}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)