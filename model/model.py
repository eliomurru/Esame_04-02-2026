import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.artists = []
        self.artists_map = {}
        self.roles = []
        self.nodes = []
        self.classifica = []

    def get_roles(self):
        self.roles = DAO.get_all_roles()
        return self.roles

    def load_artists(self, role: str):
        self.artists = DAO.get_artists_by_role(role)


    def load_nodes(self, role: str):
        self.nodes = DAO.get_nodes(role)

    def build_graph(self,role):
        self.G.clear()
        self.load_artists(role)
        self.load_nodes(role)
        for artist in self.artists:
            self.artists_map[artist.id] = artist
        for id in self.nodes:
            self.G.add_node(self.artists_map[id])

        for i, a1 in enumerate(self.nodes):
            for a2 in self.nodes[i+1:]:
                if a1 == a2:
                    continue
                else:
                    p1 = a1.produttivita
                    p2 = a2.produttivita
                    if p1==p2:
                        continue
                    else:
                        weight = abs(p1-p2)
                        if p1 < p2:
                            self.G.add_edge(p1, p2, weight=weight)
                        else:
                            self.G.add_edge(p2, p1, weight=weight)


    def get_graph_details(self):
        return self.G.number_of_nodes(), self.G.number_of_edges()

    def classifica(self):
        for a in self.nodes:
            influenza = 0
            for out_edge in self.G.out_edges(a):
                influenza += self.G[a][out_edge]['weight']
            for in_edge in self.G.in_edges(a):
                influenza -= self.G[a][in_edge]['weight']
            self.classifica.append((a, influenza))

        self.classifica = sorted(self.classifica, key=lambda x: x[1], reverse=True)
        return self.classifica


