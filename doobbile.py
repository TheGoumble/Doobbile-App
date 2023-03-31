from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
    "author": "Javier Vargas",
    "title": "Doobbile Post 1",
    "content": "This would be the SVG",
    "caption": "This is my drawing",
    "date_posted": "March 31, 2018"
    },
     {
    "author": "John Mackland",
    "title": "Doobbile Post 2",
    "content": "This would be the SVG",
    "caption": "This is my animal drawing",
    "date_posted": "March 31, 2018"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

if __name__ == "__main__":
    app.run(debug=True)