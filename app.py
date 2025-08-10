# Flask app entry point
from flask import Flask, render_template, request
from scraper import generate_captcha_image, fetch_case_data
from database import init_db, log_query
import os

app = Flask(__name__)

# Ensure captcha image folder exists
os.makedirs("static", exist_ok=True)

# Initialize database
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    data = {}
    error = ""
    if request.method == "POST":
        case_type = request.form["case_type"]
        case_number = request.form["case_number"]
        case_year = request.form["case_year"]
        captcha_text = request.form["captcha"]

        try:
            data = fetch_case_data(case_type, case_number, case_year, captcha_text)
            if "error" not in data:
                log_query(case_type, case_number, case_year, str(data))
        except Exception as e:
            error = str(e)

    generate_captcha_image()
    return render_template("index.html", data=data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
