def add():
    cid=input("Customer ID:")
    nm=input("Customer Name:")
    ad=input("Customer Address: ")
    cn=input("Contact No :")

    f=open('customer.txt','a')
    f.write(cid+'\t')
    f.write(nm+"\t")
    f.write(ad+"\t")
    f.write(cn+"\t")
    f.write("\n")
    print("Record added")
    f.close()

def delet():
    i=input("Enter the ID to remove from file")
    with open('customer.txt','r') as f:
        all=f.readlines()
    with open("customer.txt",'w') as f:
        for data in all:
            d=data.split('\t',1)
            if(d[0]!=i):
                f.writelines(data)
    print("Record detected")            
        


def update():
    i=input("Enter the ID to be updated from file")
    with open("customer.txt",'r') as f:
        all=f.readlines()
    with open("coustomer.txt",'w') as f:
        for data in all:
            d=data.split('\t',1)
            if(d[0]==i):
                New_name=input('New Name')
                New_addres=input("New Addres")
                New_contact=input("New Contact No") 
                f.writelines(d[0]+'\t'+New_name+'\t'+New_addres+'\t'+New_contact)
            else:
                f.writelines(data)
            print("Record is Updated")       

def search():
    i=input("Enter the ID to be search  from file")
    with open("customer.txt",'r') as f:
        all=f.readlines()
        for data in all:
            d=data.split('\t',1)
            if(d[0]==i):
                print(data)


def show():  
          f=open("customer.txt",'r')
          print()
          print("ID \t Name \t Address\tContact No")
          print(f.read())
          f.close()


while(True):
    print("Welcome to customer portal")
    print("1. Add new coustomer")
    print("2. Delete coustomer")
    print("3. Update  coustomer")
    print("4.Search  customer")
    print("5. Show all coustome")
    print("6. Exit")
    
    ch=int(input("Enter your choice:"))
    if ch==1:
        add()
        continue
    if ch==2:
        delet()    
    if ch==3:
        update()
    if ch==4:
        search()
    if ch==5:
        show()
    if ch==6:
        break
           
    
    

