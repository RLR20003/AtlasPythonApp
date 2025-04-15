# ==============================
# MATERIAL PRICES
# ==============================

PAVER_PRICES_PER_SQFT = {
    "high": 18.00,
    "medium": 12.00,
    "low": 8.00
}

SAND_PRICE_PER_SQFT = 0.50  # for joints
CONCRETE_PRICE_PER_CUBIC_FT = 6.00

# Edging options (material price per linear foot)
EDGING_OPTIONS = {
    "none": 0.00,
    "plastic": 1.50,
    "metal": 4.00,
    "natural_stone": 7.00
}

# Labor hours per 10ft of edging
EDGING_LABOR_HOURS_PER_10FT = {
    "none": 0.0,
    "plastic": 0.25,
    "metal": 0.5,
    "natural_stone": 1.0
}

# ==============================
# LABOR
# ==============================

WORKER_HOURLY_RATES = {
    "worker_1": 50,
    "worker_2": 55,
    "worker_3": 45
}

WORKER_EFFICIENCY = {
    "worker_1": 1.0,
    "worker_2": 1.1,
    "worker_3": 0.85
}

# Labor production constants (sqft/hour)
DIRT_REMOVAL_RATE = 50
GRAVEL_LAYING_RATE = 40
CONCRETE_EDGING_RATE = 20
PAVER_LAYING_RATE = 30

# ==============================
# FIXED COSTS
# ==============================

PROFIT_MARKUP = 0.25
OVERHEAD_PERCENTAGE = 0.06
DIRT_REMOVAL_COST_PER_CY = 30.00
DELIVERY_FEE_FLAT = 75.0
VEHICLE_COST_PER_MILE = 1.00

# ==============================
# MATERIAL DEPTHS & WASTE
# ==============================

TOTAL_DIG_DEPTH_FT = 0.5  # 6 inches
MATERIAL_WASTE_FACTOR = 0.07

