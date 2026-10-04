from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    name = ""

    if request.method == "POST":
        name = request.form.get("name")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello World!</h1>

        <form method="POST">
            <label>What is your name?</label>
            <input type="text" name="name" required>
            <button type="submit">Submit</button>
        </form>

        {"<h2>Nice to meet you, " + name + "!</h2>" if name else ""}
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)