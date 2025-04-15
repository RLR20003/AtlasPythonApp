
from Pavers.Total_Calculations import full_paver_estimate

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

results = full_paver_estimate(job)

for key, value in results.items():
    print(f"{key}: {value}")