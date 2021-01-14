##############################
# Dice Calculator ~ v1 ~ SAB #
##############################

import random as r
from tkinter import *

# template
'''
	lbl = Label(
		# master
	 	<master window>,
	 	# widget look
	 	bg = <background color; string>,
	 	height = <label size; int>,
	 	width = <label size; int>,
	 	bd = <border; int (in pixels); default = 1>,
		relief = <boarder style; default = FLAT>,
	 	# text
	 	text = <text shown; string>,
	 	fg = <text color; string>,
	 	font = <font; string>,
	 	anchor = <text poition; anchor; default = CENTER>,
	 	justify = <text position - LEFT, CENTER, or RIGHT>,
	 	padx = <extra space, left and right; string; default = 1>,
	 	pady = <extra space, left and right; string; default = 1>,
	 	# other
	 	underline = <display an underline below the nth letter of the text; default = -1>,
	 	wraplength = <limit the number of characters in each line>,
	 	cursor = <cursor apearence when on widget; cursor type>,
	 	bitmap = <display bitmap; bitmap or image object>,
	 	image = <display image; image object>,
	 	textvariable = <to slave the text displayed>
	 	)
	 
	btn = Button(
	 	# master
	 	<master window>,
	 	# widget look
	 	bg = <background color; string>,
	 	height = <label size; int>,
	 	width = <label size; int>,
	 	bd = <border; int (in pixels); default = 1>,
		relief = <boarder style; default = FLAT>,
	 	# text
	 	text = <text shown; string>,
	 	fg = <text color; string>,
	 	font = <font; string>,
	 	justify = <text position - LEFT, CENTER, or RIGHT>,
	 	padx = <extra space, left and right; string; default = 1>,
	 	pady = <extra space, left and right; string; default = 1>,
	 	# on press
	 	command = lambda: <Funcion>,
	 	activebackground = <bg when pressed>,
	 	activeforeground = <fg when pressed>,
	 	# other
	 	underline = <display an underline below the nth letter of the text; default = -1>,
	 	wraplength = <limit the number of characters in each line>,
	 	highlightcolor = <color of the focus highlight>,
	 	image = <display image; image object>,
	 	# state
	 	state = <
	 		state = DISABLED - gray out the button and make it unresponsive
	 		state = ACTIVE - the mouse is over it
	 		state = NORMAL - default
	 	>
	 	)
	 
	ent = Entry(
	 	# master
	 	<master window>,
	 	# widget look
	 	bg = <background color; string>,
	 	width = <label size; int>,
	 	bd = <border; int (in pixels); default = 1>,
		relief = <boarder style; default = FLAT>,
	 	# text (user input)
	 	fg = <text color; string>,
	 	font = <font; string>,
	 	justify = <text position - LEFT, CENTER, or RIGHT>,
	 	selectbackground = <bg of selected text>,
	 	selectforeground = <fg of selected text>,
	 	selectborderwidth = <with of boarder around selected text>,
	 	# on user updateing box
	 	command = lambda: <Funcion>,
	 	# other
	 	highlightcolor = <color of the focus highlight>,
	 	cursor = <cursor apearence when on widget; cursor type>,
	 	exportselection = <if you dont want export to clip board (ignore)>,
	 	show = <password protection; eg show="*">,
	 	textvariable = <to retrieve the current text from your entry widget
				you must set this option to an instance of the StringVar obj>,
	 	xscrollcommand = <make scrollbar stuff>,
	 	# state
	 	state = <
	 		state = DISABLED - gray out the button and make it unresponsive
	 		state = ACTIVE - the mouse is over it
	 		state = NORMAL - default
	 	>
	 	)
'''

print()

RollingWindow = Tk()
#PreSetWindow = Tk()

RollingWindow.title("Rolling Window")
RollingWindow.geometry('500x350')

#COMEBACKTO
if False:
	def start(self):
	    self.configure(text=" advantage ", command=lambda: start(self), bg='green')

	def stop(self):
	    self.configure(text=" advantage ", command=lambda: start(advantage_btn), bg='#FFFFFF')

	def _drawBars(place):
		newLine_Canv = Canvas(RollingWindow, width=2.5, height=400)
		newLine_Canv.create_line(0, 0, 0, 400, width = 10)
		newLine_Canv.place(x=place, y=0)

#LOG
Log_lbl = Label(
	# master
	RollingWindow,
	# widget look
	bg = "white",
	height = 20,
	width = 26,
	bd = 2,
	relief = "solid",
	# text
	text = "Log:",
	font=("Courier", 10),
	anchor = "nw",
	justify = "left"
	)
Log_lbl.place(x=270, y=5)

global logQueue
logQueue = ["Temp-Log"]
def Log(textInpt):
	textInpt = str(textInpt)

	print(textInpt)

	logQueue.append(textInpt)
	if len(logQueue) > 19:
		logQueue.pop(0)
	else: pass

	bigLog = "Log:"
	for i in logQueue:
		if i != "Temp-Log":
			bigLog = bigLog + "\n" + i
	Log_lbl.config(text = bigLog)
	return logQueue

#Modifiers
def toggle(self, other_BTNLIST):
	other = other_BTNLIST
	if self['bg'] == "gray":
		self.configure(bg = "green")
		for i in other:
			i.configure(bg = "gray")
	elif self['bg'] == "green":
		self.configure(bg = "gray")

adv_btn = Button(RollingWindow)
adv_btn.configure(
	bg = "gray",
	text=("Advantage"),
	font=("TkDefaultFont", 10),
	height = 1,
	width = 8,
	# on press
	command= lambda: toggle(adv_btn, [dis_btn]),
	activebackground = "green"
	)
adv_btn.place(x=10, y=10 + (35 * 6))

dis_btn = Button(RollingWindow)
dis_btn.configure(
	bg = "gray",
	text=("Disdvantage"),
	font=("TkDefaultFont", 10),
	height = 1,
	width = 8,
	# on press
	command= lambda: toggle(dis_btn, [adv_btn]),
	activebackground = "green"
	)
dis_btn.place(x=10, y=10 + (35 * 7))

# DICE
def _makeLenth(text, length):
	text = str(text)
	while len(text) != length:
		text = text + " "
	#next while
	return text

class Dice(object):
	def __init__(self, sideNum):
		self.sideNum = sideNum
		self.name    = "D" + str(sideNum)
		if self.sideNum == 100:
			self.name = "PCT"
		self.fomatedName = _makeLenth(self.name, 3)

		self.btn = Button(RollingWindow,
			bg = "gray",
			text=("roll " + self.name),
			font=("TkDefaultFont", 10),
			height = 1,
			width = 8,
			command=self.rollAction,
			activebackground = "orange4")

	def roll(self, log = True):
		mod = 0
		log = log
		roll = r.randint(1, self.sideNum)
		rollTotal = roll + mod
		formatedRoll      = _makeLenth(roll     , 3)
		formatedRollTotal = _makeLenth(rollTotal, 3)

		#Build Log:
		if True:
			formatedRoll      = _makeLenth(roll     , 3)
			formatedMod       = _makeLenth(mod      , 3)
			formatedRollTotal = _makeLenth(rollTotal, 3)

			if   mod != 0 and mod > 0:
				logResult = formatedRoll + " + " + formatedMod + " = " + formatedRollTotal
			elif mod != 0 and mod < 0:
				logResult = formatedRoll + " - " + formatedMod + " = " + formatedRollTotal
			else:
				logResult = str(formatedRoll)

			rollLog = self.fomatedName + ": " + logResult

		if log:
			Log(rollLog)
		return {'roll': roll, 'log': rollLog, 'crit':""}

	def roll_advantage(self):
		if logQueue[len(logQueue)-1] != "----------------":
			Log("----------------")
		else: pass
		roll1 = self.roll(False)
		roll2 = self.roll(False)

		if roll1['roll'] > roll2['roll']:
			Log(roll1['log'] + "<--")
			Log(roll2['log'])
		elif roll1['roll'] < roll2['roll']:
			Log(roll1['log'])
			Log(roll2['log'] + "<--")
		else:
			Log(roll1['log'])
			Log(roll2['log'])


		Log("----------------")

	def roll_disadvantage(self):
		if logQueue[len(logQueue)-1] != "----------------":
			Log("----------------")
		else: pass
		roll1 = self.roll(False)
		roll2 = self.roll(False)

		if roll1['roll'] < roll2['roll']:
			Log(roll1['log'] + "<--")
			Log(roll2['log'])
		elif roll1['roll'] > roll2['roll']:
			Log(roll1['log'])
			Log(roll2['log'] + "<--")
		else:
			Log(roll1['log'])
			Log(roll2['log'])


		Log("----------------")

	def rollAction(self):
		if adv_btn['bg'] == "green":
			self.roll_advantage()
		elif dis_btn['bg'] == "green":
			self.roll_disadvantage()
		else:
			self.roll()


class DiceWithCrits(Dice):
	def __init__(self, sideNum):
		Dice.__init__(self, sideNum)
	
	def roll(self, log = True):
		mod = 0
		log = log
		roll = r.randint(1, self.sideNum)
		rollTotal = roll + mod
		formatedRoll      = _makeLenth(roll     , 3)
		formatedRollTotal = _makeLenth(rollTotal, 3)

		#Build Log:
		if True:
			formatedRoll      = _makeLenth(roll     , 3)
			formatedMod       = _makeLenth(mod      , 3)
			formatedRollTotal = _makeLenth(rollTotal, 3)

			if   mod != 0 and mod > 0:
				logResult = formatedRoll + " + " + formatedMod + " = " + formatedRollTotal
			elif mod != 0 and mod < 0:
				logResult = formatedRoll + " - " + formatedMod + " = " + formatedRollTotal
			else:
				logResult = str(formatedRoll)

			rollLog = self.fomatedName + ": " + logResult

		if log:
			Log(rollLog)

		if roll == 1:
			crit =  " - Nat 1! -"
			if log:
				Log(crit)
		elif roll == self.sideNum:
			crit = " - Nat " + str(self.sideNum) + "! -"
			if log:
				Log(crit)
		else:
			crit = ""

		return {'roll': roll, 'log': rollLog, 'crit':crit}

dice = []
for i in (4, 6, 8, 10, 20, 100):
	if i == 20 or i == 100:
		dice.append(DiceWithCrits(i))
	else:
		dice.append(Dice(i))
#next i
loop = 0
for i in dice:
	i.btn.place(x=10, y=10+ (35 * loop))
	loop += 1
#next i

RollingWindow.mainloop()
