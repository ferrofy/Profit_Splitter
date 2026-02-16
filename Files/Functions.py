try:
    from Files.Data import Total_Savings
except ImportError:
    from Data import Total_Savings

Savings = Total_Savings.Data

Pos = [ 2 , 9 ]
File_Location = "Files/Data/Total_Savings.py"
Extra_Decimal = 0

# Calculate Profit
def Calculate_Profit(Buying_Price = 0 , Selling_Price = 0 , Quantity = 1):
    Profit = (Selling_Price - Buying_Price) * Quantity
    return Profit

# Will Give Titles Or Heading Of All Category As List
def All_Savings_Title():
    global Titles
    Titles = []
    for i in range(len(Savings)):
        Titles.append(Savings[i][0].rstrip())

# Will Calculate Total Money We Have
def Net_Worth():
    Net_Worth = 0
    for i in range(len(Savings)):
        Net_Worth += Savings[i][1]
        
    return round(Net_Worth , 2)

# Print All Things In Proper Manner
def Print_Savings_Proper_Style():
    Space_Pos = 0

    print("\n" + "=" * 10 , " Net Worth " , "=" * 10 , "\n")
    print(f"Your Net Worth ---> ₹" , Net_Worth() , "\n")

    print("=" * 10 , " Savings " , "=" * 10 , "\n")        
    for i in  range(len(Savings)):
        Space_Pos += 1
        if Space_Pos in Pos:
            if Savings[i][2] > 9:
                print(f"""{Savings[i][0]} [ {Savings[i][2]}% ] ---> ₹{Savings[i][1]}\n""")
            else:
                print(f"""{Savings[i][0]} [ {Savings[i][2]}%  ] ---> ₹{Savings[i][1]}\n""")
        else:
            if Savings[i][2] > 9:
                print(f"""{Savings[i][0]} [ {Savings[i][2]}% ] ---> ₹{Savings[i][1]}""")
            else:
                print(f"""{Savings[i][0]} [ {Savings[i][2]}%  ] ---> ₹{Savings[i][1]}""")

def Is_Decimal(Number):
    return Number % 1 != 0

# ! Add Profit To A Particular Category
def Add_To_Savings(Type , Profit):
    global Extra_Decimal
    for i in range(len(Savings)):
        if Type in Savings[i][0]:
            Prev_Amount = float(Savings[i][1])

            if Is_Decimal(Profit):
                Profit = (Profit / 100) * Savings[i][2]
                Profit = round(Profit , 4)
                Profit = str(Profit)
                List = Profit.split(".")
                Deci = List[1]
                if len(Deci) == 4:
                    Extra = Profit[-2:]
                    Profit = Profit[0:-2]
                    Extra = int(Extra)
                elif len(Deci) == 3:
                    Extra = Profit[-1:] + "0"
                    Profit = Profit[0:-1]
                    Extra = int(Extra)
                else:
                    Extra = 0
                    Extra = int(Extra)
                Profit = float(Profit)
                Profit = round(Profit , 2)
                Savings[i].pop(1)
                Savings[i].insert(1 , round(Prev_Amount + Profit , 2))
                Extra_Decimal += Extra
            else:
                Profit = (Profit / 100) * Savings[i][2]
                Profit = round(Profit , 2)
                Savings[i].pop(1)
                Savings[i].insert(1 , round(Prev_Amount + Profit , 2))

# Automatecally Add Profit According To % Given
def Auto_Add_To_Savings(Profit):
    global Extra_Decimal
    All_Savings_Title()
    for i in range(len(Titles)):
        Add_To_Savings(Titles[i] , Profit)
    Extra_Decimal = Extra_Decimal / 10000
    Prev_Amount = float(Savings[1][1])
    Savings[1].pop(1)
    Savings[1].insert(1 , round(Prev_Amount + Extra_Decimal , 2))

# Add Amount of Buying Price To Invest
def ReAdd_Amount_To_Invest(Buying_Price , Quantity):
    Prev_Amount = float(Savings[0][1])
    Savings[0].pop(1)
    Savings[0].insert(1 , (Buying_Price * Quantity) + Prev_Amount)

# Make Savings List to String
def Saving_List_To_String():
    Space_Pos = 0
    String_Mid = ""
    
    String_Starting = f'''Data = [

'''
    String_End ='''

]'''

    for i in range(len(Savings)):
        Space_Pos += 1
        if Space_Pos in Pos:
            String_Mid = String_Mid + f'\t["{Savings[i][0]}" , {round(Savings[i][1] , 4)} , {Savings[i][2]}],\n\n'
        else:
            String_Mid = String_Mid + f'\t["{Savings[i][0]}" , {round(Savings[i][1] , 4)} , {Savings[i][2]}],\n'
            


    String = String_Starting + String_Mid + String_End
    return String

# Update List
def Write_To_Savings():
    with open(File_Location, "w") as File:
        File.write(Saving_List_To_String())

# Will Give All Savings Of A Category As List
def All_Savings_Amount():
    global Money
    Money = []
    for i in range(len(Savings)):
        Money.append(Savings[i][1])

def Write_Conformation():
    while True:
        Conformation = input("\nFrom All Changes Want To Save Chnages [Y / N] ---> ").lower()
        if Conformation in ("y" , "yes"):
            Write_To_Savings()
            print("\nUpdated Your Savings List...\n")
            break
        elif Conformation  in ("n" , "no"):
            print("\nNo Problem , You Can Retry...\n")
            break
        else:
            print("\nEnter A Valid Input...")