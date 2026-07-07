# numbers = [10,20,30,40,50]
# num_sorted= True
# for i in range(len(numbers)-1):
#     if numbers[i] > numbers[i+1]:
#         num_sorted = False
#         break
# print(num_sorted)
# nested_list = [[1,2], [3,4], [5,6],]
# empty_list=[]
# for i in nested_list:
#     for j in i:
#         empty_list.append(j)
# print(empty_list)
# nested = [1,[2,[3,4],5],6]
#
# def flatten(nested):
#     output = []
#     for item in nested:
#         if isinstance(item, list):
#             output.extend(flatten(item))
#         else:
#             output.append(item)
#     return output
# print(flatten(nested))
# numbers = [1,2,3,2,4,5,1,6,3]
# seen =set()
# d=[]
# for i in numbers:
#     if i in seen and i not in d:
#         d.append(i)
#     else:
#         seen.add(i)
# print(d)
# print(seen)
# numbers = [1,2,3,2,4,5,1,6,3]
# #find all duplicate elements in a list
# #output = [1,2,3]
#
# s = set()
# d = []
# for n in numbers:
#     if n in s and n not in d:
#         d.append(n)
#     else:
#         s.add(n)
# print(sorted(d))
#find the first nonrepeating element in a list
n = [4,5,1,2,1,4,5]
# count =0
# for i in n:
#     if n.count(i) ==1:
#         print(i)
#         break
# f={}
# for i in n:
#      f[i] =f.get(i,0)+1
# for i in n:
#     if f[i]==1:
#         print(i)
#         break
# print(f)
# numbers = [2,7,11,15]
# target = 17

# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print(numbers[i], numbers[j])
# sqr= lambda n: n*n
# print(sqr(5))
#
# def total(*args):
#     print(type(args))
#     return sum(args)
#
# print(total(1,2,3,4,5))
# def show_info(**details):
#     for key, value in details.items():
#         print(f"{key}: {value}")
# show_info(name="Avinash",)

# d = {"a":10,"b":20,"c":60,"d":40,"e":80}
# sorted_dict = dict(sorted(d.items(),key=lambda item: item[1]))
# print(sorted_dict)
# num =[1,4,6,2,0,8,43,0]
# zeros= [x for x in num if x ==0]
# nonzero= [x for x in num if x != 0]
# print(nonzero + zeros)
##Given one string – ‘uNiTed StAteS oF aMeRiCa’, write code to make title string. Don’t use inbuild string methods
# s = "uNiTed StAteS oF aMeRiCa"
# result =""
# new_word =True
#
# for ch in s:
#     if ch == " ":
#         result += ch
#         new_word = False
#     else:
#         if new_word:
#             if 'a' <= ch <= 'z':
#                 result += chr(ord(ch) -32)
#             else:
#                 result += ch
#             new_word = False
#         else:
#             if 'A' <= ch <= 'Z':
#                 result += chr(ord(ch) +32)
#             else:
#                 result += ch
# print(result)
# print(s.title())
# res= []
# words= s.split()
# for word in words:
#     res.append(word.capitalize())
# print(" ".join(res))
# list_comp = " ".join([x.capitalize() for x in s.split()])
# print(list_comp)
##Given one string – ‘This is the constitution of India’, write code to return list of dictionary with each letter as key and count of that letter as value.
# s = "This is the constitution of India"
# count = {}
# for i in s:
#     if i != " ":
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1
# print(count)
##If string is ‘This is This’, output should be the below one
##e.g : - [{‘t’:1, ‘h’:1, ‘i’:1, ‘s’:1}, {‘i’:1, ‘s’:1}, {‘t’:1, ‘h’:1, ‘e’:1}]
# str= "This is This"
# result =[]
# for word in str.lower().split():
#     d = {}
#     for ch in word:
#
#         if ch in d:
#             d[ch] += 1
#         else:
#             d[ch] = 1
#     result.append(d)
# print(result)
# import re
# with open("data.txt", "r") as file:
#     content = file.read()
#     match= re.findall(r"Email:\s*[a-zA-Z]+", content)
#     if match:
#         print(f"Email found: ", match)
#     else:
#         print("No match")
# num = [1,2,2,2,3,4,4,5,6,6,7,7,8,8]
# result =[]
# for i in num:
#     if i not in result:
#         result.append(i)
# print(result)
# newsor= sorted(num, reverse=True)
# print(newsor)

##Given one file, Write code to form dictionary with each word as key and count of that word as dictionary. Than print the word with max count.
# word_count = {}
#
# with open("testfile.txt", "r") as file:
#     for line in file:
#         words = line.lower().split()
#         for word in words:
#             word = word.strip(".,;/?:")
#
#             if word in word_count:
#                 word_count[word] += 1
#             else:
#                 word_count[word] = 1
#
# print(word_count)
# max_count = max(word_count, key=word_count.get)
# print(max_count, "->", word_count[max_count])

##Given one string ‘thisforthis’, write code to remove duplicate letters
# s = "thisforthis"
# seen = set()
# result = ""
# for ch in s:
#     if ch not in seen:
#         seen.add(ch)
#         result += ch
# print(result)
#print(seen)
# unique_ips = set()
# with open("ips.txt", "r") as f:
#     for line in f:
#         ip = line.strip()
#         if ip not in unique_ips:
#             unique_ips.add(ip)
# with open ("unique_ips.txt", "w") as f:
#     for ip in unique_ips:
#         f.write(ip + "\n")
# print("duplicate reemoved")

##Given one json string, Write code to change specific key|value element or to add element to same json string.
# import json
# json_str = '''
# {
# "name": "Avinash",
# "age": 33,
# "salary": 20000
# }
# '''
# data = json.loads(json_str)
# print(data)
# data["age"] = 35
# data["salary"] = 21000
# new_json = json.dumps(data)
# print(new_json)

# try:
#     print("step 1")
#     x = 10 /2
#     print("Step 2")
# except ZeroDivisionError:
#     print("Step 2 cannot be divided by zero")
# else:
#     print("Else block")
# finally:
#     print("Final block")
# print("Program end")

##Given one top command output in file. Need to return process id depending on the max memory use.
# Top_pid =None
# max_mem = 0
# with open("Top_command.txt", "r") as file:
#     for line in file:
#         p = line.split()
#         if len(p) > 10 and p[0].isdigit():
#             pid,process = p[0],p[11]
#             mem = float(p[9])
#             if mem > max_mem:
#                 max_mem = mem
#                 Top_pid = pid,process
# print(Top_pid)
##Write one class program for Employee class where it will take firstname, lastname and role as input. And it will return full name and it will have one get method to get the id of each employee object sequentially.

# class Employee:
#     emp_id_counter = 1
#     def __init__(self,firstname,lastname,role):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.role = role
#         self.empid= Employee.emp_id_counter
#         Employee.emp_id_counter += 1
#     def get_full_name(self):
#         return f'{self.firstname} {self.lastname}'
#     def get_empid(self):
#         return self.empid
#
# emp1 = Employee("Avinash","Jha",role="Engineer")
# emp2 = Employee("Monika","Jha", role="Teacher")
# print(emp1.get_full_name() ,"-->", emp1.get_empid())
# print(emp2.get_full_name() ,"-->", emp2.get_empid())

# class Employee:
#     company = "Facebook"
#
#     @classmethod
#     def change_company(cls,value):
#         cls.company = value
#         print(cls.company)
# Employee.change_company("amazon")

# class Calculator:
#     @staticmethod
#     def add(a,b):
#         return a+b
#
# print(Calculator.add(1,2))
# ##class Variable
# class Employee:
#     company = "abc ltd"
#
# em1 = Employee()
# em2 = Employee()
# print(em1.company)
# print(em2.company)
#
# ##instance Variable
# class Employee:
#     company = "abc ltd"
#     def __init__(self, name):
#         self.name = name
#
# emp1 = Employee("Avinash")
# print(emp1.name)
# emp2 = Employee("Bablu")
# print(emp2.name)

# a = 10
#
# def sum(a, b):
#     print("Inside Function:", a)
#     return a + b
#
# sum(2, 5)
#
# print("Outside Function:", a)

# for i in range(1,7):
#     for j in range(1, i + 1):
#         print( i * j , end= " ")
#     print()
# name = input("Enter your name: ").title()
#
# for i in range(len(name)):
#     for j in range(i + 1):
#         print(name[j], end=" ")
#     print()
# X = [1,7,4,2,1,3,11,5]
# target =10
# for i in range(len(X)):
#     total =0
#     for j in range(i, len(X)):
#         total += X[j]
#         if total == target:
#             print("starting index", i)
#             print("EndIndex", j)
#             break
# X = "aaabcccdeeff"

# count ={}
# for ch in X:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1
# print(count)
# s = "   Hello\t\tPython    Programming   "
# print(" ".join(s.split()))