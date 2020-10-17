class BaseNode:
    def __init__(self):
        self.root = None
        self.now_node = None
        self.end = False
        self.main = None


class Node:
    def __init__(self, name, link):
        self.key = name
        self.link = link
        self.child_node = []
        self.parent_node = None


basenode = BaseNode()

def create_node():
    new_node = input_node()
    basenode.now_node.child_node.append(new_node)

    # if not node_data.parent_node:
    #     node_data.child_node.append(new_node)
    return f'成功新增 {new_node.key} 節點'

def next_node():
    new_node = input_node()
    _node = basenode.now_node
    basenode.now_node = _node.child_node[-1]
    basenode.now_node.child_node.append(new_node)
    basenode.now_node.parent_node = _node

    # return new_node
    return f'成功新增 {new_node.key} 子節點'

def input_node():
    node_name = input(f'請輸入子節點名稱:')
    node_link = input(f'請輸入子節點連結:')
    new_node = Node(node_name, node_link)
    return new_node

def work_start():
    node_name = input(f'請輸入根節點名稱:')
    node_link = input(f'請輸入根節點連結:')
    res_node = Node(node_name, node_link)
    basenode.root = res_node
    basenode.now_node = res_node

