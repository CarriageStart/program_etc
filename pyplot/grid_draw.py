import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

mpl.use('qt5agg')

data = [
    ["abc000", 10.0, pd.to_datetime("2024-01-02")],
    ["abc001", 12.0, pd.to_datetime("2024-01-12")],
    ["abc002", 13.0, pd.to_datetime("2024-01-18")],
    ["abc003", 18.0, pd.to_datetime("2024-01-22")],
]
column = ["Lot ID", "Step", "F/O Date"]


def main() :
    df = pd.DataFrame(data, columns=column)

    fig = plt.figure(figsize=(6,3))
    gs = mpl.gridspec.GridSpec(1, 2)
    ax0 = fig.add_subplot(gs[0,0])
    ax1 = fig.add_subplot(gs[0,1])
    ax0.table(data, colLabels=column)
    sns.barplot(df, x="Step", y="Lot ID", ax=ax1)
    fig.show()
    

if __name__ == "__main__":
    main()
