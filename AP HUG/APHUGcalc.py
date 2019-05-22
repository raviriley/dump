print ("Welcome to Ravi's 2017 AP HUG Exam Score Estimator")
print ("\n")
def calc():
    MCscore = int (input("Multiple Choice Score Out Of 75:  "))
    FRQ1n = int (input("FRQ 1 points out of 8:  "))
    FRQ1d = int (8)
    
    FRQ2n = int (input("FRQ 2 points out of 8:  "))
    FRQ2d = int (8)
    
    FRQ3n = int (input("FRQ 3 points out of 6:  "))
    FRQ3d = int (6)
    
    compoScore = ((MCscore / 75)*60) + ((60/(FRQ1d + FRQ2d + FRQ3d))*(FRQ1n + FRQ2n + FRQ3n))

    print ("\n")
    print ("Composite Score: ",compoScore)

    #Average Curve
    if 0 <= compoScore <= 41.833333:
        print ("Estimated Score Based on Average Curve: 1")  
    if 41.833333 < compoScore <= 52.166666:
        print ("Estimated Score Based on Average Curve: 2") 
    if 52.166666 < compoScore <= 64.5:
        print ("Estimated Score Based on Average Curve: 3")
    if 64.5 < compoScore <= 79.166666:
        print ("Estimated Score Based on Average Curve: 4")
    if 79.166666 < compoScore <= 120:
        print ("Estimated Score Based on Average Curve: 5")
    if 78 <= compoScore <= 80:
        print ("    NOTE: This is a high 4 or a low 5. Could be either, neither is more likely based on the average. ")

    #2001 Curve
    if 0 <= compoScore <= 40.5:
        print ("Estimated Score Based on 2001 Curve: 1")  
    if 40.5 < compoScore <= 49.5:
        print ("Estimated Score Based on 2001 Curve: 2") 
    if 49.5 < compoScore <= 61.5:
        print ("Estimated Score Based on 2001 Curve: 3")
    if 61.5 < compoScore <= 72.5:
        print ("Estimated Score Based on 2001 Curve: 4")
    if 72.5 < compoScore <= 120:
        print ("Estimated Score Based on 2001 Curve: 5")
    
    #2006 Curve
    if 0 <= compoScore <= 34.5:
        print ("Estimated Score Based on 2006 Curve: 1")  
    if 34.5 < compoScore <= 44.5:
        print ("Estimated Score Based on 2006 Curve: 2") 
    if 44.5 < compoScore <= 58.5:
        print ("Estimated Score Based on 2006 Curve: 3")
    if 58.5 < compoScore <= 73.5:
        print ("Estimated Score Based on 2006 Curve: 4")
    if 73.5 < compoScore <= 120:
        print ("Estimated Score Based on 2006 Curve: 5")

    #2016 Curve
    if 0 <= compoScore <= 50.5:
        print ("Estimated Score Based on 2016 Curve: 1")  
    if 50.5 < compoScore <= 62.5:
        print ("Estimated Score Based on 2016 Curve: 2") 
    if 62.5 < compoScore <= 73.5:
        print ("Estimated Score Based on 2016 Curve: 3")
    if 73.5 < compoScore <= 86.5:
        print ("Estimated Score Based on 2016 Curve: 4")
    if 86.5 < compoScore <= 120:
        print ("Estimated Score Based on 2016 Curve: 5")
    
    print ("--------------------------------------------")
    print ("\n")
        
while True:
    calc()
