import tkinter as tk

def show_text():
    user_input = entry.get()
    label_result.config(text=f"Ваше имя: {user_input}")

root = tk.Tk()
root.title("Пример Tkinter")
root.geometry("300x200")

label = tk.Label(root, text="Введите ваше имя:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Показать ваше имя", command=show_text)
button.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()
