import sublime, sublime_plugin
import string

#---------------------------------------------------------------
class MoveToBegOfContigBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 
		whiteChars = (chr(32), chr(9), chr(10), chr(13))
		spaceChars = (chr(32), chr(9))  
		# newlineChars = (chr(10), chr(13))
		RegionsSelOld = list(view.sel())
		view.sel().clear()
		for ThisRegion in RegionsSelOld:
		# for ThisRegion in view.sel():
			if(forward): #forward
				ThisRegionBegin = ThisRegion.a
				ThisRegionEnd = ThisRegion.b
				while((view.substr(ThisRegionEnd) not in whiteChars) and (ThisRegionEnd < view.size())):
					ThisRegionEnd += 1
				while( (view.substr(ThisRegionEnd) in spaceChars) and (ThisRegionEnd < view.size()) ):
					ThisRegionEnd += 1
				if((ThisRegionEnd < view.size()) and (ThisRegionEnd == ThisRegion.b)):
					ThisRegionEnd += 1
				# view.sel().clear()
				view.sel().add(sublime.Region(ThisRegionEnd))
				view.show(ThisRegionEnd+1)
			else: #backward
				ThisRegionBegin = ThisRegion.a
				ThisRegionEnd = ThisRegion.b-1
				while((view.substr(ThisRegionEnd) in spaceChars) and (ThisRegionEnd >= 0)):
					ThisRegionEnd -= 1
				while((view.substr(ThisRegionEnd) not in whiteChars) and (ThisRegionEnd >= 0)):
					ThisRegionEnd -= 1
				if((ThisRegionEnd >= 0) and (ThisRegionEnd+1 == ThisRegion.b)):
					ThisRegionEnd -= 1
				# view.sel().clear()
				view.sel().add(sublime.Region(ThisRegionEnd+1))
				view.show(ThisRegionEnd)

# https://ee.hawaii.edu/~tep/EE160/Book/chap4/subsection2.1.1.1.html
class MoveToBegOfSubwordBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 34=" 35=# 36=$ 37=% 38=& 39=' 61== 64=@ 58=: 63=? 46=. 44=, 43=+ 95=_ 45=- 60=< 62=> 40=( 41=) 91=[ 93=] 123={ 125=} 124=| 47=/ 92=\
		subwordDelims = [chr(32), chr(9), chr(10), chr(13), chr(34), chr(35), chr(36), chr(37), chr(38), chr(39), chr(61), chr(64), chr(58), chr(63), chr(46), chr(44), chr(43), chr(95), chr(45), chr(60), chr(62), chr(40), chr(41), chr(91), chr(93), chr(123), chr(125), chr(124), chr(47), chr(92)]
		for ThisRegion in view.sel():
			if(forward): #forward
				ThisRegionBegin = ThisRegion.a
				ThisRegionEnd = ThisRegion.b
				while( (view.substr(ThisRegionEnd) not in subwordDelims) and (ThisRegionEnd < view.size()) ):
					ThisRegionEnd += 1
				if((ThisRegionEnd < view.size()) and (ThisRegionEnd == ThisRegion.b)):
					ThisRegionEnd += 1
				view.sel().clear()
				view.sel().add(sublime.Region(ThisRegionEnd))
				view.show(ThisRegionEnd+1)
			else: #backward
				ThisRegionBegin = ThisRegion.a
				ThisRegionEnd = ThisRegion.b-1
				while( (view.substr(ThisRegionEnd) not in subwordDelims) and (ThisRegionEnd >= 0) ):
					ThisRegionEnd -= 1
				if((ThisRegionEnd >= 0) and (ThisRegionEnd+1 == ThisRegion.b)):
					ThisRegionEnd -= 1
				view.sel().clear()
				view.sel().add(sublime.Region(ThisRegionEnd+1))
				view.show(ThisRegionEnd)

#---------------------------------------------------------------
class SelectToBegOfContigBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 
		whiteChars = (chr(32), chr(9), chr(10), chr(13))
		spaceChars = (chr(32), chr(9))  
		# newlineChars = (chr(10), chr(13))
		for ThisRegion in view.sel():
			if(ThisRegion.a == ThisRegion.b):
				if(forward): #forward
					ThisRegionBegin = ThisRegion.a
					ThisRegionEnd = ThisRegion.b
					while((view.substr(ThisRegionEnd) not in whiteChars) and (ThisRegionEnd < view.size())):
						ThisRegionEnd += 1
					while((view.substr(ThisRegionEnd) in spaceChars) and (ThisRegionEnd < view.size())):
						ThisRegionEnd += 1
					if((ThisRegionEnd < view.size()) and (ThisRegionEnd == ThisRegion.b)):
						ThisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd))
					view.show(ThisRegionEnd+1)
				else: #backward
					ThisRegionBegin = ThisRegion.a
					ThisRegionEnd = ThisRegion.b-1
					while((view.substr(ThisRegionEnd) in spaceChars) and (ThisRegionEnd >= 0)):
						ThisRegionEnd -= 1
					while((view.substr(ThisRegionEnd) not in whiteChars) and (ThisRegionEnd >= 0)):
						ThisRegionEnd -= 1
					if((ThisRegionEnd >= 0) and (ThisRegionEnd+1 == ThisRegion.b)):
						ThisRegionEnd -= 1					
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd+1))
					view.show(ThisRegionEnd)
			elif(ThisRegion.a < ThisRegion.b):
				if(forward): #forward
					ThisRegionBegin = ThisRegion.a
					ThisRegionEnd = ThisRegion.b
					while((view.substr(ThisRegionEnd) not in whiteChars) and (ThisRegionEnd < view.size())):
						ThisRegionEnd += 1
					while((view.substr(ThisRegionEnd) in spaceChars) and (ThisRegionEnd < view.size())):
						ThisRegionEnd += 1
					if((ThisRegionEnd < view.size()) and (ThisRegionEnd == ThisRegion.b)):
						ThisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd))
					view.show(ThisRegionEnd+1)
				else: #backward
					ThisRegionBegin = ThisRegion.a
					ThisRegionEnd = ThisRegion.b-1
					while((view.substr(ThisRegionEnd) in spaceChars) and (ThisRegionEnd > ThisRegionBegin-1) and (ThisRegionEnd >= 0)):
						ThisRegionEnd -= 1
					while((view.substr(ThisRegionEnd) not in whiteChars) and (ThisRegionEnd > ThisRegionBegin-1) and (ThisRegionEnd >= 0)):
						ThisRegionEnd -= 1
					if((ThisRegionEnd >= 0) and (ThisRegionEnd+1 == ThisRegion.b)):
						ThisRegionEnd -= 1
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd+1))
					view.show(ThisRegionEnd)
			else: # ThisRegion.a > ThisRegion.b
				if(forward): #forward
					ThisRegionBegin = ThisRegion.a
					ThisRegionEnd = ThisRegion.b
					while((view.substr(ThisRegionEnd) not in whiteChars) and (ThisRegionEnd < ThisRegionBegin) and (ThisRegionEnd < view.size())):
						ThisRegionEnd += 1
					while((view.substr(ThisRegionEnd) in spaceChars) and (ThisRegionEnd < ThisRegionBegin) and (ThisRegionEnd < view.size())):
						ThisRegionEnd += 1
					if((ThisRegionEnd < view.size()) and (ThisRegionEnd == ThisRegion.b)):
						ThisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd))
					view.show(ThisRegionEnd+1)
				else: #backward
					ThisRegionBegin = ThisRegion.a
					ThisRegionEnd = ThisRegion.b-1
					while((view.substr(ThisRegionEnd) in spaceChars) and (ThisRegionEnd >= 0)):
						ThisRegionEnd -= 1
					while((view.substr(ThisRegionEnd) not in whiteChars) and (ThisRegionEnd >= 0)):
						ThisRegionEnd -= 1
					if((ThisRegionEnd >= 0) and (ThisRegionEnd+1 == ThisRegion.b)):
						ThisRegionEnd -= 1
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd+1))
					view.show(ThisRegionEnd)

class SelectToBegOfSubwordBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 34=" 35=# 36=$ 37=% 38=& 39=' 61== 64=@ 58=: 63=? 46=. 44=, 43=+ 95=_ 45=- 60=< 62=> 40=( 41=) 91=[ 93=] 123={ 125=} 124=| 47=/ 92=\
		subwordDelims = [chr(32), chr(9), chr(10), chr(13), chr(34), chr(35), chr(36), chr(37), chr(38), chr(39), chr(61), chr(64), chr(58), chr(63), chr(46), chr(44), chr(43), chr(95), chr(45), chr(60), chr(62), chr(40), chr(41), chr(91), chr(93), chr(123), chr(125), chr(124), chr(47), chr(92)]
		for ThisRegion in view.sel():
			if(ThisRegion.a == ThisRegion.b):
				if(forward): #forward
					ThisRegionBegin = ThisRegion.a
					ThisRegionEnd = ThisRegion.b
					while( (view.substr(ThisRegionEnd) not in subwordDelims) and (ThisRegionEnd < view.size()) ):
						ThisRegionEnd += 1
					if((ThisRegionEnd < view.size()) and (ThisRegionEnd == ThisRegionBegin)):
						ThisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd))
					view.show(ThisRegionEnd+1)
				else: #backward
					ThisRegionBegin = ThisRegion.a
					ThisRegionEnd = ThisRegion.b-1
					while( (view.substr(ThisRegionEnd) not in subwordDelims) and (ThisRegionEnd >= 0) ):
						ThisRegionEnd -= 1
					if((ThisRegionEnd >= 0) and (ThisRegionEnd+1 == ThisRegionBegin)):
						ThisRegionEnd -= 1
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd+1))
					view.show(ThisRegionEnd)
			elif(ThisRegion.a < ThisRegion.b):
				if(forward): #forward
					ThisRegionBegin = ThisRegion.a
					ThisRegionEnd = ThisRegion.b
					while( (view.substr(ThisRegionEnd) not in subwordDelims) and (ThisRegionEnd < view.size()) ):
						ThisRegionEnd += 1
					if((ThisRegionEnd < view.size()) and (ThisRegionEnd == ThisRegion.b)):
						ThisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd))
					view.show(ThisRegionEnd+1)
				else: #backward
					ThisRegionBegin = ThisRegion.a
					ThisRegionEnd = ThisRegion.b-1
					while( (view.substr(ThisRegionEnd) not in subwordDelims) and (ThisRegionEnd >= 0) ):
						ThisRegionEnd -= 1
					if((ThisRegionEnd >= 0) and (ThisRegionEnd+1 == ThisRegion.b)):
						ThisRegionEnd -= 1
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd+1))
					view.show(ThisRegionEnd)
			else: # ThisRegion.a > ThisRegion.b
				if(forward): #forward
					ThisRegionBegin = ThisRegion.a
					ThisRegionEnd = ThisRegion.b
					while( (view.substr(ThisRegionEnd) not in subwordDelims) and (ThisRegionEnd < view.size()) ):
						ThisRegionEnd += 1
					if((ThisRegionEnd < view.size()) and (ThisRegionEnd == ThisRegion.b)):
						ThisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd))
					view.show(ThisRegionEnd+1)
				else: #backward
					ThisRegionBegin = ThisRegion.a
					ThisRegionEnd = ThisRegion.b-1
					while( (view.substr(ThisRegionEnd) not in subwordDelims) and (ThisRegionEnd >= 0) ):
						ThisRegionEnd -= 1
					if((ThisRegionEnd >= 0) and (ThisRegionEnd+1 == ThisRegion.b)):
						ThisRegionEnd -= 1
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd+1))
					view.show(ThisRegionEnd)

class SelectToKnLinelimitCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		for ThisRegion in view.sel():
			if(forward): #forward
				ThisRegionEnd = view.line(ThisRegion).end()
				view.sel().clear()
				view.sel().add(sublime.Region(ThisRegion.a, ThisRegionEnd))
				view.show(ThisRegionEnd)
			else: #backward
				ThisRegionEnd = view.line(ThisRegion).begin()
				view.sel().clear()
				view.sel().add(sublime.Region(ThisRegion.a, ThisRegionEnd))
				view.show(ThisRegionEnd)	

#---------------------------------------------------------------
class ExpandSelectionToDelimsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 34=" 35=# 36=$ 37=% 38=& 39=' 61== 64=@ 58=: 63=? 46=. 44=, 43=+ 95=_ 45=- 60=< 62=> 40=( 41=) 91=[ 93=] 123={ 125=} 124=| 47=/ 92=\
		subwordDelims = [chr(32), chr(9), chr(10), chr(13), chr(34), chr(35), chr(36), chr(37), chr(38), chr(39), chr(61), chr(64), chr(58), chr(63), chr(46), chr(44), chr(43), chr(95), chr(45), chr(60), chr(62), chr(40), chr(41), chr(91), chr(93), chr(123), chr(125), chr(124), chr(47), chr(92)]
		for ThisRegion in view.sel():
			ThisRegionBegin = ThisRegion.begin() - 1
			ThisRegionEnd = ThisRegion.end()
			if( (ThisRegion.begin() != ThisRegionEnd) and (view.substr(ThisRegionBegin) in subwordDelims) ):
				ThisRegionBegin -= 1
			while((view.substr(ThisRegionBegin) not in subwordDelims) and (ThisRegionBegin >= 0)):
				ThisRegionBegin -= 1
			ThisRegionBegin += 1

			if( (ThisRegion.begin() != ThisRegionEnd) and (view.substr(ThisRegionEnd) in subwordDelims) ):
				ThisRegionEnd += 1
			while((view.substr(ThisRegionEnd) not in subwordDelims) and (ThisRegionEnd < view.size())):
				ThisRegionEnd += 1

			# view.sel().clear()
			view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd))

class ExpandSelectionToQuotesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		# 34=" 39=' 
		beginDelims = [chr(34), chr(39)]
		endDelims = [chr(34), chr(39)]
		for ThisRegion in view.sel():
			ThisRegionBegin = ThisRegion.begin() - 1
			ThisRegionEnd = ThisRegion.end()
			while((view.substr(ThisRegionBegin) not in beginDelims) and (ThisRegionBegin >= 0)):
				ThisRegionBegin -= 1
			ThisRegionBegin += 1

			while((view.substr(ThisRegionEnd) not in endDelims) and (ThisRegionEnd < view.size())):
				ThisRegionEnd += 1

			# view.sel().clear()
			view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd))

class ExpandSelectionToBracketsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		# 60=< 62=> 40=( 41=) 91=[ 93=] 123={ 125=}
		# beginDelims = [chr(60), chr(40), chr(91), chr(123)]
		# endDelims = [chr(62), chr(41), chr(93), chr(125)]
		BracketDelims = [chr(60), chr(40), chr(91), chr(123), chr(62), chr(41), chr(93), chr(125)]
		for ThisRegion in view.sel():
			ThisRegionBegin = ThisRegion.begin() - 1
			ThisRegionEnd = ThisRegion.end()
			# while((view.substr(ThisRegionBegin) not in beginDelims) and (ThisRegionBegin >= 0)):
			while((view.substr(ThisRegionBegin) not in BracketDelims) and (ThisRegionBegin >= 0)):
				ThisRegionBegin -= 1
			ThisRegionBegin += 1

			# while((view.substr(ThisRegionEnd) not in endDelims) and (ThisRegionEnd < view.size())):
			while((view.substr(ThisRegionEnd) not in BracketDelims) and (ThisRegionEnd < view.size())):
				ThisRegionEnd += 1

			# view.sel().clear()
			view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd))

class ExpandSelectionToWhitespaceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 
		whiteChars = (chr(32), chr(9), chr(10), chr(13))
		for ThisRegion in view.sel():
			ThisRegionBegin = ThisRegion.begin() - 1
			while((view.substr(ThisRegionBegin) not in whiteChars) and (ThisRegionBegin >= 0)):
				ThisRegionBegin -= 1
			ThisRegionBegin += 1

			ThisRegionEnd = ThisRegion.end()
			while((view.substr(ThisRegionEnd) not in whiteChars) and (ThisRegionEnd < view.size())):
				ThisRegionEnd += 1

			# if(ThisRegionBegin != ThisRegionEnd):
			# view.sel().clear()
			view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd))
			# else:
			# 	view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionBegin))

#---------------------------------------------------------------
class KnLinelimitCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		for ThisRegion in view.sel():
			if(forward): #forward
				ThisRegionEnd = view.line(ThisRegion).end()
				view.sel().clear()
				view.sel().add(ThisRegionEnd)
				view.show(ThisRegionEnd)
			else: #backward
				ThisRegionEnd = view.line(ThisRegion).begin()
				view.sel().clear()
				view.sel().add(ThisRegionEnd)
				view.show(ThisRegionEnd)

#---------------------------------------------------------------
class KnIndentCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		RegionsSelOld = list(view.sel())
		#view.sel().clear()
		for ThisRegion in RegionsSelOld:
			ThisRegionFullline = KnFullLine(view, ThisRegion)
			MyContent = view.substr(ThisRegionFullline)
			ListLines = MyContent.splitlines(True)
			NumLines = len(ListLines)
			ListLinesNew = list()			
			if((NumLines == 0) and forward):
				view.replace(edit, ThisRegionFullline, chr(9))
				view.sel().clear()
				view.sel().add(sublime.Region(ThisRegion.begin()+1))
				view.show(ThisRegion.begin()+1)
			elif(forward): #forward
				for ThisLine in ListLines:
					ListLinesNew.append(chr(9)+ThisLine)
				view.replace(edit, ThisRegionFullline, ''.join(ListLinesNew))
				view.sel().clear()
				view.sel().add(sublime.Region(ThisRegion.begin()+1, ThisRegion.end()+NumLines))
				view.show(ThisRegion.begin()+1)
			else: #backward
				NumLines = 0
				for ThisLine in ListLines:
					if(ThisLine[0] == chr(9)):
						NumLines += 1
						ListLinesNew.append(ThisLine[1:])
					else:
						ListLinesNew.append(ThisLine)
				view.replace(edit, ThisRegionFullline, ''.join(ListLinesNew))
				if(NumLines == 0):
					view.show(ThisRegion.begin())
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegion.begin(), ThisRegion.end()-NumLines))
				else:
					view.show(ThisRegion.begin()-1)
					view.sel().clear()
					view.sel().add(sublime.Region(ThisRegion.begin()-1, ThisRegion.end()-NumLines))

#---------------------------------------------------------------
class CopyFulllinesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for ThisRegion in view.sel():
			strThisRegionFullline = view.substr(KnFullLine(view, ThisRegion))

			if( (strThisRegionFullline[-1] == chr(10)) or (strThisRegionFullline[-1] == chr(13)) ):
				sublime.set_clipboard(strThisRegionFullline)
			else: # there was no newline found at the end - this means it is the last line in the document, so add a newline for it
				sublime.set_clipboard(strThisRegionFullline + chr(10))

class CutFulllinesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for ThisRegion in view.sel():
			ThisRegionFullline = KnFullLine(view, ThisRegion)
			sublime.set_clipboard(view.substr(ThisRegionFullline))
			self.view.erase(edit, ThisRegionFullline)

#---------------------------------------------------------------
class KnPasteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for ThisRegion in view.sel():
			# view.run_command('paste');
			sublimeclipboard = sublime.get_clipboard()
			if(ThisRegion.a != ThisRegion.b):
				view.replace(edit, ThisRegion, sublimeclipboard)
			else:
				view.insert(edit, ThisRegion.a, sublimeclipboard)
				view.show(ThisRegion.a + len(sublimeclipboard) + 1)

#---------------------------------------------------------------
class PasteAboveLinesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for ThisRegion in view.sel():

			PosSelectionBegin = ThisRegion.begin()-1
			while( not( (view.substr(PosSelectionBegin) == chr(10)) or (view.substr(PosSelectionBegin) == chr(13)) ) and (PosSelectionBegin > 0) ):
				PosSelectionBegin -= 1
			PosSelectionBegin += 1
			
			sublimeclipboard = sublime.get_clipboard()
			if(sublimeclipboard[-1:] != chr(10)):
				#print("ended in a newline not, adding one")
				view.insert(edit, PosSelectionBegin, chr(10))
				view.insert(edit, PosSelectionBegin, sublimeclipboard)
			else:
				view.insert(edit, PosSelectionBegin, sublimeclipboard)

#---------------------------------------------------------------
# duplicates line above (instead of below like innate one)
class KnDuplicateLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for ThisRegion in view.sel():

			PosSelectionBegin = ThisRegion.begin()
			PosSelectionEnd = ThisRegion.end()
			
			PosSelectionBegin -= 1
			while( (PosSelectionBegin >= 0) and not( (view.substr(PosSelectionBegin) == chr(10)) or (view.substr(PosSelectionBegin) == chr(13)) ) ):
				PosSelectionBegin -= 1
			PosSelectionBegin += 1

			if(PosSelectionBegin != PosSelectionEnd):
				PosSelectionEnd -= 1
			while( (PosSelectionEnd < view.size()) and not( (view.substr(PosSelectionEnd) == chr(10)) or (view.substr(PosSelectionEnd) == chr(13)) ) ):
				PosSelectionEnd += 1
			if(PosSelectionEnd != view.size()):
				PosSelectionEnd += 1 # add the newline that you found

			strThisRegionFullline = view.substr(sublime.Region(PosSelectionBegin, PosSelectionEnd))
		
			if(strThisRegionFullline[-1:] != chr(10)):
				view.insert(edit, PosSelectionBegin, chr(10))
				view.insert(edit, PosSelectionBegin, strThisRegionFullline)
			else:
				view.insert(edit, PosSelectionBegin, strThisRegionFullline)

#---------------------------------------------------------------
class BlanklineAddCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		RegionsSelOld = list(view.sel())
		# view.sel().clear()
		for thisregion in RegionsSelOld:
			if(forward): #forward
				posToInsertLineAt = KnFullLine(view, thisregion).end()
				#print(posToInsertLineAt)
				view.insert(edit, posToInsertLineAt, chr(10))
				# view.sel().add(sublime.Region(posToInsertLineAt))
			else: #backward
				posToInsertLineAt = KnFullLine(view, thisregion).begin()-1
				view.insert(edit, posToInsertLineAt+1, chr(10))
				# view.sel().add(sublime.Region(posToInsertLineAt+1))

#---------------------------------------------------------------
class DeleteToBegOfContigBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		whiteChars = (chr(32), chr(9), chr(10), chr(13))
		spaceChars = (chr(32), chr(9))
		# newlineChars = (chr(10), chr(13))
		for ThisRegion in view.sel():
			if(ThisRegion.a != ThisRegion.b):
				view.erase(edit, sublime.Region(ThisRegion.begin(), ThisRegion.end()))
				# view.show(ThisRegionEnd) #dont show move
			elif(forward): #forward
				ThisRegionBegin = ThisRegion.a
				ThisRegionEnd = ThisRegion.b
				while((view.substr(ThisRegionEnd) not in whiteChars) and (ThisRegionEnd < view.size())):
					ThisRegionEnd += 1
				while((view.substr(ThisRegionEnd) in spaceChars) and (ThisRegionEnd < view.size())):
					ThisRegionEnd += 1
				if((ThisRegionEnd < view.size()) and (ThisRegionEnd == ThisRegion.b)):
					ThisRegionEnd += 1
				view.erase(edit, sublime.Region(ThisRegionBegin, ThisRegionEnd))
				# view.show(ThisRegionEnd) #dont show move
			else: #backward
				ThisRegionBegin = ThisRegion.a
				ThisRegionEnd = ThisRegion.b-1
				while((view.substr(ThisRegionEnd) in spaceChars) and (ThisRegionEnd >= 0)):
					ThisRegionEnd -= 1
				while((view.substr(ThisRegionEnd) not in whiteChars) and (ThisRegionEnd >= 0)):
					ThisRegionEnd -= 1
				if((ThisRegionEnd >= 0) and (ThisRegionEnd+1 == ThisRegion.b)):
					ThisRegionEnd -= 1
				view.erase(edit, sublime.Region(ThisRegionBegin, ThisRegionEnd+1))
				view.show(ThisRegionEnd)
				
class DeleteToBegOfSubwordBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 34=" 35=# 36=$ 37=% 38=& 39=' 61== 64=@ 58=: 63=? 46=. 44=, 43=+ 95=_ 45=- 60=< 62=> 40=( 41=) 91=[ 93=] 123={ 125=} 124=| 47=/ 92=\
		subwordDelims = [chr(32), chr(9), chr(10), chr(13), chr(34), chr(35), chr(36), chr(37), chr(38), chr(39), chr(61), chr(64), chr(58), chr(63), chr(46), chr(44), chr(43), chr(95), chr(45), chr(60), chr(62), chr(40), chr(41), chr(91), chr(93), chr(123), chr(125), chr(124), chr(47), chr(92)]
		for ThisRegion in view.sel():
			if(ThisRegion.a != ThisRegion.b):
				view.erase(edit, sublime.Region(ThisRegion.a, ThisRegion.b))
				# view.show(ThisRegionEnd) #dont show move
			elif(forward): #forward
				# ThisRegionBegin = ThisRegion.a
				ThisRegionEnd = ThisRegion.b
				while( (view.substr(ThisRegionEnd) not in subwordDelims) and (ThisRegionEnd < view.size()) ):
					ThisRegionEnd += 1
				if((ThisRegionEnd < view.size()) and (ThisRegionEnd == ThisRegion.b)):
					ThisRegionEnd += 1
				view.erase(edit, sublime.Region(ThisRegion.a, ThisRegionEnd))
				# view.show(ThisRegionEnd) #dont show move
			else: #backward
				# ThisRegionBegin = ThisRegion.a
				ThisRegionEnd = ThisRegion.b-1
				while( (view.substr(ThisRegionEnd) not in subwordDelims) and (ThisRegionEnd >= 0) ):
					ThisRegionEnd -= 1
				if((ThisRegionEnd >= 0) and (ThisRegionEnd+1 == ThisRegion.b)):
					ThisRegionEnd -= 1
				view.erase(edit, sublime.Region(ThisRegion.a, ThisRegionEnd+1))
				view.show(ThisRegionEnd)
				
#---------------------------------------------------------------
class DeleteLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for ThisRegion in view.sel():
			self.view.erase(edit, KnFullLine(view, ThisRegion))

class DeleteLineWoLinebreakCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for ThisRegion in view.sel():
			self.view.erase(edit, view.line(ThisRegion))

class SelectLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for ThisRegion in view.sel():
			view.sel().add(KnFullLine(view, ThisRegion))

class SelectLineWoLinebreakCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for ThisRegion in view.sel():
			ThisRegionToDelete = view.line(ThisRegion)
			# view.sel().clear()
			view.sel().add(view.line(ThisRegion))
			# self.view.erase(edit, ThisRegionToDelete)

#---------------------------------------------------------------
#https://forum.sublimetext.com/t/bug-full-line-api-returns-another-next-line-with-it-also-if-region-given-to-it-ends-in-a-new-newline-also/44140/7
#Reimplementation of full_line due to full_line bug in ST3 some versions.
def KnFullLine(mview, mRegion):
	view = mview
	
	PosSelectionBegin = mRegion.begin()
	PosSelectionEnd = mRegion.end()
	
	PosSelectionBegin -= 1
	while( not( (view.substr(PosSelectionBegin) == chr(10)) or (view.substr(PosSelectionBegin) == chr(13)) ) and (PosSelectionBegin > 0) ):
		PosSelectionBegin -= 1
	PosSelectionBegin += 1

	if(PosSelectionBegin != PosSelectionEnd):
		PosSelectionEnd -= 1
	while( (PosSelectionEnd <= view.size()-1) and not( (view.substr(PosSelectionEnd) == chr(10)) or (view.substr(PosSelectionEnd) == chr(13)) ) ):
		PosSelectionEnd += 1
	if(PosSelectionEnd != view.size()):
		PosSelectionEnd += 1 # add the newline that you found
	
	#print("PosSelectionBegin=" + str(PosSelectionBegin))
	#print("PosSelectionEnd=" + str(PosSelectionEnd))
	ThisRegionFullline = sublime.Region(PosSelectionBegin, PosSelectionEnd)
	return ThisRegionFullline

#---------------------------------------------------------------
# Reference (no longer used)
# class ExpandSelectionToSentenceCommand(sublime_plugin.TextCommand):
# 	def run(self, edit):
# 		view = self.view
# 		oldSelRegions = list(view.sel())
# 		view.sel().clear()
# 		for ThisRegion in oldSelRegions:
# 			ThisRegionBegin = ThisRegion.begin() - 1
# 			while((view.substr(ThisRegionBegin) not in ".") and (ThisRegionBegin >= 0)):
# 				ThisRegionBegin -= 1

# 			ThisRegionBegin += 1
# 			while((view.substr(ThisRegionBegin) in whitespaceChars) and (ThisRegionBegin < view.size())):
# 				ThisRegionBegin += 1

# 			ThisRegionEnd = ThisRegion.end()
# 			while((view.substr(ThisRegionEnd) not in ".") and (ThisRegionEnd < view.size())):
# 				ThisRegionEnd += 1

# 			if(ThisRegionBegin != ThisRegionEnd):
# 				view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionEnd+1))
# 			else:
# 				view.sel().add(sublime.Region(ThisRegionBegin, ThisRegionBegin))
			
#---------------------------------------------------------------
# Reference (no longer used)
# class MoveToContigboundaryCommand(sublime_plugin.TextCommand):
# 	def run(self, edit, forward, extend=False):
# 		view = self.view
# 		oldSelRegions = list(view.sel())
# 		view.sel().clear()
# 		for ThisRegion in oldSelRegions:
# 			if(forward): #forward
# 				caretPos = ThisRegion.b
# 				if(view.substr(caretPos) in whitespaceChars): #initially have whitespace right of me, find char
# 					while((view.substr(caretPos) in whitespaceChars) and (caretPos < view.size())):
# 						caretPos += 1
# 				else: #initially have char right of me, find whitespace
# 					while((view.substr(caretPos) not in whitespaceChars) and (caretPos < view.size())):
# 						caretPos += 1
# 				if(extend):
# 					view.sel().add(sublime.Region(ThisRegion.a, caretPos))
# 					view.show(caretPos)
# 				else:
# 					view.sel().add(sublime.Region(caretPos))
# 					view.show(caretPos)
# 			else: #backward
# 				caretPos = ThisRegion.b - 1
# 				if(view.substr(caretPos) in whitespaceChars): #initially have whitespace left of me, find char
# 					while((view.substr(caretPos) in whitespaceChars) and (caretPos >= 0)):
# 						caretPos -= 1
# 				else: #initially have char left of me, find whitespace
# 					while((view.substr(caretPos) not in whitespaceChars) and (caretPos >= 0)):
# 						caretPos -= 1
# 				if(extend):
# 					view.sel().add(sublime.Region(ThisRegion.a, caretPos+1))
# 					view.show(caretPos+1)
# 				else:
# 					view.sel().add(sublime.Region(caretPos+1))
# 					view.show(caretPos+1)

#---------------------------------------------------------------
