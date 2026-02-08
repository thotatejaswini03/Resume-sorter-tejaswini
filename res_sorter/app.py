from flask import Flask, render_template, request
import docx
import re
import io
from pdfminer.high_level import extract_text
from werkzeug.utils import secure_filename
from ai_model import score_resume

app = Flask(__name__)
ALLOWED_EXTENSIONS = {"pdf", "docx"}
MAX_RESUMES = 10

selected_files = {}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_bytes):
    with io.BytesIO(file_bytes) as f:
        return extract_text(f)

def extract_text_from_docx(file_bytes):
    with io.BytesIO(file_bytes) as f:
        doc = docx.Document(f)
        return "\n".join([para.text for para in doc.paragraphs])

def extract_skills(text):
    skills_keywords = ['python', 'java', 'sql', 'javascript', 'machine learning', 'c++', 'html', 'css']
    found = []
    for skill in skills_keywords:
        if skill in text.lower():
            found.append(skill.title())
    return found

def extract_experience(text):
    matches = re.findall(r'(\d+\.?\d*)\s*(year|month)s?', text, re.IGNORECASE)
    exp = 0.0
    for number, unit in matches:
        exp += float(number) if unit.lower().startswith("year") else float(number) / 12
    return round(exp, 1)

def extract_and_average_cgpa(text):
    cgpa_matches = re.findall(r"\b(?:CGPA|cgpa|Cgpa)\s*[:=]?\s*(\d+(?:\.\d+)?)", text)
    values = [float(v) for v in cgpa_matches]
    return round(sum(values) / len(values), 2) if values else 0

@app.route("/", methods=["GET", "POST"])
def index():
    global selected_files
    candidates = []

    if request.method == "POST":
        # Upload single resume
        if "resume" in request.files:
            file = request.files["resume"]
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                selected_files[filename] = file.read()

        # Process all uploaded resumes
        if request.form.get("upload_all"):
            for filename, content in selected_files.items():
                try:
                    if filename.lower().endswith(".pdf"):
                        text = extract_text_from_pdf(content)
                    else:
                        text = extract_text_from_docx(content)
                except Exception:
                    text = ""

                avg_cgpa = extract_and_average_cgpa(text)
                skills = extract_skills(text)
                experience = extract_experience(text)
                ai_score = score_resume(text)

                total_score = round(avg_cgpa + ai_score, 2)

                candidates.append({
                    "filename": filename,
                    "cgpa": avg_cgpa,
                    "skills": skills,
                    "experience": experience,
                    "ai_score": ai_score,
                    "total_score": total_score
                })

            candidates.sort(key=lambda x: x["total_score"], reverse=True)
            for idx, c in enumerate(candidates, start=1):
                c["rank"] = idx

            selected_files.clear()

    return render_template("index.html", candidates=candidates)

if __name__ == "__main__":
    app.run(debug=True)
