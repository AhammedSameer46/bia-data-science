from load_data import load_csv
from data_stats import show_statistics
from visualization import bar_chart, heat_map

df = None

while True:

    print("\n" + "=" * 35)
    print("      CSV DATA ANALYSIS TOOL")
    print("=" * 35)

    print("1. Load CSV File")
    print("2. Show Summary Statistics")
    print("3. Generate Bar Chart")
    print("4. Generate Heat Map")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":

        df = load_csv("Housing(in).csv")

        if df is not None:
            print("Dataset loaded successfully!")

    elif choice == "2":

        if df is None:
            print("Please load the CSV file first.")
        else:
            show_statistics(df)

    elif choice == "3":

        if df is None:
            print("Please load the CSV file first.")
        else:
            bar_chart(df)

    elif choice == "4":

        if df is None:
            print("Please load the CSV file first.")
        else:
            heat_map(df)

    elif choice == "5":

        print("Thank you for using CSV Data Analysis Tool.")
        break

    else:

        print("Invalid choice. Please enter a number between 1 and 5.")