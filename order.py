"""
	A Program to find the order of any element within a finite group of number and check if the group is cyclic.

"""
from random import randint
from collections import Counter


class Order(object):

	def __init__(self,g_List=None,value=None):
		self.__groupList=[]
		self.group_list =g_List #group_list being a property returns a list 
		self.__value=value
		
	@property
	def group_list(self):
		return self.__groupList
	
	@group_list.setter
	def group_list(self,list_val):
		if list_val is None:
			print("first scenario")
			for _ in range(10):
				#print("adding!")
				self.__groupList.append(randint(1,10))
		#elif isinstance(list_val,list):
		#	print("last case")
		#	self.__groupList=list_val


	@property
	def number(self):
		return self.__value

	
	def ask_user_for_number(self):
		val=input('Enter any number from the list: ')
		self.__value=int(val)

	def computePower(self):
		listValue=[]
		dict={}
		groupList=self.group_list
		value=self.number
		length=len(groupList)
		c=0
		while True:
			for i in range(1,30):
				if dict.items() is None:
					dict[i]=value
				else:
					dict[i]=(value**i)%(length+1)
			break
		print(dict)
		for val in dict.values():
			if val==value:
				c+=1
			else:
				#print("Will continue!")
				continue
			if c==2:
				#print(val)
				max_key=list(dict.keys())[list(dict.values()).index(dict[i])]+1
				print('Order of {} is: {}'.format(value,max_key))
				print("Its cyclic!")
				break

		
def main():
	print("Example with random list")
	obj = Order()
	print("List of numbers: {}".format(obj.group_list))
	obj.ask_user_for_number()
	obj.computePower()
	#in_list = obj.number in obj.group_list
	#print(in_list)

if __name__ == '__main__':
	main()
	

			

			







