from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from utils.parser import extract_skills_from_resume
from utils.ats_score import calculate_ats_score
from utils.job_search import fetch_jobs
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "secretkey")

# MongoDB Setup
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

# Create resumes folder if not exists
app.config["UPLOAD_FOLDER"] = "resumes"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Flask-Login Setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# User Class
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id  # Here, ID will be username
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    user = mongo.db.users.find_one({"username": user_id})
    if user:
        return User(user["username"], user["username"], user["password"])
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        existing_user = mongo.db.users.find_one({"username": username})
        if existing_user:
            flash("Username already exists!", "danger")
            return redirect(url_for("register"))

        hashed_pw = generate_password_hash(password)
        mongo.db.users.insert_one({"username": username, "password": hashed_pw})
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = mongo.db.users.find_one({"username": username})
        if user and check_password_hash(user["password"], password):
            login_user(User(user["username"], user["username"], user["password"]))
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "info")
    return redirect(url_for("login"))

@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST":
        resume = request.files["resume"]
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], resume.filename)
        resume.save(filepath)

        # Extract skills and fetch jobs
        skills = extract_skills_from_resume(filepath)
        jobs = fetch_jobs(skills)

        # Score the jobs based on skills
        scored_jobs = [
            {"job": job, "score": calculate_ats_score(skills, job.get("description", ""))}
            for job in jobs
        ]

        return render_template("jobs.html", skills=skills, jobs=scored_jobs)

    return render_template("upload.html")

@app.route("/about")
@login_required
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
