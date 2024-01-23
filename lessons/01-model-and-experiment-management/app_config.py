# MODELS
MODEL_VERSION = "0.0.1"
PATH_TO_PREPROCESSOR = f"/C:/Git/Stephanie/stephina/lessons/02-model-deployment/web_service/local_models/dv_v/{MODEL_VERSION}.pkl"
PATH_TO_MODEL = f"/C:/Git/Stephanie/stephina/lessons/02-model-deployment/web_service/local_models/model_v/{MODEL_VERSION}.pkl"
CATEGORICAL_COLS = ["PUlocationID", "DOlocationID", "passenger_count"]

# MISC
APP_TITLE = "TripDurationPredictionApp"
APP_DESCRIPTION = (
    "A simple API to predict trip duration in minutes "
    "for NYC yellow taxi trips, given a pickup, a dropoff location "
    "and a passenger count."
)
APP_VERSION = "0.0.1"
