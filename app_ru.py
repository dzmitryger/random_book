import tkinter as tk
from tkinter import filedialog
import random


file_path = None

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Выберите TXT файл", filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")))
    
    if file_path:
        button_run.config(state=tk.NORMAL)
        file_label.config(text=f"Список литературы:\n {file_path}")

def get_random_line():
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    random_line = random.choice(lines).strip()
                    result_label.config(text=f"Сегодня Вы читаете:\n {random_line}")
                else:
                    result_label.config(text="Список литературы пуст!")
        except Exception as e:
            result_label.config(text=f"Ошибка: {str(e)}")
    else:
        result_label.config(text="Список литературы не выбран!")

root = tk.Tk()
root.title("Выбор случайной книги из списка литературы")
root.geometry("500x200")

button_select_file = tk.Button(root, text="Выбрать список литературы (*.txt)", command=select_file)
button_select_file.pack(pady=10)

file_label = tk.Label(root, text="Список литературы выбран", padx=20, pady=10)
file_label.pack()

button_run = tk.Button(root, text="Выбрать случайную книгу", command=get_random_line, state=tk.DISABLED)
button_run.pack(pady=10)

result_label = tk.Label(root, text="...", padx=20, pady=20)
result_label.pack()

root.mainloop()
