import customtkinter as ctk
from src.services.processor_excel import processor
from tkinter import filedialog, messagebox
import threading

class OutputFrame(ctk.CTkFrame):
    def __init__(self, parent, row):
        super().__init__(parent)
        self.grid(row=row, column=0, padx=10, pady=5, sticky="nsew")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        title_label = ctk.CTkLabel(
            self,
            text="คำสั่ง",
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, padx=5, pady=10)

        self.loading_label = ctk.CTkLabel(
            self,
            text="0.0 %",
            font=("Arial", 14),
            text_color=("gray60", "gray40")
        )
        self.loading_label.grid(row=1, column=0, padx=5, pady=5)
        
        self.process_btn = ctk.CTkButton(
            self,
            text="ประมวลผล",
            command=self.handle_process,
        )
        self.process_btn.grid(row=2, column=0, padx=5, pady=5)
        
        self.download_btn = ctk.CTkButton(
            self,
            text="ดาวน์โหลดผลลัพธ์",
            command=self.handle_download
        )
        self.download_btn.grid(row=3, column=0, padx=5, pady=(5, 10))
            
    def handle_process(self):
        self.process_btn.configure(state="disabled")

        try:
            thread = threading.Thread(target=processor.run_main_process)
            thread.daemon = True
            thread.start()
            self.update_id = self.after(1000, self.update_progress)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error processing files: {str(e)}")
    
    def handle_download(self):
        save_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")]
        )
        
        if save_path:
            try:
                processor.save(save_path)
            except Exception as e:
                messagebox.showerror("Error", f"Error saving results: {str(e)}")

    def update_progress(self):
        progress = processor.get_progress()
        if progress >= 100:
            self.loading_label.configure(text="100.0 %", text_color="green")
            self.process_btn.configure(state="normal")
            processor.current_row = 0
            self.after_cancel(self.update_id)
        else:
            self.loading_label.configure(text=f"{progress:.1f} %")
            self.update_id = self.after(100, self.update_progress)
