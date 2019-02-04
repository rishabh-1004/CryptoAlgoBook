import random

class Stream:
	def __init__(self,text):
		self.text=text

	def conv_2_binary(self):
		list=[]
		for j in self.text:
			#print (j)
			list.append(format(ord(j),"08b")) #converts ascii value to binary 
		
		#print(list)
		return list

	def encrypt(self,bin_list):
		dict={}
		Si_list=[]
		for i in bin_list:
			pseudo=random.randint(32,127) #generate random number
			con2bin=format(pseudo, "08b")#convert each bit into binary
			Si_list.append(con2bin)#makes a list of random bits
			#print(int(con2bin,2))#print the random number generated for each bit
			#print(con2bin)
			xor_values=bin(int(i,2)^int(con2bin,2)) #XOR two bits
			#print(xor_values[2:])
			dict[i]=str(xor_values[2:])
			#print(bin(xor_values)[2:].zfill(len(i)))#key=bin of bits,val=encrypted key

			#Si_list.append(con2bin)
			#l = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(i,con2bin))
			#print(int(con2bin,2))
			#dict[i]= l
		print (dict)
		return [dict,Si_list]

	def decrypt(self,encrypt_dict,random_bin):
		for key,value in encrypt_dict.items():
			#print(int(value,2))
			for ran_bit in random_bin:
				val=bin((int(ran_bit,2))^(int(value,2)))

				print(chr(int(val[2:],2)),end="")
				
		#pass

		

if __name__=='__main__':
	text=input('Enter a text:')
	obj = Stream(text)
	bin_list= obj.conv_2_binary()
	print(bin_list)
	encrypt_dict,random_bin=obj.encrypt(bin_list)
	obj.decrypt(encrypt_dict,random_bin)
	#print(encrypt_dict)
	#obj.decrypt(encrypt_dict)
	

	
