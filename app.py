from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("./index.html")

@app.route('/submit_responses', methods=['POST'])
def submit_responses():
    data = request.json
    # Process the data here (e.g., save to database)
    print(data)  # For debugging
    return jsonify({"status": "success"})

if __name__ == '__main__':
   app.run()