from flask import Flask, render_template, request

app = Flask(__name__)

travel_data = {
    "beach": ["Goa", "Maldives", "Bali"],
    "hill": ["Ooty", "Manali", "Coorg"],
    "city": ["Bangalore", "Mumbai", "Delhi"]
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        choice = request.form.get("destination")
        places = travel_data.get(choice, [])
        return render_template("result.html", places=places, choice=choice)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)

