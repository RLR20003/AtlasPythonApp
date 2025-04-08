from Crushed_stone.Total_Caculations import full_crushed_stone_estimate

# Sample job input from user
job = {
    "length": 20,
    "width": 4,
    "depth_inches": 6,
    "edging_type": "natural_stone",
    "worker_id": "worker_2",
    "terrain": "sloped",
    "access": "medium",
    "miles_to_site": 15
}

# Get full estimate results
results = full_crushed_stone_estimate(job)

print("\n🧾 ESTIMATE RESULTS\n-------------------")
for key, value in results.items():
    print(f"{key.replace('_', ' ').capitalize()}: {value}")
#this just takes the results and formats it properly.