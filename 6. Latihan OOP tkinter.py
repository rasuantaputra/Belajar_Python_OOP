from cProfile import label
import tkinter

main_windows = tkinter.Tk()

label1 = tkinter.Label(main_windows, text='label 1')
label2 = tkinter.Label(main_windows, text='label 2')

tombol1 = tkinter.Button(main_windows, text='tombol 1')
tombol2 = tkinter.Button(main_windows, text='tombol 2')

# Methode positioning
label1.pack()
label2.pack()

tombol1.pack()
tombol2.pack()

# methode menampilkan GUI
main_windows.mainloop()