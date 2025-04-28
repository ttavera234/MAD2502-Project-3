import matplotlib.pyplot as plt


def plot_histogram(x_axis: list[str], y_axis: list[int], title: str, x_label: str, y_label: str = "Number of Deaths"):
    plt.figure(figsize = (10,6))
    plt.bar(x_axis, y_axis)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

