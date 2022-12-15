class Node:
    def __init__(self, label: str):
        self.height = self._init_height(label)
        self.label = label
        self.neighbors = []

    @staticmethod
    def _init_height(label):
        if label == 'S':
            return ord('a')
        elif label == 'E':
            return ord('z')
        return ord(label)

    def add_neighbor_if_allowed(self, neighbor: 'Node'):
        if self.height - neighbor.height < 2:  # This line changed
            self.neighbors.append(neighbor)


def shortest_path_dijkstra(nodes, start_node, end_nodes):
    min_distance_from_s = {
        node: 0 if node == start_node else 1_000_000_000
        for node in nodes
    }

    unvisited_nodes = set(nodes)

    while len(unvisited_nodes) > 0:
        unvisited_nodes_with_distances = {
            node: distance for node, distance in min_distance_from_s.items()
            if node in unvisited_nodes
        }
        unvisited_node_with_least_distance = \
            sorted(unvisited_nodes_with_distances.items(),
                   key=lambda kv: kv[1])[0][0]
        current_node = unvisited_node_with_least_distance
        unvisited_nodes.discard(current_node)

        for neighbor in current_node.neighbors:
            if neighbor in unvisited_nodes:
                new_length = min_distance_from_s[current_node] + 1
                if new_length < min_distance_from_s[neighbor]:
                    min_distance_from_s[neighbor] = new_length

    min_shortest_path = 10_000_000
    for end_node in end_nodes:
        shorted_path = min_distance_from_s[end_node]
        min_shortest_path = min(shorted_path, min_shortest_path)

    return min_shortest_path


def main():
    nodes_by_coordinates = {}

    with open('input') as lines:
        for row, line in enumerate(lines):
            line = line.rstrip()
            for col, char in enumerate(line):
                node = Node(char)
                nodes_by_coordinates[(row, col)] = node
                if row > 0:
                    node_above = nodes_by_coordinates[(row-1, col)]
                    node.add_neighbor_if_allowed(node_above)
                    node_above.add_neighbor_if_allowed(node)
                if col > 0:
                    node_to_left = nodes_by_coordinates[(row, col-1)]
                    node.add_neighbor_if_allowed(node_to_left)
                    node_to_left.add_neighbor_if_allowed(node)

    nodes = nodes_by_coordinates.values()
    node_e = [node for node in nodes if node.label == 'E'][0]
    nodes_a = [node for node in nodes if node.label == 'a']

    print(shortest_path_dijkstra(nodes, node_e, nodes_a))


if __name__ == "__main__":
    main()
