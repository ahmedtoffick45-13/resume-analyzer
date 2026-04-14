from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Home → Login
@app.route('/')
def home():
    return redirect('/login')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email == "test@gmail.com" and password == "1234":
            return redirect('/upload')
        else:
            return "Invalid email or password"

    return render_template('login.html')


# Upload Resume
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('resume')

        if file:
            return redirect('/job')   # next page
        else:
            return "No file selected"

    return render_template('upload.html')


# Job Matcher (FIXED ✅)
@app.route('/job', methods=['GET', 'POST'])
def job():
    if request.method == 'POST':
        skills = request.form.get('skills')

        skills_list = [s.strip().lower() for s in skills.split(',')]

        jobs = {
            "Data Analyst": ["python", "sql", "excel"],
            "Web Developer": ["html", "css", "javascript"],
            "AI Engineer": ["python", "machine learning"]
        }

        results = {}

        for job, req_skills in jobs.items():
            match = len(set(skills_list) & set(req_skills))
            percent = int((match / len(req_skills)) * 100)
            results[job] = percent

        return render_template('match_result.html', results=results)

    return render_template('job.html')


# Result page (optional direct access)
@app.route('/match')
def match():
    return render_template('match_result.html')


# Run app (local only)
if __name__ == "__main__":
    app.run(debug=True)
