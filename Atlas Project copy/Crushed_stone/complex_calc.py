from Crushed_stone.complex_variables import (
    TERRAIN_MULTIPLIERS,
    ACCESS_MULTIPLIERS,
    WORKER_EFFICIENCY
)

def get_difficulty_rating(job):
    terrain_factor = TERRAIN_MULTIPLIERS[job["terrain"]]
    access_factor = ACCESS_MULTIPLIERS[job["access"]]
    efficiency = WORKER_EFFICIENCY[job["worker_id"]]

    combined_score = (terrain_factor * access_factor) / efficiency

    if combined_score <= 1.05:
        difficulty = "Easy"
    elif combined_score <= 1.2:
        difficulty = "Moderate"
    else:
        difficulty = "Difficult"

    return {
        "difficulty_score": round(combined_score, 3),
        "difficulty_rating": difficulty
    }


