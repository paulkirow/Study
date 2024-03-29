""" A Python Class
A simple Python graph class, demonstrating the essential
facts and functionalities of graphs.
"""
import queue


class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def bfs_search(self, source, dest):
        if source == dest:
            return True

        visited = {source: True}

        q = queue.Queue()
        for e in self.__graph_dict[source]:
            print("put " + e)
            q.put(e)

        while not q.empty():
            n = q.get()
            print("get " + n + " q = " + str(q.qsize()))
            if n == dest:
                return True
            else:
                visited[n] = True
            for e in self.__graph_dict[n]:
                if e not in visited:
                    print("put " + e + " q = " + str(q.qsize()))
                    q.put(e)

        return False

    def dfs_search(self, source, dest, visited):
        if source == dest:
            return True

        visited[source] = True

        for e in self.__graph_dict[source]:
            if e in visited:
                break
            is_found = self.dfs_search(e, dest, visited)
            if is_found:
                return True

        return False

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":
    g = {"a": ["b"],
         "b": ["1", "c"],
         "c": ["d", "4","e"],
         "d": ["a", "e"],
         "e": ["f", "g"],
         "f": ["4"],
         "g": ["f"],
         "1": ["3", "2"],
         "2": ["c"],
         "3": ["2"],
         "4": ["2"]
         }

    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph:")
    print(graph.vertices())

    print("Add an edge:")
    graph.add_edge({"a", "z"})

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x", "y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())

    print("BFS")
    print("a to f: " + str(graph.bfs_search('a', 'f')))
    print("g to a: " + str(graph.bfs_search('g', 'a')))

    print("DFS")
    print("a to f: " + str(graph.dfs_search('a', 'f', {})))
    print("g to a: " + str(graph.dfs_search('g', 'a', {})))
