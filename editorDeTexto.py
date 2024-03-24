import tkinter as tk 
from tkinter import filedialog, messagebox

class SimpleTextEditor:

    def __init__(self,root):
        self.root= root # We pass the root to the class properties
        self.text_area= tk.Text(self.root) # We create the widget 
        self.text_area.pack(fill=tk.BOTH,expand=1)# We configurate the widget Size, and We make it fill the entire window
        self.current_open_file = ""

    def open_file(self):
        file = filedialog.askopenfile(mode="r") #the path of the file, and we put that the file return y close, because we going to open in the function
        if file:
            filename = file.name # we save the path of the file
            self.text_area.delete("1.0",tk.END) #We delete the previously entered text
            with open(filename, "r") as file:
                content = file.read()
                self.text_area.insert("1.0",content) # We insert the ttext

    def quit_confirm(self):
        if messagebox.askokcancel("Quit","Do you sure that quit de window?"):
            self.root.destroy() #Quit de program

    def save_file(self):
        if not self.current_open_file:
            new_file_path = filedialog.asksaveasfilename() # we save the path of the file

            if new_file_path:
                self.current_open_file = new_file_path # the conditional say that the the new file path is save we save the path in the current path file
            else:
                return 
        with open(self.current_open_file, "w") as file: # we write the input in the file
            file.write(self.text_area.get("1.0",tk.END))

    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.current_open_file=""

root = tk.Tk()

root.geometry("700x500")
print("hola mundo")


editor = SimpleTextEditor(root)

menu_bar= tk.Menu(root)
menu_options = tk.Menu(menu_bar, tearoff=0)#We add the menu to the other menu and make sure it does not fragment/Agregamos el menu al otro menu y hacemos que no se fragemente 


#Agregando las opciones
menu_options.add_command(label="New",command=editor.new_file)
menu_options.add_command(label="Open",command=editor.open_file)
menu_options.add_command(label="Save",command=editor.save_file)
menu_options.add_command(label="Exit",command=editor.quit_confirm)

root.config(menu=menu_bar)
menu_bar.add_cascade(label="File", menu=menu_options)#By configuring that when we open the file option we have the options/Configurando que caundo abramos la opcion archivo tengamos las opcinoes 













root.mainloop()