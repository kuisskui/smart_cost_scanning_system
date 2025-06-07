from src.frame.input_frame import InputFrame
from tkinter import filedialog
from src.services.processor_excel import processor


class HistoryInputFrame(InputFrame):
    def __init__(self, parent, title, row):
        super().__init__(parent, title, row)
        
        
    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx")]
        )
        if file_path:
            file_name = file_path.split("/")[-1]
            self.file_label.configure(text=file_name)
            
            processor.set_history_file_path(file_path)
