#A function to input the elements of the list
def InputList(order,NmbrOfElmnts):
    list1=[]
    for i in range(NmbrOfElmnts):
        list1.append(input(f"Enter the element number {i + 1} of the {order} list: "))
    print()    
    return list1

#A function to compare the elements of the two lists
def CompareLists(list1,list2):
    p=0
    i=0
    while i < (len(list1)):
        while p < (len(list2)):
            if list1[i] == list2[p]:
                del list1[i]
                del list2[p]
                i = 0
                p = 0
                continue
            if list1[i] != list2[p]:p += 1
        i += 1    
        p = 0
            
            
    return(list1,list2)


#                                      BEGINING OF THE PROGRAM
#menu
print("*Welcome to lists comparing program*")
while True: #while loop to make sure the user enters a valid choice
    NmbrOfElmnts = input("Enter the number of elements in the lists: ")
    if int(NmbrOfElmnts.isdigit()) == True: #if statement to check if the number is valid and an integer
        break
    else:
        print("Invalid input!")
print()
list1 = []
print()
list2 = []
list1 = InputList("first",int(NmbrOfElmnts)) #A call of the function "InputList" to input the first list
list2 = InputList("second",int(NmbrOfElmnts)) #A call of the function "InputList" to input the second list
(list1,list2)=CompareLists(list1,list2)
if list1 != [] and list2 != []:
    print("Lists are equal = False")
elif list1 == list2 == []:
    print("Lists are equal = True")