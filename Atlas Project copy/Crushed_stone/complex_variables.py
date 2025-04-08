# Terrain difficulty multipliers
TERRAIN_MULTIPLIERS = {
    "flat": 1.0,
    "sloped": 1.15,
    "uneven": 1.3
}

# Access difficulty multipliers
ACCESS_MULTIPLIERS = {
    "easy": 1.0,
    "medium": 1.1,
    "hard": 1.25
}

# Worker efficiency factors (how fast each worker performs, relative to baseline)
WORKER_EFFICIENCY = {
    "worker_1": 1.0,
    "worker_2": 1.1,
    "worker_3": 0.85
}

#Built in difficulty rating function to categorize the combined score

def get_difficulty_rating_1(terrain_multiplier, access_multiplier, worker_efficiency):
    combined_score = (terrain_multiplier * access_multiplier) / worker_efficiency

    if combined_score <= 1.05:
        return "Easy"
    elif combined_score <= 1.2:
        return "Moderate"
    else:
        return "Difficult"


