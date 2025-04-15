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

# Layout complexity multipliers (new!)
LAYOUT_COMPLEXITY_MULTIPLIERS = {
    "straight": 1.0,
    "moderate": 1.1,
    "intricate": 1.25
}

# Worker efficiency factors (relative to baseline)
WORKER_EFFICIENCY = {
    "worker_1": 1.0,
    "worker_2": 1.1,
    "worker_3": 0.85
}

# Built-in difficulty rating function (now includes layout complexity)
def get_difficulty_rating_2(terrain_multiplier, access_multiplier, layout_multiplier, worker_efficiency):
    combined_score = (terrain_multiplier * access_multiplier * layout_multiplier) / worker_efficiency

    if combined_score <= 1.3:
        return "Easy"
    elif combined_score <= 1.75:
        return "Moderate"
    else:
        return "Difficult"
