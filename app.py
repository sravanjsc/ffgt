from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return "<h3>Home Page</h3>"


@app.route('/about')
def about():
    return "<h3>About Page</h3>"


if __name__ == "__main__":
    app.run(debug=True)
