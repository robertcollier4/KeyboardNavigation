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
		for thisregion in view.sel():
			if(forward): #forward
				thisRegionBegin = thisregion.a
				thisRegionEnd = thisregion.b
				while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd < view.size())):
					thisRegionEnd += 1
				while( (view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd < view.size()) ):
					thisRegionEnd += 1
				if((thisRegionEnd < view.size()) and (thisRegionEnd == thisregion.b)):
					thisRegionEnd += 1
				view.sel().clear()
				view.sel().add(sublime.Region(thisRegionEnd))
				view.show(thisRegionEnd+1)
			else: #backward
				thisRegionBegin = thisregion.a
				thisRegionEnd = thisregion.b-1
				while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd >= 0)):
					thisRegionEnd -= 1
				while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd >= 0)):
					thisRegionEnd -= 1
				if((thisRegionEnd >= 0) and (thisRegionEnd+1 == thisregion.b)):
					thisRegionEnd -= 1
				view.sel().clear()
				view.sel().add(sublime.Region(thisRegionEnd+1))
				view.show(thisRegionEnd)

# https://ee.hawaii.edu/~tep/EE160/Book/chap4/subsection2.1.1.1.html
class MoveToBegOfSubwordBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 34=" 35=# 36=$ 37=% 38=& 39=' 61== 64=@ 58=: 46=. 44=, 43=+ 95=_ 45=- 60=< 62=> 40=( 41=) 91=[ 93=] 123={ 125=} 124=| 47=/ 92=\
		subwordDelims = [chr(32), chr(9), chr(10), chr(13), chr(34), chr(35), chr(36), chr(37), chr(38), chr(39), chr(61), chr(64), chr(58), chr(46), chr(44), chr(43), chr(95), chr(45), chr(60), chr(62), chr(40), chr(41), chr(91), chr(93), chr(123), chr(125), chr(124), chr(47), chr(92)]
		for thisregion in view.sel():
			if(forward): #forward
				thisRegionBegin = thisregion.a
				thisRegionEnd = thisregion.b
				while( (view.substr(thisRegionEnd) not in subwordDelims) and (thisRegionEnd < view.size()) ):
					thisRegionEnd += 1
				if((thisRegionEnd < view.size()) and (thisRegionEnd == thisregion.b)):
					thisRegionEnd += 1
				view.sel().clear()
				view.sel().add(sublime.Region(thisRegionEnd))
				view.show(thisRegionEnd+1)
			else: #backward
				thisRegionBegin = thisregion.a
				thisRegionEnd = thisregion.b-1
				while( (view.substr(thisRegionEnd) not in subwordDelims) and (thisRegionEnd >= 0) ):
					thisRegionEnd -= 1
				if((thisRegionEnd >= 0) and (thisRegionEnd+1 == thisregion.b)):
					thisRegionEnd -= 1
				view.sel().clear()
				view.sel().add(sublime.Region(thisRegionEnd+1))
				view.show(thisRegionEnd)

#---------------------------------------------------------------
class SelectToBegOfContigBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 
		whiteChars = (chr(32), chr(9), chr(10), chr(13))
		spaceChars = (chr(32), chr(9))  
		# newlineChars = (chr(10), chr(13))
		for thisregion in view.sel():
			if(thisregion.a == thisregion.b):
				if(forward): #forward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b
					while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd < view.size())):
						thisRegionEnd += 1
					while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd < view.size())):
						thisRegionEnd += 1
					if((thisRegionEnd < view.size()) and (thisRegionEnd == thisregion.b)):
						thisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))
					view.show(thisRegionEnd+1)
				else: #backward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b-1
					while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd >= 0)):
						thisRegionEnd -= 1
					while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd >= 0)):
						thisRegionEnd -= 1
					if((thisRegionEnd >= 0) and (thisRegionEnd+1 == thisregion.b)):
						thisRegionEnd -= 1					
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd+1))
					view.show(thisRegionEnd)
			elif(thisregion.a < thisregion.b):
				if(forward): #forward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b
					while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd < view.size())):
						thisRegionEnd += 1
					while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd < view.size())):
						thisRegionEnd += 1
					if((thisRegionEnd < view.size()) and (thisRegionEnd == thisregion.b)):
						thisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))
					view.show(thisRegionEnd+1)
				else: #backward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b-1
					while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd > thisRegionBegin-1) and (thisRegionEnd >= 0)):
						thisRegionEnd -= 1
					while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd > thisRegionBegin-1) and (thisRegionEnd >= 0)):
						thisRegionEnd -= 1
					if((thisRegionEnd >= 0) and (thisRegionEnd+1 == thisregion.b)):
						thisRegionEnd -= 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd+1))
					view.show(thisRegionEnd)
			else: # thisregion.a > thisregion.b
				if(forward): #forward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b
					while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd < thisRegionBegin) and (thisRegionEnd < view.size())):
						thisRegionEnd += 1
					while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd < thisRegionBegin) and (thisRegionEnd < view.size())):
						thisRegionEnd += 1
					if((thisRegionEnd < view.size()) and (thisRegionEnd == thisregion.b)):
						thisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))
					view.show(thisRegionEnd+1)
				else: #backward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b-1
					while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd >= 0)):
						thisRegionEnd -= 1
					while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd >= 0)):
						thisRegionEnd -= 1
					if((thisRegionEnd >= 0) and (thisRegionEnd+1 == thisregion.b)):
						thisRegionEnd -= 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd+1))
					view.show(thisRegionEnd)

class SelectToBegOfSubwordBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 34=" 35=# 36=$ 37=% 38=& 39=' 61== 64=@ 58=: 46=. 44=, 43=+ 95=_ 45=- 60=< 62=> 40=( 41=) 91=[ 93=] 123={ 125=} 124=| 47=/ 92=\
		subwordDelims = [chr(32), chr(9), chr(10), chr(13), chr(34), chr(35), chr(36), chr(37), chr(38), chr(39), chr(61), chr(64), chr(58), chr(46), chr(44), chr(43), chr(95), chr(45), chr(60), chr(62), chr(40), chr(41), chr(91), chr(93), chr(123), chr(125), chr(124), chr(47), chr(92)]
		for thisregion in view.sel():
			if(thisregion.a == thisregion.b):
				if(forward): #forward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b
					while( (view.substr(thisRegionEnd) not in subwordDelims) and (thisRegionEnd < view.size()) ):
						thisRegionEnd += 1
					if((thisRegionEnd < view.size()) and (thisRegionEnd == thisRegionBegin)):
						thisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))
					view.show(thisRegionEnd+1)
				else: #backward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b-1
					while( (view.substr(thisRegionEnd) not in subwordDelims) and (thisRegionEnd >= 0) ):
						thisRegionEnd -= 1
					if((thisRegionEnd >= 0) and (thisRegionEnd+1 == thisRegionBegin)):
						thisRegionEnd -= 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd+1))
					view.show(thisRegionEnd)
			elif(thisregion.a < thisregion.b):
				if(forward): #forward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b
					while( (view.substr(thisRegionEnd) not in subwordDelims) and (thisRegionEnd < view.size()) ):
						thisRegionEnd += 1
					if((thisRegionEnd < view.size()) and (thisRegionEnd == thisregion.b)):
						thisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))
					view.show(thisRegionEnd+1)
				else: #backward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b-1
					while( (view.substr(thisRegionEnd) not in subwordDelims) and (thisRegionEnd >= 0) ):
						thisRegionEnd -= 1
					if((thisRegionEnd >= 0) and (thisRegionEnd+1 == thisregion.b)):
						thisRegionEnd -= 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd+1))
					view.show(thisRegionEnd)
			else: # thisregion.a > thisregion.b
				if(forward): #forward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b
					while( (view.substr(thisRegionEnd) not in subwordDelims) and (thisRegionEnd < view.size()) ):
						thisRegionEnd += 1
					if((thisRegionEnd < view.size()) and (thisRegionEnd == thisregion.b)):
						thisRegionEnd += 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))
					view.show(thisRegionEnd+1)
				else: #backward
					thisRegionBegin = thisregion.a
					thisRegionEnd = thisregion.b-1
					while( (view.substr(thisRegionEnd) not in subwordDelims) and (thisRegionEnd >= 0) ):
						thisRegionEnd -= 1
					if((thisRegionEnd >= 0) and (thisRegionEnd+1 == thisregion.b)):
						thisRegionEnd -= 1
					view.sel().clear()
					view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd+1))
					view.show(thisRegionEnd)

class SelectToKnLinelimitCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		for thisregion in view.sel():
			if(forward): #forward
				thisRegionEnd = view.line(thisregion).end()
				view.sel().clear()
				view.sel().add(sublime.Region(thisregion.a, thisRegionEnd))
				view.show(thisRegionEnd)
			else: #backward
				thisRegionEnd = view.line(thisregion).begin()
				view.sel().clear()
				view.sel().add(sublime.Region(thisregion.a, thisRegionEnd))
				view.show(thisRegionEnd)	

#---------------------------------------------------------------
class ExpandSelectionToDelimsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 34=" 35=# 36=$ 37=% 38=& 39=' 61== 64=@ 58=: 46=. 44=, 43=+ 95=_ 45=- 60=< 62=> 40=( 41=) 91=[ 93=] 123={ 125=} 124=| 47=/ 92=\
		subwordDelims = [chr(32), chr(9), chr(10), chr(13), chr(34), chr(35), chr(36), chr(37), chr(38), chr(39), chr(61), chr(64), chr(58), chr(46), chr(44), chr(43), chr(95), chr(45), chr(60), chr(62), chr(40), chr(41), chr(91), chr(93), chr(123), chr(125), chr(124), chr(47), chr(92)]
		for thisregion in view.sel():
			thisRegionBegin = thisregion.begin() - 1
			thisRegionEnd = thisregion.end()
			if( (thisregion.begin() != thisRegionEnd) and (view.substr(thisRegionBegin) in subwordDelims) ):
				thisRegionBegin -= 1
			while((view.substr(thisRegionBegin) not in subwordDelims) and (thisRegionBegin >= 0)):
				thisRegionBegin -= 1
			thisRegionBegin += 1

			if( (thisregion.begin() != thisRegionEnd) and (view.substr(thisRegionEnd) in subwordDelims) ):
				thisRegionEnd += 1
			while((view.substr(thisRegionEnd) not in subwordDelims) and (thisRegionEnd < view.size())):
				thisRegionEnd += 1

			# view.sel().clear()
			view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))

class ExpandSelectionToQuotesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		# 34=" 39=' 
		beginDelims = [chr(34), chr(39)]
		endDelims = [chr(34), chr(39)]
		for thisregion in view.sel():
			thisRegionBegin = thisregion.begin() - 1
			thisRegionEnd = thisregion.end()
			while((view.substr(thisRegionBegin) not in beginDelims) and (thisRegionBegin >= 0)):
				thisRegionBegin -= 1
			thisRegionBegin += 1

			while((view.substr(thisRegionEnd) not in endDelims) and (thisRegionEnd < view.size())):
				thisRegionEnd += 1

			# view.sel().clear()
			view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))

class ExpandSelectionToBracketsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		# 60=< 62=> 40=( 41=) 91=[ 93=] 123={ 125=}
		beginDelims = [chr(60), chr(40), chr(91), chr(123)]
		endDelims = [chr(62), chr(41), chr(93), chr(125)]
		for thisregion in view.sel():
			thisRegionBegin = thisregion.begin() - 1
			thisRegionEnd = thisregion.end()
			while((view.substr(thisRegionBegin) not in beginDelims) and (thisRegionBegin >= 0)):
				thisRegionBegin -= 1
			thisRegionBegin += 1

			while((view.substr(thisRegionEnd) not in endDelims) and (thisRegionEnd < view.size())):
				thisRegionEnd += 1

			# view.sel().clear()
			view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))

class ExpandSelectionToWhitespaceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 
		whiteChars = (chr(32), chr(9), chr(10), chr(13))
		for thisregion in view.sel():
			thisRegionBegin = thisregion.begin() - 1
			while((view.substr(thisRegionBegin) not in whiteChars) and (thisRegionBegin >= 0)):
				thisRegionBegin -= 1
			thisRegionBegin += 1

			thisRegionEnd = thisregion.end()
			while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd < view.size())):
				thisRegionEnd += 1

			# if(thisRegionBegin != thisRegionEnd):
			# view.sel().clear()
			view.sel().add(sublime.Region(thisRegionBegin, thisRegionEnd))
			# else:
			# 	view.sel().add(sublime.Region(thisRegionBegin, thisRegionBegin))

#---------------------------------------------------------------
class KnLinelimitCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		for thisregion in view.sel():
			if(forward): #forward
				thisRegionEnd = view.line(thisregion).end()
				view.sel().clear()
				view.sel().add(thisRegionEnd)
				view.show(thisRegionEnd)
			else: #backward
				thisRegionEnd = view.line(thisregion).begin()
				view.sel().clear()
				view.sel().add(thisRegionEnd)
				view.show(thisRegionEnd)

#---------------------------------------------------------------
class KnIndentCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		for thisregion in view.sel():
			thisregionfullline = view.full_line(thisregion)
			mycontent = view.substr(thisregionfullline)
			listlines = mycontent.splitlines(True)
			numlines = len(listlines)
			listlinesnew = list()			
			if((numlines == 0) and forward):
				view.replace(edit, thisregionfullline, chr(9))
				view.sel().clear()
				view.sel().add(sublime.Region(thisregion.begin()+1))
				view.show(thisregion.begin()+1)
			elif(forward): #forward
				for thisline in listlines:
					listlinesnew.append(chr(9)+thisline)
				view.replace(edit, thisregionfullline, ''.join(listlinesnew))
				view.sel().clear()
				view.sel().add(sublime.Region(thisregion.begin()+1, thisregion.end()+numlines))
				view.show(thisregion.begin()+1)
			else: #backward
				for thisline in listlines:
					if(thisline[0] == chr(9)):
						listlinesnew.append(thisline[1:])
					else:
						listlinesnew.append(thisline)
				view.replace(edit, thisregionfullline, ''.join(listlinesnew))
				view.show(thisregion.begin()-1)
				# not needed to rebuild the selection
				# view.sel().clear()
				# view.sel().add(sublime.Region(thisregion.begin()-1, thisregion.end()-numlines))

#---------------------------------------------------------------
class CopyFulllinesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for thisregion in view.sel():
			thisregionfullline = view.full_line(thisregion)
			strthisregionfullline = view.substr(thisregionfullline)
			if( (strthisregionfullline[-1] == chr(10)) or (strthisregionfullline[-1] == chr(13)) ):
				sublime.set_clipboard(strthisregionfullline)
			else: # this line does not end in newline even though full_line was used - this means its the last line the document, so add a newline for it
				sublime.set_clipboard(strthisregionfullline + chr(10))

class CutFulllinesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for thisregion in view.sel():
			thisregionfullline = view.full_line(thisregion)
			strthisregionfullline = view.substr(thisregionfullline)
			if( (strthisregionfullline[-1] == chr(10)) or (strthisregionfullline[-1] == chr(13)) ):
				sublime.set_clipboard(strthisregionfullline)
				self.view.erase(edit, thisregionfullline)
			else: # this line does not end in newline even though full_line was used - this means its the last line the document, so add a newline for it
				sublime.set_clipboard(strthisregionfullline + chr(10))
				self.view.erase(edit, thisregionfullline)

#---------------------------------------------------------------
class KnPasteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for thisregion in view.sel():
			# view.run_command('paste');
			sublimeclipboard = sublime.get_clipboard()
			if(thisregion.a != thisregion.b):
				view.replace(edit, thisregion, sublimeclipboard)
			else:
				view.insert(edit, thisregion.a, sublimeclipboard)
				view.show(thisregion.a + len(sublimeclipboard) + 1)

#---------------------------------------------------------------
class PasteIntoLinesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for thisregion in view.sel():
			thisregionfullline = view.full_line(thisregion)
			thisregionfulllineBeginning = thisregionfullline.begin()
			sublimeclipboard = sublime.get_clipboard()
			if(sublimeclipboard[-1:] != chr(10)):
				sublime.status_message("PasteIntoLines: There is not newlines ending content in clipboard, adding newline after")
				view.insert(edit, thisregionfulllineBeginning, sublime.get_clipboard() + chr(10))
				view.show(thisregion.a + len(sublimeclipboard) + 1)
			else:
				view.insert(edit, thisregionfulllineBeginning, sublime.get_clipboard())
				view.show(thisregion.a + len(sublimeclipboard) + 1)

#---------------------------------------------------------------
# duplicates line above (instead of below like innate one)
class KnDuplicateLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for numthisregion, thisregion in enumerate(view.sel()):
			thisregionfullline = view.full_line(thisregion)
			if(view.substr(thisregionfullline)[-1:] != chr(10)):
				view.insert(edit, thisregionfullline.begin(), view.substr(thisregionfullline) + chr(10))
			else:
				view.insert(edit, thisregionfullline.begin(), view.substr(thisregionfullline))
		# view.show(thisregionfullline.a) # not needed

#---------------------------------------------------------------
class BlanklineAddCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		RegionsSelOld = list(view.sel())
		view.sel().clear()
		for thisregion in RegionsSelOld:
			if(forward): #forward
				posToInsertLineAt = view.full_line(thisregion).b
				print(posToInsertLineAt)
				view.insert(edit, posToInsertLineAt, chr(10))
				view.sel().add(sublime.Region(posToInsertLineAt))
			else: #backward
				posToInsertLineAt = view.full_line(thisregion).a-1
				view.insert(edit, posToInsertLineAt+1, chr(10))
				view.sel().add(sublime.Region(posToInsertLineAt+1))

#---------------------------------------------------------------
class DeleteToBegOfContigBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		whiteChars = (chr(32), chr(9), chr(10), chr(13))
		spaceChars = (chr(32), chr(9))
		# newlineChars = (chr(10), chr(13))
		for thisregion in view.sel():
			if(thisregion.a != thisregion.b):
				view.erase(edit, sublime.Region(thisregion.begin(), thisregion.end()))
				# view.show(thisRegionEnd) #dont show move
			elif(forward): #forward
				thisRegionBegin = thisregion.a
				thisRegionEnd = thisregion.b
				while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd < view.size())):
					thisRegionEnd += 1
				while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd < view.size())):
					thisRegionEnd += 1
				if((thisRegionEnd < view.size()) and (thisRegionEnd == thisregion.b)):
					thisRegionEnd += 1
				view.erase(edit, sublime.Region(thisRegionBegin, thisRegionEnd))
				# view.show(thisRegionEnd) #dont show move
			else: #backward
				thisRegionBegin = thisregion.a
				thisRegionEnd = thisregion.b-1
				while((view.substr(thisRegionEnd) in spaceChars) and (thisRegionEnd >= 0)):
					thisRegionEnd -= 1
				while((view.substr(thisRegionEnd) not in whiteChars) and (thisRegionEnd >= 0)):
					thisRegionEnd -= 1
				if((thisRegionEnd >= 0) and (thisRegionEnd+1 == thisregion.b)):
					thisRegionEnd -= 1
				view.erase(edit, sublime.Region(thisRegionBegin, thisRegionEnd+1))
				view.show(thisRegionEnd)
				
class DeleteToBegOfSubwordBoundaryCommand(sublime_plugin.TextCommand):
	def run(self, edit, forward):
		view = self.view
		# 32=space 9=tab 10=newline 13=carriagereturn 34=" 35=# 36=$ 37=% 38=& 39=' 61== 64=@ 58=: 46=. 44=, 43=+ 95=_ 45=- 60=< 62=> 40=( 41=) 91=[ 93=] 123={ 125=} 124=| 47=/ 92=\
		subwordDelims = [chr(32), chr(9), chr(10), chr(13), chr(34), chr(35), chr(36), chr(37), chr(38), chr(39), chr(61), chr(64), chr(58), chr(46), chr(44), chr(43), chr(95), chr(45), chr(60), chr(62), chr(40), chr(41), chr(91), chr(93), chr(123), chr(125), chr(124), chr(47), chr(92)]
		for thisregion in view.sel():
			if(thisregion.a != thisregion.b):
				view.erase(edit, sublime.Region(thisregion.a, thisregion.b))
				# view.show(thisRegionEnd) #dont show move
			elif(forward): #forward
				# thisRegionBegin = thisregion.a
				thisRegionEnd = thisregion.b
				while( (view.substr(thisRegionEnd) not in subwordDelims) and (thisRegionEnd < view.size()) ):
					thisRegionEnd += 1
				if((thisRegionEnd < view.size()) and (thisRegionEnd == thisregion.b)):
					thisRegionEnd += 1
				view.erase(edit, sublime.Region(thisregion.a, thisRegionEnd))
				# view.show(thisRegionEnd) #dont show move
			else: #backward
				# thisRegionBegin = thisregion.a
				thisRegionEnd = thisregion.b-1
				while( (view.substr(thisRegionEnd) not in subwordDelims) and (thisRegionEnd >= 0) ):
					thisRegionEnd -= 1
				if((thisRegionEnd >= 0) and (thisRegionEnd+1 == thisregion.b)):
					thisRegionEnd -= 1
				view.erase(edit, sublime.Region(thisregion.a, thisRegionEnd+1))
				view.show(thisRegionEnd)
				
#---------------------------------------------------------------
class DeleteLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for thisRegion in view.sel():
			self.view.erase(edit, view.full_line(thisRegion))

class DeleteLineWoLinebreakCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for thisRegion in view.sel():
			self.view.erase(edit, view.line(thisRegion))

class SelectLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for thisRegion in view.sel():
			thisRegionToDelete = view.full_line(thisRegion)
			# view.sel().clear()
			view.sel().add(view.full_line(thisRegion))
			# self.view.erase(edit, thisRegionToDelete)

class SelectLineWoLinebreakCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for thisRegion in view.sel():
			thisRegionToDelete = view.line(thisRegion)
			# view.sel().clear()
			view.sel().add(view.line(thisRegion))
			# self.view.erase(edit, thisRegionToDelete)

#---------------------------------------------------------------
# Reference (no longer used)
# class ExpandSelectionToSentenceCommand(sublime_plugin.TextCommand):
# 	def run(self, edit):
# 		view = self.view
# 		oldSelRegions = list(view.sel())
# 		view.sel().clear()
# 		for thisregion in oldSelRegions:
# 			thisRegionBegin = thisregion.begin() - 1
# 			while((view.substr(thisRegionBegin) not in ".") and (thisRegionBegin >= 0)):
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
# 					while((view.substr(caretPos) not in whitespaceChars) and (caretPos < view.size())):
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
# 					while((view.substr(caretPos) in whitespaceChars) and (caretPos >= 0)):
# 						caretPos -= 1
# 				else: #initially have char left of me, find whitespace
# 					while((view.substr(caretPos) not in whitespaceChars) and (caretPos >= 0)):
# 						caretPos -= 1
# 				if(extend):
# 					view.sel().add(sublime.Region(thisregion.a, caretPos+1))
# 					view.show(caretPos+1)
# 				else:
# 					view.sel().add(sublime.Region(caretPos+1))
# 					view.show(caretPos+1)

#---------------------------------------------------------------
