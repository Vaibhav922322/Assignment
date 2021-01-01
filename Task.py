import json
import sys
import os
import time

def strt():
    try:
        f = open('Data.txt','r')
    except:
        f = open('Data.txt','w')
    f.close()
    
    #check if key is already present in data or not, if not present it will create one 
def kPresent(f,k):
    s=" "
    while s:
        s=f.readline()      #read file linewise
        l=s.split()
        if len(l)>0:
            if l[0]==k:             #key is present
                return True
    return False                    #key is Absent

    # open object wrt. key
def oOpen(f):   
    print("Enter the key for object:")
    k=input().strip()
    l=[]
    s=" "
    v=""
    while s:
        s=f.readline()
        l=s.split()
        if len(l)>0:
            if l[0]==k:
                #check for live-time of key
                if (((int(round(time.time()))) - int(l[-1])) <= 1800):
                    v=s[s.index('{'):s.index('}')+1]
                    print(v)
                else:
                    print("Key Live-time Expired , You Can't read/delete the key")
                return

    print("Entered Key not Found")
    return
        
    # add new object with key    
def kAppend(f):
    print("\n\n\t\t\t***NOTE***\n Key will locked after 30 min.")
    print("After this time, you can't read / delete the object \n\n")
    
    print("Make sure length of key doesn't exceed 32 bits and size of object doens't exceed 16KB")
    print("Enter key:",end="")
    i='1'
    k=input().strip()
    
    #check the length of key
    while len(k)>32:                    
        if len(k)>32 and i=='1':
            print("Key size limit exceed")

        print("Press 1 to re-enter key or press 3 to go to main menu ")
        i=input()
        if i=='1':
            k=input().strip()
            continue
        elif i=='3':
            return
        else:
            print("Wrong selection")

    if(kPresent(f,k)):
        print("Key Already Exist")
        return
        
            
    print("Enter Value(JSON Object): ")
    v=input()                   #taking input of JSON object as string
    v=json.loads(v)                 #string to JSON object conversion
    if sys.getsizeof(v)>16*1024:            #checking size of JSON object
        print("JSON Object size limit exceed")
        return

    f=open("Data.txt",'a')
    f.write(k+" : "+(str(v))+" "+str(int(round(time.time())))+"\n")
    f.close()
    f=open("Data.txt",'r')
    print("\n\nEntry Successful\n\n")
    return

    #Delete Object with key    
def kDelete(f):
    t=open("tem.txt",'w')           #creating new temporary file
    t.close()
    t=open("tem.txt",'a')
    s=" "
    print("Enter the key to delete:",end='')
    k=input().strip()
    d=False
    while s:                        #this while loop will copy all key and object
        s=f.readline()              #from datafile to temp. file
        l=s.split()
        if len(l)==0:
            continue
        if len(l)>0 and not d:
            if l[0]==k:
                d=True
                if (int(round(time.time()) - int(l[-1]) <= 1800)) :
                    print("Delete Successful")
                    continue
                else:
                    print("Key Live-time Expired , You Can't read/delete the key")
                
        t.write(s)
    t.close()
    f.close()
    os.remove("Data.txt")               #deleting original file 
    os.rename("tem.txt","Data.txt")     # remaing temp file as of original
    f=open("Data.txt",'r')
    if not d:
        print("Key not found")
    return
        
    
def main():
    strt()                          #initializing file
    sz=True
    while(True):
        
        f=open('data.txt','r')
        r=sys.getsizeof("data.txt")         #check file size
        if r > (1024*1024*1024):
            print("!!!WARNING!!!!! \nFilesize limit  exceed, can't append more objects")
            sz=False
            
        print("\nPress the number with respect to the operation desired:")
        print("1 : Add new object")
        print("2 : Open object with key")
        print("3 : Delete object")
        print("4 : Exit")
        
        x=input()
        if x=='1':      #Add Object
            if sz:
                kAppend(f)
            
            if not(sz):
                print("Can't add more objects since max. allowed file size exceeds ")
                print(" Delete some objects and try again!" )
                
        elif x=='2':    #open Object
            oOpen(f)
            f.close()

        elif x=='3':    #Delete object
            kDelete(f)
            f.close()
        elif x=='4':    #Exit
            f.close()
            break
        else:
            print("Wrong Input  ")
            f.close()    
        

if __name__=="__main__":
    main()
