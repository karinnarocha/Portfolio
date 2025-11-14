from flask import Blueprint, render_template

LulunremiStudyCase = Blueprint('LulunremiStudyCase', __name__)


@LulunremiStudyCase.route("/LulunRemi-StudyCase")
def LulunremiCaseStudy():
    return render_template("LulunremiCaseStudy.html")
