from flask import Flask, render_template, request,send_file
import main
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    file = request.files["image"]

    edge_lower = int(request.form["edge_lower"])
    edge_higher = int(request.form["edge_higher"])
    bg_points = int(request.form["bg_points"])
    sift_features = int(request.form["sift_features"])
    output = main.triangulator(file,
        int(bg_points),int(edge_lower),int(edge_higher),int(sift_features))
    return send_file(output, mimetype="image/png")
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")
if __name__ == "__main__":
    app.run(debug=True)