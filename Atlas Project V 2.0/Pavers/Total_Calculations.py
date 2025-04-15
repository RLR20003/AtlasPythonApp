from Pavers.simple_calc import calculate_paver_basics
from Pavers.complex_calc import get_difficulty_rating_and_score

def full_paver_estimate(job):
    # Step 1: Get material, labor, cost, and project stats
    basic_results = calculate_paver_basics(job)

    # Step 2: Get difficulty rating & score
    difficulty_rating, difficulty_score = get_difficulty_rating_and_score(
        terrain_key=job["terrain"],
        access_key=job["access"],
        layout_key="straight",  # default for now unless user provides
        worker_key=job["worker_id"]
    )

    # Step 3: Merge both outputs
    full_estimate = {
        **basic_results,
        "difficulty_score": round(difficulty_score, 2),
        "difficulty_rating": difficulty_rating
    }

    return full_estimate