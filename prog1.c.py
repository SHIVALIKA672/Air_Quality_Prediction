"""
Experiment-1(c)
Name : SHIVALIKA JAIRAM PILLAI
Class :SE-COMPS-B      Roll No: 461         Batch: B3

Aim : Write a menu-driven program to demonstrate the use of a dictionary in python.
a)Create a key/value pair dictionary
b)Update/concatenate and delete the item of the existing dictionary
c)Find a key and print its value
d)Map two list into a dictionary

Program :
"""
d1 = {}
d2 = {}

def dict1():
    global d1
    n = int(input("Enter number of values:"))
    for i in range(0,n):
        key = int(input('Enter key(int):'))
        value = input("Enter value:")
        d1.update({key:value})
    print("The dictionary is:")
    print(d1)

def dict2():
    global d2
    n = int(input("Enter number of values:"))
    for i in range(0,n):
        key = int(input("Enter key(int):"))
        value = input("Enter value:")
        d2.update({key:value})
    print("The dictionary is:")
    print(d2)

def dict_update():
    m = int(input('Enter key of value to be updated:'))
    val = input("Enter updated value")
    if m in d1:
        d1[m] = val
        print("Updated dictionary is ",d1)
    print("\nDictionary:",d2,"will be concatenated to:",d1)

def dict_delete():
    m = int(input("Enter key of value to be deleted: "))
    if m in d1:
        print("Deleted value:",d1[m])
        del d1[m]
        print("Dictionary after deletion:",d1)
    else:
        print("Key not present in the dictionary")

def dict_find():
    m = int(input("Enter key to be searched: "))
    if m in d1:
        print("The key value is:",d1[m])
    else:
        print("Key not present in dictionary")

def dict_map():
    key=[]
    values=[]
    n = int(input("Enter no. of elements:"))
    for i in range(0,n):
        ekey = int(input("Enter key:"))
        key.append(ekey)
        evalue = input("Enter value:")
        values.append(evalue)
    print("key list:",key,"\nValue list:",values)
    Dict3 = dict(zip(key,values))
    print("Dictionary after mapping:",Dict3)


choice=0
while choice!=6:
    print('---------------------------------------------------------------')
    print('1.Enter first dictionary.\n2.Enter second dictionary.\n3.Update dictionary and delete the item.\n4.Find a key and print its value.\n5. Map two list into a dictionary.')
    choice = int(input('Enter Choice: '))
    print("---------------------------------------------------------------")
    if choice == 1:
        dict1()
    elif choice == 2:
        dict2()
    elif choice == 3:
        dict_update()
        dict_delete()
    elif choice == 4:
        dict_find()
    elif choice == 5:
        dict_map()
    else:
        exit(0)
"""
Output:
---------------------------------------------------------------
1.Enter first dictionary.
2.Enter second dictionary.
3.Update dictionary and delete the item.
4.Find a key and print its value.
5. Map two list into a dictionary.
Enter Choice: 1
---------------------------------------------------------------
Enter number of values:3
Enter key(int):1
Enter value:25
Enter key(int):2
Enter value:38
Enter key(int):3
Enter value:56
The dictionary is:
{1: '25', 2: '38', 3: '56'}
---------------------------------------------------------------
1.Enter first dictionary.
2.Enter second dictionary.
3.Update dictionary and delete the item.
4.Find a key and print its value.
5. Map two list into a dictionary.
Enter Choice: 2
---------------------------------------------------------------
Enter number of values:3
Enter key(int):4
Enter value:40
Enter key(int):7
Enter value:39
Enter key(int):6
Enter value:60
The dictionary is:
{4: '40', 7: '39', 6: '60'}
---------------------------------------------------------------
1.Enter first dictionary.
2.Enter second dictionary.
3.Update dictionary and delete the item.
4.Find a key and print its value.
5. Map two list into a dictionary.
Enter Choice: 3
---------------------------------------------------------------
Enter key of value to be updated:1
Enter updated value 70
Updated dictionary is  {1: ' 70', 2: '38', 3: '56'}

Dictionary: {4: '40', 7: '39', 6: '60'} will be concatenated to: {1: ' 70', 2: '38', 3: '56'}
Enter key of value to be deleted: 4
Key not present in the dictionary
---------------------------------------------------------------
1.Enter first dictionary.
2.Enter second dictionary.
3.Update dictionary and delete the item.
4.Find a key and print its value.
5. Map two list into a dictionary.
Enter Choice: 3
---------------------------------------------------------------
Enter key of value to be updated:2
Enter updated value 45
Updated dictionary is  {1: ' 70', 2: ' 45', 3: '56'}

Dictionary: {4: '40', 7: '39', 6: '60'} will be concatenated to: {1: ' 70', 2: ' 45', 3: '56'}
Enter key of value to be deleted: 3
Deleted value: 56
Dictionary after deletion: {1: ' 70', 2: ' 45'}
---------------------------------------------------------------
1.Enter first dictionary.
2.Enter second dictionary.
3.Update dictionary and delete the item.
4.Find a key and print its value.
5. Map two list into a dictionary.
Enter Choice: 4
---------------------------------------------------------------
Enter key to be searched: 6
Key not present in dictionary
---------------------------------------------------------------
1.Enter first dictionary.
2.Enter second dictionary.
3.Update dictionary and delete the item.
4.Find a key and print its value.
5. Map two list into a dictionary.
Enter Choice: 4
---------------------------------------------------------------
Enter key to be searched: 1
The key value is:  70
---------------------------------------------------------------
1.Enter first dictionary.
2.Enter second dictionary.
3.Update dictionary and delete the item.
4.Find a key and print its value.
5. Map two list into a dictionary.
Enter Choice: 5
---------------------------------------------------------------
Enter no. of elements: 3
Enter key:1
Enter value:26
Enter key:6
Enter value:17
Enter key:32
Enter value:41
key list: [1, 6, 32] 
Value list: ['26', '17', '41']
Dictionary after mapping: {1: '26', 6: '17', 32: '41'}
"""
