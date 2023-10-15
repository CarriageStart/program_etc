
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

mpl.use("QTAGG")


def main() -> None:
    fig = plt.figure(figsize=(8, 2.5), facecolor="#f1f1f1")
    ax = fig.add_axes((0.1, 0.1, 0.8, 0.8), facecolor="#e1e1e1")
    
    x = np.linspace(-2, 2, 1000)
    y_packet = np.exp(-x**2)
    y = np.cos(40.*x) * y_packet

    ax.plot(x, y)
    ax.plot(x, y_packet, "g")
    ax.plot(x, -y_packet, "g")

    ax.set_xlabel("x")
    ax.set_ylabel("y")

    plt.show()


if __name__=="__main__":
    main()

