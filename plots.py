import matplotlib.pyplot as plt
import numpy as np

# Create points to classify
x_plus = [1, 1, 5, 5]
y_plus = [1, 5, 1, 5]
x_minus = [3]
y_minus = [3]

def initial_plot():
    # Plot figure with 4 plus points and 1 minus point
    fig, ax = plt.subplots()
    ax.hold(True)
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.scatter(x_plus, y_plus, color='blue', marker='^', s=100);
    ax.scatter(x_minus, y_minus, color='red', marker='v', s=100);
    return fig

def step_1(fig):
    # First step classifies the two blue points on the left correct, but the
    # ones on the right incorrectly
    ax = fig.gca()
    ax.set_title("Step 1")
    ax.axvline(x=2, ymin=0, ymax=8, linestyle=':', color = 'k')
    ax.axvspan(0, 2, color='b', alpha=0.2, lw=0)
    ax.axvspan(2, 6, color='r', alpha=0.2, lw=0)
    return fig

def emphasize_incorrect():
    fig, ax = plt.subplots()
    ax.hold(True)
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.scatter(x_plus, y_plus, color='blue', marker='^', s=100);
    ax.scatter(x_minus, y_minus, color='red', marker='v', s=100);
    # Add weight to blue points on the right
    ax.scatter([5, 5], [5, 1], marker='^', s=200);
    return fig

def step_2(fig):
    ax = fig.gca()
    ax.set_title("Step 2")
    ax.axvline(x=2, ymin=0, ymax=8, linestyle=':', color = 'k')
    ax.axvspan(0, 2, color='b', alpha=0.2, lw=0)
    ax.axvspan(2, 6, color='r', alpha=0.2, lw=0)
    ax.axvline(x=4, ymin=0, ymax=8, linestyle=':', color = 'k')
    ax.axvspan(0, 4, color='r', alpha=0.2, lw=0)
    ax.axvspan(4, 6, color='b', alpha=0.2, lw=0)
    return fig

def show_hypotheses():
    fig, axarray = plt.subplots(1,2, sharex=True, sharey=True)
    fig.set_size_inches(4, 2)

    for idx, ax in enumerate(axarray):
	ax.hold(True)
	ax.set_xlim(0, 6)
	ax.set_ylim(0, 6)

	ax.scatter(x_plus, y_plus, color='blue', marker='^', s=100);
	ax.scatter(x_minus, y_minus, color='red', marker='v', s=100);
	ax.set_title("Hypothesis {}".format(idx + 1))

    axarray[0].axvline(x=2, ymin=0, ymax=6, linestyle=':', color = 'k')
    axarray[0].axvspan(0, 2, color='b', alpha=0.2, lw=0);
    axarray[0].axvspan(2, 6, color='r', alpha=0.2, lw=0);
    axarray[1].axvline(x=4, ymin=0, ymax=6, linestyle=':', color = 'k')
    axarray[1].axvspan(0, 4, color='r', alpha=0.2, lw=0);
    axarray[1].axvspan(4, 6, color='b', alpha=0.2, lw=0);
    return fig

def combined_hypothesis():
    # FINAL 
    fig, ax = plt.subplots()
    ax.set_title("Combined hypothesis")
    ax.hold(True)
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.scatter(x_plus, y_plus, color='blue', marker='^', s=100);
    ax.scatter(x_minus, y_minus, color='red', marker='v', s=100);
    ax.axvline(x=2, ymin=0, ymax=6, linestyle=':', color = 'k')
    ax.axvline(x=4, ymin=0, ymax=6, linestyle=':', color = 'k')
    ax.axvspan(0, 2, color='b', alpha=0.2, lw=0);
    ax.axvspan(2, 4, color='r', alpha=0.2, lw=0);
    ax.axvspan(4, 6, color='b', alpha=0.2, lw=0);
    return fig
