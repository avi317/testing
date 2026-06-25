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
#find the first non repeating element in a list
n = [4,5,1,2,1,4,5]
# count =0
# for i in n:
#     if n.count(i) ==1:
#         print(i)
#         break
# f ={}
# for i in n:
#      f[i] =f.get(i,0)+1
# for i in n:
#     if f[i]==1:
#         print(i)
#         break
# print(f)
numbers = [2,7,11,15]
target = 17
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])
