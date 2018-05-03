import unittest

# The parseData function will take a filename and use it to calculate the average 
# alue of the X-DSPAM-Confidence in that file.  The function should return a string 
# of the form "Average spam confidence is XXX."  This assignment is based on Exercise 2
# from Chapter 7 in the textbook.

# I have provided a unittest that will run your code and check to make sure that you have covered
# different test cases, e.g, messy or missing data.

def parseData(fname):
	# Expecting one of two strings to be returned:
	# "Average spam confidence is XX"   or "No data to report."
	
	# Your code goes here.


	f=open(fname,'r')
	f_list=f.readlines()
	count=0
	sum=0
	for i in f_list:
		if i[:18]=='X-DSPAM-Confidence':
			#print (i[20])
			
			if i[20]!='0':
				sum+=0
			else:
				count+=1
				sum+=float(i[20:-1])
				#print(i[19:-1])
			
	try:
		aver=sum/count
		return 'Average spam confidence is {}'.format(aver)
	except:
		return 'No data to report.'


class Test1(unittest.TestCase): 
	def test1(self): 
		self.assertEqual(parseData("mbox.txt"),'Average spam confidence is 0.8941280467445736')

	def test2(self): 
		self.assertEqual(parseData("mbox-short.txt"),'Average spam confidence is 0.7507185185185187')

	def test3(self): 
		self.assertEqual(parseData("test1.txt"),'Average spam confidence is 0.8945416062465136')

	def test4(self): 
		self.assertEqual(parseData("test2.txt"),'No data to report.')


  
    
unittest.main()  # outside the class--this tells the framework to run



# Test 3 removes some of the data after an X-DSPAM string
# Test 4 removes all of the X-DSPAM lines