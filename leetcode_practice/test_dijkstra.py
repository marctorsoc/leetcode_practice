import heapq
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    label: str
    connections: dict[str, int]
    value: int = 1_000
    parent: Optional["Node"] = None

    def __lt__(self, other):
        return self.value < other.value
    

def test_exercise():
    A = Node("A", {"B": 3, "C": 2})
    B = Node("B", {"A": 3, "D": 3, "E": 5})
    C = Node("C", {"A": 2, "E": 2, "H": 4, "F": 3})
    D = Node("D", {"B": 3, "E": 1})
    E = Node("E", {"B": 5, "C": 2, "D": 1, "G": 5})
    F = Node("F", {"C": 3, "G": 5})
    G = Node("G", {"E": 5, "F": 5})
    H = Node("H", {"C": 4})

    # List of all nodes (optional, for convenience)
    nodes = {node.label: node for node in [A, B, C, D, E, F, G, H]}

    path = dijkstra(nodes, "A", "G")
    print(f"The shortest path is {path}")


def dijkstra(nodes: dict[str, Node], start: str, end: str):
    """
    heap = all nodes
    mark all nodes with value inf except for start
    while len(heap) > 0:
        heapify
        node = pop min
        if node in seen:
            continue
        if node is end:
            break
        add node to seen
        
        for each connection from node
            dist_from_node = node.value + weights[node, conn]
            if dist_from_node < conn.value:
                conn.value = dist_from_node
                conn.parent = node

    path = [node.label]
    while node.parent:
        path.append(node.parent.label)
        node = node.parent
    
    """

    q = list(nodes.values())
    seen = set()
    for node_label, node in nodes.items():
        node.value = 0 if node_label == start else 1000
    
    while len(q) > 0:
        heapq.heapify(q)
        print("\n" + "\n".join(str({"label": node.label, "value": node.value}) for node in q))
        
          # reorder the heap given last update
        node = heapq.heappop(q)  # remove min
        print(f"Visiting {node.label}")

        if node.label == end:
            break
        seen.add(node.label)  # mark as visited

        # for each connection, ignore if seen, then update its value to node.value + weight
        for conn_label, conn_weight in node.connections.items():
            if conn_label in seen:
                continue
            conn_node = nodes[conn_label]
            dist_from_node = node.value + conn_weight
            if conn_node.value > dist_from_node:
                conn_node.value = dist_from_node
                conn_node.parent = node

    path = [node.label]
    while node.parent:
        path.append(node.parent.label)
        node = node.parent
    return path[::-1]
