import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pyeda.inter import expr

# Função para desenhar a porta OR
def draw_or_gate(ax, x, y):
    ax.add_patch(patches.Wedge((x+1, y), 2, 45, 315, fill=True, edgecolor='black', lw=2, facecolor='lightgray'))
    ax.plot([x - 1.5, x], [y - 0.5, y - 0.5], color='black', lw=2)
    ax.plot([x - 1.5, x], [y + 0.5, y + 0.5], color='black', lw=2)
    ax.plot([x + 2, x + 3], [y, y], color='black', lw=2)
    ax.text(x - 1.8, y - 0.5, 'A', fontsize=12, verticalalignment='center')
    ax.text(x - 1.8, y + 0.5, 'B', fontsize=12, verticalalignment='center')
    ax.text(x + 3.2, y - 0.2, 'C', fontsize=12)

# Função para desenhar a porta AND
def draw_and_gate(ax, x, y):
    ax.add_patch(patches.Arc((x + 1, y), 2, 2, theta1=270, theta2=90, fill=True, edgecolor='black', lw=2, facecolor='lightgray'))
    ax.add_patch(patches.Rectangle((x, y - 1), 1, 2, fill=True, edgecolor='black', lw=2, facecolor='lightgray'))
    ax.plot([x - 1.5, x], [y - 0.5, y - 0.5], color='black', lw=2)
    ax.plot([x - 1.5, x], [y + 0.5, y + 0.5], color='black', lw=2)
    ax.plot([x + 2, x + 3], [y, y], color='black', lw=2)
    ax.text(x - 1.8, y - 0.5, 'A', fontsize=12, verticalalignment='center')
    ax.text(x - 1.8, y + 0.5, 'B', fontsize=12, verticalalignment='center')
    ax.text(x + 3.2, y - 0.2, 'Out', fontsize=12)

# Função para desenhar a porta NOT
def draw_not_gate(ax, x, y):
    ax.add_patch(patches.Polygon([[x-1, y-0.5], [x-1, y+0.5], [x, y]], fill=True, edgecolor='black', lw=2, facecolor='lightgray'))
    ax.add_patch(patches.Circle((x + 0.5, y), 0.2, fill=True, edgecolor='black', lw=2, facecolor='lightgray'))
    ax.plot([x - 2, x - 1], [y, y], color='black', lw=2)
    ax.plot([x + 0.7, x + 2], [y, y], color='black', lw=2)
    ax.text(x - 2.5, y, 'A', fontsize=12, verticalalignment='center')
    ax.text(x + 2.2, y, 'Out', fontsize=12)

# Função para desenhar a porta NAND
def draw_nand_gate(ax, x, y):
    draw_and_gate(ax, x, y)
    ax.add_patch(patches.Circle((x + 2.5, y), 0.2, fill=True, edgecolor='black', lw=2, facecolor='lightgray'))
    ax.plot([x + 2.7, x + 3], [y, y], color='black', lw=2)

# Função para desenhar a porta NOR
def draw_nor_gate(ax, x, y):
    draw_or_gate(ax, x, y)
    ax.add_patch(patches.Circle((x + 2.5, y), 0.2, fill=True, edgecolor='black', lw=2, facecolor='lightgray'))
    ax.plot([x + 2.7, x + 3], [y, y], color='black', lw=2)

# Função para desenhar a porta XOR
def draw_xor_gate(ax, x, y):
    ax.add_patch(patches.Wedge((x+1, y), 2, 45, 315, fill=True, edgecolor='black', lw=2, facecolor='lightgray'))
    ax.add_patch(patches.Arc((x, y), 2, 2, theta1=45, theta2=315, fill=False, edgecolor='black', lw=2))
    ax.plot([x - 2, x], [y - 0.5, y - 0.5], color='black', lw=2)
    ax.plot([x - 2, x], [y + 0.5, y + 0.5], color='black', lw=2)
    ax.plot([x + 2, x + 3], [y, y], color='black', lw=2)
    ax.text(x - 2.2, y - 0.5, 'A', fontsize=12, verticalalignment='center')
    ax.text(x - 2.2, y + 0.5, 'B', fontsize=12, verticalalignment='center')
    ax.text(x + 3.2, y - 0.2, 'Out', fontsize=12)

# Função para processar a expressão e desenhar o circuito
def process_expression(expression):
    # Convertendo a expressão para uma forma booleana com PyEDA
    boolean_expr = expr(expression)
    print(f"Expressão Booleana: {boolean_expr}")
    
    # Criar a figura e os eixos
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim([-5, 10])
    ax.set_ylim([-5, 5])

    # Desenhar o circuito lógico equivalente
    if boolean_expr.equivalent(expr("A | B")):
        draw_or_gate(ax, 0, 0)
    elif boolean_expr.equivalent(expr("A & B")):
        draw_and_gate(ax, 0, 0)
    elif boolean_expr.equivalent(expr("~A")):
        draw_not_gate(ax, 0, 0)
    elif boolean_expr.equivalent(expr("A & B").not_()):
        draw_nand_gate(ax, 0, 0)
    elif boolean_expr.equivalent(expr("A | B").not_()):
        draw_nor_gate(ax, 0, 0)
    elif boolean_expr.equivalent(expr("A ^ B")):
        draw_xor_gate(ax, 0, 0)
    
    # Ajustar e mostrar o gráfico
    ax.axis('off')
    plt.show()

# Receber expressão do usuário
user_input = input("Digite uma expressão lógica (por exemplo, A | B, A & B, ~A, A ^ B): ")
process_expression(user_input)