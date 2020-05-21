import json
from datetime import datetime, timedelta

def subtract_time_delta_from_date_string(time_delta, date_time_string):
    format = "%Y-%m-%dT%H:%M:%S.%fZ"
    base_time = datetime.strptime(date_time_string, format)
    result = base_time - time_delta
    return result.strftime(format)

# Load data.json file into memory

json_file_path = "resources/data.json"
with open(json_file_path) as json_file:
    json_object = json.load(json_file)

# Extract & Print to console: Home & Away (Corners, Fouls, Goal Kicks, ThrowIns and Goals)

    message_template = "{0}:\n\tHome: {1}\n\tAway: {2}\n"
    for key in ["Corners", "Fouls", "GoalKicks", "ThrowIns", "Goals"]:
        home_value = json_object[key]["Score"]["Home"]
        away_value = json_object[key]["Score"]["Away"]
        print(message_template.format(key, home_value, away_value))

# Modify:
    # FixtureId to 1000

    json_object["FixtureId"] = 1000

    # CustomerId to 1

    json_object["CustomerId"] = 1

    # Start Times: First Half, to (Date – 1h30m) & Second Half to (Date – 30m)

    first_half = json_object["StartTimes"]["FirstHalf"]
    time_delta_1 = timedelta(hours=1, minutes=30)
    json_object["StartTimes"]["FirstHalf"] = subtract_time_delta_from_date_string(time_delta_1, first_half)

    second_half = json_object["StartTimes"]["SecondHalf"]
    time_delta_2 = timedelta(minutes=30)
    json_object["StartTimes"]["SecondHalf"] = subtract_time_delta_from_date_string(time_delta_2, second_half)

# Print modified payload

    print("### Modified payload: ###\n")
    print(json.dumps(json_object, indent=2))

