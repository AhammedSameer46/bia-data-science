import matplotlib.pyplot as plt
import seaborn as sns

def bar_chart(df):

    if df is None:
        print("Load data first.")
        return

    plt.figure(figsize=(8,5))

    df['bedrooms'].value_counts().plot(kind='bar')

    plt.title("Number of Houses by Bedrooms")

    plt.xlabel("Bedrooms")

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