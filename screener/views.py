from django.shortcuts import render
from .forms import ResumeForm
from .models import ParsedResume
from .utils.extract_text_from_resume import extract_text_from_resume
from .utils.nlp_utils import (
    extract_email, extract_phone, extract_skills,
    extract_name, extract_education, extract_experience,
    score_resume
)

def home(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES.get('resume')

        if uploaded_file:
            # Step 1: Extract raw text from resume file
            resume_text = extract_text_from_resume(uploaded_file)
            print("Extracted Text:", resume_text)

            # Step 2: NLP field extraction
            name = extract_name(resume_text)
            email = extract_email(resume_text)
            phone = extract_phone(resume_text)
            skills = extract_skills(resume_text)
            education = extract_education(resume_text)
            experience = extract_experience(resume_text)
            score, matched_skills = score_resume(
                resume_text,
                ['python', 'java', 'sql', 'html', 'css', 'javascript', 'django']
            )

            # Step 3: Save parsed data to database
            ParsedResume.objects.create(
                name=name,
                email=email,
                phone=phone,
                skills=", ".join(skills),
                education=education,
                experience=experience,
                score=score,
                matched_skills=", ".join(matched_skills),
                resume_file=uploaded_file
            )

            # Step 4: Prepare context for template
            context = {
                'extracted_info': {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'skills': ", ".join(skills),
                    'education': education,
                    'experience': experience,
                    'score': score,
                    'matched_skills': ", ".join(matched_skills)
                },
                'extracted_text': resume_text,
                'all_resumes': ParsedResume.objects.all().order_by('-uploaded_at'),
                'form': ResumeForm()
            }

    else:
        # Initial page load
        context = {
            'form': ResumeForm(),
            'all_resumes': ParsedResume.objects.all().order_by('-uploaded_at')
        }

    return render(request, 'home.html', context)
