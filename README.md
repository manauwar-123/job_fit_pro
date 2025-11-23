# Job Fit Pro -- Resume Analysis & Job Matching Tool

A web application built using **Python, Flask, HTML, CSS, and MongoDB**
that analyzes resume quality, calculates ATS score, extracts skills, and
recommends jobs using the **SERP API**.

## ⭐ Features

### ✅ Resume Quality Check

-   Analyzes uploaded resumes and extracts key information.
-   Evaluates formatting, keyword usage, skills, and clarity.

### ✅ ATS (Applicant Tracking System) Score

-   Evaluates resume structure, formatting, keywords, and skills.
-   Generates an ATS-friendly score to show resume strength.

### ✅ Job Recommendation System

-   Fetches job listings using **SERP API**.
-   Matches user's extracted skills and suggests relevant jobs.

### ✅ User Authentication

-   Signup/login functionality.
-   Secure resume upload and session management.

### ✅ Database Integration

-   Uses **MongoDB** for storing:
    -   User accounts
    -   Resume uploads
    -   Skill extraction results

------------------------------------------------------------------------

## 🏗️ Tech Stack

  Layer       Technology
  ----------- ----------------------------------------
  Frontend    HTML, CSS
  Backend     Python (Flask)
  Database    MongoDB
  API         SERP API
  Libraries   pdf2, regex, TF-IDF, cosine similarity

------------------------------------------------------------------------

## 📂 Folder Structure

    Job-Fit-Pro/
    │── app.py
    │── templates/
    │── static/
    │── utils/
    │── uploads/
    │── requirements.txt
    │── README.md

------------------------------------------------------------------------

## 🚀 Installation & Setup

### 1. Clone the repository

    git clone https://github.com/your-username/job-fit-pro.git
    cd job-fit-pro

### 2. Create virtual environment

    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate    # Windows

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Create `.env` file

    MONGO_URI=your_mongodb_url
    SERP_API_KEY=your_serp_api_key
    SECRET_KEY=your_flask_secret_key

### 5. Run the server

    python app.py

------------------------------------------------------------------------

## 🌟 Future Enhancements

-   AI-based resume improvement
-   Job filters (location, salary, remote)
-   Exportable ATS report
-   Multi-resume comparison

------------------------------------------------------------------------

## 📄 License

This project is licensed under the MIT License.
