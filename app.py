import matplotlib.pyplot as plt
import random

x1 = [1, 2, 3, 4]
y1 = [13, 21, 6, 34]
x2 = [2, 3, 5, 6]
y2 = [19, 4, 26, 20]

# Grafico de Linea
plt.plot(x1, y1, color="red", linewidth=5, label="linea 1")
plt.plot(x2, y2, color="green", linewidth=5, label="linea 2")
plt.legend()
plt.show()

# Grafico de barras
plt.bar(x1, y1, color="blue", linewidth=3, label="barras")
plt.legend()
plt.show()

# Grafico de torta
plt.pie(y1, labels=x1)
plt.axis("equal")
plt.title("torta")
plt.show()

# Grafico de histograma
histo_data = [[random.randint(1, 100) for _ in range(40)]]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(histo_data, bins=bins, color="green", histtype="bar", rwidth=0.8)
plt.title("histograma")
plt.ylabel("eje Y")
plt.xlabel("eje X")
plt.show()

# Grafico de Dispersion
dx1 = [0.25, 1.25, 2.25, 3.25, 4.25]
dy1 = [10, 55, 80, 32, 40]
dx2 = [0.75, 1.75, 2.75, 3.75, 4.75]
dy2 = [42, 26, 50, 10, 16]

plt.scatter(dx1, dy1, color="red", label="Datos 1")
plt.scatter(dx2, dy2, color="green", label="Datos 2")

plt.title("Grafico de dispersión")
plt.ylabel("eje Y")
plt.xlabel("eje X")
plt.legend()
plt.show()