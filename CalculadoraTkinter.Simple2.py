import tkinter as tk

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 15))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button_text in buttons:
            tk.Button(root, text=button_text, font=("Arial", 15), command=lambda t=button_text: self.on_button_click(t)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button_text):
        if button_text == 'C':
            self.result_var.set('')
        elif button_text == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except:
                self.result_var.set('Error')
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + button_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
