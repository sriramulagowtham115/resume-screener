import os
import fitz  # PyMuPDF
import docx
import tempfile

def extract_text_from_resume(uploaded_file):
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as temp:
            for chunk in uploaded_file.chunks():
                temp.write(chunk)
            temp_path = temp.name

        ext = os.path.splitext(temp_path)[-1].lower()

        if ext == ".pdf":
            text = ""
            with fitz.open(temp_path) as doc:
                for page in doc:
                    text += page.get_text()
            return text

        elif ext == ".docx":
            doc = docx.Document(temp_path)
            return "\n".join([para.text for para in doc.paragraphs])

        else:
            return "Unsupported file format."

    except Exception as e:
        print("Error extracting resume text:", e)
        return ""

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
