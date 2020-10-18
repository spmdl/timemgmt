from model import basenode, work_start, input_node
from tomato import Tomato, tomato

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

def change_node(res, target_node):
    target_node.key = res.key
    target_node.link = res.link
    target_node.notes = res.notes
    target_node.spend_time = res.spend_time

def traversal_node(now_node, name):
    for num, node in enumerate(now_node.child_node):
        if node.key == name:
            res = input_node()
            change_node(res, node)
            break
        # 檢查子節點是否存在
        if node.child_node:
            traversal_node(node, name)

def revise_node():
    target_node = input(f'請輸入要修改的節點名稱:')
    traversal_node(basenode.root, target_node)
    return f'修改成功'

def break_prtn():
    if not basenode.now_node.parent_node: return f'已在最上層'
    now_node = basenode.now_node.parent_node
    basenode.now_node = now_node
    return f'返回到上一層 {basenode.now_node.key} 節點'

def save_xmind():
    basenode.end = 'e'
    basenode.main.plot_xmind(basenode.root)
    basenode.main.save_xmin('t', 'mindmap')
    return 'End'

def start_tomato():
    ret = tomato.start(tomato.work_minutes, tomato.break_minutes)
    basenode.now_node.spend_time += tomato.spend_time
    return ret

def set_tomato():
    tomato.work_minutes = input(f'請輸入計時的時間:')
    tomato.break_minutes = input(f'請輸入休息時間:')
    return f'計時 {tomato.work_minutes} 分鐘、休息 {tomato.break_minutes} 分鐘'

def get_tomato():
    if not basenode.now_node.spend_time:
        return

    ret = basenode.now_node.spend_time
    basenode.now_node.spend_time = 0
    return ret

def create_node():
    spend_time = get_tomato()
    new_node = input_node(spend_time)
    basenode.now_node.child_node.append(new_node)

    return f'成功新增 {new_node.key} 節點'

def next_node():
    if not basenode.now_node.child_node: return f'請先輸入 c 創建節點'
    spend_time = get_tomato()
    new_node = input_node(spend_time)
    _node = basenode.now_node
    basenode.now_node = _node.child_node[-1]
    basenode.now_node.child_node.append(new_node)
    basenode.now_node.parent_node = _node

    # return new_node
    return f'成功新增 {new_node.key} 子節點'

def error_order():
    return f'請輸入正確指令'

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
        's': start_tomato,
        'st': set_tomato,
        'e': save_xmind,
    }

    res = input(f'{msg}\n請輸入指令:')
    print(order_mapping.get(res, error_order)())

def input_data(main):
    work_start()
    basenode.main = main
    while not basenode.end:
        inpur_order('查看結構 t, 新增節點 c, 新增子結點 n,  修改節點 r, 回上一層 b, 蕃茄鐘啟動 s, 設定蕃茄鐘時間 st, 結束 e')

if __name__ == '__main__':
    input_data()
