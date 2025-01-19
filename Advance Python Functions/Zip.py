list1=[1,2,3,4]
list2=[5,6,7,8]
list3=list(zip(list1,list2))
print(list3)

for x,y in zip(list1,list2[::-1]):
    print(x,y)

list4=["Kayleon","Karthik","Arjun"]
list5=[27,16,4]

dic={name:no for name,no in zip(list4,list5)}
print(dic)
