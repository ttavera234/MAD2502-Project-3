import matplotlib.pyplot as plt


def plot_histogram(x_axis: list[str], y_axis: list[int], title: str, x_label: str, y_label: str = "Number of Deaths") -> None:
    """
        Description:
            Visualizes the data passed in through a histogram
        Parameters:
            x_axis: Either a list of states, age groups, or genders
            y_axis: Number of casualties
            title: Title of the plot
            x_label: x-axis title
            y_label: y-axis title
    """

    plt.figure(figsize = (10,6))
    plt.bar(x_axis, y_axis)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

