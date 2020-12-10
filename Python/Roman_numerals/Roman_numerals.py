from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text = "Roman Numeral Canvas")
        self.lbl.grid(row = 0, columnspan = 5)

        #Set the Canvas
        self.canvas = Canvas(self, width = 300, height = 300, highlightbackground = "black", highlightthickness = 1)
        self.canvas.grid(row = 1, column = 0, rowspan = 5)

        #Number Label
        self.number_lbl = Label(self, text = "Number:")
        self.number_lbl.grid(row = 1, column = 1)

        self.num_ent = Entry(self)
        self.num_ent.grid(row = 1, column = 2, columnspan = 1)

        #Line Width Label
        self.width_lbl = Label(self, text = "Line Width:")
        self.width_lbl.grid(row = 2, column = 1)

        #Line color Label
        self.color_lbl = Label(self, text = "Line Color:")
        self.color_lbl.grid(row = 3, column = 1)

        #Click picture Label
        self.click_lbl = Label(self, text = "Click the picture to draw the number:")
        self.click_lbl.grid(row = 4, column = 1)

        #Set width default choice
        self.width_choice = StringVar()
        self.width_choice.set("1")

        #Width options(buttons)
        Radiobutton(self, text = "1", variable = self.width_choice,
                    value = "1").grid(row = 2, column = 2,)

        Radiobutton(self, text = "3", variable = self.width_choice,
                    value = "3").grid(row = 2, column = 3)

        Radiobutton(self, text = "5", variable = self.width_choice,
                    value = "5").grid(row = 2, column = 4)

        #Set color choice default
        self.color_choice = StringVar()
        self.color_choice.set("black")

        #Color options(buttons)
        Radiobutton(self, text = "Black", variable = self.color_choice,
                    value = "black").grid(row = 3, column = 2)

        Radiobutton(self, text = "Red", variable = self.color_choice,
                    value = "red").grid(row = 3, column = 3)

        Radiobutton(self, text = "Blue", variable = self.color_choice,
                    value = "blue").grid(row = 3, column = 4)
        #set the image to their own variables 
        self.roman = PhotoImage(file="roman.gif")


        #place the roman button image, this will use the class which tells what letter to draw
        self.roman_bttn = Button(self, image = self.roman,
                                 command = self.valid_ent)
        self.roman_bttn.grid(row = 4, column = 2)


        #set where the first letter will be started on the canvas
        self.x = 20
        self.y = 20

    #draw the letter M
    def draw_m(self):
        num_width = int(self.width_choice.get())
        color = self.color_choice.get()
        self.canvas.delete("all")
            
        self.canvas.create_line(self.x, self.y, self.x+6, self.y,width = num_width, fill=color)
        self.canvas.create_line(self.x+3, self.y, self.x+3, self.y+40, width = num_width, fill = color)
        self.canvas.create_line(self.x, self.y+40, self.x+6, self.y+40, width = num_width, fill = color)
        self.canvas.create_line(self.x+3, self.y, self.x+8, self.y+14, width = num_width, fill = color)
        self.canvas.create_line(self.x+8, self.y+14, self.x+16, self.y,width = num_width, fill = color)
        self.canvas.create_line(self.x+14, self.y, self.x+20, self.y,width = num_width, fill = color)
        self.canvas.create_line(self.x+17, self.y, self.x+17, self.y+40,width = num_width, fill = color)
        self.canvas.create_line(self.x+14, self.y+40, self.x+20, self.y+40,width = num_width, fill = color)

    #draw the letter D
    def draw_d(self):
        num_width = int(self.width_choice.get())
        color = self.color_choice.get()
        self.canvas.delete("all")
        

        self.canvas.create_line(self.x, self.y, self.x+10, self.y, width = num_width, fill = color)
        self.canvas.create_line(self.x, self.y, self.x, self.y+40, width = num_width, fill = color)
        self.canvas.create_line(self.x+10, self.y, self.x+20, self.y +10, width = num_width, fill = color)
        self.canvas.create_line(self.x+20, self.y+10, self.x+20, self.y+30, width = num_width, fill = color)
        self.canvas.create_line(self.x, self.y+40, self.x+10, self.y+40, width = num_width, fill = color)
        self.canvas.create_line(self.x+10, self.y+40, self.x+20, self.y+30, width = num_width, fill = color)

    #draw the letter C
    def draw_c(self):
        num_width = int(self.width_choice.get())
        color = self.color_choice.get()
        self.canvas.delete("all")
       

        self.canvas.create_line(self.x+20, self.y, self.x+10, self.y,width = num_width, fill = color)
        self.canvas.create_line(self.x+10, self.y, self.x, self.y+10,width = num_width, fill = color)
        self.canvas.create_line(self.x, self.y+10, self.x, self.y+30,width = num_width, fill = color)
        self.canvas.create_line(self.x, self.y+30, self.x+10, self.y+40,width = num_width, fill = color)
        self.canvas.create_line(self.x+10, self.y+40, self.x+20, self.y+40,width = num_width, fill = color)

    #draw the letter L
    def draw_l(self):
        num_width = int(self.width_choice.get())
        color = self.color_choice.get()
        self.canvas.delete("all")

        self.canvas.create_line(self.x, self.y, self.x+10, self.y,width = num_width, fill = color)
        self.canvas.create_line(self.x+5, self.y, self.x+5, self.y+40,width = num_width, fill = color)
        self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40,width = num_width, fill = color)

    #draw the letter X
    def draw_x(self):
        num_width = int(self.width_choice.get())
        color = self.color_choice.get()
        self.canvas.delete("all")
       

        self.canvas.create_line(self.x, self.y, self.x+20, self.y,width = num_width, fill = color)
        self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40,width = num_width, fill = color)
        self.canvas.create_line(self.x+5, self.y, self.x+15, self.y+40,width = num_width, fill = color)
        self.canvas.create_line(self.x+5, self.y+40, self.x+15, self.y,width = num_width, fill = color)

    #draw the letter V
    def draw_v(self):
        num_width = int(self.width_choice.get())
        color = self.color_choice.get()
        self.canvas.delete("all")
        

        self.canvas.create_line(self.x, self.y, self.x+20, self.y,width = num_width, fill = color)
        self.canvas.create_line(self.x+5, self.y, self.x+10, self.y+40,width = num_width, fill = color)
        self.canvas.create_line(self.x+10, self.y+40, self.x+15, self.y,width = num_width, fill = color)
        self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40,width = num_width, fill = color)

    #draw the letter I
    def draw_i(self):
        num_width = int(self.width_choice.get())
        color = self.color_choice.get()
        self.canvas.delete("all")
        

        self.canvas.create_line(self.x, self.y, self.x+20, self.y,width = num_width, fill = color)
        self.canvas.create_line(self.x+10, self.y, self.x+10, self.y+40,width = num_width, fill = color)
        self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40,width = num_width, fill = color)
        
    #This will go through each letter in the entry and decide what letter to draw 
    def valid_ent(self):
        entry = self.num_ent.get()
        #go through the entry and narrow down what letter it is, then tell it which one to draw
        #If user enters the roman number also draw the numeral
        for letter in entry:
            if entry.upper() == "M":
                self.draw_m()
            elif entry.upper() == "D":
                self.draw_d()
            elif entry.upper() == "C":
                self.draw_c()
            elif entry.upper() == "L":
                self.draw_l()
            elif entry.upper() == "X":
                self.draw_x()
            elif entry.upper() == "V":
                self.draw_v()
            elif entry.upper() == "I":
                self.draw_i()


        
        

        
# main
root = Tk()
root.title("Roman Numerals")
root.geometry("1000x500")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
