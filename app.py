from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': "Sravan",
        'title': 'Watch Blog',
        'content': 'First Post content',
        'date': 'April 20, 2020'
    },
    {
        'author': "Jayalakshmi",
        'title': 'Cooking Blog',
        'content': 'First Post about cooking',
        'date': 'July 20, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
