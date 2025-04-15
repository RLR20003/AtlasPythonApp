from Crushed_stone.simple_calc import calculate_crushed_stone_basics
from Crushed_stone.complex_calc import get_difficulty_rating

def full_crushed_stone_estimate(job):
    # Run the basic material/labor cost estimate
    simple_results = calculate_crushed_stone_basics(job)

    # Get the complexity score and difficulty label
    difficulty_data = get_difficulty_rating(job)

    # Combine both outputs into one dictionary
    full_estimate = {
        **simple_results,
        **difficulty_data
    }

    return full_estimate

