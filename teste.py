from pyeda.inter import expr
from pyeda.boolalg.bdd import bddvar
import pydot
from IPython.display import Image

# Definir as variáveis booleanas
a, b, c = map(bddvar, 'abc')

# Definir a expressão booleana
f = a & b | a & c | b & c

# Gerar a representação DOT
dot_data = f.to_dot()

# Salvar a representação DOT em um arquivo temporário
with open("boolean_expression.dot", "w") as f:
    f.write(dot_data)

# Usar o pydot para converter o arquivo DOT em PNG
(graph,) = pydot.graph_from_dot_file("boolean_expression.dot")
graph.write_png("boolean_expression.png")

# Exibir a imagem no Colab
Image("boolean_expression.png")