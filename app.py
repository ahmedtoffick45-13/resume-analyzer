from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/login')

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

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('resume')

        if file:
            return redirect('/job')   # 👈 next page
        else:
            return "No file selected"

    return render_template('upload.html')

@app.route('/job')
def job():
    return render_template('job.html')

@app.route('/match')
def match():
    return render_template('match_result.html')

if __name__ == "__main__":
    app.run(debug=True)
