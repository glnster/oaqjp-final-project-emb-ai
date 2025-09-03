from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

# Routes
@app.route("/emotionDetector")
def sent_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    
    # parse result to get just the scores
    result_scores = {}
    for emotion, score in result.items():
        if emotion != "dominant_emotion":
            result_scores[emotion] = score
    first_scores = dict(list(result_scores.items())[:-1])
    last_score = result_scores.popitem()
    
    # strip braces out
    first_scores = str(first_scores)[1:-1]
    last_score = str(last_score)[1:-1]

    dominant_emotion = result["dominant_emotion"]

    formatted_output = "For the given statement, the system response is " \
                       f"{first_scores} and " \
                       f"{last_score}. " \
                       f"The dominant emotion is {dominant_emotion}."

    return formatted_output

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)