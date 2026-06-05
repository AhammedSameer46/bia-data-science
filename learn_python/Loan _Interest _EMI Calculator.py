def simple_interest():
    p = float(input("Enter Principal Amount: "))
    r = float(input("Enter Rate of Interest (%): "))
    t = float(input("Enter Time (years): "))

    si = (p * r * t) / 100
    print("Simple Interest =", si)


def compound_interest():
    p = float(input("Enter Principal Amount: "))
    r = float(input("Enter Rate of Interest (%): "))
    t = float(input("Enter Time (years): "))

    ci = p * ((1 + r / 100) ** t) - p
    print("Compound Interest =", round(ci, 2))


def emi_calculation():
    p = float(input("Enter Loan Amount: "))
    annual_rate = float(input("Enter Annual Interest Rate (%): "))
    years = int(input("Enter Loan Period (Years): "))

    r = annual_rate / (12 * 100)
    n = years * 12

    emi = (p * r * (1 + r) ** n) / (((1 + r) ** n) - 1)

    print("Monthly EMI =", round(emi, 2))


while True:

    print("\nLoan Interest & EMI Calculator")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. EMI Calculation")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        simple_interest()

    elif choice == "2":
        compound_interest()

    elif choice == "3":
        emi_calculation()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid Choice")