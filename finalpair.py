import sys
#calculate Self separete tax
Allowance = 132000
def Selfseparetetax(SelfIncome):

    #personal allowance
    SelfnetIncome = SelfIncome - Allowance - SelfMPF
    if SelfnetIncome < 0:
            SelfOutput = 0
            return SelfOutput
    else:
        #progressivetax
        if SelfnetIncome <= 50000:
                progressivetax = SelfnetIncome * 0.02

        elif 50000 < SelfnetIncome  and SelfnetIncome <= 100000:
                progressivetax = float(SelfnetIncome - 50000)*0.06 + 1000

        elif 100000 < SelfnetIncome  and SelfnetIncome <= 150000:
                progressivetax = float(SelfnetIncome - 100000)*0.1 + 4000
                        
        elif 150000 < SelfnetIncome and SelfnetIncome <= 200000:
                progressivetax = float(SelfnetIncome - 150000)*0.14 + 9000
                        
        else:
                progressivetax = (SelfnetIncome - 200000)*0.17 + 16000


    #standard tax calculate
    standardtax = (SelfIncome - SelfMPF) * 0.15
    # compare which one is lower
    if standardtax < progressivetax:
            SelfOutput = standardtax
    else:
            SelfOutput = progressivetax
    return SelfOutput

#calculate Spouse separete tax
def Spouseseparetetax(SpouseIncome):

    #personal allowance
    SpousenetIncome = SpouseIncome - Allowance - SpouseMPF
    if SpousenetIncome <= 0:
            SpouseOutput = 0
            return SpouseOutput
    else:
        #progressivetax
        if SpousenetIncome <= 50000:
                progressivetax = SpousenetIncome * 0.02

        elif 50000 < SpousenetIncome  and SpousenetIncome <= 100000:
                progressivetax = float(SpousenetIncome - 50000)*0.06 + 1000
                
        elif 100000 < SpousenetIncome  and SpousenetIncome <= 150000:
                progressivetax = float(SpousenetIncome - 100000)*0.1 + 4000
                        
        elif 150000 < SpousenetIncome and SpousenetIncome <= 200000:
                progressivetax = float(SpousenetIncome - 150000)*0.14 + 9000

        else:
                progressivetax = float(SpousenetIncome - 200000)*0.17 + 16000


        #standard tax calculate
        standardtax = (SpouseIncome - SpouseMPF) * 0.15

        # compare which one is lower    
        if standardtax < progressivetax:
                SpouseOutput = standardtax
        else: 
                SpouseOutput = progressivetax
                        
        return SpouseOutput

#calculate joint tax
def jointtax(SelfIncome,SpouseIncome):
        
        SumOfJointTax = (SelfIncome+SpouseIncome)
        SumOfJointTax = SumOfJointTax - Allowance * 2 - SelfMPF - SpouseMPF
        if SumOfJointTax < 0:
                SumOfJointTax = 0
                return SumOfJointTax
        else:
                #progressivetax
                if SumOfJointTax <= 50000:
                        progressivetax = SumOfJointTax*0.02
                                
                                
                elif 50000 < SumOfJointTax  and SumOfJointTax <= 100000:
                        progressivetax = float(SumOfJointTax - 50000)*0.06 + 1000
                                
                        
                elif 100000 < SumOfJointTax  and SumOfJointTax <= 150000:
                        progressivetax = float(SumOfJointTax - 100000)*0.1 + 4000
                                
                elif 150000 < SumOfJointTax and SumOfJointTax <= 200000:
                        progressivetax = float(SumOfJointTax - 150000)*0.14 + 9000
                                
                else :
                        progressivetax = float(SumOfJointTax - 200000)*0.17 + 16000
                                

                #standard tax calculate
                standardtax = (SelfIncome + SpouseIncome - SelfMPF - SpouseMPF) * 0.15
                        

                # compare which one is lower    
                if standardtax < progressivetax:
                        SumOfJointTax = standardtax
                else: 
                        SumOfJointTax = progressivetax
                return SumOfJointTax       

#which paid tax method
def assessmentrecommend(SelfIncome,SpouseIncome):
        if jointtax(SelfIncome,SpouseIncome) < Selfseparetetax(SelfIncome) + Spouseseparetetax(SpouseIncome):
                print("e)Joint assessment contributes to lower tax rate, so it is recommended.")


        elif jointtax(SelfIncome, SpouseIncome) == Selfseparetetax(SelfIncome) + Spouseseparetetax(SpouseIncome):
                print("e)Both assessments are the same, so either of them are recommended.")

        else :
                print("e)Separate assessment contributes to lower tax rate, so it is recommended.")
        return ""



#main program
try:
    SelfIncome = float(input("input your Yearly personal income" + ':'))
except ValueError:
    print("Please enter NUMBER of your Yearly personal income. ")
    sys.exit()

if SelfIncome/12 < 7100.0:
        SelfMPF = 0.0
elif 7100.0 < SelfIncome/12 and SelfIncome/12 < 30000.0:
        SelfMPF = SelfIncome/12 * 0.05
else:
        SelfMPF = 18000.0

print("a1)Your MPF mandatory contribution based on personal income are " + str(int(SelfMPF)) + ".")
print("a2)The salaries tax you should pay is " + str(int(Selfseparetetax(SelfIncome))))

try:
    SpouseIncome = float(input("input your spouse Yearly personal income" + ':'))
except ValueError:
    print("Please enter NUMBER of your spouse Yearly personal income. ")
    sys.exit(1)



if SpouseIncome/12 < 7100.0:
        SpouseMPF = 0.0
elif 7100.0 < SpouseIncome/12 and SpouseIncome/12 < 30000.0:
        SpouseMPF = SpouseIncome/12 * 0.05
else:
        SpouseMPF = 18000.0


print("b1)Your spouse MPF mandatory contribution based on personal income are " + str(int(SpouseMPF)) + ".")
print("b2)The salaries tax your spouse should pay " + str(int(Spouseseparetetax(SpouseIncome))))
print("c)The salaries tax should be paid " + str(int(Selfseparetetax(SelfIncome)) + int(Spouseseparetetax(SpouseIncome))) + " if separate assessment assumed.")
print("d)The salaries tax should be paid " + str(int(jointtax(SelfIncome, SpouseIncome))) + " if joint assessment assumed.")
print(assessmentrecommend(SelfIncome, SpouseIncome))

