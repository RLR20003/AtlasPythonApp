from Pavers.simple_variables import (
    PAVER_PRICES_PER_SQFT,
    SAND_PRICE_PER_SQFT,
    CONCRETE_PRICE_PER_CUBIC_FT,
    EDGING_OPTIONS,
    EDGING_LABOR_HOURS_PER_10FT,
    WORKER_HOURLY_RATES,
    DIRT_REMOVAL_RATE,
    GRAVEL_LAYING_RATE,
    CONCRETE_EDGING_RATE,
    PAVER_LAYING_RATE,
    PROFIT_MARKUP,
    OVERHEAD_PERCENTAGE,
    DIRT_REMOVAL_COST_PER_CY,
    DELIVERY_FEE_FLAT,
    VEHICLE_COST_PER_MILE,
    TOTAL_DIG_DEPTH_FT,
    MATERIAL_WASTE_FACTOR
)

def calculate_paver_basics(job):
    length = job["length"]
    width = job["width"]
    depth_ft = job["depth_inches"] / 12
    worker = job["worker_id"]
    edging_type = job["edging_type"]
    miles = job["miles_to_site"]

    # Area & perimeter
    area_sqft = length * width
    perimeter_ft = 2 * (length + width)

    # Volumes
    volume_cubic_ft = area_sqft * TOTAL_DIG_DEPTH_FT * (1 + MATERIAL_WASTE_FACTOR)
    volume_cubic_yards = volume_cubic_ft / 27

    # Material Costs
    sand_cost = area_sqft * SAND_PRICE_PER_SQFT
    paver_cost = area_sqft * PAVER_PRICES_PER_SQFT["medium"]  # default to medium for now
    concrete_volume = perimeter_ft * 0.25 * 0.25  # trench: 3" x 3"
    concrete_cost = concrete_volume * CONCRETE_PRICE_PER_CUBIC_FT
    edging_cost = perimeter_ft * EDGING_OPTIONS[edging_type]

    material_cost = sand_cost + paver_cost + concrete_cost + edging_cost

    # Labor Hours
    edging_labor = (perimeter_ft / 10) * EDGING_LABOR_HOURS_PER_10FT[edging_type]
    dirt_hours = area_sqft / DIRT_REMOVAL_RATE
    gravel_hours = area_sqft / GRAVEL_LAYING_RATE
    concrete_hours = perimeter_ft / CONCRETE_EDGING_RATE
    paver_hours = area_sqft / PAVER_LAYING_RATE

    total_labor_hours = dirt_hours + gravel_hours + concrete_hours + paver_hours + edging_labor
    labor_cost = total_labor_hours * WORKER_HOURLY_RATES[worker]

    # Overhead & Profit
    overhead = (material_cost + labor_cost) * OVERHEAD_PERCENTAGE
    profit = (material_cost + labor_cost + overhead) * PROFIT_MARKUP

    # Additional Costs
    delivery_fee = DELIVERY_FEE_FLAT
    dirt_removal_cost = volume_cubic_yards * DIRT_REMOVAL_COST_PER_CY
    vehicle_cost = miles * VEHICLE_COST_PER_MILE

    total_price = (
        material_cost +
        labor_cost +
        overhead +
        profit +
        delivery_fee +
        dirt_removal_cost +
        vehicle_cost
    )

    return {
        "area_sqft": round(area_sqft, 2),
        "linear_ft_edging": round(perimeter_ft, 2),
        "material_cost": round(material_cost, 2),
        "edging_cost": round(edging_cost, 2),
        "labor_hours": round(total_labor_hours, 2),
        "labor_cost": round(labor_cost, 2),
        "overhead": round(overhead, 2),
        "profit": round(profit, 2),
        "delivery_fee": round(delivery_fee, 2),
        "dirt_removal_cost": round(dirt_removal_cost, 2),
        "vehicle_cost": round(vehicle_cost, 2),
        "total_price": round(total_price, 2),
        "estimated_material_yards": round(volume_cubic_yards, 2)
    }
