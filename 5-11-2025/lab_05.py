import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------
# Computer Science, Lab 05
# May 2022
# Your Name
# -----------------------------------------------------

def read_file(name):
    input_file = open(name, "r")
    number_buckets = int(input_file.readline())
    total_counties = int(input_file.readline())

    county_populations = np.zeros([total_counties], dtype="int")
    for county_number in range(total_counties):
        line = input_file.readline().split(",")
        county_populations[county_number] = int(line[1])
    county_populations.sort()
    input_file.close()

    return number_buckets, county_populations

def print_summary(averages):
    print("Population Grouping Summary")
    print("---------------------------")
    for grouping in range(len(averages)):
        print("Grouping", grouping + 1, "has a population average of",
              averages[grouping])

def calculate_averages(number_buckets, county_populations):
    n = len(county_populations) // number_buckets
    averages = np.zeros(number_buckets, dtype=int)

    for i in range(number_buckets):
        start = i * n
        end = start + n
        group = county_populations[start:end]
        averages[i] = int(np.mean(group))

    return averages

def graph_summary(averages):
    x = np.arange(1, len(averages) + 1)

    plt.figure()
    plt.plot(x, averages, "h--", color="cyan", markerfacecolor="blue")

    plt.title("Montana County Population Analysis")
    plt.xlabel("County Groupings")
    plt.ylabel("County Population Average")
    plt.xticks(x)
    plt.show()

# === DRIVER ===
number_buckets, county_populations = read_file("montana-counties.txt")
averages = calculate_averages(number_buckets, county_populations)
print_summary(averages)
graph_summary(averages)
