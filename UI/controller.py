import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self.roles = []
        self.load_roles()
        self.artists = []
        self.classifica = []
        self.load_classifica


    def load_roles(self):
        self.roles = self._model.get_roles()

    def load_classifica(self):
        self.classifica = self._model.get_classifica()

    def handle_crea_grafo(self,e):
        role = self._view.dd_ruolo.value
        self._model.build_graph(role)
        n_nodes, n_edges = self._model.get_graph_details()
        self._view.list_risultato.controls.clear()
        self._view.list_risultato.controls.append(ft.Text(f"Nodi: {n_nodes} | Archi: {n_edges}"))
        self._view.update()



    def handle_classifica(self, e):
        self._view.list_risultato.controls.clear()
        self._view.list_risultato.controls.append(ft.Text('Artisti in ordine decrescente di influenza:'))
        for a in self.classifica:
            self._view.list_risultato.controls.append(ft.Text(f"{a[0]} -> Delta = {a[1]}"))
        self._view.update()