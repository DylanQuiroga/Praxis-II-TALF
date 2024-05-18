from graphviz import Digraph

# Crear un gráfico dirigido
dot = Digraph()

# Añadir nodos
dot.node('A')
dot.node('B')
dot.node('C')
dot.node('D')

# Añadir aristas con pesos (distancias)
dot.edge('A', 'B', label='1.5')
dot.edge('B', 'C', label='2.2')
dot.edge('C', 'D', label='3.1')
dot.edge('D', 'A', label='4.6')

# Imprimir el gráfico en formato DOT
print(dot.source)