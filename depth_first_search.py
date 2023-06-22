class Node:

    def __init__(self, value):
        self.value = value
        self.children = []

    def insert(self, value):
        self.children.append(Node(value))


def depth_first_search(node: Node):
    queue = [node]

    while queue:
        current_node = queue.pop(0)
        print(current_node.value)
        queue.extend(current_node.children)


if __name__ == '__main__':
    root = Node(1)
    root.insert(2)
    root.insert(3)
    root.insert(4)
    root.children[0].insert(5)
    root.children[0].insert(6)
    root.children[0].insert(7)
    root.children[1].insert(8)
    root.children[1].insert(9)
    root.children[1].insert(10)
    root.children[2].insert(11)
    root.children[2].insert(12)
    root.children[2].insert(13)

    depth_first_search(root
