import statistics

sensor_data = [
    {"id": 1, "value": 12.5},
    {"id": 2, "value": -999.0},
    {"id": 3, "value": 14.2},
    {"id": 4, "value": 13.8},
    {"id": 5, "value": -999.0}
]

def filter_and_average(data_list):
    valid_value = []

    for data in data_list:
        if data["value"] > 0.0:
            valid_value.append(data["value"])
    
    return statistics.mean(valid_value)

average_result =filter_and_average(sensor_data)
print(f"平均値：{average_result}")