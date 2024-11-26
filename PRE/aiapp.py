from flask import Flask, render_template, request
import wolframalpha

app = Flask(__name__)

# Wolfram Alpha API setup
api_key = "G8WX5E-77XKG66HUA"  # Replace with your API key
client = wolframalpha.Client(api_key)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        query = request.form["query"]
        try:
            # Get result from Wolfram Alpha API
            res = client.query(query)
            result = next(res.results).text
        except Exception as e:
            result = "Error: Could not get a valid result from Wolfram Alpha."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
