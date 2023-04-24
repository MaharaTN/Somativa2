from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/text", methods=["GET"])
def count_text():
    text = request.args.get("text")
    count = len(text)
    return f"O texto tem {count} caracteres"

if __name__ == "__main__":
    app.run(debug=True)
