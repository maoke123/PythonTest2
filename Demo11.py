def tupleVarArgs(arg1,arg2='defaultB',*theRest):
	'display regular args non-keyword variable agrs'
	print 'formal arg 1:',arg1
	print 'formal arg 2:',arg2
	for eachXtrArg in theRest:
		print 'another arg:',eachXtrArg
