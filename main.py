import customtkinter as ctk, theme
from src.gui import GraphicUserInterface

def main():
    ctk.set_appearance_mode("System")  # Use system theme
    ctk.set_default_color_theme("blue")  # Set default color theme    
    
    app = GraphicUserInterface()
    app.mainloop()

if __name__ == "__main__":
    main() 