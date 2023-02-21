import customtkinter as ctk 

class My_Frame(ctk.CTkFrame):
    def __init__(self, my_padx, my_pady, text, master, width, height, border_width, **kwargs):
        super().__init__(master = master,width = width, height = height, border_width = border_width, **kwargs)
        self.PADX = my_padx
        self.PADY = my_pady
        self.LABEL = ctk.CTkLabel(self, text= text, compound= ctk.LEFT, font=("helvitica", 20))
        self.LABEL.grid(padx= my_padx, pady = my_pady)
