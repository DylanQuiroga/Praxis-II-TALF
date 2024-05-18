from tkinter import *
from tkinter import messagebox
from antlr4 import *
from arithmeticLexer import arithmeticLexer
from arithmeticParser import arithmeticParser

def calculate():
    input_text = entry.get()
    lexer = arithmeticLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = arithmeticParser(stream)
    tree = parser.file_()
    print(tree.toStringTree(recog=parser))
    messagebox.showwarning('Salida', tree.toStringTree(recog=parser) )
    #result = tree.toStringTree(recog=parser)

root = Tk()
root.geometry('300x100')
root.resizable(0,0)
root.title("APP 1.1")

window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth()/2 - window_width/2)
position_down = int(root.winfo_screenheight()/2 - window_height/2)
root.geometry("+{}+{}".format(position_right, position_down))

Label(root, text="Inserte la expresión que desea calcular.").pack()
Label(root, text="Ejem: (2+4*20/3)").pack()

entry = Entry(root)
entry.pack()

Button(root, text="Aceptar", command=calculate).pack()

root.mainloop()
