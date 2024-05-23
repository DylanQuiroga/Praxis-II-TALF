import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from antlr4 import *
from GraphLexer import GraphLexer
from GraphParser import GraphParser
from GraphListener import GraphListener

def generate_graph(input_string):
    input_stream = InputStream(input_string)
    lexer = GraphLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GraphParser(stream)
    tree = parser.graph()

    listener = GraphListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Guarda el gráfico en un archivo .dot y genera la imagen
    listener.dot.save('graph.dot')
    listener.dot.render('graph.dot', format='png')

def show_graph():
    window = tk.Toplevel()
    image = Image.open('graph.dot.png')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(window, image=photo)
    label.image = photo  # Mantén una referencia a la imagen
    label.pack()

def on_button_click(text_area):
    input_string = text_area.get("1.0", 'end-1c')
    try:
        generate_graph(input_string)
        show_graph()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    root.title("APP 3")
    text_area = tk.Text(root)
    text_area.insert(tk.INSERT, "Graph {\n\n\tA -> B (10) \n\tB -> C (20) \n\tD -> E (30) \n\tA -> E (12) \n\tB -> D (8)\n\n}")
    text_area.pack()
    button = tk.Button(root, text="Graficar", command=lambda: on_button_click(text_area))
    button.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
