
from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title ('โปรแกรมคำนวณ')
GUI.geometry('800x700')

'''bg = PhotoImage(file='car.png')'''

##เก็บรูปแบบpatr เต็ม###
bg = PhotoImage(file=r'E:\Python\Python For Beginners\car.png')
BG = Label(GUI,image=bg)
BG.pack()

L = Label(GUI,text = 'กรุณากรอกจำนวน',font=(None,20))
L.pack()


v_quantity = StringVar()        #เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable = v_quantity, font=(None,20))
E1.pack()

def Cal():
    try:
        quan = float(v_quantity.get())
        calc = quan * 40 #40 ค่าคงที่
        messagebox.showinfo('ราคาทั้งหมด','ราคาของทั้งหมด {} บาท'.format(calc))
        v_quantity.set('')
        E1.focus()
    except:
        messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
        v_quantity.set('')
        E1.focus()

B = ttk.Button(GUI, text = 'คำนวณ',command=Cal)
B.pack(ipadx=30,ipady=20)   #ipadx ขยายความกว้าง x/y




GUI.mainloop()
