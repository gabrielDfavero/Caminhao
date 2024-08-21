import networkx as nx
import matplotlib.pyplot as plt

# N = int #numero de ilhas (vértices/node)
# M = int #numero de pontes (arestas/edges)
# S = int #numero de sedes
# A, B e P compões as informações de uma ponte#
# A = int #1ª ilha
# B = int #2ª ilha
# P = int #peso máximo permitido na ponte
# Saida = int #peso máximo que pode ser transportado de um deposito ate uma sede

f = open('entrada.txt', 'r')

#tranformar ints do arquivo em um vetor
dados = f.read()
dados = dados.split()
vetor_dados = []
vetor_dados = [int(num) for num in dados]
#print(vetor_dados)

#Ler a primeira linha
N = vetor_dados[0]
M = vetor_dados[1]
S = vetor_dados[2]
#Criar os vértices
G = nx.Graph()
vertices = range(1,N+1)
G.add_nodes_from(vertices)
#Criar as arestas:
arestas = []
for i in range(1,M+1):
  A = vetor_dados[3*i]
  B = vetor_dados[1+3*i]
  P = vetor_dados[2+3*i]
  arestas.append((A,B,P))
  #print(A,B,P)
G.add_weighted_edges_from(arestas)
#print(G.edges(data=True))

#Plotar o grafo:
pos = nx.spring_layout(G)
nx.draw(G,pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos,nx.get_edge_attributes(G,'weight'))
plt.show()

arv = nx.maximum_spanning_tree(G,"weight")

pos = nx.spring_layout(arv)
nx.draw(arv,pos, with_labels=True)
labels = nx.get_edge_attributes(arv, 'weight')
nx.draw_networkx_edge_labels(arv, pos,nx.get_edge_attributes(arv,'weight'))
plt.show()

def achar_menor_peso(a,A,B):
  menor_caminho= nx.shortest_path(a, source=A, target=B)
  menor_peso = 9999
  for i in range (len(menor_caminho)-1):
    vertice1 = menor_caminho[i]
    vertice2 = menor_caminho[i+1]
    peso_atual = int(a[vertice1][vertice2]['weight'])
    if peso_atual < menor_peso:
      menor_peso = peso_atual
  return menor_peso

for i in range((M+1)*3,len(vetor_dados),2):
  A = vetor_dados[i]
  B = vetor_dados[i+1]
  saida = achar_menor_peso(arv,A,B)
  print(saida)