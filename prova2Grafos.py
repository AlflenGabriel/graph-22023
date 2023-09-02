import itertools

def create_graph(vertices, edges):

  graph = {}
  for vertex in vertices:
    graph[vertex] = []
  for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
  return graph

def degree(graph, vertex):
  """Returns the degree of the given vertex."""

  return len(graph[vertex])

def neighbors(graph, vertex):
  """Returns the neighbors of the given vertex."""

  return graph[vertex]

def is_complete(graph):
  """Returns True if the graph is complete, False otherwise."""

  for vertex in graph:
    for neighbor in graph:
      if vertex != neighbor and neighbor not in graph[vertex]:
        return False

  return True

def is_path(graph, vertices):
  """Returns True if the given vertices represent a path, False otherwise."""

  if len(vertices) == 0:
    return True

  if vertices[0] not in graph or vertices[-1] not in graph:
    return False

  for i in range(len(vertices) - 1):
    if vertices[i] not in graph[vertices[i + 1]]:
      return False

  return True

def is_circuit(graph, vertices):
  """Returns True if the given vertices represent a circuit, False otherwise."""

  if is_path(graph, vertices):
    return vertices[0] == vertices[-1]

  return False

num_vertices = 5
vertices = [chr(65 + i) for i in range(num_vertices)]
edges = list(itertools.combinations(vertices, 2))
edges = [(edge[0], edge[1]) for edge in edges]
graph = create_graph(vertices, edges)


print("A verificacao booleana se o Grafo e caminho: ", is_path(graph, vertices))
print("A verificacao booleana se o Grafo e circuito: ", is_circuit(graph, vertices))
print("O grau de um determinado vertice: ", degree(graph, 'A'))
print("A vizinhanca de um determinado vertice", neighbors(graph, 'A'))
print("A verificacao booleana se o Grafo e completo.", is_complete(graph))

def is_connected(graph):
    """Returns True if the graph is connected, False otherwise."""
    
    if not graph:
        return False
    
    start_vertex = list(graph.keys())[0]
    
    visited = set()
    stack = [start_vertex]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

    return len(visited) == len(graph)

num_vertices = 5
vertices = [chr(65 + i) for i in range(num_vertices)]
edges = list(itertools.combinations(vertices, 2))
edges = [(edge[0], edge[1]) for edge in edges]
graph = create_graph(vertices, edges)

print("A verificacao booleana se o Grafo e conexo: ", is_connected(graph))
