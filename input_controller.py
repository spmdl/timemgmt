from model import basenode, work_start, create_node, next_node


def tree(depth=-1, interval='', last_file=False):
    if depth == -1:
        print(f"\n.{basenode.root.key}")
        basenode.now_node = basenode.root

    else:
        if last_file:
            interval += '     '
        else:
            interval += '│    '

    now_node = basenode.now_node
    for num, node in enumerate(now_node.child_node):
        if num == len(now_node.child_node) - 1:
            print(f'{interval}└── {node.key}')
            last_file = True
        else:
            print(f'{interval}├── {node.key}')
            last_file = False

        # 檢查子節點是否存在
        if node.child_node:
            basenode.now_node = node
            tree(depth + 1, interval, last_file)

    return '\n'

def revise_node():
    return 'revise'

def break_prtn():
    now_node = basenode.now_node.parent_node
    basenode.now_node = now_node
    return f'返回到上一層 {basenode.now_node.key} 節點'

def save_xmind():
    basenode.end = 'e'
    basenode.main.plot_xmind(basenode.root)
    basenode.main.save_xmin('t', 'mindmap')
    return 'End'

def inpur_order(msg):
    order_mapping = {
        't': tree,
        'tree': tree,
        'c': create_node,
        'create': create_node,
        'n': next_node,
        'next': next_node,
        'r': revise_node,
        'revise': revise_node,
        'b': break_prtn,
        'e': save_xmind,
    }

    res = input(f'{msg}\n請輸入指令:')
    print(order_mapping.get(res, '請輸入正確指令')())

def input_data(main):
    work_start()
    basenode.main = main
    while not basenode.end:
        inpur_order('查看結構 t, 新增節點 c, 新增子結點 n,  修改節點 r,回上一層 b, 結束 e')

if __name__ == '__main__':
    input_data()
