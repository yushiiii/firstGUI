#!/usr/bin/python3
from tkinter import *
import math
	
class Sample(Tk):
	def __init__(self,*args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		container = Frame(self)
		container.pack(side="top", fill="both", expand = True)
		#container.grid(row=0, column=0, sticky="nsew")
		self.frames = {}
		self.container=container
		#for F in (PageOne, PageTwo):
			#page_name=F.__name__
		frame=PageOne(self.container, self)
		self.frames[PageOne]=frame
		frame_=PageTwo(self.container, self)
		self.frames[PageTwo] = frame_
		frame1=PageThree(self.container, self)
		self.frames[PageThree] = frame1
		frame2=PageFour(self.container, self)
		self.frames[PageFour] = frame2
			#frame.grid(row=0, column=0, sticky="nsew")
		frame.pack(side="top", fill="both", expand=True)

		#frame_.pack(side="top", fill="both", expand=True)
		self.show_frame(PageOne)

	def show_frame(self, page):
		frame = self.frames[page]

		frame.pack(side="top", fill="both", expand=True)
		frame.tkraise()

	def quitAll(self):
		Tk.destroy(self)
	
class PageOne(Frame):

	def __init__(self,parent,controller):
		Frame.__init__(self,parent)
		self.parent = parent
		self.controller=controller
		self.label = Label(self, text="Welcome!")
		self.label.pack()
		Button(self, text="Next", command=lambda:self.closeCur(controller)).pack()
		pass
	
	def closeCur(self,controller):
		self.pack_forget()
		controller.show_frame(PageTwo)

class PageTwo(Frame):
    
    expression = ""
	
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        Label(self, text="Calculator").pack()
        Button(self, text="Next", command=lambda:self.closeCur(controller)).pack()

    def press(num): 
	     
	    global expression 
	
	    expression = expression + str(num) 
 
	    equation.set(expression) 
 
    def equalpress(): 
	 
	    try: 
            
             #global expression 
	        
             total = str(eval(expression)) 
	        
             equation.set(total) 
            
             expression = "" 
            
            except: 
            
             equation.set(" error ") 
             expression = "" 

    def clear(): 
        
        global expression 
        expression = "" 
        equation.set("") 

    # Driver code 
    if __name__ == "__main__": 
        
        gui = Tk()  
    
        equation = StringVar() 

        expression_field = Entry(gui, textvariable=equation) 

        expression_field.grid(columnspan=4, ipadx=150) 

        equation.set('enter your expression') 

        button1 = Button(gui, text=' 1 ', fg='black', 
                        command=lambda: press(1), height=5, width=11) 
        button1.grid(row=2, column=0) 

        button2 = Button(gui, text=' 2 ', fg='black', 
                        command=lambda: press(2), height=5, width=11) 
        button2.grid(row=2, column=1) 

        button3 = Button(gui, text=' 3 ', fg='black', 
                        command=lambda: press(3), height=5, width=11) 
        button3.grid(row=2, column=2) 

        button4 = Button(gui, text=' 4 ', fg='black', 
                        command=lambda: press(4), height=5, width=11) 
        button4.grid(row=3, column=0) 

        button5 = Button(gui, text=' 5 ', fg='black', 
                        command=lambda: press(5), height=5, width=11) 
        button5.grid(row=3, column=1) 

        button6 = Button(gui, text=' 6 ', fg='black', 
                        command=lambda: press(6), height=5, width=11) 
        button6.grid(row=3, column=2) 

        button7 = Button(gui, text=' 7 ', fg='black', 
                        command=lambda: press(7), height=5, width=11) 
        button7.grid(row=4, column=0) 

        button8 = Button(gui, text=' 8 ', fg='black', 
                        command=lambda: press(8), height=5, width=11) 
        button8.grid(row=4, column=1) 

        button9 = Button(gui, text=' 9 ', fg='black', 
                        command=lambda: press(9), height=5, width=11) 
        button9.grid(row=4, column=2) 

        button0 = Button(gui, text=' 0 ', fg='black', 
                        command=lambda: press(0), height=5, width=11) 
        button0.grid(row=5, column=0) 

        plus = Button(gui, text=' + ', fg='black', 
                    command=lambda: press("+"), height=5, width=11) 
        plus.grid(row=2, column=3) 

        minus = Button(gui, text=' - ', fg='black', 
                    command=lambda: press("-"), height=5, width=11) 
        minus.grid(row=3, column=3) 

        multiply = Button(gui, text=' * ', fg='black', 
                        command=lambda: press("*"), height=5, width=11) 
        multiply.grid(row=4, column=3) 

        divide = Button(gui, text=' / ', fg='black', 
                        command=lambda: press("/"), height=5, width=11) 
        divide.grid(row=5, column=3) 

        equal = Button(gui, text=' = ', fg='black', 
                    command=equalpress, height=5, width=11) 
        equal.grid(row=5, column=2) 

        clear = Button(gui, text='Clear', fg='black', 
                    command=clear, height=5, width=11) 
        clear.grid(row=5, column='1') 

	
	def closeCur(self,controller):
		self.pack_forget()
		controller.show_frame(PageThree)

class PageThree(Frame):

	def __init__(self,parent,controller):

		Frame.__init__(self, parent)
		self.controller=controller
		Label(self, text="Feedback").pack()
		Button(self, text="Next", command=lambda:self.closeCur(controller)).pack()
	        Label(self, text="First Name:").pack(padx=10)#grid(row=0,column=1)
        	self.nf = Entry(self).pack(padx=10)#grid(row=0,column=2,columnspan=6)
        	Label(self, text="Second Name:").pack(padx=10)#grid(row=1,column=1)
        	self.ns = Entry(self).pack(padx=10)#grid(row=1,column=2,columnspan=6)
        
        	val=IntVar()
		val.set(0)
		Label(self, text="Rate your experience").pack()
		rating = [("Excellent",1),
				("V.Good",2),
				("Good",3),
				("Okay",4),
				("V.Bad",5)]
		for v,r in enumerate(rating):
			Radiobutton(self, 
				text=r,
				padx = 20, 
				variable=val, 
				command=lambda:self.ShowChoice(val),
				value=v).pack(anchor=W)

	        var=StringVar(self)
		var.set("choose")
	        Label(self, text="Profession: ").pack(padx=10)
        	prof=["Editor","Student","Dev","HR"]
        	obj= OptionMenu(self,var,*prof)
        	obj.pack()
      
	def closeCur(self,controller):
		self.pack_forget()
		controller.show_frame(PageFour)

	def ShowChoice(self,val):
		print(val.get())


class PageFour(Frame):
	def __init__(self,parent,controller):

		Frame.__init__(self, parent)
		self.controller=controller
		Label(self, text="Thank you, you may exit").pack()
		Button(self, text="Quit", command=lambda:self.closeAll(controller)).pack()

	def closeAll(self,controller):
		#self.pack_forget()
		controller.quitAll()


#root = Tk()		
app = Sample()
app.geometry("500x500+500+500")
app.mainloop()
