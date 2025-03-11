import tkinter as tk

        
def dosomething():
    aBox = MyCrazyBox('Info', 'Running test case 1..')
    root.after(5000, lambda: aBox.updateInfo('Congrats', 'Test case 1 Passed.'))
    # just to simulate a delay of 5 sec in checking test case
    
root = tk.Tk()
tk.Button(root, text='Do something', command=dosomething).pack()
root.mainloop()