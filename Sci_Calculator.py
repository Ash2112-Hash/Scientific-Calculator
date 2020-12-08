

# Name: Ashwin Unnithan
# Date: Friday, January 17 2019
# Purpose: To create a user-interface



from Tkinter import *
import easygui
import math
import parser
import tkMessageBox



screen = Tk()
screen.title("RAM Scientific Calculator")
screen.configure(bg = "steel blue")
screen.resizable(width = False, height = False)
screen.geometry("900x670")
calculator = Frame(screen)
calculator.grid()




class Calculate():
    def __init__(self):
        self.sum = 0
        self.current = ""
        self.input_Value = True
        self.check_sum = False
        self.operator = ""
        self.result = False



    def Enter_Number(self, num):
        self.result = False
        Fir_Num = TextDisplay.get()
        Sec_Num = str(num)

        if self.input_Value:
            self.current = Sec_Num
            self.input_Value = False

        else:
            if Sec_Num == '.':
                if Sec_Num in Fir_Num:
                    return
            self.current = Fir_Num + Sec_Num

        self.Display(self.current)



    def Sum(self):
        self.result = True
        self.current = float(self.current)

        if self.check_sum == True:
            self.Main()

        else:
            self.sum = float(TextDisplay.get())




    def Display(self, value):
        TextDisplay.delete(0, END)
        TextDisplay.insert(0, value)



    def Main(self):
        if self.operator == "add":
            self.sum += self.current

        if self.operator == "sub":
            self.sum -= self.current

        if self.operator == "multi":
            self.sum *= self.current

        if self.operator == "divide":
            self.sum /= self.current

        if self.operator == "mod":
            self.sum %= self.current


        self.input_Value = True
        self.check_sum = False
        self.Display(self.sum)


    def operation(self, operator):
        self.current = float(self.current)

        if self.check_sum:
            self.Main()


        elif not self.result:
            self.sum = self.current
            self.input_Value = True
        self.check_sum = True
        self.operator = operator
        self.result = False





# ---------- Special Key Functions ---------------------------------------------



    def Special_Pi (self):
        self.result = False
        self.current = math.pi
        self.Display(self.current)


    def Special_E (self):
        self.result = False
        self.current = math.e
        self.Display(self.current)


    def Clear (self):
        self.result = False
        self.current = "0"
        self.Display(0)
        self.input_Value = True


    def All_Clear (self):
        self.Clear()
        self.sum = 0


    def Special_PlusMinus (self):
           self.result = False
           self.current = (-float(TextDisplay.get()))
           self.Display(self.current)


    def Special_Sqrt (self):
        self.result = False
        self.current = math.sqrt(float(TextDisplay.get()))
        self.Display(self.current)



    def Special_Cos (self):
        self.result = False
        self.current = math.cos(float(TextDisplay.get()))
        self.Display(self.current)


    def Special_Sin (self):
        self.result = False
        self.current = math.sin(math.radians(float(TextDisplay.get())))
        self.Display(self.current)


    def Special_Tan (self):
        self.result = False
        self.current = math.tan(math.radians(float(TextDisplay.get())))
        self.Display(self.current)


    def Special_Cosh (self):
        self.result = False
        self.current = math.cosh(math.radians(float(TextDisplay.get())))
        self.Display(self.current)


    def Special_Sinh (self):
        self.result = False
        self.current = math.sinh(math.radians(float(TextDisplay.get())))
        self.Display(self.current)


    def Special_Tanh (self):
        self.result = False
        self.current = math.tanh(math.radians(float(TextDisplay.get())))
        self.Display(self.current)


    def Special_Log (self):
        self.result = False
        self.current = math.log(float(TextDisplay.get()))
        self.Display(self.current)


    def Special_Exp (self):
        self.result = False
        self.current = math.exp(float(TextDisplay.get()))
        self.Display(self.current)


    def Special_Expm1 (self):
        self.result = False
        self.current = math.expm1(float(TextDisplay.get()))
        self.Display(self.current)


    def Special_Degrees (self):
        self.result = False
        self.current = math.degrees(float(TextDisplay.get()))
        self.Display(self.current)


    def Special_log2 (self):
        self.result = False
        self.current = math.log2(float(TextDisplay.get()))
        self.Display(self.current)


    def Sqaured (self):
        self.result = False
        self.current = math.pow(float(TextDisplay.get()), 2)
        self.Display(self.current)






# ---------- Long-Special Key Functions ----------------------------------------

def Q_Form():
       msg = "Please Enter corresponding Values for the Quadratic Formula"
       title = "RAM Scientific Calculator"
       fieldNames = ["a:", "b:", "c:"]
       fieldValues = (easygui.multenterbox(msg, title, fieldNames))

       Real_a = float(fieldValues[0])
       Real_b = float(fieldValues[1])
       Real_c = float(fieldValues[2])

       Sub1 = (Real_b**2) - (4*Real_a*Real_c)
       Sub2 = (-Real_b + math.sqrt(Sub1))/(2*Real_a)
       Sub2_Al = (-Real_b - math.sqrt(Sub1))/(2*Real_a)

       X = Sub2/(2*Real_a)
       XAl = Sub2_Al/(2*Real_a)


       Real_X = round(X, 2)
       Real_XAl = round(XAl, 2)


       easygui.msgbox(msg = "Therefore, X = " + str(Real_X) + " or X = " + str(Real_XAl), title = "Scientific Calculator")




def Exponential():
    msg = "Please Enter corresponding Values "
    title = "RAM Scientific Calculator"
    fieldNames = ["X:", "Y:"]
    fieldValues = (easygui.multenterbox(msg, title, fieldNames))


    Real_X = float(fieldValues[0])
    Real_Y = float(fieldValues[1])


    Answ = math.pow(Real_X, Real_Y)

    easygui.msgbox(msg = "Your Answer is" + str(Answ), title = "Scientific Calculator")






Add_Val = Calculate()



TextDisplay = Entry(calculator, font = ('calibri', 25, 'bold'), bg = "gray64", bd = 20, width = 30, justify = RIGHT)
TextDisplay.grid(row = 0, column = 0, columnspan = 5, pady = 1)
TextDisplay.insert(0,"0")



Numbers = "789456123"
i = 0
button = []
for l in range(2,5):
    for m in range(3):
        button.append(Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, bg = "gray63", fg = "white",text = Numbers[i]))
        button[i].grid(row = l, column = m, pady = 1)
        button[i]["command"] = lambda x = Numbers [i]: Add_Val.Enter_Number(x)

        i += 1









# ----------- Basic Operation Buttons ------------------------------------------------

Clear_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "C", command = Add_Val.Clear).grid(row = 1, column = 0, pady = 3)

AllClear_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "CE", command = Add_Val.All_Clear).grid(row = 1, column = 1, pady = 3)

Sqrt_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "Sqrt", command = Add_Val.Special_Sqrt).grid(row = 1, column = 2, pady = 3)

Add_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "+", command = lambda:Add_Val.operation("add")).grid(row = 1, column = 3, pady = 3)

Subtract_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "-", command = lambda:Add_Val.operation("sub")).grid(row = 2, column = 3, pady = 3)

Division_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "/",command = lambda:Add_Val.operation("divide") ).grid(row = 3, column = 3, pady = 3)

Multiply_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "x", command = lambda:Add_Val.operation("multi")).grid(row = 4, column = 3, pady = 3)

Zero_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "0", command = lambda: Add_Val.Enter_Number(0)).grid(row = 5, column = 0, pady = 3)

Decimal_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = ".", command = lambda: Add_Val.Enter_Number(".")).grid(row = 5, column = 1, pady = 3)

PlusandMinus_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "+-", command = Add_Val.Special_PlusMinus).grid(row = 5, column = 2, pady = 3)

Eqaul_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "=", command = Add_Val.Sum).grid(row = 5, column = 3, pady = 3)








# ---------- First Set of Scientific Operation Buttons -------------------------------------------

Pi_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "PI", command = Add_Val.Special_Pi).grid(row = 1, column = 4, pady = 3)

SIN_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "SIN", command = Add_Val.Special_Sin).grid(row = 1, column = 5, pady = 3)

COS_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "COS", command = Add_Val.Special_Cos).grid(row = 1, column = 6, pady = 3)

TAN_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "TAN", command = Add_Val.Special_Tan).grid(row = 1, column = 7, pady = 3)

SINh_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "SINh", command = Add_Val.Special_Sinh).grid(row = 2, column = 4, pady = 3)

COSh_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "COSh", command = Add_Val.Special_Cosh).grid(row = 2, column = 5, pady = 3)

TANh_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "TANh", command = Add_Val.Special_Tanh).grid(row = 2, column = 6, pady = 3)







# ---------- Second Set of Scientific Operation Buttons -------------------------------------------

LOG_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "LOG", command = Add_Val.Special_Log).grid(row = 2, column = 7, pady = 3)

EXP_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "Exp", command = Add_Val.Special_Exp).grid(row = 3, column = 4, pady = 3)

E_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "E", command = Add_Val.Special_E).grid(row = 3, column = 5, pady = 3)

DEG_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "Deg", command = Add_Val.Special_Degrees).grid(row = 3, column = 6, pady = 3)

LOG2_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "LOG2", command = Add_Val.Special_log2).grid(row = 3, column = 7, pady = 3)

MOD_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "MOD", command = lambda:Add_Val.operation("mod")).grid(row = 4, column = 4, pady = 3)

X2_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "Sqaure", command = Add_Val.Sqaured).grid(row = 4, column = 5, pady = 3)

EXMP1_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "Exmp 1", command = Add_Val.Special_Expm1).grid(row = 4, column = 6, pady = 3)

quadF_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "QuadF", command = Q_Form).grid(row = 4, column = 7, pady = 3)

Exponential_Button = Button(calculator, width = 6, height = 2, font = ('calibri', 23, 'bold'), bd = 4, text = "X*y", command = Exponential).grid(row = 5, column = 4, pady = 3)




# ------------------ Menu and Options -----------------------------------------------

Menubar = Menu(calculator)


def User_Exit():
    User_Exit = tkMessageBox.askyesno("Scientific Calculator", "Confirm if you want to Exit")

    if User_Exit == True:
        User_Appclosed = tkMessageBox.askokcancel("Scientific Calculator", "The Application will be Closed")
        if User_Appclosed == True:
            screen.destroy()
            return




Filemenu = Menu(Menubar, tearoff = 0)
Menubar.add_cascade(label = "File", menu = Filemenu)
Filemenu.add_separator()
Filemenu.add_command(label = "Exit", command = User_Exit)


Editmenu = Menu(Menubar, tearoff = 0)
Menubar.add_cascade(label = "Edit", menu = Editmenu)
Editmenu.add_command(label = "Cut")
Editmenu.add_command(label = "Copy")
Editmenu.add_separator()
Editmenu.add_command(label = "Paste")


Helpmenu = Menu(Menubar, tearoff = 0)
Menubar.add_cascade(label = "Help", menu = Helpmenu)
Helpmenu.add_command(label = "Calculator Manual")
Helpmenu.add_separator()
Helpmenu.add_command(label = "About")




screen.config(menu = Menubar)


screen.mainloop()







