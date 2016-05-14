class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
		
	def print_score(self):
		print "%s: %s" % (self.__name,self.__score)
	def get_score(self):
		return self.__score
	def set_score(self,score):
		if 0 <= score <=100:
			self.__score=score
		else:
			raise ValueError('bad score')
class Exstudent(Student):
	def print_cr(self):
		print "USA"


ex=Exstudent("EXStudent",89)
ex.set_score(45)
exscore=ex.get_score()
print 'ex score %s:' % exscore
ex.print_cr()

S1=Student("NBO",556)
S2=Student("JIA",99)
S2score=S2.get_score()
print 'S2 spcore %s:' % S2score
S2.set_score(23)
S2score=S2.get_score()
print 'After set,S2 spcore %s:' % S2score

print "%s" % type(ex)
print "%s" % type(S1)

		
