from flask import Flask, render_template, request, redirect, url_for, session
from utils.model import generate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_prompt = request.form.get("prompt", "Generate a modern homepage")
        generated_html = generate(user_prompt)
        session["generated_html"] = generated_html
        return redirect(url_for("preview"))
    return render_template("index.html")

@app.route("/preview")
def preview():
    generated_html = session.get("generated_html", "")
    return render_template("preview.html", generated_html=generated_html)

if __name__ == "__main__":
    app.run(debug=True)
