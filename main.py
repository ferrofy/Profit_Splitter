from Files import Actions
from Files import Functions
from Files import Animations

Total_Ways = ["ReSelling" , "Spend" , "Rewards" , "Loan" , "Check Balance" , "Exit"]
Len_Animation = 50

while True:
    print("Total Ways To Earn \n")
    for i in range(len(Total_Ways)):
        print(f"[{i + 1}] ---> {Total_Ways[i]}")
        
    Way = input("\nWhat Action You Want To Choose ---> ")

    print("\nLoading...\n")

    if Way == "1":
        print(Animations.UnderScore_Line(Len_Animation))
        Actions.ReSell()
        print(Animations.UnderScore_Line(Len_Animation))

    elif Way == "2":
        print(Animations.UnderScore_Line(Len_Animation))
        Actions.Spent()
        print(Animations.UnderScore_Line(Len_Animation))

    elif Way == "3":
        print(Animations.UnderScore_Line(Len_Animation))
        Actions.Rewards()
        print(Animations.UnderScore_Line(Len_Animation))

    elif Way == "4":
        print(Animations.UnderScore_Line(Len_Animation))
        Actions.Loan()
        print(Animations.UnderScore_Line(Len_Animation))

    elif Way == "5":
        print(Animations.UnderScore_Line(Len_Animation))
        Actions.Check_Balance()
        print(Animations.UnderScore_Line(Len_Animation))

    elif Way in ("Exit" , "6"):
        print(Animations.UnderScore_Line(Len_Animation))
        Actions.Exit()
        print(Animations.UnderScore_Line(Len_Animation))
        break

    else:
        print(Animations.UnderScore_Line(Len_Animation))
        print("Enter A Valid Way...")
        print(Animations.UnderScore_Line(Len_Animation))

Functions.Write_Conformation()