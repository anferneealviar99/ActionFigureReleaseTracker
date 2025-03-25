import tkinter as tk
from tkinter import ttk
import webbrowser
import web_scraper

def open_link(url):
    """Open figure link in browser"""
    webbrowser.open(url)
    
def update_widget():
    """Refresh widget with the latest figures"""
    
    for widget in frame.winfo_children():
        widget.destroy()
        
    figures = web_scraper.get_all_figures()
    
    for fig in figures:
        print(fig)
        lbl = ttk.Label(frame, text=f"{fig['name']} - {fig['price']} ({fig['store']})", cursor="hand2", wraplength=300)
        lbl.pack(anchor="w", padx=5, pady=2)
        lbl.bind("<Button-1>", lambda e, url=fig['link']: open_link(url))
        
    root.after(3600000, update_widget)
    

# Create GUI Window
root=tk.Tk()
root.title("Action Figure Listing Tracker")
root.geometry("500x500")
root.attributes("-topmost", True)
root.resizable(False, False)

# Scrollable Frame
canvas = tk.Canvas(root)
frame = tk.Frame(canvas)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=frame, anchor="nw")

frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

update_widget()
root.mainloop()