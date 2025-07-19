# Crop yield prediction code
def predict_yield(area, crop_type):
    yield_per_hectare = {
        "rice": 2.5,
        "wheat": 3.2,
        "maize": 2.0
    }
    return yield_per_hectare.get(crop_type.lower(), 2.0) * area

