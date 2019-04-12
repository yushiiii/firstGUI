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

	def __init__(self, parent, controller):

		Frame.__init__(self, parent)
		self.controller=controller
		Label(self, text="Next Page").pack()
		Button(self, text="Next", command=lambda:self.closeCur(controller)).pack()
	
	def closeCur(self,controller):
		self.pack_forget()
		controller.show_frame(PageThree)

class PageThree(Frame):
	def __init__(self,parent,controller):

		Frame.__init__(self, parent)
		self.controller=controller
		Label(self, text="Feedback").pack()
		Button(self, text="Next", command=lambda:self.closeCur(controler)).pack()
		val=IntVar()
		val.set(0)
		Label(self, text="Rate your experience").pack()
		rating = [("Excellent",1),
				("Very Good",2),
				("Good",3),
				("Bad",4),
				("Very Bad",5)]
		for v,r in enumerate(rating):
			Radiobutton(self, 
				text=r,
				padx = 20, 
				variable=val, 
				command=lambda:self.ShowChoice(val),
				value=v).pack(anchor=W)

	def closeCur(self,controller):
		self.pack_forget()
		controller.show_frame(PageFour)

	def ShowChoice(self,val):
		print(val.get())


class PageFour(Frame):
	def __init__(self,parent,controller):

		Frame.__init__(self, parent)
		self.controller=controller
		Label(self, text="Page 4").pack()
		Button(self, text="Quit", command=lambda:self.closeAll(controller)).pack()

	def closeAll(self,controller):
		#self.pack_forget()
		controller.quitAll()


#root = Tk()		
app = Sample()
app.mainloop()
