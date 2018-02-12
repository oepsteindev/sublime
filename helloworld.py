import sublime
import sublime_plugin
import datetime



class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		day = (datetime.datetime.now().strftime("%Y-%m-%d")) 
		sig = "//OE " + day
		self.view.insert(edit, self.view.sel()[0].begin(), sig)
