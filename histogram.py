import matplotlib.pyplot as plt

def plot_histogram(data, title = "Epidemic Cases", xlabel = "State", ylabel= "Number of Cases"):

    states = list(data.keys())
    case_counts = list(data.values())

    plt.figure(figsize = (10,6))
    plt.bar(states, case_counts)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
