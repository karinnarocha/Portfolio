from flask import Blueprint, render_template

AlbertStudyCase = Blueprint('AlbertStudyCase', __name__)


@AlbertStudyCase.route("/Albert-StudyCase")
def AlbertCaseStudy():
    return render_template("AlbertCaseStudy.html")
