import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Step 1: Load the Excel data into a DataFrame
    df = pd.read_excel("weather.csv")

    # Step 2–4: Process with a loop
    hottest_temp = float('-inf')
    coldest_temp = float('inf')
    hottest_day = None
    coldest_day = None
    rain_days = 0

    for index, row in df.iterrows():
        avg = row["tempavg"]

        # Find hottest day
        if avg > hottest_temp:
            hottest_temp = avg
            hottest_day = row

        # Find coldest day
        if avg < coldest_temp:
            coldest_temp = avg
            coldest_day = row

        # Count rainy days
        if "rain" in str(row["conditions"]).lower():
            rain_days += 1

    # Print hottest day
    print("Dates with hottest average temperature")
    print("-----------------------------------")
    print(f"Date: {hottest_day['datetime']}, Max Temp: {hottest_day['tempmax']}, Min Temp: {hottest_day['tempmin']}, Avg Temp: {hottest_day['tempavg']}\n")

    # Print coldest day
    print("Dates with coldest average temperature")
    print("-----------------------------------")
    print(f"Date: {coldest_day['datetime']}, Max Temp: {coldest_day['tempmax']}, Min Temp: {coldest_day['tempmin']}, Avg Temp: {coldest_day['tempavg']}\n")

    # Print rainy day count
    print("The number of days with rain: ", rain_days)


    # Step 5: Plotting
    plt.figure(figsize=(12, 6))  # Width = 12", Height = 6"

    # Plot max temperatures in red
    plt.plot(df["datetime"], df["tempmax"], color='darkred', label='Max Temp')

    # Plot min temperatures in blue
    plt.plot(df["datetime"], df["tempmin"], color='navy', label='Min Temp')

    # Titles and labels
    plt.title("Temperature Extremes")
    plt.xlabel("Date")
    plt.ylabel("Temperature")

    # Legend and formatting
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
