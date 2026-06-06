import matplotlib.pyplot as plt
import seaborn as sns

def bar_chart(df):

    if df is None:
        print("Load data first.")
        return

    print("\nAvailable Columns:")
    print(list(df.columns))

    column = input("\nEnter column name for Bar Chart: ")

    if column not in df.columns:
        print("Invalid column name!")
        return

    plt.figure(figsize=(8,5))

    df[column].value_counts().plot(kind='bar')

    plt.title(f"Bar Chart of {column}")

    plt.xlabel(column)

    plt.ylabel("Count")

    plt.show()


def heat_map(df):

    if df is None:
        print("Load data first.")
        return

    numeric_df = df.select_dtypes(include='number')

    corr = numeric_df.corr()

    plt.figure(figsize=(10,8))

    sns.heatmap(corr, annot=True, cmap="coolwarm")

    plt.title("Correlation Heatmap")

    plt.show()