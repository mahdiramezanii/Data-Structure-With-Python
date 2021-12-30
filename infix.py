class Stack_Save:
    maxsize=100
    items=[]
#========================== (Stack(Save)) ===================================
    def isfull(self):
        if (len(self.items)==self.maxsize):
            return 1
        else:
            return 0
#============================ (empty) ===================================
    def isEmpty(self):
        if (len(self.items)==0):
            return 1
        else:
            return 0
#========================== (Push) ===================================    
    def push(self,x):
        if self.isfull():
            return None
        else:
            self.items.append(x)

#========================== (pop) ===================================
    def delet(self):
        
        if self.isEmpty():
            return None
        else:
            self.items.pop()     
#=========================== (show) ==================================
    
    def show(self):
        if self.isEmpty():
            return None
        else:
            for i in range(len(self.items)-1,-1,-1):
                print(self.items[i],end="")
         
    
#========================= (Class Stack) ==========================================  
    
   
class stack:
    maxsize=100
    items=[]
    
#========================== (Full) ===================================
    def isfull(self):
        if (len(self.items)==self.maxsize):
            return 1
        else:
            return 0
#============================ (empty) ===================================
    def isEmpty(self):
        if (len(self.items)==0):
            return 1
        else:
            return 0
#========================== (Push) ===================================    
    def push(self,x):
        if self.isfull():
            return None
        else:
            self.items.append(x)

#========================== (pop) ===================================
    def delet(self):
        
        if self.isEmpty():
            return None
        else:
            self.items.pop()     
#=========================== (show) ==================================
    
    def show(self):
        if self.isEmpty():
            return None
        else:
            return self.items
         
    
#========================== (peak) ==========================================           


    def peak(self):
        if self.isEmpty():
            return None
        else:
            return self.items[-1] 
        
#=========================== (Main) ================================

x1=Stack_Save()
s1=stack()

def revers(str_):
    st=""
    for i in range(len(str_)-1,-1,-1):
        if str_[i]==")":
            st+="("
            
        elif str_[i]=="(":
            st+=")"
        else:
            st+=str_[i]
            
    return st


data="zxcvbnmlkjhgfdsaqwertyuiopZXCVBNMLKJHGFDSAPOIUYTREWQ"
   
string=input("enter: ")
        
select=input("Pasvandi or pishvandi: ")
select=select.lower()     
 
#=========================== (postfix) ================================   
     
def pasvandi(st):
    
    
    for char in st:
#======================================= (Char) =================================================            
        if char in data:
            
            
            print(char,end="")
#======================================= (+) =================================================            
            
        elif char=="+":
                
            if (not(s1.isEmpty())):
                    
            
                if(s1.peak()=="*"):
                    print(s1.peak(),end="")
                    s1.delet()
                        
                elif(s1.peak()=="/"):
                    print(s1.peak(),end="")
                    s1.delet()
                        
                elif(s1.peak()=="%"):
                    print(s1.peak(),end="")
                    s1.delet()
                    
                elif(s1.peak()=="^"):
                        print(s1.peak(),end="")
                        s1.delet()
                    
                if(s1.peak()=="-"):
                    print(s1.peak(),end="")
                    s1.delet()   
                    
                   
            s1.push(char)
            
                
  #======================================= (-) =================================================            
      
            
        elif char=="-":
            
            if (not(s1.isEmpty())):
                
            
                if(s1.peak()=="*"):
                        print(s1.peak(),end="")
                        s1.delet()
                    
                elif(s1.peak()=="/"):
                        print(s1.peak(),end="")
                        s1.delet()
                        
                elif(s1.peak()=="%"):
                        print(s1.peak(),end="")
                        s1.delet() 
                
                elif(s1.peak()=="^"):
                        print(s1.peak(),end="")
                        s1.delet()
            
                if(s1.peak()=="+"):
                    print(s1.peak(),end="")
                    s1.delet()
                                        
                        
            s1.push(char)    
            
#======================================= (*) =================================================            
            
        elif char=="*":
            if s1.isEmpty():
                pass
                
            elif(s1.peak()=="*" or s1.peak()=="%" or s1.peak()=="^"):
                
                    print(s1.peak(),end="")
                    s1.delet()
                          
            s1.push(char)
 
 #======================================= (%) =================================================            

                
        elif char=="%":
            if s1.isEmpty():
                pass
                
            elif(s1.peak()=="*" or s1.peak()=="%" or s1.peak()=="^"):
                
                    print(s1.peak(),end="")
                    s1.delet() 
                          
            s1.push(char)
           
 #======================================= (/) =================================================            
          
            
        elif char=="/":
            if s1.isEmpty():
                pass
                
            elif(s1.peak()=="*" or s1.peak()=="%" or s1.peak()=="^"):
                
                    print(s1.peak(),end="")
                    s1.delet() 
                          
            s1.push(char) 
               
#======================================= (^) ==========================================

        elif char=="^":
            if s1.isEmpty():
                pass
                
            elif(s1.peak()=="*" or s1.peak()=="%" or s1.peak()=="/"):
                
                    print(s1.peak(),end="")
                    s1.delet() 
                          
            s1.push(char)        
                
#======================================= () =================================================            
                
        elif char=="(":
                
            s1.push(char)    
                 
            
    
        elif (char==")"):
                
            for i in range((len(s1.items))-1,-1,-1):
                    
                if s1.items[i]=="(":
                    s1.delet()
                    break
                    
                print(s1.items[i],end="")
                s1.delet()
                    
    for i in range((len(s1.items))-1,-1,-1):
        print(s1.items[i],end="")
            
#======================================= (Prefix) ================================================= 

def pishvandi(st):
       
    st=revers(st)
    
    for char in st:
#======================================= (Char) =================================================            
       
        if char in data:
            
            x1.push(char)
            
#======================================= (+) =================================================            
            
        elif char=="+":
                    
            if (not(s1.isEmpty())):
                              
                if(s1.peak()=="*"):
                    x1.push(char)
                    s1.delet()
                        
                if(s1.peak()=="/"):
                    x1.push(char)
                    s1.delet()
                        
                if(s1.peak()=="%"):
                    x1.push(char)
                    s1.delet() 
                
                if(s1.peak()=="^"):
                    x1.push(char)
                    s1.delet()   
               
            s1.push(char)
            
                
  #======================================= (-) =================================================            
      
        elif char=="-":
               
            if (not(s1.isEmpty())):
                              
                if(s1.peak()=="*"):
                    x1.push(char)
                    s1.delet()
                        
                if(s1.peak()=="/"):
                    x1.push(char)
                    s1.delet()
                        
                if(s1.peak()=="%"):
                    x1.push(char)
                    s1.delet() 
                
                if(s1.peak()=="^"):
                    x1.push(char)
                    s1.delet()                
                        
            s1.push(char)    
            
#======================================= (*) =================================================            
            
        elif char=="*":
                          
            s1.push(char)
 
 #======================================= (%) =================================================            

                
        elif char=="%":
            
            s1.push(char)
            
 #======================================= (^) =================================================   
                 
        elif char=="^":
            
            s1.push(char)
           
 #======================================= (/) =================================================            
                
        elif char=="/":
          
            s1.push(char)    
                 
#======================================= () =================================================            
                
        elif char=="(":
                
            s1.push(char)    
                 
        elif (char==")"):
                
            for i in range((len(s1.items))-1,-1,-1):
                    
                if s1.items[i]=="(":
                    s1.delet()
                    break
                    
                x1.push(s1.items[i])
                s1.delet()
                    
    for i in range((len(s1.items))-1,-1,-1):
        x1.push(s1.items[i])
            
#================================= cout =================================================            


if select=="pasvandi":
    
    pasvandi(string)

elif select=="pishvandi":
    
     pishvandi(string)
     
     print("\n***It turned out to be successful***\n")
     
     d=input("Do you want to see??? ")
     
     if d=="yes":
         
        x1.show()

#========================== test ==============================

#pasvandi:

#input_1 ---> a+b%r/(n-m*p)%d
#output_1 ---> abr%nmp*-/d%+

#input_2 ---> m*S-((D+p)%r)/N
#output_2 ---> mS*Dp+r%N/-

#input_3 ---> a+b*(c^d-e)^(f+g*h)-i
#output_3 ---> abcd^e-*fgh*+^+i-

#-------------------------------------

#Pishvandi:

#input_1 ---> a*n(s-n)/s^m
#output_1 ---> ^/*an-snsm

#input_2 ---> A^B+C/D
#output_2 ---> +^AB+CD