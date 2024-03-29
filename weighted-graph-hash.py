import queue
import sys
import heapq

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
            self.__graph_dict[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        self.__graph_dict[vertex1][vertex2] = weight

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex, self.__graph_dict[vertex][neighbour]} not in edges:
                    edges.append([vertex, neighbour, self.__graph_dict[vertex][neighbour]])
        return edges

    def dijkstras(self, source):
        dist_map = {source: 0}
        visited = {}

        for v in graph.vertices():
            n = self.__min_dist(dist_map, visited)
            visited[n] = True

            if n is None:
                return None

            edges = self.__graph_dict[n]
            for e in edges.keys():
                if e not in dist_map:
                    dist_map[e] = edges[e] + dist_map[n]
                else:
                    dist_map[e] = min(dist_map[e], edges[e] + dist_map[n])

        return dist_map

    def dijkstras_dest(self, source, dest):
        dist_map = {source: 0}
        visited = {}
        path = {}
        final_path = [source]

        for v in graph.vertices():
            n = self.__min_dist(dist_map, visited)

            visited[n] = True

            if n is None:
                return None

            edges = self.__graph_dict[n]
            for e in edges.keys():
                if e not in dist_map:
                    dist_map[e] = edges[e] + dist_map[n]
                    path[e] = n
                elif edges[e] + dist_map[n] < dist_map[e]:
                    dist_map[e] = edges[e] + dist_map[n]
                    path[e] = n

            if n == dest:
                final_path = [dest]
                x = dest
                while x != source:
                    final_path.append(path[x])
                    x = path[x]
                break

        return dist_map[n], final_path


    @staticmethod
    def __min_dist(dist_map, visited_map):
        min_index = None
        min = sys.maxsize
        for v in graph.vertices():
            if (v in dist_map and dist_map[v] < min) and (v not in visited_map):
                min = dist_map[v]
                min_index = v
        return min_index

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
    g = {"a": {"b": 14, "d": 13},
         "b": {"1": 26, "c": 180, "a": 14},
         "c": {"b": 180, "d": 101, "4": 5, "e": 99, "2": 31},
         "d": {"a": 13, "e": 3, "c": 101},
         "e": {"f": 33, "g": 40, "d": 3, "c": 99},
         "f": {"4": 7, "g": 10, "e": 33},
         "g": {"f": 10, "e": 40},
         "1": {"3": 18, "2": 12, "b": 26},
         "2": {"c": 31, "4": 8, "3": 17, "1": 12},
         "3": {"2": 17, "1": 18},
         "4": {"2": 8, "c": 5, "f": 7},
         "Nan": {}
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

    print("Dijsktra's Shortest Path Dict:")
    print(graph.dijkstras("a"))

    print("Dijsktra's Shortest Path Destination:")
    print(graph.dijkstras_dest("a", "f"))
    print(graph.dijkstras_dest("c", "a"))
    print(graph.dijkstras_dest("g", "b"))
    print(graph.dijkstras_dest("3", "g"))
    print(graph.dijkstras_dest("1", "3"))
    print(graph.dijkstras_dest("e", "3"))
    print(graph.dijkstras_dest("Nan", "f"))
    print(graph.dijkstras_dest("f", "Nan"))

