import math
def investment_calculator():
    p = float(input("Enter the amount of money you're depositing : "))
    r = float (input("Enter the interest rate for the year : ")) /100
    t = int(input("Enter the amount of year, you would like the interest for : "))
    interest_type = input("Enter 'simple' or 'compound' interest : ").lower()

    if interest_type == "simple":
        A = p * (1+(r*t))
    elif interest_type == "compound":
        A = p * math.pow(1+(r),t)
    else:
        print("Invalid Interest type. Please enter 'simple' or 'compound',")
        return
    print(f"\n The final amount after {t} years is: {A:.2f}")

def bond_repayment_calculator():
    p= float(input("Enter the present value of the house : "))
    r=float(input("Enter thr annual interest rate(as a percentage): ")) /100
    n=int(input("Enter the number of years for repayment : "))

    i = r / 12
    monthly_payments = (i *p) / (1+i)**(-n)
    print(f"\n The monthly repayment amount is : {monthly_payments:.2f}")

def main():
        print("Welcome to the Finance Calculator App")
        print(f"\nInvestment - to calculate the amount of interest you'll earn on your investment")
        print(f"\nBond- to calculate the amount you'll have to pay on home loan")
        choice = input(f"\nEnter 'investment' for investment calculator or 'bond' for Bond repayment calculator : ").lower()
        if choice == "investment":
            investment_calculator()
        elif choice == "bond":
            bond_repayment_calculator()
        else:
            print("Invalid Choice. Please enter 'Investment' or 'Bond' .")

main()
