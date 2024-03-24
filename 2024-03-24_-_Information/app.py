from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():

    if request.method == "POST":
        if "delete" in request.form:
            filename = request.form.get("filename")

            os.remove("static/information/" + filename)

    infos = []

    for info in os.scandir("static/information"):
        infos.append(
            {
                "name": info.name
            }
        )

    return render_template("home.html", infos=infos)


@app.route("/add", methods=["POST", "GET"])
def add():

    if request.method == "POST":
        if "add" in request.form:
            filename = request.form.get("filename")
            content = request.form.get("content")

            with open("static/information/" + filename + ".txt", "w") as fw:
                fw.write(content)

    return render_template("add.html")


@app.route("/info/<file>", methods=["POST", "GET"])
def info(file):

    with open("static/information/" + file, "r") as fr:
        content = fr.readlines()

    return render_template("info.html", file=file, content=content)


if __name__ == "__main__":
    app.run()