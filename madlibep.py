from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/question", methods=['POST'])
def endpoint():
    data = request.form
    print(data)
    output = f"""
<!doctype html>
<head>
    <title> Form Result </title>
    <style>
        .result {{
            color: blue;
            font-size: 2em;
        }}
    </style>
</head>
<body>
    <div class ='result'>Madlib Story</div>
    One <b>{data["adjective"]}</b> morning, I woke up to the sound of a <b>{data["noun"]}</b> crashing outside my window. I quickly <b>{data["verbpt"]}</b> out of bed and ran to the <b>{data["place"]}</b> to see what was going on. To my surprise, a giant <b>{data["animal"]}</b> was standing there, surrounded by a group of curious <b>{data["pluralNoun"]}</b>.

It was acting very <b>{data["adverb"]}</b>, as if it had just wandered into town by accident. Suddenly, <b>{data["celebrity"]}</b> appeared out of nowhere and shouted, “Don’t worry, I’ve got this!”

I watched in <b>{data["emotion"]}</b> as the celebrity offered the animal a piece of <b>{data["food"]}</b>, and just like that, it calmed down and peacefully walked away.
</body>
    """
    return output

@app.route("/", methods=['POST'])
def anotherfunction():
    pass

app.run(port=5000)