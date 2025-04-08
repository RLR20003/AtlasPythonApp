
#MATERIAL PRICES

# Crushed Stone Material price per square foot
MATERIAL_PRICE_PER_SQFT = 3.00

# Edging options (cost per linear foot)
EDGING_OPTIONS = {
    "none": 0.00,
    "plastic": 1.50,
    "metal": 4.00,
    "natural_stone": 7.00}

#LABOR PRICES

# Base labor hours per 100 square feet of Crushed Stone installed
BASE_LABOR_HOURS_PER_100_SQFT = 2.0

# Worker hourly rates (just money values)
WORKER_HOURLY_RATES = {
    "worker_1": 50,
    "worker_2": 55,
    "worker_3": 45}

# Labor hours required per 10 linear feet of edging installed
EDGING_LABOR_HOURS_PER_10FT = {
    "none": 0.0,
    "plastic": 0.25,         # 15 minutes per 10 ft
    "metal": 0.5,            # 30 minutes per 10 ft
    "natural_stone": 1.0     # 1 hour per 10 ft
}

#FIXED COSTS

# Profit markup (25% over cost)
PROFIT_MARKUP = 0.25

# Overhead (e.g., 6% of base cost)
OVERHEAD_PERCENTAGE = 0.06

#ADDITIONAL COSTS

# Dirt removal cost per cubic yard
DIRT_REMOVAL_COST_PER_CUBIC_YARD = 30.00

# Delivery fees
DELIVERY_THRESHOLD_YARDS = 5        # Free if over 5 yards
DELIVERY_FEE_UNDER_THRESHOLD = 75.0

# Vehicle cost per mile (gas + wear & tear)
VEHICLE_COST_PER_MILE = 1.00
