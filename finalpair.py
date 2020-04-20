import sys

# calculate Self separate tax
Allowance = 132000


def selfSeparateTax():
    # personal allowance
    selfNetIncome = SelfIncome - Allowance - SelfMPF
    if selfNetIncome < 0:
        SelfOutput = 0
        return SelfOutput
    else:
        # progressive tax
        if selfNetIncome <= 50000:
            progressiveTax = selfNetIncome * 0.02

        elif 50000 < selfNetIncome <= 100000:
            progressiveTax = float(selfNetIncome - 50000) * 0.06 + 1000

        elif 100000 < selfNetIncome <= 150000:
            progressiveTax = float(selfNetIncome - 100000) * 0.1 + 4000

        elif 150000 < selfNetIncome <= 200000:
            progressiveTax = float(selfNetIncome - 150000) * 0.14 + 9000

        else:
            progressiveTax = (selfNetIncome - 200000) * 0.17 + 16000

    # standard tax calculate
    standardTax = (SelfIncome - SelfMPF) * 0.15
    # compare which one is lower
    if standardTax < progressiveTax:
        SelfOutput = standardTax
    else:
        SelfOutput = progressiveTax
    return SelfOutput


# calculate Spouse separate tax
def spouseSeparateTax():
    # personal allowance
    spouseNetIncome = SpouseIncome - Allowance - SpouseMPF
    if spouseNetIncome <= 0:
        SpouseOutput = 0
        return SpouseOutput
    else:
        # progressive tax
        if spouseNetIncome <= 50000:
            progressiveTax = spouseNetIncome * 0.02

        elif 50000 < spouseNetIncome <= 100000:
            progressiveTax = float(spouseNetIncome - 50000) * 0.06 + 1000

        elif 100000 < spouseNetIncome <= 150000:
            progressiveTax = float(spouseNetIncome - 100000) * 0.1 + 4000

        elif 150000 < spouseNetIncome <= 200000:
            progressiveTax = float(spouseNetIncome - 150000) * 0.14 + 9000

        else:
            progressiveTax = float(spouseNetIncome - 200000) * 0.17 + 16000

        # standard tax calculate
        standardTax = (SpouseIncome - SpouseMPF) * 0.15

        # compare which one is lower    
        if standardTax < progressiveTax:
            SpouseOutput = standardTax
        else:
            SpouseOutput = progressiveTax

        return SpouseOutput


# calculate joint tax
def jointTax():
    SumOfJointTax = (SelfIncome + SpouseIncome)
    SumOfJointTax = SumOfJointTax - Allowance * 2 - SelfMPF - SpouseMPF
    if SumOfJointTax < 0:
        SumOfJointTax = 0
        return SumOfJointTax
    else:
        # progressive tax
        if SumOfJointTax <= 50000:
            progressiveTax = SumOfJointTax * 0.02

        elif 50000 < SumOfJointTax <= 100000:
            progressiveTax = float(SumOfJointTax - 50000) * 0.06 + 1000

        elif 100000 < SumOfJointTax <= 150000:
            progressiveTax = float(SumOfJointTax - 100000) * 0.1 + 4000

        elif 150000 < SumOfJointTax <= 200000:
            progressiveTax = float(SumOfJointTax - 150000) * 0.14 + 9000

        else:
            progressiveTax = float(SumOfJointTax - 200000) * 0.17 + 16000

        # standard tax calculate
        standardTax = (SelfIncome + SpouseIncome - SelfMPF - SpouseMPF) * 0.15

        # compare which one is lower
        if standardTax < progressiveTax:
            SumOfJointTax = standardTax
        else:
            SumOfJointTax = progressiveTax
        return SumOfJointTax

    # which paid tax method


def assessmentRecommend():
    if jointtax(SelfIncome, SpouseIncome) < selfSeparateTax() + spouseSeparateTax():
        print("e)Joint assessment contributes to lower tax rate, so it is recommended.")

    elif jointtax() == selfSeparateTax() + spouseSeparateTax():
        print("e)Both assessments are the same, so either of them are recommended.")

    else:
        print("e)Separate assessment contributes to lower tax rate, so it is recommended.")
    return ""


# main program
try:
    SelfIncome = float(input("input your Yearly personal income" + ':'))
except ValueError:
    print("Please enter NUMBER of your Yearly personal income. ")
    sys.exit(1)

if SelfIncome / 12 < 7100.0:
    SelfMPF = 0.0
elif 7100.0 < SelfIncome / 12 < 30000.0:
    SelfMPF = SelfIncome / 12 * 0.05
else:
    SelfMPF = 18000.0

print("a1)Your MPF mandatory contribution based on personal income are " + str(int(SelfMPF)) + ".")
print("a2)The salaries tax you should pay is " + str(int(selfSeparateTax())))
print(type(SelfMPF))

try:
    SpouseIncome = float(input("input your spouse Yearly personal income" + ':'))
except ValueError:
    print("Please enter NUMBER of your spouse Yearly personal income. ")
    sys.exit(1)

if SpouseIncome / 12 < 7100.0:
    SpouseMPF = 0.0
elif 7100.0 < SpouseIncome / 12 < 30000.0:
    SpouseMPF = SpouseIncome / 12 * 0.05
else:
    SpouseMPF = 18000.0

print("b1)Your spouse MPF mandatory contribution based on personal income are " + str(int(SpouseMPF)) + ".")
print("b2)The salaries tax your spouse should pay " + str(int(spouseSeparateTax())))
print("c)The salaries tax should be paid " + str(
    int(selfSeparateTax()) + int(spouseSeparateTax())) + " if separate assessment assumed.")
print("d)The salaries tax should be paid " + str(
    int(jointTax())) + " if joint assessment assumed.")
print(assessmentRecommend())
