import xmind
import time
from input_controller import work_start


class Mindmap:
    def __init__(self):
        self.filename = 'my.xmind'
        self.workbook = xmind.load(self.filename)
        self.sheet = None

    def creat_xmind(self):
        sheet = self.workbook.getPrimarySheet()
        # time_name = basic_sheet(sheet, workbook)
        self.sheet = sheet

    def plot_xmind(self):

        sheet = self.sheet
        sheet.setTitle("first sheet")

        root_topic = sheet.getRootTopic()  # creat root
        root_topic.setTitle("root")  # set root name

        r2 = root_topic.addSubTopic()  # next node
        r2.setTitle("one") # content

        r3 = r2.addSubTopic()  # next node
        r3.setTitle("two")  # content

        r4 = r3.addSubTopic()  # next node
        r4.setTitle("three")  # content

    def save_xmin(self, file_name, folder_name):
        file_name = f"{file_name}_{time.strftime('%H%M', time.localtime(time.time()))}"
        xmind.save(self.workbook, path=f'{folder_name}/{file_name}.xmind')

if __name__ == "__main__" :
    mindmap = Mindmap()
    mindmap.creat_xmind()
    work_start()
    mindmap.save_xmin('t', 'mindmap')







