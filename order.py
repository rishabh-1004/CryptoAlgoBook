"""
	A Program to find the order of any element within a finite group of number and check if the group is cyclic.

"""
from random import randint

list_val=[]
dict={}
class Order(object):

	def __init__(self,num_elem):
		self._groupList=num_elem
		self._number=None
		print(self.groupList)


	@property
	def groupList(self):
		print("Getting Values!")
		return self._groupList
	
	@groupList.setter
	def _groupList(self,num_elem):
		global list_val
		for _ in range(num_elem):
			currentelement= randint(1,15)
			list_val.append(currentelement)
		self._groupList=list(set(list_val))

	@property
	def number(self):
		return self._number

	@number.setter
	def number(self,val):
		val=input('Enter any number from the list: ')
		self._number=val

	def computePower(self):
		global dict
		length=len(self.group_list)
		i=1
		while i>1:
			dict[i]=dict[i-1]^self.number
			tempVar=dict[i] % length 
			if tempVar==self.number:
				print("The group is cyclic!")
				print("Order of The number {} is {}".format(self.number,i))
				return
			
			i+=1

if __name__ == '__main__':
	Order(num_elem=10)
	

			

			







