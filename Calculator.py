

# Name: Ashwin Unnithan
# Date: Friday, January 17 2019
# Purpose: To make a scientific calculator using Tkinter



from Tkinter import*
screen = Tk()
screen.title("Scientific Calculator")
operator = ""


text_Input = StringVar()
txtDisplay = Entry(screen,font = ('calibri', 20, 'bold'), textvariable = text_Input, bd = 30, insertwidth = 4, bg = "SteelBlue1", justify = 'right').grid(columnspan = 4)


def Button_Click(num):
    global operator
    operator = operator + str(num)
    text_Input.set(operator)




def Clear_Display():
    global operator
    operator = ""
    text_Input.set("")



def Calculate():
    global operator
    Sum = str(eval(operator))
    text_Input.set(Sum)
    operator = ""




def Btn(width, padding, fore_color, txt, number , row_num, col_num):
    Button(screen, padx = width, bd = padding, fg = fore_color, font = ('calibri', 20, 'bold'),text = txt, command = Button_Click(number)).grid(row = row_num, column = col_num)

    return width
    return padding
    return fore_color
    return txt
    return row_num
    return col_num




Btn7 = Btn(16,9,"black","7", 7, 1, 0)

Btn8 = Btn(16,9,"black","8", 8, 1, 1)

Btn9 = Btn(16,9,"black","9", 9, 1, 2)

Btn_Add = Btn(16,9,"red","+","+", 1, 3)

Btn4 = Btn(16,9,"black","4", 4, 2, 0)

Btn5 = Btn(16,9,"black","5", 5, 2, 1)

Btn6 = Btn(16,9,"black","6", 6, 2, 2)

Btn_Subtract = Btn(16,9,"red","-", "-", 2, 3)

Btn1 = Btn(16,9,"black","1",1, 3, 0)

Btn2 = Btn(16,9,"black","2",2, 3, 1)

Btn3 = Btn(16,9,"black","3",3, 3, 2)

Btn_Multiply = Btn(16,9,"red","x","x", 3, 3)

Btn_0 = Btn(16,9,"black","0", 0,4, 0)

Btn_Clear = Button(screen, padx = 16, bd = 9, fg = "black", font = ('calibri', 20, 'bold'),text = "C", command = Clear_Display).grid(row = 4, column = 1)

Btn_Equal = Button(screen, padx = 16, bd = 9, fg = "black", font = ('calibri', 20, 'bold'),text = "=", command = Calculate).grid(row = 4, column = 2)

Btn_Division = Btn(16,9,"red","/", "/", 4, 3)





screen.mainloop()






