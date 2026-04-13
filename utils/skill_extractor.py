def extract_skills(text):
    skills_list = [
        "python", "java", "c++", "sql", "html", "css", "javascript",
        "machine learning", "data science", "excel", "flask", "django"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills