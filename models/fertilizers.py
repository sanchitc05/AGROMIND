# Fertilizer recommendation logic
def recommend_fertilizer(N, P, K):
    if N < 50:
        return "Add Urea (Nitrogen-rich fertilizer)"
    elif P < 40:
        return "Add SSP (Single Super Phosphate)"
    elif K < 40:
        return "Add MOP (Muriate of Potash)"
    else:
        return "Soil nutrient levels are adequate"
