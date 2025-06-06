import customtkinter as ctk


class FooterFrame(ctk.CTkFrame):
    def __init__(self, parent, row):
        super().__init__(parent)
        self.grid(row=row, column=0, padx=10, pady=5, sticky="ew")
        
        # Configure grid weights
        self.grid_columnconfigure(0, weight=1)  # Center the content
        
        # Creator info label
        creator_label = ctk.CTkLabel(
            self,
            text="Created by: kuisskui | Version 1.0",
            font=("Arial", 12),
            text_color=("gray60", "gray70")
        )
        creator_label.grid(row=0, column=0, padx=10, pady=5) 