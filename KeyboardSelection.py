import sublime, sublime_plugin
import string

class MoveToBegOfContigBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		oldSelRegions = list(view.sel())
		view.sel().clear()
		for thisregion in oldSelRegions:
			if(forward): #forward
				caretPos = thisregion.b
				if(view.substr(caretPos) not in string.whitespace): #initially have char right of me, find whitespace
					while ((view.substr(caretPos) not in string.whitespace) and (caretPos < view.size())):
						caretPos += 1
				while((view.substr(caretPos) in string.whitespace) and (caretPos < view.size())): #now have whitespace right of me, find char beginning
					caretPos += 1
				else:
					view.sel().add(sublime.Region(caretPos))
					view.show(caretPos)
			else: #backward
				caretPos = thisregion.b - 1
				if(view.substr(caretPos) in string.whitespace): #initially have whitespace left of me, find char
					while ((view.substr(caretPos) in string.whitespace) and (caretPos >= 0)):
						caretPos -= 1
				while ((view.substr(caretPos) not in string.whitespace) and (caretPos >= 0)): #now have char left of me, find whitespace
					caretPos -= 1
				else:
					view.sel().add(sublime.Region(caretPos+1))
					view.show(caretPos+1)

class MoveToBegOfSubwordBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		# chr(34) is doublequote
		# chr(9) is tab
		# chr(10) is new line
		# chr(13) is carriage return
		subwordDelims = [" ", chr(9), chr(10), chr(13), chr(34), ".", "+", "_", "<", ">", "[", "]", "{", "}", "-", "(", ")", "|", "\\"]
		view = self.view
		oldSelRegions = list(view.sel())
		view.sel().clear()
		for thisregion in oldSelRegions:
			if(forward): #forward
				caretPos = thisregion.b
				haveMovedAtleastOnce = False
				while ( (view.substr(caretPos) not in subwordDelims) and (caretPos < view.size()) ):
					if(not haveMovedAtleastOnce):
						haveMovedAtleastOnce = True
					caretPos += 1
				if(not haveMovedAtleastOnce):
					caretPos += 1
				view.sel().add(sublime.Region(caretPos))
				view.show(caretPos)
			else: #backward
				caretPos = thisregion.b - 1
				haveMovedAtleastOnce = False
				while ( (view.substr(caretPos) not in subwordDelims) and (caretPos >= 0) ):
					if(not haveMovedAtleastOnce):
						haveMovedAtleastOnce = True
					caretPos -= 1
				if(not haveMovedAtleastOnce):
					caretPos -= 1
				view.sel().add(sublime.Region(caretPos+1))
				view.show(caretPos+1)

class ExpandSelectionToDelimsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# chr(9) is tab
		# chr(10) is new line
		# chr(13) is carriage return
		universalDelims = [" ", "\"", "\'", "-", "(", ")", "<", ">", "[", "]", "{", "}", ":", ".", ",", "%", "@", "&", chr(9), "\n"]
		view = self.view
		oldSelRegions = list(view.sel())
		for thisregion in oldSelRegions:
			thisRegionBegin = thisregion.begin() - 1
			thisRegionEnd = thisregion.end()
			if( (thisregion.begin() != thisRegionEnd) and (view.substr(thisRegionBegin) in universalDelims) ):
				thisRegionBegin -= 1
			while ((view.substr(thisRegionBegin) not in universalDelims) and (thisRegionBegin >= 0)):
				thisRegionBegin -= 1
			thisRegionBegin += 1

			if( (thisregion.begin() != thisRegionEnd) and (view.substr(thisRegionEnd) in universalDelims) ):
				thisRegionEnd += 1
			while((view.substr(thisRegionEnd) not in universalDelims) and (thisRegionEnd < view.size())):
				thisRegionEnd += 1

			view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))

class ExpandSelectionToQuotesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		beginDelims = ["\"", "\'"]
		endDelims = ["\"", "\'"]
		view = self.view
		oldSelRegions = list(view.sel())
		for thisregion in oldSelRegions:
			thisRegionBegin = thisregion.begin() - 1
			thisRegionEnd = thisregion.end()
			while ((view.substr(thisRegionBegin) not in beginDelims) and (thisRegionBegin >= 0)):
				thisRegionBegin -= 1
			thisRegionBegin += 1

			while((view.substr(thisRegionEnd) not in endDelims) and (thisRegionEnd < view.size())):
				thisRegionEnd += 1

			view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))

class ExpandSelectionToBracketsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		beginDelims = ["(", "<", "[", "{"]
		endDelims = [")", ">", "]", "}"]
		view = self.view
		oldSelRegions = list(view.sel())
		for thisregion in oldSelRegions:
			thisRegionBegin = thisregion.begin() - 1
			thisRegionEnd = thisregion.end()
			while ((view.substr(thisRegionBegin) not in beginDelims) and (thisRegionBegin >= 0)):
				thisRegionBegin -= 1
			thisRegionBegin += 1

			while((view.substr(thisRegionEnd) not in endDelims) and (thisRegionEnd < view.size())):
				thisRegionEnd += 1

			view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))

class ExpandSelectionToWhitespaceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		oldSelRegions = list(view.sel())
		# view.sel().clear()
		for thisregion in oldSelRegions:
			thisRegionBegin = thisregion.begin() - 1
			while ((view.substr(thisRegionBegin) not in string.whitespace) and (thisRegionBegin >= 0)):
				thisRegionBegin -= 1
			thisRegionBegin += 1

			thisRegionEnd = thisregion.end()
			while((view.substr(thisRegionEnd) not in string.whitespace) and (thisRegionEnd < view.size())):
				thisRegionEnd += 1

			# if(thisRegionBegin != thisRegionEnd):
			view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))
			# else:
			# 	view.sel().add(sublime.Region(thisRegionBegin, thisRegionBegin))

class DeleteToBegNextContigBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("delete_word", {"forward": True})
		for thisregion in self.view.sel():
			if(self.view.substr(thisregion.begin()) in string.whitespace):
					nonWhitespacePos = thisregion.begin()
					while((self.view.substr(nonWhitespacePos) in string.whitespace) and (nonWhitespacePos < self.view.line(thisregion.begin()).end())):
						nonWhitespacePos += 1
					self.view.erase(edit, sublime.Region(thisregion.begin(), nonWhitespacePos))

# TODO
class SelectToNextContigBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		pass

# TODO
class SelectToNextSubwordBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		pass
		
# Reference (no longer used)
# class ExpandSelectionToSentenceCommand(sublime_plugin.TextCommand):
# 	def run(self, edit):
# 		view = self.view
# 		oldSelRegions = list(view.sel())
# 		view.sel().clear()
# 		for thisregion in oldSelRegions:
# 			thisRegionBegin = thisregion.begin() - 1
# 			while ((view.substr(thisRegionBegin) not in ".") and (thisRegionBegin >= 0)):
# 				thisRegionBegin -= 1

# 			thisRegionBegin += 1
# 			while((view.substr(thisRegionBegin) in string.whitespace) and (thisRegionBegin < view.size())):
# 				thisRegionBegin += 1

# 			thisRegionEnd = thisregion.end()
# 			while((view.substr(thisRegionEnd) not in ".") and (thisRegionEnd < view.size())):
# 				thisRegionEnd += 1

# 			if(thisRegionBegin != thisRegionEnd):
# 				view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd+1))
# 			else:
# 				view.sel().add(sublime.Region(thisRegionBegin, thisRegionBegin))
			
# Reference (no longer used)
# class MoveToContigboundaryCommand(sublime_plugin.TextCommand):
# 	def run(self, edit, forward, extend=False):
# 		view = self.view
# 		oldSelRegions = list(view.sel())
# 		view.sel().clear()
# 		for thisregion in oldSelRegions:
# 			if(forward): #forward
# 				caretPos = thisregion.b
# 				if(view.substr(caretPos) in string.whitespace): #initially have whitespace right of me, find char
# 					while((view.substr(caretPos) in string.whitespace) and (caretPos < view.size())):
# 						caretPos += 1
# 				else: #initially have char right of me, find whitespace
# 					while ((view.substr(caretPos) not in string.whitespace) and (caretPos < view.size())):
# 						caretPos += 1
# 				if(extend):
# 					view.sel().add(sublime.Region(thisregion.a, caretPos))
# 					view.show(caretPos)
# 				else:
# 					view.sel().add(sublime.Region(caretPos))
# 					view.show(caretPos)
# 			else: #backward
# 				caretPos = thisregion.b - 1
# 				if(view.substr(caretPos) in string.whitespace): #initially have whitespace left of me, find char
# 					while ((view.substr(caretPos) in string.whitespace) and (caretPos >= 0)):
# 						caretPos -= 1
# 				else: #initially have char left of me, find whitespace
# 					while ((view.substr(caretPos) not in string.whitespace) and (caretPos >= 0)):
# 						caretPos -= 1
# 				if(extend):
# 					view.sel().add(sublime.Region(thisregion.a, caretPos+1))
# 					view.show(caretPos+1)
# 				else:
# 					view.sel().add(sublime.Region(caretPos+1))
# 					view.show(caretPos+1)

# Reference (no longer used)
# class DeleteWordWhitespaceCommand(sublime_plugin.TextCommand):
# 	def run(self, edit):
# 		self.view.run_command("delete_word", {"forward": True})
# 		for thisregion in self.view.sel():
# 			if(self.view.substr(thisregion.begin()) in string.whitespace):
# 					nonWhitespacePos = thisregion.begin()
# 					while((self.view.substr(nonWhitespacePos) in string.whitespace) and (nonWhitespacePos < self.view.line(thisregion.begin()).end())):
# 						nonWhitespacePos += 1
# 					self.view.erase(edit, sublime.Region(thisregion.begin(), nonWhitespacePos))
