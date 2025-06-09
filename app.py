from flask import Flask, render_template, request
from resume_parser import extract_resume_text, match_resume_with_job

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    match_score = None
    missing_skills = []
    if request.method == "POST":
        resume = request.files["resume"]
        job_desc = request.form["jobdesc"]
        resume_text = extract_resume_text(resume)
        match_score, missing_skills = match_resume_with_job(resume_text, job_desc)
    return render_template("index.html", score=match_score, skills=missing_skills)

if __name__ == "__main__":
    app.run(debug=True)
