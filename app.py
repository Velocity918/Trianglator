from flask import Flask, render_template, request,send_file
import main
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    file = request.files["image"]
    output = main.triangulator(file)
    return send_file(output, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)