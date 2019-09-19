from flask import Flask,render_template
app = Flask(__name__)

posts = [{
        'author' : 'Madhav Kothari',
        'title' : 'Blog Post 1',
        'content' : 'Fist post content',
        'date_posted' : 'Sep 20',
        },
    {
         'author' : 'Madhav Kothari',
         'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'Sep 200',
        }    
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html',title='About')

if __name__ == '__main__':
    app.run(debug=True)