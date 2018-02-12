# Save as signature.py
import datetime, getpass
import sublime, sublime_plugin
class SignatureCommand(sublime_plugin.TextCommand):
        def run(self, edit):
                signature = "[%s %s <%s@example.com>]\n\n\t" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), getpass.getuser(), getpass.getuser().lower())

                self.view.insert(edit, 0, signature)
Tagged w/ #date time sublime snippet #signature #snippets #sublime text 2 #text 
