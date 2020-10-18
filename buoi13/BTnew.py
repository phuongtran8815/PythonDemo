from datetime import datetime
id=int(input("Please enter your ID: "))
amountMoney=int(input("Please enter the amount of money you'd like to borrow from the bank: "))
loanDate=str(input("Please enter the date you have requested the loan : "))
numberOfMonth=int(input("Please enter the number of month you expect to repay the loan:"))
adjLoanDate=datetime.strptime(loanDate, '%Y-%m-%d').date()
nowDate=datetime.now().date()
loanTerm=(nowDate-adjLoanDate).days
try:
    interest = (loanTerm* amountMoney * 0.17)/(numberOfMonth)
    print(interest)
except ArithmeticError:
    print("Please renter the number of month:")




