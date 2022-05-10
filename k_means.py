import math
import csv

import matplotlib.pyplot as plt

data_points = []
for row in csv.reader(open('data.csv')):
    x = float(row[0])
    y = float(row[1])
    data_points.append([x, y])

centers = []
for row in csv.reader(open('centers.csv')):
    x = float(row[0])
    y = float(row[1])
    centers.append([x, y])

Clusters = []
for i in range(len(centers)):
    Clusters.append([])

iteration = 0
while True:
    Temp_Clusters = []
    for i in range(len(centers)):
        Temp_Clusters.append([])

    for i in range(len(data_points)):
        min_index = 0

        for j in range(len(centers)):
            new_dist = math.dist(data_points[i], centers[j])
            old_dist = math.dist(data_points[i], centers[min_index])

            if new_dist < old_dist:
                min_index = j

        Temp_Clusters[min_index].append(i)

    for c in range(len(centers)):
        if len(Temp_Clusters[c]) > 0:
            for j in range(2):
                total = 0
                for i in Temp_Clusters[c]:
                    total += data_points[i][j]

                avg = total / len(Temp_Clusters[c])
                centers[c][j] = avg

    if iteration > 1:
        shift = 0
        for i in range(len(Clusters)):
            for j in Clusters[i]:
                if j not in Temp_Clusters[i]:
                    shift += 1
        if shift < 10:
            Clusters = Temp_Clusters
            break

    Clusters = Temp_Clusters
    iteration += 1


def find_color(i):
    for j in range(len(Clusters)):
        if i in Clusters[j]:
            return j


x = []
y = []
c = []
for i in range(len(data_points)):
    x.append(data_points[i][0])
    y.append(data_points[i][1])
    c.append(find_color(i))

plt.scatter(x, y, c=c)


x = []
y = []
c = []
for i in range(len(centers)):
    x.append(centers[i][0])
    y.append(centers[i][1])
    c.append("black")

plt.scatter(x, y, c=c)
plt.show()
