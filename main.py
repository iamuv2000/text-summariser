#Module imports
from flask import Flask
from flask import render_template, jsonify, request
from summarizer import summarize

# Creates a Flask application, named app
app = Flask(__name__)

# Route to get main html page
@app.route("/")
def hello():
    return render_template('index.html')

# Route to get text summary
@app.route('/api/getSummary', methods=['POST'])
def api_all():
    text = request.json['text']
    no_of_sentence = request.json['no_of_sentence']
    summary_text = summarize(text , no_of_sentence)
    return jsonify(summary_text)


# Run the application
if __name__ == "__main__":
    app.run(debug=True)