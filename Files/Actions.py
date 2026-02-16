try:
    from Files.Data import Total_Savings
    from Files import Functions
except ImportError:
    from Data import Total_Savings
    import Functions

Savings = Total_Savings.Data

def ReSell():
    Buying_Price = float(input("Enter Your Buying Price ---> ₹"))
    Selling_Price = float(input("Enter Your Selling Price ---> ₹"))
    Quantity = float(input("Enter Your Quantity ---> "))
    Profit = Functions.Calculate_Profit(Buying_Price , Selling_Price , Quantity)
    Profit = round(Profit , 2)

    print(f"Your Profit ---> ₹{Profit} ")

    Functions.ReAdd_Amount_To_Invest(Buying_Price , Quantity)
    Functions.Auto_Add_To_Savings(Profit)

def Spent():
    Functions.All_Savings_Title()
    print("In Which Category You Spent Money...\n")
    for i in range(len(Functions.Titles)):
        print(f"[{i+1}] ---> {Functions.Titles[i]}")
        
    Spent_Category = int(input("\nIn Which Category You Spent ---> "))
    Spent_Amount = float(input("How Much Amount You Spent ---> "))
    if Spent_Category >= 1 and Spent_Category <= len(Functions.Titles):
        
        Index = Spent_Category - 1
        Prev_Amount = float(Savings[Index][1])
        Savings[Index][1] = Prev_Amount - Spent_Amount
        
        Functions.Write_To_Savings()
    else:
        print("Enter A Valid Number...")

def Rewards():
    Amount = float(input("What Was The Amount For Your Reward ---> "))
    Functions.Auto_Add_To_Savings(Amount)

def Loan():
    Loan_Amount = float(input("What Was Loan Amount You Got ---> "))
    Invest_Amount = (Loan_Amount * 75) / 100
    ReAdd = Loan_Amount - Invest_Amount
    Functions.ReAdd_Amount_To_Invest(Invest_Amount , 1)
    Functions.Auto_Add_To_Savings(ReAdd)

def Check_Balance():
    Functions.Print_Savings_Proper_Style()

def Exit():
    print("Exiting...")