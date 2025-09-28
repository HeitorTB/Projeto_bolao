from flask import Flask, render_template
app = Flask(__name__)

# Lista de jogos (pode vir de banco de dados ou API futuramente)
jogos = [
    {"id": 1, "time1": "Brasil", "time2": "Alemanha"},
    {"id": 2, "time1": "Argentina", "time2": "França"},
    {"id": 3, "time1": "Portugal", "time2": "Inglaterra"},
    {"id": 4, "time1": "Espanha", "time2": "Holanda"},
]

@app.route("/")
def index():
    return render_template("index.html", jogos=jogos)

if __name__ == "__main__":
    app.run(debug=True)
