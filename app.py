from flask import Flask, render_template, request, redirect, session
import os
import csv

from ranker import rank_candidate
from auth import check_login
from parser import parse_resume   # ✅ import once at top

app = Flask(__name__)
app.secret_key = "secret123"

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

results = []

# 🔐 LOGIN ROUTE
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        if check_login(user, pwd):
            session['user'] = user
            return redirect('/home')

    return render_template('login.html')


# 🏠 HOME PAGE
@app.route('/home')
def home():
    if 'user' not in session:
        return redirect('/')
    return render_template('index.html')


# 📤 UPLOAD + PROCESS
@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('resume')

    for file in files:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        # ✅ REAL RESUME PARSING
        data = parse_resume(path)

        # 🔥 DEBUG (VERY IMPORTANT)
        print("Extracted Data:", data)

        name = data.get('name', 'Unknown')
        skills = data.get('skills', [])

        # 🎯 RANKING
        role, score, matched = rank_candidate(skills)

        result = {
            "name": name,
            "role": role,
            "score": score,
            "matched": matched
        }

        results.append(result)

        # 💾 SAVE RESULT
        with open("results.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, role, score])

    return render_template('dashboard.html', results=results)


# 🚪 LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# ▶️ RUN APP
if __name__ == "__main__":
    app.run(debug=True)