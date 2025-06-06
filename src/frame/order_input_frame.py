from src.frame.input_frame import InputFrame
from tkinter import filedialog
from src.services.processer_excel import processor


class OrderInputFrame(InputFrame):
    def __init__(self, parent, title, row):
        super().__init__(parent, title, row)
        
        
    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx")]
        )
        if file_path:
            file_name = file_path.split("/")[-1]
            self.file_label.configure(text=file_name)
            
            processor.orders_file_path = file_path