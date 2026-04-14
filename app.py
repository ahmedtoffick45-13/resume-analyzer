from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Home → direct upload
@app.route('/')
def home():
    return redirect('/upload')

# Upload
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('resume')

        if not file:
            return "No file selected"

        return redirect('/job')

    return render_template('upload.html')


# Job Matcher (SAFE VERSION)
@app.route('/job', methods=['GET', 'POST'])
def job():
    if request.method == 'POST':
        skills = request.form.get('job_desc')

        if not skills:
            return "Please enter skills"

        skills_list = [s.strip().lower() for s in skills.split(',')]

        jobs = {
            "Data Analyst": ["python", "sql", "excel"],
            "Web Developer": ["html", "css", "javascript"],
            "AI Engineer": ["python", "machine learning"]
        }

        results = {}

        for job_name, req_skills in jobs.items():
            match = len(set(skills_list) & set(req_skills))
            percent = int((match / len(req_skills)) * 100)
            results[job_name] = percent

        return render_template('match_result.html', results=results)

    return render_template('job.html')


if __name__ == "__main__":
    app.run(debug=True)