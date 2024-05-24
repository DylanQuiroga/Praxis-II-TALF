from tkinter import *
from tkinter import messagebox
from antlr4 import *
from arithmeticLexer import arithmeticLexer
from arithmeticParser import arithmeticParser
from sympy import symbols, Eq, solve, sympify

def solve_equation(equation_str):
    try:
        # Define the symbols dynamically based on the equation
        variables = set()
        for char in equation_str:
            if char.isalpha():
                variables.add(char)
        symbols_list = symbols(' '.join(variables))

        # Split the equation into left and right sides
        left_side, right_side = equation_str.split('=')
        left_expr = sympify(left_side)
        right_expr = sympify(right_side)

        # Create an equation object
        equation = Eq(left_expr, right_expr)

        # Solve the equation
        solution = solve(equation, symbols_list)
        return solution
    except Exception as e:
        return f"Error al evaluar la ecuación: {e}"

def calculate():
    input_text = entry_expr.get()
    lexer = arithmeticLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = arithmeticParser(stream)
    tree = parser.file_()
    print(tree.toStringTree(recog=parser))
    messagebox.showwarning('Salida', tree.toStringTree(recog=parser) )
    try:
        input_text = entry_expr.get()
        print(f"Expresión ingresada: {input_text}")

        if '=' in input_text:
            solution = solve_equation(input_text)
            print(f"Resultado del cálculo: {solution}")

            messagebox.showinfo('Resultado', f'La solución es: {solution}')
        else: 
            expr = sympify(input_text)
            resultado = expr.evalf()
            print(f"Resultado del cálculo: {resultado}")
            messagebox.showwarning('Salida', f'El resultado es: {resultado}')
    except Exception as e:
        messagebox.showerror('Error', f'Error al evaluar la ecuación: {e}')

root = Tk()
root.geometry('300x250')
root.resizable(0, 0)
root.title("Calculadora de Ecuaciones")

window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry("+{}+{}".format(position_right, position_down))

Label(root, text="Inserte la ecuación que desea resolver.").pack()
Label(root, text="Ejem: 2*x + 8*y = 10 o 2 + 3*4 - 5/2").pack()

entry_expr = Entry(root)
entry_expr.pack()

Button(root, text="Aceptar", command=calculate).pack()

root.mainloop()
