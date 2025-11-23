import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SERP_API_KEY")

def fetch_jobs(skills):
    query = ", ".join(skills)
    url = f"https://serpapi.com/search.json?q={query}+jobs&api_key={API_KEY}&engine=google_jobs"

    response = requests.get(url)
    job_list = []

    if response.status_code == 200:
        data = response.json()
        results = data.get("jobs_results", [])
        for result in results:
            job = {
                "title": result.get("title", "N/A"),
                "company": result.get("company_name", "N/A"),
                "location": result.get("location", "N/A"),
                "description": result.get("description", "No description provided."),
                "posted_at": result.get("detected_extensions", {}).get("posted_at", "N/A"),
                "via": result.get("via", "N/A"),
                "job_id": result.get("job_id", ""),
                "link": result.get("apply_options", [{}])[0].get("link", "#")
            }
            job_list.append(job)
    else:
        print("❌ SerpAPI request failed:", response.status_code, response.text)

    return job_list
