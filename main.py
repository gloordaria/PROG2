from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

app = Flask("Lernaufwandrechner")

@app.route("/startseite")
def startseite():
    return url_for("startseite.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)



