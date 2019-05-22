print ("Welcome to Ravi's AP Seminar Grade Calculator")
print ("\n")
def calc():
    percent = float (input("Grade percentage in the class (ex: 94.5): "))
    possiblePoints = int (((percent/100)*421)+0.5)
    print (possiblePoints)
    a = 465.3 - possiblePoints
    b = 100*(a/96)
    #print ("To get an A (get a 90%) you need to get a "+b+"on the IWA and IMP. /n")
    #print ("This means you need "+a+"points out of 96 for the IWA and IMP combined.")
    print ("To get an A (get a 90%) you need to get a",b,"% on the IWA and IMP.\nThis means you need",a,"points out of 96 for the IWA and IMP combined.")

   
    print ("--------------------------------------------")
    print ("\n")
        
while True:
    calc()
