#!python2
#App Name: Python Virtual Assistant - GUI
#App Description: Python Digital Assistant GUI with wxPython and Text To Speech Audio Assistance
#Python Version 2.7
#Developper: Larry Georges Muala

import wx
import wikipedia
import wolframalpha
import pyttsx

	
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None,
			pos=wx.DefaultPosition, size=wx.Size(450, 100),
			style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
			wx.CLOSE_BOX | wx.CLIP_CHILDREN,
			title="Python Digital Assistant")
		
		panel = wx.Panel(self)
		my_sizer = wx.BoxSizer(wx.VERTICAL)
		lbl = wx.StaticText(panel,
		label="Welcome to the Python Interactive and Vocal Assistant. How can I help you?")
		my_sizer.Add(lbl, 0, wx.ALL, 5)
		self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
		self.txt.SetFocus()
		self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
		my_sizer.Add(self.txt, 0, wx.ALL, 5)
		panel.SetSizer(my_sizer)
		self.Show()
		
		
		engine = pyttsx.init()
		rate = engine.getProperty('rate')
		engine.setProperty('rate', rate-65)
		engine.say('Welcome, to the Python Interactive, and Vocal Assistant. How can I help you?')
		engine.runAndWait()
		
		

		
		
	def OnEnter(self, event):
		input = self.txt.GetValue()
		input = input.lower()
		
		
		try:
			#WolfRam
			app_id = "G639QJ-GRP8YT7V92"

			client = wolframalpha.Client(app_id)

			res = client.query(input)

			answer = next(res.results).text
			
			print answer
			
			engine = pyttsx.init()
			rate = engine.getProperty('rate')
			engine.setProperty('rate', rate-65)
			engine.say(answer)
			engine.runAndWait()
	
		except:
			#Wikipedia
			print wikipedia.summary(input)
			
			engine = pyttsx.init()
			rate = engine.getProperty('rate')
			engine.setProperty('rate', rate-65)
			engine.say('You searched for ' + input)
			engine.runAndWait()
	
	
	
if __name__ == "__main__":
	app = wx.App(True)
	frame = MyFrame()
	app.MainLoop()
	