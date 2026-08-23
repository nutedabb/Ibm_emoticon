from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route("/emotionDetector")
def emotion():
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)
    return text



if __name__ == "__main__":
    app.run(debug = True)
