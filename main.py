from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=["GET"])  # DO NOT USE THIS PLEASE!!!
def index():
    return render_template("index.html")


@app.get("/")  # READ
def index():
    return render_template("index.html")


@app.post("/")  # CREATE
def index():
    return render_template("index.html")


@app.put("/")  # UPDATE
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
