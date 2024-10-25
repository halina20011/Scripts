import getHoles
import random
import matplotlib.pyplot as plt

points = [];
for y in range(-2, 2, 1):
    for x in range(-2, 2, 1):
        points.append([x, y]);

squareMins = getHoles.SquareMins();
random.shuffle(points);

for point in points:
    squareMins.update(point[0], point[1], point);

points2 = squareMins.get();
print(points2);

x1, y1 = zip(*points);
x2, y2 = zip(*points2);

plt.scatter(x1, y1, color="blue");
plt.scatter(x2, y2, color="red");

plt.grid(True);
# plt.show();
