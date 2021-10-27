"""
Experiment-1(b)
Name : SHIVALIKA JAIRAM PILLAI
Class :SE-COMPS-B      Roll No: 461         Batch: B3

Aim : Write a menu-driven program to demonstrate the use of list in python.
    i) Put Even and Odd elements into Two Different Lists.
    ii) Merge and sort the two lists.
    iii) Update the first element with X value and delete the middle element of the list.
    iv) Find max and min elements from the list.
    v) Add N names into the existing number list and check if word python is present in the list.
Program :
"""
even=[]
odd=[]
mrg=[]

def chk_even(a):
    if a%2==0:
        return 1
    else:
        return 0

def tkinp():
    global n
    n=int(input("Enter number: "))
    if(chk_even(n)):
        even.append(n)
    else:
        odd.append(n)

def merge():
    global mrg
    mrg=even+odd
    print("Merged list: ",mrg)

def list_sort():
    print("Unsorted list: ",mrg)
    mrg.sort()
    print("Sorted list: ",mrg)

def maximum():
    print("Maximum",max(mrg))
    print("Minimum",min(mrg))

def up_1():
    first=int(input("Enter new element: "))
    mrg[0]=first
    print("Updated list: ",mrg)
    mid=int((len(mrg)-1)/2)
    del mrg[mid]
    print("List after middle term deletion: ",mrg)

def list_inp():
    N=int(input("Enter no. of elements: "))
    for i in range(0,N):
        x=input("Enter new element: ")
        mrg.append(x)
    print("The list: ",mrg)

def list_chk():
    if 'python' in mrg:
        print('python" exists in the list')
    else:
        print('python" does not exist in the list')

choice=0
while(choice!=7):
    print("1.Enter input\n2.Show even and odd lists\n3.Merge lists and sort in ascending order\n4.Find max and min number")
    print("5.Update first element. Delete middle term\n6.Input new string and check presence of 'python' in string\n7.Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        tkinp()
    elif choice==2:
        print("Even list",even)
        print("Odd list",odd)
    elif choice==3:
        merge()
        list_sort()
    elif choice==4:
        maximum()
    elif choice==5:
        up_1()
    elif choice==6:
        list_inp()
        list_chk()
    else:
        exit(0)
"""
Output :
1.Enter input
2.Show even and odd lists
3.Merge lists and sort in ascending order
4.Find max and min number
5.Update first element. Delete middle term
6.Input new string and check presence of 'python' in string
7.Exit
Enter choice:1
Enter number: 6
1.Enter input
2.Show even and odd lists
3.Merge lists and sort in ascending order
4.Find max and min number
5.Update first element. Delete middle term
6.Input new string and check presence of 'python' in string
7.Exit
Enter choice: 1
Enter number: 17
1.Enter input
2.Show even and odd lists
3.Merge lists and sort in ascending order
4.Find max and min number
5.Update first element. Delete middle term
6.Input new string and check presence of 'python' in string
7.Exit
Enter choice: 1
Enter number: 28
1.Enter input
2.Show even and odd lists
3.Merge lists and sort in ascending order
4.Find max and min number
5.Update first element. Delete middle term
6.Input new string and check presence of 'python' in string
7.Exit
Enter choice: 1
Enter number: 35
1.Enter input
2.Show even and odd lists
3.Merge lists and sort in ascending order
4.Find max and min number
5.Update first element. Delete middle term
6.Input new string and check presence of 'python' in string
7.Exit
Enter choice: 2
Even list [6, 28]
Odd list [17, 35]
1.Enter input
2.Show even and odd lists
3.Merge lists and sort in ascending order
4.Find max and min number
5.Update first element. Delete middle term
6.Input new string and check presence of 'python' in string
7.Exit
Enter choice: 3
Merged list:  [6, 28, 17, 35]
Unsorted list:  [6, 28, 17, 35]
Sorted list:  [6, 17, 28, 35]
1.Enter input
2.Show even and odd lists
3.Merge lists and sort in ascending order
4.Find max and min number
5.Update first element. Delete middle term
6.Input new string and check presence of 'python' in string
7.Exit
Enter choice: 4
Maximum 35
Minimum 6
1.Enter input
2.Show even and odd lists
3.Merge lists and sort in ascending order
4.Find max and min number
5.Update first element. Delete middle term
6.Input new string and check presence of 'python' in string
7.Exit
Enter choice: 5
Enter new element: 7
Updated list:  [7, 17, 28, 35]
List after middle term deletion:  [7, 28, 35]
1.Enter input
2.Show even and odd lists
3.Merge lists and sort in ascending order
4.Find max and min number
5.Update first element. Delete middle term
6.Input new string and check presence of 'python' in string
7.Exit
Enter choice: 6
Enter no. of elements: 3
Enter new element: shivalika
Enter new element: jairam
Enter new element: pillai
The list:  [7, 28, 35, 'shivalika', 'jairam', 'pillai']
python" does not exist in the list
1.Enter input
2.Show even and odd lists
3.Merge lists and sort in ascending order
4.Find max and min number
5.Update first element. Delete middle term
6.Input new string and check presence of 'python' in string
7.Exit
Enter choice: 7
"""
