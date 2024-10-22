import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_and_gate(ax, x, y):
    ax.add_patch(patches.Arc((x, y), 2, 2, theta1=270, theta2=90, fill=False, edgecolor='black', lw=2))
    ax.add_patch(patches.Rectangle((x-1, y-1), 1, 2, fill=False, edgecolor='black', lw=2))
    ax.text(x - 0.8, y - 0.2, 'A', fontsize=12)
    ax.text(x - 0.8, y + 0.8, 'B', fontsize=12)
    ax.text(x + 1.2, y - 0.2, 'Out', fontsize=12)

def draw_or_gate(ax, x, y):
    ax.add_patch(patches.Wedge((x-1, y), 2, 45, 315, fill=False, edgecolor='black', lw=2))
    ax.add_patch(patches.Arc((x, y), 2, 2, theta1=270, theta2=90, fill=False, edgecolor='black', lw=2))
    ax.text(x - 1.8, y - 0.2, 'A', fontsize=12)
    ax.text(x - 1.8, y + 0.8, 'B', fontsize=12)
    ax.text(x + 1.2, y - 0.2, 'Out', fontsize=12)

def draw_not_gate(ax, x, y):
    ax.add_patch(patches.Polygon([[x-1, y-1], [x-1, y+1], [x+1, y]], fill=False, edgecolor='black', lw=2))
    ax.add_patch(patches.Circle((x+1.5, y), 0.2, fill=False, edgecolor='black', lw=2))
    ax.text(x - 1.8, y - 0.2, 'A', fontsize=12)
    ax.text(x + 1.8, y - 0.2, 'Out', fontsize=12)

# Criar a figura e os eixos
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim([-4, 6])
ax.set_ylim([-3, 3])

# Desenhar portas lógicas
draw_and_gate(ax, 0, 0)
draw_or_gate(ax, 4, 0)
draw_not_gate(ax, -4, 0)

# Ajustar e mostrar o gráfico
ax.axis('off')
plt.show()