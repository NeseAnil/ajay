import random

def oven_in_out(input1,v) :
	
	# list1=["rice","toast","croissant","hamburger","pizza","sandwiches","fish","chicken","pizza-toast","cookie","cake","coffee"]
	# value1=[1,2,3,4,5,6,7,8,9,10,11,12]

	#read input
	# input1=input("Enter the name: ")
	# print()

	# if input1 in list1 :
		
	display_name='"'+input1+'"\n }\n'
	sample_string = 'abcdef0123456789'
	result = ''.join((random.choice(sample_string)) for x in range(4)) 
	name='"/m/'+result+'"'
	string='item { \nname: '+name +'\nid: '+str(v)+'\ndisplay_name: '+display_name
	#string=
	print(string)
	return string

	#output

	# print("item { ")
	# print('name: ',name)
	# print('id: ',Id)
	# print('display_name: ',display_name)
	# print('}')

# else :
# 	print("Match not found")

#calling function
# oven_in_out()
f = open("input_file.txt", "r")
var=0
new_file= open("output_file.txt","a+")
for i in f:
	var+=1
	resu=oven_in_out(i,var)
	new_file.write(resu)

new_file.close() 








