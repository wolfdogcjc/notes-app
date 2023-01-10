import tkinter as tk

class NotesApplication:
    def __init__(self, master):
        self.master = master
           
        self.master.title("Notes")
      
        self.text = tk.Text(self.master, font=("Helvetica", 12))
        self.text.pack()
        self.save_button = tk.Button(self.master, text="Save", command=self.save)
        self.save_button.pack()
        self.new_button = tk.Button(self.master, text="New", command=self.new)
        self.new_button.pack()
        
        # Add a Scale widget to change the font size
        self.font_size = tk.Scale(self.master, from_=9, to=14, orient=tk.HORIZONTAL, command=self.change_font_size)
        self.font_size.pack()
    
    def save(self):
        # Get the current text from the Text widget
        text = self.text.get("1.0", "end")
        # Saves the text to a .txt file
        with open("notes.txt", "w") as f:
            f.write(text)
    
    def new(self):
        # Click the new button to clear text (wont save it tho)
        self.text.delete("1.0", "end")
        
    def change_font_size(self, event):
        # Get the current value of the Scale widget
        font_size = self.font_size.get()
        # Set the font size of the Text widget
        self.text.configure(font=("Helvetica", font_size))

# Run the program
root = tk.Tk()
app = NotesApplication(root)
root.mainloop()
