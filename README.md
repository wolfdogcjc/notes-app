# notes-app
Simple Tkinter Gui Notes App


[Python Program Documentation.txt](https://github.com/wolfdogcjc/notes-app/files/10412112/Python.Program.txt)


 
My program is an implementation of a simple note-taking application using the Tkinter library in Python. Tkinter is a library that provides a set of tools to create graphical user interfaces in Python. The program creates a window (referred to as the "master" in the code) with a title "Notes" and several widgets, including a Text widget, two Button widgets, and a Scale widget.
The Text widget is where the user can type their notes, and the two Button widgets are labeled "Save" and "New". When the "Save" button is clicked, the program retrieves the current text from the Text widget and saves it to a file called "notes.txt" in the same directory. When the "New" button is clicked, it clears the Text widget, allowing the user to start a new note. The Scale widget allows the user to adjust the font-size of the text. The program keeps running until the user closes the window, and the notes are saved only when the user clicks the "Save" button.
I encountered some challenges while working on the program. I was not able to reposition the "New" and "Save" buttons in the desired location without disrupting the layout of the text input box. Additionally, I was unable to figure out a way to increase the text size in the saved ".txt" file, though I was able to adjust the font size within the GUI.
Overall, even though my program did not turn out exactly as I had intended, I believe it was a well-executed concept for a final Python project.
 
Here are some sources where I found information:
https://www.guru99.com/reading-and-writing-files-in-python.html
https://www.geeksforgeeks.org/reading-writing-text-files-python/
https://www.pythontutorial.net/tkinter/tkinter-button/
https://www.tutorialspoint.com/python/tk_text.htm
Along with these examples I also looked at my previous tkinter projects.
https://github.com/wolfdogcjc/tkinter_2widget
https://github.com/wolfdogcjc/tkinter
 
 
 
 
Using this Notes App Code I found out how to make a text box and change text font:	
https://github.com/ShubhamPy/Note-Taking-App/blob/master/start.py
p=Label(root,text="Notespro*", height="18",width="250",bg='brown',fg='white',font=('Helvetica','20','bold','italic'))
