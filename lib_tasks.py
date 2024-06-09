from datetime import datetime
import csv
from os import getcwd
#add new books

def newbook(var_shelf):
    
    c1='Yes'
    while c1=='Yes' or c1=='Y':
        name=input('Enter book name -').title()
        auth=input('Enter Authors name -').title()
        pub=input('Enter Publisher name -').title()
        genre=input('Enter genre category -').title()
        b=1
        while b==1:
            try:
                quan=int(input('Enter Quantity of above book -'))
                b=2
            except:
                print('Please enter digit')
        var_shelf.append(([len(var_shelf)+1,name,auth,pub,genre,quan]))
        c1 = input('Do you want to add another book [yes/no]? -').title()
    
    return var_shelf

#update borrower details

def u_user(a):
          print('yet to be ready')
          
#find elemnts in lib

def find(var_shelf):
    varfind=input('Enter [book-name/author-name/publisher-name] to be searchhed: ')
    f_name=[]
    f_auth=[]
    f_pub=[]
    f_genre=[]
    
    search=[]
    
    for l in (var_shelf):
        f_name.append(l[1])
        f_auth.append(l[2]) 
        f_pub.append(l[3])
        f_genre.append(l[4])
    for m in range(len(f_name)):
        if varfind==f_name[m] or varfind==f_name[m].title() :
            search.append(var_shelf[m])
                
    for m in range(len(f_auth)):
        if varfind==f_auth[m] or varfind==f_auth[m].title():
            search.append(var_shelf[m])
       
    for m in range(len(f_pub)):
        if varfind==f_pub[m] or varfind==f_pub[m].title():
            search.append(var_shelf[m])     
                
    for m in range(len(f_genre)):
        if varfind==f_genre[m] or varfind==f_genre[m].title():
            search.append(var_shelf[m])
       
    var_shelf=search
    return var_shelf
    
    

#remove an element   
    
def remove(var_shelf):
    Sno = eval(input('Enter S.No(s). of book : '))
    for i in var_shelf:
        if i[o]==Sno:
    	    var_shelf.remove(i)
    return var_shelf
    


#Update one/more element in library

def edit(var_shelf):
    edt={'i':'Name','ii':'AuthName','iii':'PubName','iv':'Genre','v':'Quantity'}
    print()
    Sno = input('Enter S.No. of book : ')
    sample=[]
    for n in edt.keys():
        print ('\t',n,'\t:',edt[n])
    print()
    c2 = input('Enter from above options[ex-i,iii...] -')
    h1 = c2.split(',')
    for i in var_shelf:
        if i[0]==Sno:
            for o in h1 :
                if o=='i' or o=='1':
                    n1 = input('Enter new name -').title()
                    i[1]=n1
                elif o=='ii' or o=='2':
                    n2 = input('Enter new Author-name -').title()
                    i[2]=n2
                elif o=='iii' or o=='3':
                    n3 = input('Enter new Pub-name -').title()
                    i[3]=n3
                elif o=='iv' or o=='4':
                    n4 = input('Enter new Genre -').title()
                    i[4]=n4
                elif o=='v' or o=='5':
                    b=1
                    while b==1:
                        try:
                            n5=int(input('Enter Quantity of above book -'))
                            b=2
                        except:
                            print('Please enter digit')
                    i[5]=n5
             
            sample.append(i)
        else:
            sample.append(i)

    return sample
    
def arng_alph(var_shelf):
    f_name=[]
    f_auth=[]
    f_pub=[]
    f_genre=[]
    f_quan=[]
    
    for i in var_shelf:
        f_name.append(i[1].title())
        f_auth.append(i[2].title()) 
        f_pub.append(i[3].title())
        f_genre.append(i[4].title())
        f_quan.append(i[5])
        
    for r in range(len(f_name)-1):
        for s in range(len(f_name)-1-r):
            if f_name[s]>f_name[s+1]:
                f_name[s],f_name[s+1]=f_name[s+1],f_name[s]
                f_auth[s],f_auth[s+1]=f_auth[s+1],f_auth[s]
                f_pub[s],f_pub[s+1]=f_pub[s+1],f_pub[s]
                f_genre[s],f_genre[s+1]=f_genre[s+1],f_genre[s]
                f_quan[s],f_quan[s+1]=f_quan[s+1],f_quan[s]
                
    u=len(var_shelf)
    var_shelf.clear()
    for t in range(1,u+1):
        var_shelf.append([t,f_name[t-1],f_auth[t-1],f_pub[t-1],f_genre[t-1],f_quan[t-1]])
    return var_shelf
    

    


