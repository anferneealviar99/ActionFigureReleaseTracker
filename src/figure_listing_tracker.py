import tkinter as tk
from tkinter import ttk
import webbrowser
import web_scraper

def open_link(url):
    """Open figure link in browser"""
    webbrowser.open(url)
    
def update_widget():
    """Refresh widget with the latest figures"""
        
    figures = web_scraper.get_all_figures()
    for tab in tab_mcfarlane_dc.winfo_children():
        tab.destroy()
        
    for tab in tab_marvel_legends.winfo_children():
        tab.destroy()
        
    for tab in tab_transformers.winfo_children():
        tab.destroy()
        
    dc_figs = list(filter(lambda x: x['line'] == "McFarlane DC", figures))
    
    for fig in dc_figs:
        lbl = ttk.Label(tab_mcfarlane_dc, text=f"{fig['name']} - {fig['price']} ({fig['store']})", cursor="hand2", wraplength=300)
        lbl.pack(anchor="w", padx=5, pady=2)
        lbl.bind("<Button-1>", lambda e, url=fig['link']: open_link(url))
        
    marvel_figs = list(filter(lambda x: x['line'] == "Marvel Legends", figures))
    
    for fig in marvel_figs:
        lbl = ttk.Label(tab_marvel_legends, text=f"{fig['name']} - {fig['price']} ({fig['store']})", cursor="hand2", wraplength=300)
        lbl.pack(anchor="w", padx=5, pady=2)
        lbl.bind("<Button-1>", lambda e, url=fig['link']: open_link(url))
        
    transformers_figs = list(filter(lambda x: x['line'] == "Transformers", figures))
    for fig in transformers_figs:
        lbl = ttk.Label(tab_transformers, text=f"{fig['name']} - {fig['price']} ({fig['store']})", cursor="hand2", wraplength=300)
        lbl.pack(anchor="w", padx=5, pady=2)
        lbl.bind("<Button-1>", lambda e, url=fig['link']: open_link(url))
            
    root.after(3600000, update_widget)
    
class ScrollableFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = tk.Canvas(self)
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.scrollbar.pack(side="right", fill="y")
        
        self.update_scrollregion()
        
    def update_scrollregion(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def add_widget(self, widget):
        widget.pack(anchor="w", padx=5, pady=2)
    

# Create GUI Window
root=tk.Tk()
root.title("Action Figure Listing Tracker")
root.geometry("500x500")
root.attributes("-topmost", True)
root.resizable(False, False)

# Create notebook
notebook = ttk.Notebook(root)

# Create tabs for each category
tab_mcfarlane_dc = ttk.Frame(notebook)
tab_marvel_legends = ttk.Frame(notebook)
tab_transformers = ttk.Frame(notebook)

# Add tabs to notebook
notebook.add(tab_mcfarlane_dc, text="McFarlane DC")
notebook.add(tab_marvel_legends, text="Marvel Legends")
notebook.add(tab_transformers, text="Transformers")

mcfarlane_dc_scrollable = ScrollableFrame(tab_mcfarlane_dc)
marvel_legends_scrollable = ScrollableFrame(tab_marvel_legends)
transformers_scrollable = ScrollableFrame(tab_transformers)

# Pack the notebook (tabs)
mcfarlane_dc_scrollable.pack(fill="both", expand=True)
marvel_legends_scrollable.pack(fill="both", expand=True)
transformers_scrollable.pack(fill="both", expand=True)

notebook.pack(expand=True, fill="both")

# Update the widget (load the figures)
update_widget()

# Start the GUI loop
root.mainloop()