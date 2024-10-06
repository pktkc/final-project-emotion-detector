""" Import required module."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

@app.route("/")
def home():
    """ This code displays home page index.html."""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detect():
    """ This function takes user input text and gets emotion score and diplays the result."""
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"

    return f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. The dominant emotion is <b>{result['dominant_emotion']}</b>."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
