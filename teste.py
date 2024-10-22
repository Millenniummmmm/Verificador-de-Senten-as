from pyeda.inter import expr
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Função para desenhar a porta OR
def draw_or_gate(ax, x, y):
    ax.add_patch(patches.Wedge((x+1, y), 2, 45, 315, fill=False, edgecolor='black', lw=2))
    ax.plot([x - 1.5, x], [y - 0.5, y - 0.5], color='black', lw=2)
    ax.plot([x - 1.5, x], [y + 0.5, y + 0.5], color='black', lw=2)
    ax.plot([x + 2, x + 3], [y, y], color='black', lw=2)
    ax.text(x - 1.8, y - 0.5, 'A', fontsize=12, verticalalignment='center')
    ax.text(x - 1.8, y + 0.5, 'B', fontsize=12, verticalalignment='center')
    ax.text(x + 3.2, y - 0.2, 'C', fontsize=12)

# Função para processar a expressão e desenhar o circuito
def process_expression(expression):
    # Convertendo a expressão para uma forma booleana com PyEDA
    boolean_expr = expr(expression)
    print(f"Expressão Booleana: {boolean_expr}")
    
    # Criar a figura e os eixos
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlim([-4, 6])
    ax.set_ylim([-3, 3])

    # Desenhar a porta OR para a expressão A | B
    draw_or_gate(ax, 0, 0)

    # Ajustar e mostrar o gráfico
    ax.axis('off')
    plt.show()

# Exemplo de entrada em lógica proposicional
logical_expression = "A | B"  # Exemplo de expressão: A OR B
process_expression(logical_expression)