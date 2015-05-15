from tkinter import *

root = Tk()
root.wm_title('Yancy\'s Editor v0.1')

main_menu = Menu(root)

f_menu = Menu(main_menu)    # create a new menu on main_menu
for item in ['New', 'Open', 'Save']:
    f_menu.add_command(label = item)

e_menu = Menu(main_menu)
for item in ['Undo', 'Find']:
    e_menu.add_command(label = item)

h_menu = Menu(main_menu)
for item in ['Version', 'Developer', 'About']:
    h_menu.add_command(label = item)

main_menu.add_cascade(label = 'File', menu = f_menu)
main_menu.add_cascade(label = 'Edit', menu = e_menu)
main_menu.add_cascade(label = 'Help', menu = h_menu)
root['menu'] = main_menu
root.mainloop()
