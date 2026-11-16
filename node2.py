'''
Name-Shaikh Ummehabiba
roll no-30

Problem Statement- To create a student record Management System using a singly
linked list that stores student data(Roll no, Name, Marks) and allows operation
such as Add, Delete, Update, Search and Sort, as well as displaying records in
ascending or descending order based on Roll No, Name, or Marks.
'''
class Node:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks
        self.next = None      
             
       

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,rollno, name, marks):
        new_node = Node(rollno, name, marks)
       
        if self.head is None:
           self.head = new_node
           return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
        
    def print_list(self):
        current = self.head
        print("Roll no\t\t""Name\t\t""Marks")
        while current:
            print(current.rollno,"\t\t",current.name,"\t\t",current.marks)    
            current = current.next
            
            
    def delet_node(self, rollno):
        current = self.head
        prev = None
        while current:
           if current.rollno == rollno:
              if prev:
                 prev.next = current.next
           else:
                self.head = current.next     
                print("Student Record Not Found")
                return
        prev = current
        current = current.next
        print("Student data not found")
        
    def update(self, key, rollno, new_roll):
        current = self.head
        while curent:
           if current.rollno == rollno:
              current.rollno = new_roll
        current = current.next
        
        
    def search(self, rollno):
        current = self.head
        while current:
            if current.rollno == rollno:
                print("record found")
            print("Record not found")  
        
    def menu(self):
        while True:
              print("1.append")
              print("2.Display")
              print("3.Delete")
              print("4.update")
              print("5.search")
              print("6.Exit")
              ch = input("enter the number of your choice:")

              if ch == '1':
                 rollno = int(input("enter the roll_no:"))
                 name = input("enter the name:")
                 marks = int(input("enter the marks:"))
                 self.append(rollno, name, marks) 
                 print("data inseted")
              

              elif ch == '2':
                   self.print_list()
               
              elif ch == '3':
                   key = input("Enter Roll No to delete data:") 
                   self.delet_node(rollno)
                   print("The remaining data is:")
                   self.print_list()

              elif ch == '4':
                   rollno = input("Enter Roll No to update:")
                   self.search(rollno)
                
                   rollno = input("Enter old roll no:")
                   new_roll = input("Enter new roll no:")
                   self.update(rollno, new_roll)
              
              elif ch == '5':
                   rollno = input("Enter roll no:")
                   self.search(rollno)           
              elif ch == '6':
                   break

              else:
                  print("Invalid choice please try again")
L1 =Linkedlist()
L1.menu()
#L1.append

'''
1.append 
2.Display 
3.Delete 
4.update 
5.search 
6.Exit 
enter the number of your choice:1 
enter the roll_no:30 
enter the name:Shaikh Ummehabiba 
enter the marks:85 
data inserted 
1.append 
2.Display 
3.Delete 
4.update 
5.search 
6.Exit 
enter the number of your choice:1 
enter the roll_no:31 
enter the name:Riya 
enter the marks:90 
data inserted 
1.append 
2.Display 
3.Delete 
4.update 
5.search 
6.Exit 
enter the number of your choice:1 
enter the roll_no:32 
enter the name:Diya 
enter the marks:78 
data inserted 
1.append 
2.Display 
3.Delete 
4.update 
5.search 
6.Exit 
enter the number of your choice:2 
Roll no   Name                Marks
30        Shaikh Ummehabiba   90
31        Riya                85
32        Diya                78
1.append 
2.Display 
3.Delete 
4.update 
5.search 
6.Exit 
enter the number of your choice:5 
Enter roll no:31 
Record found 
1.append 
2.Display 
3.Delete 
4.update 
5.search 
6.Exit 
enter the number of your choice:4 
Enter old roll no:32 
Enter new roll no:33 
Record Updated 
1.append 
2.Display 
3.Delete 
4.update 
5.search 
6.Exit 
enter the number of your choice:2 
Roll no   Name               Marks 
30        Shaikh Ummehabiba  90
31        Riya               85
33        Diya               78
1.append 
2.Display 
3.Delete 
4.update 
5.search 
6.Exit     
enter the number of your choice:3 
Enter Roll No to delete data:33 
Student Record Deleted 
The remaining data is: 
Roll no   Name                Marks
30        Shaikh Ummehabiba   90
31        Riya                85
1.append 
2.Display 
3.Delete 
4.update 
5.search 
6.Exit 
enter the number of your choice:6 
Exiting. 
''' 
