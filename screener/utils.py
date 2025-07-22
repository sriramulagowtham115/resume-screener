import os
import tempfile
from PyPDF2 import PdfReader  # or use textract, docx2txt, etc.

def extract_text_from_resume(resume_file):
    # Save uploaded file to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
        tmp.write(resume_file.read())
        tmp_path = tmp.name

    extracted_text = ''
    
    # 🛠 Open PDF in read-only mode to release it later
    with open(tmp_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            extracted_text += page.extract_text()

    # ✅ Now it's safe to delete
    os.remove(tmp_path)

    return extracted_text
