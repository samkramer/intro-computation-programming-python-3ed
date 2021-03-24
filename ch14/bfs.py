# 14.2 Graph Optimization Problems
# Breadth-first-search shortest path algorithm

# # Figure 14-7 on page 294
class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self._name = name
        
    def get_name(self):
        return self._name
    
    def __str__(self):
        return self._name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self._src = src
        self._dest = dest
        
    def get_source(self):
        return self._src
    
    def get_destination(self):
        return self._dest
    
    def __str__(self):
        return self._src.get_name() + '->' + self._dest.get_name()

# Figure 14-8 on page 296
class Digraph(object):
    # nodes is a list of the nodes in the graph
    # edges is a dict mapping each node to a list of its children
    def __init__(self):
        self._nodes = []
        self._edges = {}
        
    def add_node(self, node):
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node] = []
            
    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in graph')
        self._edges[src].append(dest)
        
    def children_of(self, node):
        return self._edges[node]
    
    def has_node(self, node):
        return node in self._nodes
        
    def __str__(self):
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result = (result + src.get_name() + '->'
                         + dest.get_name() + '\n')
        return result[:-1] # omit final newline

        
def print_path(path):
    """Assumes path is a list of nodes"""
    return '->'.join(map(str, path))

# # Figure 14-11 on page 303
def BFS(graph, start, end, to_print = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    init_path = [start]
    path_queue = [init_path]
    
    while len(path_queue) > 0:
        # Get and remove oldest element in path_queue
        tmp_path = path_queue.pop(0)
        if to_print:
            print('Current BFS path:', print_path(tmp_path))
            
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path
        
        for next_node in graph.children_of(last_node):
            if next_node not in tmp_path:
                new_path = tmp_path + [next_node]
                if to_print:
                    print('    New candidate path:', print_path(new_path))
                path_queue.append(new_path)
    return None


# test_sp modifed as per code on page 303
# Output:
#   Current BFS path: 0
#   Current BFS path: 0->1
#   Current BFS path: 0->2
#   Current BFS path: 0->1->2
#   Current BFS path: 0->2->3
#   Current BFS path: 0->2->4
#   Current BFS path: 0->1->2->3
#   Current BFS path: 0->1->2->4
#   Current BFS path: 0->2->3->4
#   Current BFS path: 0->2->3->5
#   Shortest path found by BFS: 0->2->3->5
def test_SP():
    nodes = []
    for name in range(6): # Create 6 nodes
        nodes.append(Node(str(name)))
        
    g = Digraph()
    for n in nodes:
        g.add_node(n)
        
    g.add_edge(Edge(nodes[0],nodes[1]))
    g.add_edge(Edge(nodes[1],nodes[2]))
    g.add_edge(Edge(nodes[2],nodes[3]))
    g.add_edge(Edge(nodes[2],nodes[4]))
    g.add_edge(Edge(nodes[3],nodes[4]))
    g.add_edge(Edge(nodes[3],nodes[5]))
    g.add_edge(Edge(nodes[0],nodes[2]))
    g.add_edge(Edge(nodes[1],nodes[0]))
    g.add_edge(Edge(nodes[3],nodes[1]))
    g.add_edge(Edge(nodes[4],nodes[0]))
    
    sp = BFS(g, nodes[0], nodes[5], to_print = True)
    print('Shortest path found by BFS:', print_path(sp))

    
if __name__ == "__main__":
    test_SP()
