# 🧠 AI Resume Sorter Web App
The AI Resume Sorter Web App is a web-based application that helps automate the process of screening and ranking resumes. Unlike manual shortlisting, this application extracts meaningful information from resumes and ranks candidates using an AI-inspired scoring mechanism. The platform provides a simple web interface where recruiters can upload resumes and instantly view ranked candidates based on skills, CGPA, experience, and relevance score.

This project combines frontend rendering (HTML, CSS), backend logic (Flask), document parsing (PDF & DOCX), and AI-inspired scoring to create an efficient and user-friendly resume screening system.

### 🚀 Features
_**Resume Upload**: Upload resumes in PDF and DOCX formats.

_**Text Extraction**: Automatically extracts text from uploaded resumes.

_**Skill Detection**: Identifies technical skills such as Python, Java, SQL, Machine Learning, etc.

_**CGPA & Experience Extraction**: Extracts academic scores and years of experience from resumes.

_**AI-Based Relevance Scoring**: Assigns an AI-inspired relevance score based on resume content.

_**Candidate Ranking**: Ranks candidates automatically based on combined scoring logic.

_**Simple Web Interface**: Easy-to-use web UI for recruiters or evaluators.

### 📁 Project Structure

RESUME_SORTER/
│
│---app.py               # Main Flask application
│---ai_model.py         # AI-inspired scoring logic
│
│---templates/          # HTML templates
│    └── index.html     # Main UI page
│
│---static/             # Static assets
│    └── style.css      # CSS styling
│
│---requirements.txt    # Python dependencies
│---README.md           # Project documentation

### ⚡ Quick Start

🔧 _**Prerequisites**

Python 3.8 or higher

Git (for cloning)

### 1️⃣ Clone or Download the Project

_**Option 1**: Clone with Git

git clone https://github.com/your-username/ai-resume-sorter.git
cd ai-resume-sorter

_**Option 2**: Download and extract the ZIP file

### 2️⃣ Install Dependencies

pip install flask pdfminer.six python-docx werkzeug


### 3️⃣ Run the Application

python app.py
The application will start at:
👉 http://127.0.0.1:5000

## 🧪 How to Use

_**Upload Resumes**

Open the web app in your browser.

Upload resumes one by one using the Upload Resume button.

Click Upload All to process and rank all uploaded resumes.

_**View Ranked Candidates**

The system displays candidates in descending order of total score.

Each candidate card shows:

Rank

CGPA

Skills

Experience

AI Relevance Score

Total Score

## ⚙️ Technical Details

### 🛠️ Technologies Used

_ **Frontend**: HTML, CSS
_ **Backend**: Flask (Python Web Framework)
_ **Document Parsing**: pdfminer.six (PDF), python-docx (DOCX)
_ **AI Logic**: Keyword-based scoring model
_ **Language**: Python 3.8+

### 🔑 Key Components

**app.py**
Handles file uploads, resume parsing, scoring, ranking, and rendering results to the frontend.

**ai_model.py**
Contains the AI-inspired scoring logic based on keyword relevance and resume content.

**templates/index.html**
Frontend UI for uploading resumes and displaying ranked candidates.

**static/style.css**
Styles the web interface for better readability and presentation.

**requirements.txt**
Lists all required Python packages.

### 🛠️ Troubleshooting

**Resume upload not working**
Cause: Missing enctype="multipart/form-data" in HTML form.
Solution: Ensure the upload form includes correct encoding type.

**PDF text not extracted**
Cause: pdfminer.six not installed properly.
Solution: Reinstall using:

--pip install pdfminer.six


**Styling not visible**
Cause: CSS file not linked or cached by browser.
Solution:

Ensure <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}"> is present.

Hard refresh the browser (Ctrl + Shift + R).

**App crashes on file upload**
Cause: Unsupported file format.
Solution: Upload only .pdf or .docx files.

### ⚠️ Common Issues

_File upload fails
→ Ensure the file input name matches Flask backend (name="resume").

_No candidates displayed
→ Click Upload All after uploading resumes.

_Wrong ranking order
→ Check scoring logic in ai_model.py and total_score calculation.

### 🔮 Future Enhancements

-- **Job Description Matching**
Match resumes with specific job descriptions using NLP.

-- **ML/NLP-Based Scoring**
Replace keyword-based scoring with TF-IDF, embeddings, or transformer models.

-- **Database Integration**
Store resumes and candidate scores in a database.

-- **Admin Dashboard**
Add dashboard for recruiters to filter, search, and export shortlisted candidates.

-- **Resume Parsing Improvements**
Extract sections like education, projects, certifications more accurately.

-- **Authentication System**
Add login system for recruiters.

### 📞 Support

If you face any issues or have questions:

--- Phone: 9177485045
--- Email: tejaswininaiduthota03@gmail.com