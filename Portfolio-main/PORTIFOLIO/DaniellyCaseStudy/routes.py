from flask import Blueprint, render_template

DaniellyStudyCase = Blueprint('DaniellyStudyCase',__name__)

@DaniellyStudyCase.route("/Danielly-StudyCase")
def DaniellyCaseStudy():
    return render_template("DaniellyCaseStudy.html")