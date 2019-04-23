import sublime, sublime_plugin
import string

class MoveToBegOfContigBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 
		whitespaceChars = [chr(32), chr(9), chr(10), chr(13)]
		oldSelRegions = list(view.sel())
		view.sel().clear()
		for thisregion in oldSelRegions:
			if(forward): #forward
				caretPos = thisregion.b
				if(view.substr(caretPos) not in whitespaceChars): #initially have char right of me, find whitespace
					while ((view.substr(caretPos) not in whitespaceChars) and (caretPos < view.size())):
						caretPos += 1
				while((view.substr(caretPos) in whitespaceChars) and (caretPos < view.size())): #now have whitespace right of me, find char beginning
					caretPos += 1
				else:
					view.sel().add(sublime.Region(caretPos))
					view.show(caretPos)
			else: #backward
				caretPos = thisregion.b - 1
				if(view.substr(caretPos) in whitespaceChars): #initially have whitespace left of me, find char
					while ((view.substr(caretPos) in whitespaceChars) and (caretPos >= 0)):
						caretPos -= 1
				while ((view.substr(caretPos) not in whitespaceChars) and (caretPos >= 0)): #now have char left of me, find whitespace
					caretPos -= 1
				else:
					view.sel().add(sublime.Region(caretPos+1))
					view.show(caretPos+1)

class MoveToBegOfSubwordBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 34=" 39=' 37=% 64=@ 38=& 58=: 46=. 44=, 43=+ 95=_ 45=- 60=< 62=> 40=( 41=) 91=[ 93=] 123={ 125=} 124=| 92=\
		subwordDelims = [chr(32), chr(9), chr(10), chr(13), chr(34), chr(39), chr(37), chr(64), chr(38), chr(58), chr(46), chr(44), chr(43), chr(95), chr(45), chr(60), chr(62), chr(40), chr(41), chr(91), chr(93), chr(123), chr(125), chr(124), chr(92)]
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
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 34=" 39=' 37=% 64=@ 38=& 58=: 46=. 44=, 43=+ 95=_ 45=- 60=< 62=> 40=( 41=) 91=[ 93=] 123={ 125=} 124=| 92=\
		subwordDelims = [chr(32), chr(9), chr(10), chr(13), chr(34), chr(39), chr(37), chr(64), chr(38), chr(58), chr(46), chr(44), chr(43), chr(95), chr(45), chr(60), chr(62), chr(40), chr(41), chr(91), chr(93), chr(123), chr(125), chr(124), chr(92)]
		oldSelRegions = list(view.sel())
		for thisregion in oldSelRegions:
			thisRegionBegin = thisregion.begin() - 1
			thisRegionEnd = thisregion.end()
			if( (thisregion.begin() != thisRegionEnd) and (view.substr(thisRegionBegin) in subwordDelims) ):
				thisRegionBegin -= 1
			while ((view.substr(thisRegionBegin) not in subwordDelims) and (thisRegionBegin >= 0)):
				thisRegionBegin -= 1
			thisRegionBegin += 1

			if( (thisregion.begin() != thisRegionEnd) and (view.substr(thisRegionEnd) in subwordDelims) ):
				thisRegionEnd += 1
			while((view.substr(thisRegionEnd) not in subwordDelims) and (thisRegionEnd < view.size())):
				thisRegionEnd += 1

			view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))

class ExpandSelectionToQuotesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		# 34=" 39=' 
		beginDelims = [chr(34), chr(39)]
		endDelims = [chr(34), chr(39)]
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
		view = self.view
		# 60=< 62=> 40=( 41=) 91=[ 93=] 123={ 125=}
		beginDelims = [chr(60), chr(40), chr(91), chr(123)]
		endDelims = [chr(62), chr(41), chr(93), chr(125)]
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
		# 32=space 9=tab 10=newline 13=carriagereturn 
		whitespaceChars = [chr(32), chr(9), chr(10), chr(13)]
		oldSelRegions = list(view.sel())
		# view.sel().clear()
		for thisregion in oldSelRegions:
			thisRegionBegin = thisregion.begin() - 1
			while ((view.substr(thisRegionBegin) not in whitespaceChars) and (thisRegionBegin >= 0)):
				thisRegionBegin -= 1
			thisRegionBegin += 1

			thisRegionEnd = thisregion.end()
			while((view.substr(thisRegionEnd) not in whitespaceChars) and (thisRegionEnd < view.size())):
				thisRegionEnd += 1

			# if(thisRegionBegin != thisRegionEnd):
			view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))
			# else:
			# 	view.sel().add(sublime.Region(thisRegionBegin, thisRegionBegin))

class DeleteToBegNextContigBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 
		whitespaceChars = [chr(32), chr(9), chr(10), chr(13)]
		view.run_command("delete_word", {"forward": True})
		for thisregion in self.view.sel():
			if(self.view.substr(thisregion.begin()) in whitespaceChars):
					nonWhitespacePos = thisregion.begin()
					while((self.view.substr(nonWhitespacePos) in whitespaceChars) and (nonWhitespacePos < self.view.line(thisregion.begin()).end())):
						nonWhitespacePos += 1
					self.view.erase(edit, sublime.Region(thisregion.begin(), nonWhitespacePos))

class SelectToNextContigBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		whiteChars = (chr(32), chr(9), chr(10), chr(13))
		spaceChars = (chr(32), chr(9))
		newlineChars = (chr(10), chr(13))
		for thisregion in view.sel():
			if(thisregion.a == thisregion.b):
				if(forward): #forward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b
					if(view.substr(thisRegionEnd) in newlineChars): # have newline to right of me
						thisRegionEnd += 1
					elif(view.substr(thisRegionEnd) in spaceChars): #have space to right of me
						while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd < view.size())): #have whitespace to right of me, find char beginning
							thisRegionEnd += 1
					else: # have char to right of me
						while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd < view.size())):
							thisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))
					view.show(thisRegionEnd)
				else: #backward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b-1
					if(thisRegionEnd < 0):
						pass
					elif(view.substr(thisRegionEnd) in newlineChars): # have newline to left of me
							thisRegionEnd -= 1
					elif(view.substr(thisRegionEnd) in spaceChars): # have space to left of me
						while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd >= 0)):
							thisRegionEnd -= 1
					else: # have char to left of me
						while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd >= 0)):
							if(view.substr(thisRegionEnd) in newlineChars): # stop at newline to left of me
								break
							thisRegionEnd -= 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd+1))
					view.show(thisRegionEnd)
			elif(thisregion.a < thisregion.b):
				if(forward): #forward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b
					if(view.substr(thisRegionEnd) in newlineChars): # have newline to right of me
						thisRegionEnd += 1
					elif(view.substr(thisRegionEnd) in spaceChars): # have space to right of me
						while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd < view.size())): #have whitespace to right of me, find char beginning
							thisRegionEnd += 1
					else: # have char to right of me
						while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd < view.size())):
							thisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))
					view.show(thisRegionEnd)
				else: #backward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b-1
					if(thisRegionEnd < 0):
						pass
					elif(view.substr(thisRegionEnd) in newlineChars): # have newline to left of me
							thisRegionEnd -= 1				
					elif(view.substr(thisRegionEnd) in spaceChars): # have space to left of me
						while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd >= 0) and (thisRegionEnd > thisRegionBegin-1)):
							thisRegionEnd -= 1
					else: # have char to left of me
						while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd >= 0) and (thisRegionEnd > thisRegionBegin-1)):
							if(view.substr(thisRegionEnd) in newlineChars): # stop at newline to left of me
								break
							thisRegionEnd -= 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd+1))
					view.show(thisRegionEnd)
			else: # thisregion.a > thisregion.b
				if(forward): #forward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b
					if(view.substr(thisRegionEnd) in newlineChars): # have newline to right of me
						thisRegionEnd += 1
					elif(view.substr(thisRegionEnd) in spaceChars): # have space to right of me
						while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd < view.size() and (thisRegionEnd < thisRegionBegin))): #have whitespace to right of me, find char beginning
							thisRegionEnd += 1
					else: # have char to right of me
						while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd < view.size()) and (thisRegionEnd < thisRegionBegin)):
							thisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))
					view.show(thisRegionEnd)
				else: #backward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b-1
					if(thisRegionEnd < 0):
						pass
					elif(view.substr(thisRegionEnd) in newlineChars): # have newline to left of me
							thisRegionEnd -= 1				
					elif(view.substr(thisRegionEnd) in spaceChars): # have space to left of me
						while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd >= 0)):
							thisRegionEnd -= 1
					else: # have char to left of me
						while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd >= 0)):
							if(view.substr(thisRegionEnd) in newlineChars): # stop at newline to left of me
								break
							thisRegionEnd -= 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd+1))
					view.show(thisRegionEnd)

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
# 			while((view.substr(thisRegionBegin) in whitespaceChars) and (thisRegionBegin < view.size())):
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
# 				if(view.substr(caretPos) in whitespaceChars): #initially have whitespace right of me, find char
# 					while((view.substr(caretPos) in whitespaceChars) and (caretPos < view.size())):
# 						caretPos += 1
# 				else: #initially have char right of me, find whitespace
# 					while ((view.substr(caretPos) not in whitespaceChars) and (caretPos < view.size())):
# 						caretPos += 1
# 				if(extend):
# 					view.sel().add(sublime.Region(thisregion.a, caretPos))
# 					view.show(caretPos)
# 				else:
# 					view.sel().add(sublime.Region(caretPos))
# 					view.show(caretPos)
# 			else: #backward
# 				caretPos = thisregion.b - 1
# 				if(view.substr(caretPos) in whitespaceChars): #initially have whitespace left of me, find char
# 					while ((view.substr(caretPos) in whitespaceChars) and (caretPos >= 0)):
# 						caretPos -= 1
# 				else: #initially have char left of me, find whitespace
# 					while ((view.substr(caretPos) not in whitespaceChars) and (caretPos >= 0)):
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
# 			if(self.view.substr(thisregion.begin()) in whitespaceChars):
# 					nonWhitespacePos = thisregion.begin()
# 					while((self.view.substr(nonWhitespacePos) in whitespaceChars) and (nonWhitespacePos < self.view.line(thisregion.begin()).end())):
# 						nonWhitespacePos += 1
# 					self.view.erase(edit, sublime.Region(thisregion.begin(), nonWhitespacePos))
