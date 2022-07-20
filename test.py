# # # Python3 code to demonstrate working of
# # # Convert numeric words to numbers
# # # Using join() + split()
# #
# # # Python3 code to demonstrate working of
# # # Convert numeric words to numbers
# # # Using join() + split()
# #
# # help_dict = {
# #         'one': '1',
# #         'two': '2',
# #         'three': '3',
# #         'four': '4',
# #         'five': '5',
# #         'six': '6',
# #         'seven': '7',
# #         'eight': '8',
# #         'nine': '9',
# #         'zero': '0',
# #         'double two':,
# #         # 'double three':'33',
# #         # 'double four':'44',
# #         # 'double five':'55',
# #         # 'double six':'66',
# #         # 'double seven':'77',
# #         # 'double eight':'88',
# #         # 'double nine': '99',
# #         # 'double zero': '00',
# #         # 'triple one': '111',
# #         # 'triple two': '222',
# #         # 'triple three': '333',
# #         # 'triple four': '444',
# #         # 'triple five': '555',
# #         # 'triple six': '666',
# #         # 'triple seven': '777',
# #         # 'triple eight': '888',
# #         # 'triple nine': '999',
# #         # 'triple zero': '000',
# #     }
# #
# # # initializing string
# # test_str = "one double two triple seven"
# # lstinp=test_str.split(" ")
# # print(lstinp)
# # lst=lstinp
# # length=len(lstinp)
# # for
#
# a=input()
# dbl=a.find("double")
# trp=a.find("triple")
# dbl=dbl+6
# trp=trp+6
# print(a[trp].("-"))
# # a[trp]=
# # print(a)
# # Python3 code to demonstrate working of
# # Convert numeric words to numbers
# # Using join() + split()
# #
# # help_dict = {
# # 	'one-': '1',
# # 	'two-': '2',
# # 	'three-': '3',
# # 	'four-': '4',
# # 	'five-': '5',
# # 	'six-': '6',
# # 	'seven-': '7',
# # 	'eight-': '8',
# # 	'nine-': '9',
# # 	'zero-' : '0',
# #     'double-one':'11',
# #     'double-one':'11',
# #
# # }
# #
# # # initializing string
# # # printing original string
# # print("The original string is : " + a)
# #
# # # Convert numeric words to numbers
# # # Using join() + split()
# # res = ''.join(help_dict[ele] for ele in a.split())
# #
# # # printing result
# # print("The string after performing replace : " + res)
#
#
#
# Python3 code to demonstrate working of
# Convert numeric words to numbers
# Using join() + split()

help_dict = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9',
	'zero' : '0',
    "double-one":'11'
}
#
# # initializing string
# test_str = "zero four zero  one"
#
# # printing original string
# print("The original string is : " + test_str)
#
# # Convert numeric words to numbers
# # Using join() + split()
# res = ''.join(help_dict[ele] for ele in test_str.split())
#
# # printing result
# print("The string after performing replace : " + res)
a=input()
dbl=a.find("double")
trp=a.find("triple")
dbl=dbl+6
trp=trp+6
new_character="-"
temp = list(a)
print(temp)
temp[dbl] = new_character
a = "".join(temp)
print(a)
temp2=list(a)
print(temp2)
temp2[trp] = new_character
a = "".join(temp2)
print(a)

help_dict = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9',
	'zero' : '0',
    "double-one":'11',
"double-two":'22',
"double-three":'33',
"double-four":'44',
"double-five":'55',
"double-six":'66',
"double-seven":'77',
"double-eight":'88',
"double-nine":'99',
"double-zero":'00',
	"triple-one":'111',
"triple-two":'222',
"triple-three":'333',
"triple-four":'444',
"triple-five":'555',
"triple-six":'666',
"triple-seven":'777',
"triple-eight":'888',
"triple-nine":'999',
"triple-zero":'000',



}
print("The original string is : " + a)

# Convert numeric words to numbers
# Using join() + split()
res = ''.join(help_dict[ele] for ele in a.split())

# printing result
print("The string after performing replace : " + res)