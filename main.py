from Files import Actions
from Files import Functions

Total_Ways = ["ReSelling" , "Spend" , "Rewards" , "Loan" , "Check Balance" , "Exit"]

while True:
    print("Total Ways To Earn \n")
    for i in range(len(Total_Ways)):
        print(f"[{i + 1}] ---> {Total_Ways[i]}")
        
    Way = input("\nWhat Action You Want To Choose ---> ")

    print("\nLoading...\n")

    if Way == "1":
        pass
        Actions.ReSell()
    elif Way == "2":
        Actions.Spent()
    elif Way == "3":
        Actions.Rewards()
    elif Way == "4":
        Actions.Loan()
    elif Way == "5":
        Actions.Check_Balance()
    elif Way == "Exit":
        Actions.Exit()
        break
    else:
        print("Enter A Valid Way...")

Functions.Write_Conformation()