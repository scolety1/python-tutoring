import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Step 1: Load the Excel data into a DataFrame
    df = pd.read_excel("Weather.xlsx")

    # Step 2: Find the day with the hottest average temperature
    hottest_day = df.loc[df["tempavg"].idxmax()]
    print("Dates with hottest average temperature")
    print("-----------------------------------")
    print(f"Date: {hottest_day['datetime']}, Max Temp: {hottest_day['tempmax']}, Min Temp: {hottest_day['tempmin']}, Avg Temp: {hottest_day['tempavg']}\n")

    # Step 3: Find the day with the coldest average temperature
    coldest_day = df.loc[df["tempavg"].idxmin()]
    print("Dates with coldest average temperature")
    print("-----------------------------------")
    print(f"Date: {coldest_day['datetime']}, Max Temp: {coldest_day['tempmax']}, Min Temp: {coldest_day['tempmin']}, Avg Temp: {coldest_day['tempavg']}\n")

    # Step 4: Count days with 'Rain' in the 'conditions' column
    rain_days = df["conditions"].str.contains("Rain", case=False).sum()
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
