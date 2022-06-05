import csv
class Income:
    
    def __init__(self):
        pass
    
    def update_monthly_income(self, new_amount):
        with open("monthlyIncome.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([new_amount])
        f.close()