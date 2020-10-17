import xmind
import time
from input_controller import input_data


class Mindmap:
    def __init__(self):
        self.filename = 'my.xmind'
        self.workbook = xmind.load(self.filename)
        self.sheet = None

        # xmind 初始化
        self.creat_xmind()

        # 開始輸入
        input_data(self)

    def creat_xmind(self):
        sheet = self.workbook.getPrimarySheet()
        self.sheet = sheet

    def plot_subnode(self, node, topic):
        for num, node in enumerate(node.child_node):
            subtopic = topic.addSubTopic()  # next node
            subtopic.setTitle(node.key) # content
            if node.link:subtopic.setURLHyperlink(node.link)

            # 檢查子節點是否存在
            if node.child_node:
                self.plot_subnode(node, subtopic)

    def plot_rootnode(self, node, sheet):
        root_topic = sheet.getRootTopic()  # creat root
        root_topic.setTitle(node.key)  # set root name
        return root_topic

    def plot_xmind(self, node):
        sheet = self.sheet
        sheet.setTitle("first sheet")

        root_topic = self.plot_rootnode(node, sheet)
        self.plot_subnode(node, root_topic)

    def save_xmin(self, file_name, folder_name):
        file_name = f"{file_name}_{time.strftime('%H%M', time.localtime(time.time()))}"
        xmind.save(self.workbook, path=f'{folder_name}/{file_name}.xmind')

if __name__ == "__main__" :
    mindmap = Mindmap()






