import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Função para desenhar porta AND
def draw_and_gate(ax, x, y):
    # Parte frontal arredondada
    ax.add_patch(patches.Arc((x + 1, y), 2, 2, theta1=270, theta2=90, fill=False, edgecolor='black', lw=2))
    # Parte retangular
    ax.add_patch(patches.Rectangle((x, y - 1), 1, 2, fill=False, edgecolor='black', lw=2))
    # Entradas e saída
    ax.plot([x - 1, x], [y - 0.5, y - 0.5], color='black', lw=2)
    ax.plot([x - 1, x], [y + 0.5, y + 0.5], color='black', lw=2)
    ax.plot([x + 2, x + 3], [y, y], color='black', lw=2)
    # Nomes das entradas e saída
    ax.text(x - 1.5, y - 0.5, 'A', fontsize=12, verticalalignment='center')
    ax.text(x - 1.5, y + 0.5, 'B', fontsize=12, verticalalignment='center')
    ax.text(x + 3.2, y - 0.2, 'Out', fontsize=12)

# Função para desenhar porta OR
def draw_or_gate(ax, x, y):
    # Parte arredondada em arco
    ax.add_patch(patches.Wedge((x + 1, y), 2, 45, 315, fill=False, edgecolor='black', lw=2))
    # Entrada da esquerda
    ax.plot([x - 1.5, x], [y - 0.5, y - 0.5], color='black', lw=2)
    ax.plot([x - 1.5, x], [y + 0.5, y + 0.5], color='black', lw=2)
    # Saída
    ax.plot([x + 2, x + 3], [y, y], color='black', lw=2)
    # Nomes das entradas e saída
    ax.text(x - 1.8, y - 0.5, 'A', fontsize=12, verticalalignment='center')
    ax.text(x - 1.8, y + 0.5, 'B', fontsize=12, verticalalignment='center')
    ax.text(x + 3.2, y - 0.2, 'Out', fontsize=12)

# Função para desenhar porta NOT
def draw_not_gate(ax, x, y):
    # Triângulo da porta NOT
    ax.add_patch(patches.Polygon([[x - 1, y - 0.5], [x - 1, y + 0.5], [x, y]], fill=False, edgecolor='black', lw=2))
    # Círculo da negação
    ax.add_patch(patches.Circle((x + 0.5, y), 0.2, fill=False, edgecolor='black', lw=2))
    # Entrada e saída
    ax.plot([x - 2, x - 1], [y, y], color='black', lw=2)
    ax.plot([x + 0.7, x + 2], [y, y], color='black', lw=2)
    # Nomes das entradas e saída
    ax.text(x - 2.5, y, 'A', fontsize=12, verticalalignment='center')
    ax.text(x + 2.2, y, 'Out', fontsize=12)

# Criar a figura e os eixos
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim([-3, 10])
ax.set_ylim([-3, 3])

# Desenhar portas lógicas
draw_and_gate(ax, 0, 1)
draw_or_gate(ax, 5, 1)
draw_not_gate(ax, -2, -2)

# Ajustar e mostrar o gráfico
ax.axis('off')
plt.show()