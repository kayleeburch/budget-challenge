from classes.monthly_income import Income
from classes.expenses import Expenses

def main():
    new_expense = Expenses()
    new_income = Income()
    mode = input("\nWhat would you like to do?\nOptions:\n1.Add expense(add category + expense cost)\n2.update monthly income (update csv file)\n3.view monthly expenses \n4.expense breakdown(show percentage of all categories)\n5.Quit\n")
    if mode == '1':
        enter_category = input("\nPlease select a category\nOptions:\n1.House\n2.Food\n3.Auto\n4.Savings\n5.Leisure\n")
        if enter_category == '1':
            enter_category = 'House'
        elif enter_category == '2':
            enter_category = 'Food'
        elif enter_category == '3':
            enter_category = 'Auto'
        elif enter_category == '4':
            enter_category = 'Savings'
        elif enter_category == '5':
            enter_category = 'Leisure'
        else:
            main()
        enter_amount = input("\nPlease enter amount:\n")
        new_expense.add_expenses(enter_category, enter_amount)
        main()
    elif mode == '2':
        new_monthly_amount = input("\nPlease enter amount:\n")
        new_income.update_monthly_income(new_monthly_amount)
        main()
    elif mode == '3':
        new_expense.print_category_amounts()
        main()
    elif mode == '4':
        new_expense.percentage_breakdown()
        main() 
    elif mode == '5':
        return
    else:
        print('Incorrect entry, please try again.')
        main()
    
    
    
if __name__ == '__main__':
    main()