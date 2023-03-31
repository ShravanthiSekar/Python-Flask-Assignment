from flask import Flask

app = Flask(__name__)

@app.route("/")
def python():
    return"Python Flask assignment by Shravanthi"

if __name__ == "__main__" :
    app.run()
