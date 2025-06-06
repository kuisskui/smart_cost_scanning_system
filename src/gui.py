import customtkinter as ctk
from src.frame.history_input_frame import HistoryInputFrame
from src.frame.order_input_frame import OrderInputFrame
from src.frame.text_input_frame import TextInputFrame
from src.frame.output_frame import OutputFrame
from src.frame.footer_frame import FooterFrame

class GraphicUserInterface(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("ระบบหาราคาสินค้าอัจฉริยะ")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        self.history_frame = HistoryInputFrame(self, "ประวัติการซื้อสินค้า", 0)
        self.orders_frame = OrderInputFrame(self, "รายการสินค้า", 1)
        
        self.text_input_frame = TextInputFrame(self, 3)

        self.output_frame = OutputFrame(self, 4)
        
        self.footer_frame = FooterFrame(self, 5)
