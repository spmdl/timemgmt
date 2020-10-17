class BaseNode:
    def __init__(self):
        self.root = None
        self.now_node = None
        self.first_node = None
        self.end = False


class Node:
    def __init__(self, name, link):
        self.key = name
        self.link = link
        self.child_node = []
        self.parent_node = None


