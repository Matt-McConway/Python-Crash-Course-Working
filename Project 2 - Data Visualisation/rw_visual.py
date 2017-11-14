import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make Random walks as long as the program is active
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    # Set the size of the plotting window.
    plt.figure(dpi=320, figsize=(21, 9))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # Emphasize the first and last points.
    # Changed from 0 to x/y_value[0] to future-proof against changes to random walk class
    plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break

# Up to page 336