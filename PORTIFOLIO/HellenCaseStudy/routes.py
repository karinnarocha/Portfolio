from flask import Blueprint, render_template

HellenStudyCase = Blueprint('HellenStudyCase',__name__)

@HellenStudyCase.route("/Hellen-StudyCase")
def HellenCaseStudy():
    return render_template("HellenCaseStudy.html")