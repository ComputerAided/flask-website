from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(host = '10.0.0.17', port = 80, debug = True) # Feel free to change to your IP
