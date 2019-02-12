"""
	A Program to find the order of any element within a finite group of number and check if the group is cyclic.

"""
from random import randint

dict={}
class Order(object):

	def __init__(self,g_List=None,value=None):
		self.__groupList=[]
		self.group_list =g_List

		self.__value=value
		

	@property
	def group_list(self):
		return self.__groupList
	
	@group_list.setter
	def group_list(self,list_val):
		if list_val is None:
			for _ in range(10):
				self.__groupList.append(randint(1,15))
		elif isinstance(list_val,list):
			self.__groupList=list_val


	@property
	def number(self):
		return self.__value

	
	def ask_user_for_number(self):
		val=input('Enter any number from the list: ')
		self.__value=int(val)

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

def main():
	print("Example with random list")
	obj = Order()
	print("List of numbers: {}".format(obj.group_list))
	#print("User selected: {}".format(obj.number))
	obj.ask_user_for_number()
	in_list = obj.number in obj.group_list
	print(in_list)

if __name__ == '__main__':
	main()
	

			

			







