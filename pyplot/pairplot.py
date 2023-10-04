import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", color_codes=True)

def draw_default(iris: pd.DataFrame) -> None:
    sns.pairplot(iris, hue="species", palette="husl")
    plt.show()

def draw_specific_columns(iris: pd.DataFrame) -> None:
    sns.pairplot(
        iris, hue="species", palette="husl", vars=["sepal_width", "sepal_length"]
    )
    plt.show()

def draw_jointplot(iris: pd.DataFrame, kind=None) -> None:
    if (kind is None) :
        sns.jointplot(
            data=iris, x="petal_width", y="petal_length"
        )
    else:
        sns.jointplot(
            data=iris, x="petal_width", y="petal_length", kind=kind
        )
    plt.show()


def draw_tsplot() -> None:
    x = np.linspace(0, 15, 31)
    data = np.sin(x) + np.random.rand(10, 31) + np.random.randn(10,1)

    est = data.mean(axis=0)
    sd = data.std(axis=0)
    cis = (est-sd, est+sd)
    plt.fill_between(x, cis[0], cis[1], alpha=0.2)
    plt.plot(x, est)
    plt.show()


def main() -> None:
    iris = sns.load_dataset("iris")
    print("Iris data : \n", iris.head())


    draw_funcs = [
         draw_default, draw_specific_columns, draw_jointplot
    ]
    for func in draw_funcs:
        func(iris)

    draw_jointplot(iris, "kde")
    draw_tsplot()

if __name__=="__main__":
    main()



