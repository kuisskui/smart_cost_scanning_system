import customtkinter as ctk
from src.services.processor_excel import processor
from datetime import datetime
from dateutil.relativedelta import relativedelta

class TextInputFrame(ctk.CTkFrame):
    def __init__(self, parent, row):
        super().__init__(parent)
        self.grid(row=row, column=0, padx=10, pady=0, sticky="nsew")
        
        self.grid_columnconfigure(1, weight=1)  # Make middle column expandable
        
        self.create_widgets()
        
    def create_widgets(self):
        self.text_input_label = ctk.CTkLabel(self, text="ตั้งเเต่วันที่")
        self.text_input_label.grid(row=0, column=0, padx=15, pady=10, sticky="w")

        self.text_input = ctk.CTkEntry(self, width=200, placeholder_text="ตัวอย่าง 24/08/2566")
        self.text_input.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.set_date_btn = ctk.CTkButton(self, text="ตกลง", command=self.set_date, width=120, height=32)
        self.set_date_btn.grid(row=0, column=2, padx=(0, 15), pady=10, sticky="e")

    def set_date(self):
        processor.date = be_date_to_datetime(self.text_input.get())
        self.text_input.configure(text_color="green")

def be_date_to_datetime(be_date: str) -> datetime:

    if be_date == "":
        return datetime.today() + relativedelta(years=543)
    
    day, month, year_be = map(int, be_date.split("/"))
    year_ce = year_be

    return datetime(year_ce, month, day)