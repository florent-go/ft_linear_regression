import sys
import matplotlib.pyplot as plt

# ===================Define========================= #

INT_MAX = sys.maxsize
INT_MIN = -1 * sys.maxsize

# ===================Parse_File========================= #

def ParseFile():
    file = open("data.csv")
    lines = []
    lines = file.readlines()

    dataX = []
    dataY = []
    i = 0
    for line in lines:
        if i > 0:
            x, y = line.split(',')
            dataX.append(int(x))
            dataY.append(int(y))
        i += 1
    return [dataX, dataY]



# ===============erreur_quadratique===================== #

def erreur_quadratique(m, b, normData):
    total_error = 0
    n = len(normData)
    for i in range(n):
        x = normData[0][i]
        y = normData[1][i]
        total_error += (y - (m * x + b)) ** 2
    total_error / float(n)
    return total_error

# =================gradient_descent===================== #

def gradient_descent(m_now, b_now, normData, L):
    m_gradient = 0
    b_gradient = 0

    n = len(normData[0])
    for i in range(n):
        x = normData[0][i]
        y = normData[1][i]

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
    
    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b

# ======================normalizeData===================== #

def getMinMaxData(data):
    xmin = INT_MAX
    xmax = INT_MIN
    ymin = INT_MAX
    ymax = INT_MIN
    for i in range(len(data[0])):
        if data[0][i] < xmin:
            xmin = data[0][i]
        if data[0][i] > xmax:
            xmax = data[0][i]
        if data[1][i] < ymin:
            ymin = data[1][i]
        if data[1][i] > ymax:
            ymax = data[1][i]
    return xmin, xmax, ymin, ymax

def normalizeData(data):
    xmin, xmax, ymin, ymax = getMinMaxData(data)
    dataX = []
    dataY = []
    for i in range(len(data[0])):
        x = data[0][i]
        y = data[1][i]
        normX = (x - xmin) / (xmax  - xmin)
        normY = (y - ymin) / (ymax - ymin)
        dataX.append(normX)
        dataY.append(normY)
    return [dataX, dataY]
        
                

# ======================Main========================= #

data = ParseFile()
normData = normalizeData(data)

m = 0
b = 0
L = 0.1
iteration = 4000
for i in range(iteration):
    m, b = gradient_descent(m, b, normData, L)


# ======================Resultat==================== #

print(f"Value Normalized m = {m} b = {b}")

xmin, xmax, ymin, ymax = getMinMaxData(data)

unNorm_m = m * (ymax - ymin) / (xmax - xmin)
unNorm_b = ymin + ((ymax - ymin) * b) + unNorm_m * (-xmin)

print(f"Value Unnormalized m = {unNorm_m} b = {unNorm_b}")

print(f"y = mx + b")

print(f"y = {round(unNorm_m,4)}x + {round(unNorm_b,4)}")

print(f"error_quadratique = {erreur_quadratique(m, b, normData)}")

# ======================Save_file==================== #

file = open("save.csv", "w")
file.write(f"{unNorm_m} {unNorm_b}")
file.close()

# ======================Affichage==================== #

# plot with various axes scales
plt.figure()

# Value Unormalized
plt.subplot(221)
plt.plot(data[0], data[1], 'ro')
plt.xlabel('km')
plt.ylabel('price')
plt.yscale('linear')
plt.title('Value Unormalized')
plt.grid(True)

# Value Normalized
plt.subplot(222)
plt.plot(normData[0], normData[1], "ro")
plt.xlabel('km')
plt.ylabel('price')
plt.yscale('linear')
plt.title('Value Normalized')
plt.grid(True)

# Value UnNormalized with linear_regression courbe
r = range(int(xmin), int(xmax), 1000)
plt.subplot(223)
plt.scatter(data[0], data[1], color="black")
plt.xlabel('km')
plt.ylabel('price')
plt.plot(list(r), [unNorm_m * x + unNorm_b for x in r], color="red")
plt.yscale('linear')
plt.title('Value UnNormalized with linear_regression courbe')
plt.grid(True)

# Value Normalized with linear_regression courbe
plt.subplot(224)
plt.scatter(normData[0], normData[1], color="black")
plt.xlabel('km')
plt.ylabel('price')
plt.plot(list(range(0, 2)), [m * x + b for x in range(0, 2)], color="red")
plt.yscale('linear')
plt.title('Value Normalized with linear_regression courbe')
plt.grid(True)

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()