def match_skills(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched = resume_set.intersection(job_set)
    missing = job_set - resume_set

    if len(job_set) == 0:
        score = 0
    else:
        score = (len(matched) / len(job_set)) * 100

    return {
        "score": round(score, 2),
        "matched": list(matched),
        "missing": list(missing)
    }