from flask import Flask

app = Flask(__name__)

@app.route("/api")
def read_file():
    file = open("text.txt", "r")
    content = file.read()
    file.close()
    return {"text": content}  


if __name__ == "__main__":
    app.run(debug=True)