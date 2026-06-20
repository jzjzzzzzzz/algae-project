import matplotlib.pyplot as plt

def plot_growth(algae_history):
    plt.plot(algae_history)
    plt.xlabel("Step")
    plt.ylabel("Algae amount")
    plt.title("Algae Growth Over Time")
    plt.show()