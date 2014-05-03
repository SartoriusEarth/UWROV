import Tkinter as tk	   

class OrcusGUI(tk.Frame):			  
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)  
		self.frontLeft = 0
		self.frontRight = 0
		self.backLeft = 0
		self.backRight = 0
		self.frontVert = 0
		self.backVert = 0
		
		self.C = tk.Canvas(self, height=275, width=200)
		self.rov = self.C.create_rectangle(20,20,180,255, fill='#4c0099')
		self.frontLeftLine = self.C.create_line(0,0,0,0)
		self.frontRightLine = self.C.create_line(0,0,0,0)
		self.backLeftLine = self.C.create_line(0,0,0,0)
		self.backRightLine = self.C.create_line(0,0,0,0)
		self.frontVertLine = self.C.create_line(0,0,0,0)
		self.backVertLine = self.C.create_line(0,0,0,0)
		self.C.grid(row = 0, column = 0, rowspan = 6)
		
		self.grid()		
		self.getControlInput()
		self.drawMotorStatus()
	
	# Motor control slider callbacks
	def frontLeftMotorValue(self, value = 0):
		self.frontLeft = int(value)
		self.printMotorValues()
		self.drawMotorStatus()
	def frontRightMotorValue(self, value = 0):
		self.frontRight = int(value)
		self.printMotorValues()
		self.drawMotorStatus()
	def backLeftMotorValue(self, value = 0):
		self.backLeft = int(value)
		self.printMotorValues()
		self.drawMotorStatus()
	def backRightMotorValue(self, value = 0):
		self.backRight = int(value)
		self.printMotorValues()
		self.drawMotorStatus()
	def frontVertMotorValue(self, value = 0):
		self.frontVert = int(value)
		self.printMotorValues()
		self.drawMotorStatus()
	def BackVertMotorValue(self, value = 0):
		self.backVert = int(value)
		self.printMotorValues()
		self.drawMotorStatus()
			
	# gets control information from sliders
	def getControlInput(self):
		motorValueCallbacks = [self.frontLeftMotorValue, self.frontRightMotorValue, self.backLeftMotorValue, self.backRightMotorValue, self.frontVertMotorValue, self.BackVertMotorValue]
		
		motorLabels = ["FrontLeft", "FrontRight", "BackLeft", "BackRight", "FrontVert", "BackVert"]
		
		# Create scroll bars for each motor
		for i in range(0,6):
			label = motorLabels[i]
			self.motorScaleLabel = tk.Label(self, text = label)
			self.motorScaleLabel.grid(row = i, column = 1, sticky = tk.W)
			
			self.motorScroll = tk.Scale(self, command=motorValueCallbacks[i], orient=tk.HORIZONTAL)
			self.motorScroll.grid(row = i, column = 2, padx = 0, pady = 10, ipadx = 100)
	
	# prints motor values from sliders
	def printMotorValues(self):
		print ("FrontLeft: " + str(self.frontLeft))
		print ("FrontRight: " + str(self.frontRight))
		print ("BackLeft: " + str(self.backLeft))
		print ("BackRight: " + str(self.backRight))
		print ("FrontVert: " + str(self.frontVert))
		print ("BackVert: " + str(self.backVert))
	
	# draws ROV motors status
	def drawMotorStatus(self):
		FRONT_Y = 50;
		BACK_Y = 210;
		LEFT_X = 40;
		RIGHT_X = 160;
		VERT_X = 100;
		FRONT_VERT_Y = 75;
		BACK_VERT_Y = 180;
		
		self.C.delete(self.frontLeftLine)
		self.C.delete(self.frontRightLine)
		self.C.delete(self.backLeftLine)
		self.C.delete(self.backRightLine)
		self.C.delete(self.frontVertLine)
		self.C.delete(self.backVertLine)
		
		self.frontLeftLine = self.C.create_line(LEFT_X, FRONT_Y, LEFT_X+0.5*(int(self.frontLeft)-50), FRONT_Y-0.866*(int(self.frontLeft)-50), width=10)
		self.frontRightLine = self.C.create_line(RIGHT_X, FRONT_Y, RIGHT_X-0.5*(int(self.frontRight)-50), FRONT_Y-0.866*(int(self.frontRight)-50), width=10)
		self.backLeftLine = self.C.create_line(LEFT_X, BACK_Y, LEFT_X+0.5*(int(self.backLeft)-50), BACK_Y+0.866*(int(self.backLeft)-50), width=10)
		self.backRightLine = self.C.create_line(RIGHT_X, BACK_Y, RIGHT_X-0.5*(int(self.backRight)-50), BACK_Y+0.866*(int(self.backRight)-50), width=10)
		self.frontVertLine = self.C.create_line(VERT_X, FRONT_VERT_Y, VERT_X, FRONT_VERT_Y-50+int(self.frontVert), width=10)
		self.backVertLine = self.C.create_line(VERT_X, BACK_VERT_Y, VERT_X, BACK_VERT_Y-50+int(self.backVert), width=10)

gui = OrcusGUI()		
gui.master.geometry("500x500")			   
gui.master.title('ROV ORCUS')  
gui.mainloop()   