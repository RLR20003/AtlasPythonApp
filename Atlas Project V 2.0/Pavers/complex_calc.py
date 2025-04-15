from Pavers.complex_variables import (
    TERRAIN_MULTIPLIERS,
    ACCESS_MULTIPLIERS,
    LAYOUT_COMPLEXITY_MULTIPLIERS,
    WORKER_EFFICIENCY
)

# ==============================
# DIFFICULTY RATING CALCULATOR
# ==============================

def get_difficulty_rating_and_score(terrain_key, access_key, layout_key, worker_key):
    terrain_multiplier = TERRAIN_MULTIPLIERS[terrain_key]
    access_multiplier = ACCESS_MULTIPLIERS[access_key]
    layout_multiplier = LAYOUT_COMPLEXITY_MULTIPLIERS[layout_key]
    worker_efficiency = WORKER_EFFICIENCY[worker_key]

    combined_score = (terrain_multiplier * access_multiplier * layout_multiplier) / worker_efficiency

    if combined_score <= 1.3:
        difficulty = "Easy"
    elif combined_score <= 1.75:
        difficulty = "Moderate"
    else:
        difficulty = "Difficult"

    return difficulty, combined_score
