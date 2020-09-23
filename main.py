# Nedbank Loan Calculator
print("---Welcome To Nedbank Loan Console Calculator---")

loan_amount = int(input("Please enter loan amount: "))
interest_rate = float(input("Please enter your interest rate without a percentage sign: "))
_number_of_months = 12  # how long it would take you to repay the loan.

total_repayment = loan_amount + (loan_amount * interest_rate)
monthly_installment = total_repayment / _number_of_months



if interest_rate <7:
    print("The interest rate is less than seven")
if interest_rate >24.5:
    print("The interest rate is greater than 24.5")
else : print(total_repayment)


print('Total Repayment: ', total_repayment)
print("Monthly installment: ", monthly_installment)
print("Please go to the nearest nedbank branch with you bank statement, ID and proof  of residence.")


int(1011)
