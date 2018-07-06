from scrapy.exporters import JsonItemExporter
import time

class rmrbPipeline:
    def __init__(self):
        j = time.strftime("人民日报%Y年%m月%d日.json")
        self.file = open(j, 'wb')
        # 初始化 exporter 实例，执行输出的文件和编码
        self.exporter = JsonItemExporter(self.file,encoding='utf-8',ensure_ascii=False)
        # 开启倒数
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    # 将 Item 实例导出到 json 文件
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item