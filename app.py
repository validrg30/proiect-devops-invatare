import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Afisam un mesaj si ID-ul containerului (hostname)
    return f"Salut din Docker! NOUAAA VESRSIUNE Rulez pe: {os.getenv('HOSTNAME')}"

if __name__ == "__main__":
    # Rulam serverul pe orice interfata (0.0.0.0) pe portul 5000
    app.run(host='0.0.0.0', port=5000)
