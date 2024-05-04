from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story
app.config['SECRET_KEY']= "secret"
app = Flask(__name__)

@app.route("/")
def home_page():
    prompt = story.prompts
    return render_template("mad-lib-form.html")

@app.route("/story" methods=["POST"])
def mad_lib_create():
    """create the mad lib page"""
    your_story = story.generate(request.args)
    return render_template("story.html" your_story= your_story)
