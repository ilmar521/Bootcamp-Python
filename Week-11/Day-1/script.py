import flask

app = flask.Flask(__name__)


@app.route('/blog')
def blog():
    return "Welcome to my blog!"


@app.route('/blog/articles')
def blog_articles():
    return '''
        <ul>
            <li>1 article</li>
            <li>2 article</li>
            <li>3 article</li>
        <ul>
    '''


app.run()
