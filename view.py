import tkinter as tk
from tkinter import ttk

class TextAnalyzerView:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Frequency Analyzer")

        self.input_label = ttk.Label(root, text="Enter your text:")
        self.input_label.pack()

        self.text_input = tk.Text(root, height=10, width=50)
        self.text_input.pack()

        self.analyze_button = ttk.Button(root, text="Analyze")
        self.analyze_button.pack()

        self.result_label = ttk.Label(root, text="Word Frequency:")
        self.result_label.pack()

        self.result_output = tk.Text(root, height=10, width=50, state="disabled")
        self.result_output.pack()

    def get_input_text(self):
        return self.text_input.get("1.0", tk.END).strip()

    def display_results(self, results):
        self.result_output.config(state="normal")
        self.result_output.delete("1.0", tk.END)
        for word, count in results.items():
            self.result_output.insert(tk.END, f"{word}: {count}\n")
        self.result_output.config(state="disabled")
