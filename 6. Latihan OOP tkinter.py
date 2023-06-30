import os
os.system("cls")

import tkinter

'''
1. Setiap tanda titik yang diikuti huruf besar, maka itu adalah class
2. Setiap tanda titik yang diikuti huruf kecil, maka itu adalah method/funsi
'''

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text= "label1")
label2 = tkinter.Label(main_window, text= "label2")

tombol1 = tkinter.Button(main_window, text= "tombol1")
tombol2 = tkinter.Button(main_window, text= "tombol2")

# method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method menampilkan GUI
main_window.mainloop()

