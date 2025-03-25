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

notebook.pack(expand=True, fill="both")

# Create a canvas for each tab to make it scrollable
tab_mcfarlane_dc_canvas = tk.Canvas(tab_mcfarlane_dc)
tab_mcfarlane_dc_frame = tk.Frame(tab_mcfarlane_dc_canvas)
tab_mcfarlane_dc_scrollbar = ttk.Scrollbar(tab_mcfarlane_dc, orient="vertical", command=tab_mcfarlane_dc_canvas.yview)
tab_mcfarlane_dc_canvas.configure(yscrollcommand=tab_mcfarlane_dc_scrollbar.set)
tab_mcfarlane_dc_canvas.pack(side="left", fill="both", expand=True)
tab_mcfarlane_dc_canvas.create_window((0, 0), window=tab_mcfarlane_dc_frame, anchor="nw")
tab_mcfarlane_dc_scrollbar.pack(side="right", fill="y")

# Repeat for other tabs
tab_marvel_legends_canvas = tk.Canvas(tab_marvel_legends)
tab_marvel_legends_frame = tk.Frame(tab_marvel_legends_canvas)
tab_marvel_legends_scrollbar = ttk.Scrollbar(tab_marvel_legends, orient="vertical", command=tab_marvel_legends_canvas.yview)
tab_marvel_legends_canvas.configure(yscrollcommand=tab_marvel_legends_scrollbar.set)
tab_marvel_legends_canvas.pack(side="left", fill="both", expand=True)
tab_marvel_legends_canvas.create_window((0, 0), window=tab_marvel_legends_frame, anchor="nw")
tab_marvel_legends_scrollbar.pack(side="right", fill="y")

tab_transformers_canvas = tk.Canvas(tab_transformers)
tab_transformers_frame = tk.Frame(tab_transformers_canvas)
tab_transformers_scrollbar = ttk.Scrollbar(tab_transformers, orient="vertical", command=tab_transformers_canvas.yview)
tab_transformers_canvas.configure(yscrollcommand=tab_transformers_scrollbar.set)
tab_transformers_canvas.pack(side="left", fill="both", expand=True)
tab_transformers_canvas.create_window((0, 0), window=tab_transformers_frame, anchor="nw")
tab_transformers_scrollbar.pack(side="right", fill="y")

# Pack the notebook (tabs)
notebook.pack(expand=True, fill="both")

# Update the widget (load the figures)
update_widget()

# Start the GUI loop
root.mainloop()