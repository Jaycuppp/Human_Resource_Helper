# Reusable Exception Handlings
def CorrectHours(Hours, Days_Worked):
    while (Hours < 0):
        Hours = float(input(f'''Invalid Input.\nEnter Hours worked above 0 in the past {Days_Worked} days: '''))

def CorrectPay(Pay, Days_Worked):
    while (Pay < 0):
        Pay = float(input("Invalid Input.\nEnter a Payrate above 0"))

class HRTools():
    def Total_Pay(Standard_Work_Hours, Over_Time_Multiplier, Days_Worked):
        
        # California Tax Rate Thresholds based on Hourly Pay Rates in USD $
        Tax_Threshold_One = 5.72916667
        Tax_Threshold_Two = 23.2942708
        Tax_Threshold_Three = 49.6744792
        Tax_Threshold_Four = 94.84375
        Tax_Threshold_Five = 120.442708
        Tax_Threshold_Six = 310.106771
        
        # California Income Tax Bracket %s So Far for the Year of 2023
        Tax_Bracket_One = 0.10
        Tax_Bracket_Two = 0.12
        Tax_Bracket_Three = 0.22
        Tax_Bracket_Four = 0.24
        Tax_Bracket_Five = 0.32
        Tax_Bracket_Six = 0.35
        Tax_Bracket_Seven = 0.37

        
        # Getting The Correct Total Hours Worked
        Total_Hours_Worked = float(input(f"Enter Hours Worked In Past {Days_Worked} Days: "))
        
        try:
            CorrectHours(Total_Hours_Worked, Days_Worked)
                
        except TypeError and ValueError:
            CorrectHours(Total_Hours_Worked, Days_Worked)
        

        # Getting The Correct Payrate
        Pay_Rate = float(input("Enter Hourly Payrate: "))

        try:
            CorrectPay(Pay_Rate, Days_Worked)

        except UnboundLocalError and ValueError:
            CorrectPay(Pay_Rate, Days_Worked)
        
        
        # With Overtime Pay Calculation
        if Total_Hours_Worked > Standard_Work_Hours: 
            Overtime = Total_Hours_Worked - Standard_Work_Hours
            Regulartime = Total_Hours_Worked - Overtime 
            RegularPay = Regulartime * Pay_Rate
            OvertimePay = Overtime * Pay_Rate * Over_Time_Multiplier
            ActualPay = RegularPay + OvertimePay

        # No Overtime Pay Calculation
        elif Total_Hours_Worked <= Standard_Work_Hours:
            ActualPay = Total_Hours_Worked * Pay_Rate

        # Tax Brack 1 Condition
        if 0 < Pay_Rate <= Tax_Threshold_One:
            Income_Tax_Percentage = Tax_Bracket_One

        # Tax Bracket 2 Condition
        elif Tax_Threshold_One < Pay_Rate <= Tax_Threshold_Two :
            Income_Tax_Percentage = Tax_Bracket_Two

        # Tax Bracket 3 Condition
        elif Tax_Threshold_Two < Pay_Rate <= Tax_Threshold_Three:
            Income_Tax_Percentage = Tax_Bracket_Three
            
        # Tax Bracket 4 Condition   
        elif Tax_Threshold_Three < Pay_Rate <= Tax_Threshold_Four:
            Income_Tax_Percentage = Tax_Bracket_Four
            
        # Tax Bracket 5 Condition
        elif Tax_Threshold_Four < Pay_Rate <= Tax_Threshold_Five:
            Income_Tax_Percentage = Tax_Bracket_Five
            
        # Tax Bracket 6 Condition
        elif Tax_Threshold_Five < Pay_Rate <= Tax_Threshold_Six:
            Income_Tax_Percentage = Tax_Bracket_Six
            
        # Tax Bracket 7 Condition
        elif Tax_Threshold_Six < Pay_Rate:
            Income_Tax_Percentage = Tax_Bracket_Seven

        # Now Factoring In the Tax Rate
        Amount_Taxed = ActualPay * Income_Tax_Percentage
        Post_Tax_Pay = ActualPay - Amount_Taxed

        return print(f"Here is your paycheck amount for the past {Days_Worked} days Before Tax: ${ActualPay}\nHere is the total amount you are Taxed: ${Amount_Taxed}\nHere is the actual amount of money you can legally keep to yourself: ${Post_Tax_Pay}")


if __name__ == "__main__":
    # Standard Working Hour Vars
    Weekly_Hours = 40
    Bi_Weekly_Hours = 80

    # Multiplier for Overtime Pay Calculation
    Over_Time_Multiplier = 1.5

    # Total Amount of Days in terms of Weeks
    One_Week = 7
    Two_Weeks = 14

    Employee_Choice = str(input("Hello, Enter one of the following\n1) Paycheck Amount for past 1 Week of Work \n2) Paycheck Amount for past 2 Weeks of Work\n3) Quit the Program"))

    while Employee_Choice != "1" and Employee_Choice != "2":
        Employee_Choice = input("Sorry Invalid Choice. Please enter the numerical value for one of these choicses\n1) Paycheck Amount for past 1 Week of Work\n2) Paycheck Amount for past 2 Weeks of Work\n3) Quit the Program")

    if Employee_Choice == '1':
        Weekly_Pay_Amount = HRTools.Total_Pay(Weekly_Hours, Over_Time_Multiplier, One_Week)
        
    if Employee_Choice == '2':
        Bi_Weekly_Pay_Amount = HRTools.Total_Pay(Bi_Weekly_Hours, Over_Time_Multiplier, Two_Weeks)
            
    elif Employee_Choice == 'q' or Employee_Choice == 'Q':
            print("You exited the program. Have a Nice Day :) ")
