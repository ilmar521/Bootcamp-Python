import flask
import markdown as md

app = flask.Flask(__name__)


@app.route('/exercises')
def exercises():
    with open("exercises.md") as md_obj:
        md_str = md_obj.read()
        html = md.markdown(md_str)
        return html


@app.route('/lesson')
def lesson():
    with open("in-this-chapter.md") as md_obj:
        md_str = md_obj.read()
        html = md.markdown(md_str)
        return html


app.run()
