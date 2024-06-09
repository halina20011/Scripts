import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


class Debug:
    def __init__(self):
        self.fig, self.ax = plt.subplots();
        plt.axis("equal");

    def rect(self, x, y, width, height, color):
        left_bottom_x = x - width / 2;
        left_bottom_y = y - height / 2;
        rectangle = Rectangle((left_bottom_x, left_bottom_y), width, height, edgecolor='black', facecolor=color);

        # Plotting
        ax.add_patch(rectangle);
        ax.plot(x, y, 'ro', color="green", markersize=3, label='Center of Rectangle');

    def addPoint(self, x, y, color):
        self.ax.plot(x, y, marker='o', color=color);

    def draw(self):
        plt.show();

