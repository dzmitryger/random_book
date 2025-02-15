import tkinter as tk
from tkinter import filedialog
import random


file_path = None

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Select TXT file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    
    if file_path:
        button_run.config(state=tk.NORMAL)
        file_label.config(text=f"List of books:\n {file_path}")

def get_random_line():
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    random_line = random.choice(lines).strip()
                    result_label.config(text=f"Today you are reading:\n {random_line}")
                else:
                    result_label.config(text="Book list is empty!")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")
    else:
        result_label.config(text="Book list not selected!")

root = tk.Tk()
root.title("Selecting a random book from the Book List")
root.geometry("500x200")

button_select_file = tk.Button(root, text="Select book list (*.txt)", command=select_file)
button_select_file.pack(pady=10)

file_label = tk.Label(root, text="List of books selected", padx=20, pady=10)
file_label.pack()

button_run = tk.Button(root, text="Choose a random book", command=get_random_line, state=tk.DISABLED)
button_run.pack(pady=10)

result_label = tk.Label(root, text="...", padx=20, pady=20)
result_label.pack()

root.mainloop()
