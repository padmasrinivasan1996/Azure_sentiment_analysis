from flask import Flask, request, render_template
import requests

app = Flask(__name__)

AZURE_KEY = "YOUR_AZURE_KEY"
AZURE_ENDPOINT = "YOUR_AZURE_RESORCE_ENDPOINT"

def analyze_sentiment(text):
    url = AZURE_ENDPOINT + "text/analytics/v3.1/sentiment"
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Content-Type": "application/json"
    }
    body = {
        "documents": [
            {
                "id": "1",
                "language": "en",
                "text": text
            }
        ]
    }
    response = requests.post(url, headers=headers, json=body)

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    response.raise_for_status()
    result = response.json()
    sentiment = result["documents"][0]["sentiment"]
    confidence_scores = result["documents"][0]["confidenceScores"]
    return sentiment, confidence_scores

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    confidence = None
    text = ""
    error = None

    if request.method == "POST":
        text = request.form.get("text", "")
        try:
            sentiment, confidence = analyze_sentiment(text)
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template("index.html", sentiment=sentiment, confidence=confidence, text=text, error=error)

if __name__ == "__main__":
    app.run(debug=True)
