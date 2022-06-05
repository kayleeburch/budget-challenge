import csv
from nis import cat
class Expenses:
    
    def __init__(self):
        get_expenses = Expenses.total_category_amounts()
        self.auto = get_expenses['Auto']
        self.house = get_expenses['House']
        self.food = get_expenses['Food']
        self.saving = get_expenses['Savings']
        self.leisure = get_expenses['Leisure']
        
        
    
    def add_expenses(self, category, amount):
        with open('expenses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([category, amount]) 
        file.close()
        
    def total_category_amounts():
        dict = {'Auto': 0, 'House': 0, 'Food': 0, 'Savings': 0, 'Leisure': 0}
        with open('expenses.csv', newline='') as f:
            expense_reader = csv.reader(f, delimiter=' ')
            next(f)
            for row in expense_reader:
                new_row = row[0].split(',')
                dict[new_row[0]] += int(new_row[1])
        f.close()
        return dict
    
    def percentage_breakdown(self):
        total_expense = self.auto + self.house + self.food + self.saving + self.leisure
        print(f"\n---PERCENTAGE BREAKDOWN---\nAuto: {100 * round(self.auto / total_expense, 2)}%\nFood: {100 * round(self.food / total_expense, 2)}%\nLeisure: {100 * round(self.leisure / total_expense, 2)}%\nHouse: {100 * round(self.house / total_expense, 2)}%\nSavings: {100 * round(self.saving / total_expense, 2)}")
        
    
    def print_category_amounts(self):
        print(f"\n---MONTHLY EXPENSES---\nAuto: {self.auto}\nHouse: {self.house}\nFood: {self.food}\nSavings: {self.saving}\nLeisure: {self.leisure}\n")
        
    
    
