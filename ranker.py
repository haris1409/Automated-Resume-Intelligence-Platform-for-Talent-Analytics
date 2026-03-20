import pandas as pd

# basic synonym mapping (AI-like behavior)
skill_map = {
    "ml": "machine learning",
    "js": "javascript",
    "py": "python"
}

def normalize(skills):
    normalized = []
    for s in skills:
        s = s.lower()
        if s in skill_map:
            s = skill_map[s]
        normalized.append(s)
    return normalized

def calculate_score(candidate, job):
    candidate = set(normalize(candidate))
    job = set(job.split())

    match = candidate.intersection(job)
    score = (len(match) / len(job)) * 100

    return score, list(match)

def rank_candidate(skills):
    df = pd.read_csv("jobs.csv")

    best = ("None", 0, [])

    for _, row in df.iterrows():
        score, matched = calculate_score(skills, row['Skills'])

        if score > best[1]:
            best = (row['Job Role'], score, matched)

    return best[0], round(best[1], 2), best[2]