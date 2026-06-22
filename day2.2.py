measurements = {"Sample_A": 12.5, "Sample_B": 8.0, "Sample_C": 15.2, "Sample_D": 5.4}
valid_results = []

for i in measurements.values():
    if i >= 10.0:
        valid_results.append(i * 1.5)

print(valid_results)