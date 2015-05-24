#!/usr/bin/env python

import Tkinter as tk
from Tkinter import*

class TunerGui(tk.Frame):	
	def __init__(self, master=None):
		# Initialize root frame
		tk.Frame.__init__(self, master)  
		
		# reads slider
		self.getSlider()
		self.grid()

	def getSlider(self):
		# create label frame for sliders
		self.sliderFrame = Label(self, text= '')
		
		# create empy list of sliders
		self.sliderFrame.motorScrolls = [None]*9	
		
		# Create list of motor labels
		sliderLabels = ["r Kp", "r Ki", "r Kd", "y Kp", "y Ki", "y Kd", "gamma Kp", "gamma Ki", "gamma Kd" ]

		# Create scroll bars for each PID constant
		for i in range(0,9):
			label = sliderLabels[i]				
			self.sliderFrame.motorScaleLabel = Label(self.sliderFrame, text=label)
			self.sliderFrame.motorScaleLabel.grid(row=i, column=0, sticky=W)
	
			self.sliderFrame.motorScrolls[i] = Scale(self.sliderFrame, orient=tk.HORIZONTAL, from_=0,to=100, length=450)
			self.sliderFrame.motorScrolls[i].grid(row=i, column=1, sticky=W+E)
			
		self.sliderFrame.grid(row=0, column=0, columnspan=2, ipadx=10, sticky=W+E)		
		

	def getConstants(self):
		constantsList = []
		for i in range(0,9):
			constantsList.append(self.sliderFrame.motorScrolls[i].get())
		return constantsList

