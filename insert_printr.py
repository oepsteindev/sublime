import sublime
import sublime_plugin
import datetime



class DumpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sig = "print_r(); "
		self.view.insert(edit, self.view.sel()[0].begin(), sig)
