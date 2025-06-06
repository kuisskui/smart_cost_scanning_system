import customtkinter as ctk
from tkinter import filedialog
from src.services.processer_excel import processor

class InputFrame(ctk.CTkFrame):
    def __init__(self, parent, title, row):
        super().__init__(parent)
        self.grid(row=row, column=0, padx=10, pady=5, sticky="ew")
        
        self.grid_columnconfigure(1, weight=1)
        
        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Arial", 16, "bold"),
            anchor="w"
        )
        title_label.grid(row=0, column=0, padx=(15, 10), pady=10, sticky="w")
        
        self.file_label = ctk.CTkLabel(
            self,
            text="ไม่มีไฟล์ที่อัพโหลด",
            height=32,
            anchor="e",
            width=200
        )
        self.file_label.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="e")
        
        self.browse_btn = ctk.CTkButton(
            self,
            text="อัพโหลดไฟล์",
            command=self.browse_file,
            width=120,
            height=32,
            font=("Arial", 13),
            hover_color=("#1f538d", "#14375e")
        )
        self.browse_btn.grid(row=0, column=2, padx=(0, 15), pady=10, sticky="e")
        
    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx *.xls")]
        )
        if file_path:
            file_name = file_path.split("/")[-1]
            self.file_label.configure(text=file_name)
            
            processor.history_file_path = file_path
