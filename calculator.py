import tkinter as tk
import tkmacosx as tkmac
import operator


class Calculator:
    operator_dic = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    operator_precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    @staticmethod
    def calculate(expr):
        tokens = Calculator.__parse_input__(expr)
        rpn = Calculator.__infix_to_rpn__(tokens)
        return Calculator.__eval_rpn__(rpn)

    @staticmethod
    def __parse_input__(expr):
        tokens = []
        signal = 0
        for char in expr:
            if char.isnumeric():
                if signal == 0:
                    signal = 1
                    tokens.append(int(char))
                else:
                    new_num = tokens.pop() * 10 + int(char)
                    tokens.append(new_num)
            else:
                tokens.append(char)
                signal = 0
        return tokens

    @staticmethod
    def __operator_precedence__(opt):
        high_precedence = ["*", "/"]
        low_precedence = ["+", "-"]
        if opt in high_precedence:
            return 2
        elif opt in low_precedence:
            return 1

    @staticmethod
    def __infix_to_rpn__(input_tokens):
        output = []
        operators = []
        for token in input_tokens:
            if token in ["+", "-", "*", "/"]:
                if len(operators) == 0:
                    operators.append(token)
                elif operators[-1] == '(':
                    operators.append(token)
                else:
                    curr_precedence = Calculator.operator_precedence[token]
                    prev_precedence = Calculator.operator_precedence[operators[-1]]
                    if curr_precedence <= prev_precedence:
                        output.append(operators.pop())
                    operators.append(token)
            elif token == "(":
                operators.append(token)
            elif token == ")":
                while operators[-1] != "(":
                    output.append(operators.pop())
                else:
                    operators.pop()
            else:
                output.append(token)

        while len(operators):
            output.append(operators.pop())
        return output

    @staticmethod
    def __eval_rpn__(rpn_tokens):
        final_stack = []
        for token in rpn_tokens:
            if type(token) != int:
                num2 = final_stack.pop()
                num1 = final_stack.pop()
                final_stack.append(Calculator.operator_dic[token](num1, num2))
            else:
                final_stack.append(token)
        return final_stack[-1]


class CalculatorApp(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill="none", expand=1)
        self.create_widgets()
        self.has_result = False
        self.has_dot = False

    def create_widgets(self):
        self.input_frame = tk.Frame(self, background="grey")
        self.input_frame.pack(side="top", fill="x", expand=1)
        self.number_frame = tk.Frame(self, background="light grey");
        self.number_frame.pack(side="bottom", fill="both", expand=1)

        self.input_area = tk.Text(self.input_frame, height=1, width=51, bg="light pink")
        self.input_area.grid(row=0, column=0, padx=10, pady=10, sticky="EW")
        self.input_area.configure(state='disabled')

        self.left_bracket = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.left_bracket["text"] = "("
        self.left_bracket["command"] = self.click_left
        self.left_bracket.grid(row=1, column=0, sticky="EW", padx=(10, 0), pady=(10, 0))

        self.right_bracket = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.right_bracket["text"] = ")"
        self.right_bracket["command"] = self.click_right
        self.right_bracket.grid(row=1, column=1, sticky="EW", padx=(5, 0),  pady=(10, 0))

        self.multiply = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.multiply["text"] = "*"
        self.multiply["command"] = self.click_multiply
        self.multiply.grid(row=1, column=2,  sticky="EW", padx=(5, 0),  pady=(10, 0))

        self.divide = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.divide["text"] = "/"
        self.divide["command"] = self.click_divide
        self.divide.grid(row=1, column=3,  sticky="EW", padx=(5, 10), pady=(10, 0))

        self.one = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.one["text"] = "1"
        self.one["command"] = self.click_one
        self.one.grid(row=2, column=0, sticky="EW", padx=(10, 0), pady=(5, 0))

        self.two = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.two["text"] = "2"
        self.two["command"] = self.click_two
        self.two.grid(row=2, column=1, sticky="EW", padx=(5, 0), pady=(5, 0))

        self.three = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.three["text"] = "3"
        self.three["command"] = self.click_three
        self.three.grid(row=2, column=2, sticky="EW", padx=(5, 0), pady=(5, 0))

        self.plus = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.plus["text"] = "+"
        self.plus["command"] = self.click_plus
        self.plus.grid(row=2, column=3, sticky="EW", padx=(5, 10), pady=(5, 0))

        self.four = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.four["text"] = "4"
        self.four["command"] = self.click_four
        self.four.grid(row=3, column=0, sticky="EW", padx=(10, 0), pady=(5, 0))

        self.five = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.five["text"] = "5"
        self.five["command"] = self.click_five
        self.five.grid(row=3, column=1, sticky="EW", padx=(5, 0), pady=(5, 0))

        self.six = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.six["text"] = "6"
        self.six["command"] = self.click_six
        self.six.grid(row=3, column=2, sticky="EW", padx=(5, 0), pady=(5, 0))

        self.minus = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.minus["text"] = "-"
        self.minus["command"] = self.click_minus
        self.minus.grid(row=3, column=3, sticky="EW", padx=(5, 10), pady=(5, 0))

        self.seven = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.seven["text"] = "7"
        self.seven["command"] = self.click_seven
        self.seven.grid(row=4, column=0, sticky="EW", padx=(10, 0), pady=(5, 0))

        self.eight = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.eight["text"] = "8"
        self.eight["command"] = self.click_eight
        self.eight.grid(row=4, column=1, sticky="EW", padx=(5, 0), pady=(5, 0))

        self.nine = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.nine["text"] = "9"
        self.nine["command"] = self.click_nine
        self.nine.grid(row=4, column=2, sticky="EW", padx=(5, 0), pady=(5, 0))

        self.equalsButton = tkmac.Button(self.number_frame, fg="white", bg="orange", borderless=True)
        self.equalsButton["text"] = "="
        self.equalsButton["command"] = self.click_calculate
        self.equalsButton.grid(row=4, column=3, rowspan=2, sticky="EWNS", padx=(5, 10), pady=(5, 10))

        self.zero = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.zero["text"] = "0"
        self.zero["command"] = self.click_zero
        self.zero.grid(row=5, column=0, columnspan=2, sticky="EW", padx=(10, 0), pady=(5, 10))

        self.dot = tkmac.Button(self.number_frame, fg="white", bg="grey", borderless=True)
        self.dot["text"] = "."
        self.dot["command"] = self.click_dot
        self.dot.grid(row=5, column=2, sticky="EW", padx=(5, 0), pady=(5, 10))

    def click_one(self):
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '1')
        self.input_area.configure(state='disabled')

    def click_two(self):
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '2')
        self.input_area.configure(state='disabled')

    def click_three(self):
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '3')
        self.input_area.configure(state='disabled')

    def click_four(self):
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '4')
        self.input_area.configure(state='disabled')

    def click_five(self):
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '5')
        self.input_area.configure(state='disabled')

    def click_six(self):
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '6')
        self.input_area.configure(state='disabled')

    def click_seven(self):
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '7')
        self.input_area.configure(state='disabled')

    def click_eight(self):
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '8')
        self.input_area.configure(state='disabled')

    def click_nine(self):
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '9')
        self.input_area.configure(state='disabled')

    def click_left(self):
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '(')
        self.input_area.configure(state='disabled')

    def click_right(self):
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', ')')
        self.input_area.configure(state='disabled')

    def click_plus(self):
        self.has_dot = False
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '+')
        self.input_area.configure(state='disabled')

    def click_minus(self):
        self.has_dot = False
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '-')
        self.input_area.configure(state='disabled')

    def click_multiply(self):
        self.has_dot = False
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '*')
        self.input_area.configure(state='disabled')

    def click_divide(self):
        self.has_dot = False
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '/')
        self.input_area.configure(state='disabled')

    def click_zero(self):
        self.__clear_input__()
        self.input_area.configure(state='normal')
        self.input_area.insert('end', '0')
        self.input_area.configure(state='disabled')

    def click_dot(self):
        if not self.has_dot:
            self.input_area.configure(state='normal')
            self.input_area.insert('end', '.')
            self.input_area.configure(state='disabled')
            self.has_dot = True

    def click_calculate(self):
        self.input_area.configure(state='normal')
        input_str = self.input_area.get("1.0", "end-1c")
        self.input_area.delete('1.0', "end")
        self.input_area.insert('end', Calculator.calculate(input_str))
        self.input_area.configure(state='disabled')
        self.has_result = True

    def __clear_input__(self):
       if self.has_result:
           self.input_area.configure(state='normal')
           self.input_area.delete('1.0', "end")
           self.input_area.configure(state='disabled')
           self.has_result = False
           self.has_dot = False


if __name__ == "__main__":
    root = tk.Tk()
    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("400x250+{}+{}".format(positionRight, positionDown))
    root.title("Calculator")
    app = CalculatorApp(parent=root)
    app.mainloop()