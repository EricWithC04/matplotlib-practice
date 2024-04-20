import matplotlib.pyplot as plt

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