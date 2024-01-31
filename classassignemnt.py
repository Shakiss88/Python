class practice():
    def items():
        print("Sub fields in AI. subfields")
        t="Sub fields in AI are :"
        m="maching Learning"
        n="Neural Learning"
        v="Vision"
        r="Robotics"
        s="Speech processing"
        n="Natural language processing"
        lists=[t,m,n,v,r,s,n]
        for items in lists:
                print(items)   
       
    def oddeven():
        num=int(input("Enter a number : "))
        if((num%2)==1):
            print(num,"is Odd number")
            message=("Odd number")
        else:
            print(num,"is Even number")
            message=("Even number")
        return message
    
    def eligliblity ():
        Gender=input("your Gender : ")
        age =int(input("Your age:"))
        eligiblity="male"
        eligiblity1="Female"
        if(Gender==eligiblity and (age>=21)):
            print("Eligible")
            marriage="Eligible"
        elif(Gender==eligiblity1 and (age>=18)):    
            print("Eligible")
            marriage="Eligible"
        else:
            print("Not Eligible")
            marriage="Not Eligible"
        return marriage

    def addition ():
        Subject1=int(input("Subject1 = "))
        Subject2=int(input("Subject2 = "))
        Subject3=int(input("Subject3 = "))
        Subject4=int(input("Subject4 ="))
        Subject5=int(input("Subject5 = "))
        add=Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total =",add)        
        percentage=add/5
        print("percentage =",percentage)
        
    def perimeter():
        Height=int(input("Height:"))
        Breath=int(input("Breath: "))
        formula=(Height*Breath)/2
        print("Area of Triangle :",formula)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breath1=int(input("Breath1: "))
        perimeterformula=Height1+Height2+Breath1
        print("perimeter of triange :",perimeterformula)

       
