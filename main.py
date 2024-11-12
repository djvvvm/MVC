import tkinter as tk
from view import TextAnalyzerView
from controller import TextAnalyzerController

def main():
    root = tk.Tk()
    view = TextAnalyzerView(root)
    controller = TextAnalyzerController(view)
    root.mainloop()

if __name__ == "__main__":
    main()
