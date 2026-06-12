# 导入依赖
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.core.window import Window
import pdfplumber
import os

# 主界面布局
class PDF2TXTLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(PDF2TXTLayout, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10

        # 状态提示文本
        self.status_label = Label(text="请选择PDF文件", font_size=16)
        self.add_widget(self.status_label)

        # 文件选择器
        self.file_chooser = FileChooserListView()
        # 只显示 pdf 文件
        self.file_chooser.filters = ["*.pdf"]
        self.add_widget(self.file_chooser)

        # 转换按钮
        self.convert_btn = Button(text="开始转换 PDF → TXT", font_size=16, size_hint=(1, 0.2))
        self.convert_btn.bind(on_press=self.do_convert)
        self.add_widget(self.convert_btn)

    # 核心转换逻辑（复用你原来的PDF提取文本代码）
    def do_convert(self, instance):
        try:
            # 获取选中的PDF路径
            selected = self.file_chooser.selection
            if not selected:
                self.status_label.text = "⚠️ 未选择PDF文件！"
                return

            pdf_path = selected[0]
            # 同目录生成同名 TXT
            dir_path = os.path.dirname(pdf_path)
            pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
            txt_path = os.path.join(dir_path, f"{pdf_name}.txt")

            self.status_label.text = "⏳ 正在提取文本..."
            all_text = ""

            # 逐页提取文本
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        all_text += text + "\n"

            # 写入TXT
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(all_text)

            self.status_label.text = f"✅ 转换成功！\n保存路径：{txt_path}"

        except Exception as e:
            self.status_label.text = f"❌ 转换失败：{str(e)}"

# 主APP
class PDF2TXTApp(App):
    def build(self):
        self.title = "PDF转TXT工具"
        return PDF2TXTLayout()

# 程序入口
if __name__ == "__main__":
    PDF2TXTApp().run()