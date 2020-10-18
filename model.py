class BaseNode:
    def __init__(self):
        self.root = None
        self.now_node = None
        self.end = False
        self.main = None
        self.work_minutes = 25
        self.break_minutes = 0


class Node:
    def __init__(self, name, link, node_notes, spend_time=0):
        self.key = name
        self.link = link
        self.notes = node_notes
        self.spend_time = spend_time
        self.child_node = []
        self.parent_node = None


basenode = BaseNode()

def input_node(spend_time):
    node_name = input(f'請輸入子節點名稱:')
    node_link = input(f'請輸入子節點連結:')
    node_notes = input(f'請輸入子節點備註:')
    new_node = Node(node_name, node_link, node_notes, spend_time)
    return new_node

def work_start():
    node_name = input(f'請輸入根節點名稱:')
    node_link = input(f'請輸入根節點連結:')
    node_notes = input(f'請輸入根節點備註:')
    res_node = Node(node_name, node_link, node_notes)
    basenode.root = res_node
    basenode.now_node = res_node

