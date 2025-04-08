from Crushed_stone.simple_variables import (
    MATERIAL_PRICE_PER_SQFT,
    BASE_LABOR_HOURS_PER_100_SQFT,
    PROFIT_MARKUP,
    WORKER_HOURLY_RATES,
    OVERHEAD_PERCENTAGE,
    DIRT_REMOVAL_COST_PER_CUBIC_YARD,
    DELIVERY_THRESHOLD_YARDS,
    DELIVERY_FEE_UNDER_THRESHOLD,
    VEHICLE_COST_PER_MILE,
    EDGING_OPTIONS,
    EDGING_LABOR_HOURS_PER_10FT
)

def calculate_crushed_stone_basics(job):
    # Unpack user inputs
    length = job["length"]
    width = job["width"]
    depth_inches = job["depth_inches"]
    edging_type = job["edging_type"]
    worker_id = job["worker_id"]
    miles = job["miles_to_site"]

    # Basic geometry
    area_sqft = length * width
    linear_ft_edging = 2 * (length + width)

    # Material & edging costs
    material_cost = area_sqft * MATERIAL_PRICE_PER_SQFT
    edging_cost = linear_ft_edging * EDGING_OPTIONS[edging_type]

    # Dirt removal volume
    cubic_yards_dirt = (length * width * depth_inches / 12) / 27
    dirt_removal_cost = cubic_yards_dirt * DIRT_REMOVAL_COST_PER_CUBIC_YARD

    # Labor hours
    base_labor_hours = (area_sqft / 100) * BASE_LABOR_HOURS_PER_100_SQFT
    edging_labor_hours = (linear_ft_edging / 10) * EDGING_LABOR_HOURS_PER_10FT[edging_type]
    total_labor_hours = base_labor_hours + edging_labor_hours

    # Labor cost
    hourly_rate = WORKER_HOURLY_RATES[worker_id]
    labor_cost = total_labor_hours * hourly_rate

    # Vehicle cost
    vehicle_cost = miles * VEHICLE_COST_PER_MILE

    # Delivery fee logic (assume 3” depth default material = 1 cubic yard per 108 sqft)
    estimated_material_yards = (area_sqft * (depth_inches / 12)) / 27
    if estimated_material_yards < DELIVERY_THRESHOLD_YARDS:
        delivery_fee = DELIVERY_FEE_UNDER_THRESHOLD
    else:
        delivery_fee = 0.0

    # Base + overhead + profit
    base_cost = material_cost + edging_cost + labor_cost
    overhead = base_cost * OVERHEAD_PERCENTAGE
    profit = (base_cost + overhead) * PROFIT_MARKUP
    total_price = base_cost + overhead + profit + delivery_fee + dirt_removal_cost + vehicle_cost

    return {
        "area_sqft": round(area_sqft, 2),
        "linear_ft_edging": round(linear_ft_edging, 2),
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
        "estimated_material_yards": round(estimated_material_yards, 2)
    }

