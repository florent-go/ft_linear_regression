import csv
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("data.csv")

# def erreur_quadratique(m, b, points):
#     total_error = 0
#     for i in range(len(points)):
#         x = points.iloc[i].km
#         y = points.iloc[i].price
#         total_error += (y - (m * x + b)) ** 2
#     total_error / float(len(points))

def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].km
        y = points.iloc[i].price

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
    
    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b

m = 0
b = 0
L = 0.01
iteration = 4000
points = (data - data.min())/ (data.max() - data.min())
for i in range(iteration):
    m, b = gradient_descent(m, b, points, L)

plt.scatter(points.km, points.price, color="black")
plt.plot(list(range(0, 2)), [m * x + b for x in range(0, 2)], color="red")
plt.show()

