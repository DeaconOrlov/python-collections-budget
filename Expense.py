import csv
import csv
from datetime import datetime
from datetime import datetime
class Expense():
class Expense():
    def __init__(self, date_str, vendor, category, amount):
    def __init__(self, date_str, vendor, category, amount):
        self.date_time = datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')
        self.date_time = datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')
        self.vendor = vendor
        self.vendor = vendor
        self.category = category
        self.category = category
        self.amount = amount
        self.amount = amount
class Expenses():
class Expenses():
    def __init__(self):
    def __init__(self):
        self.list = []
        self.list = []
        self.sum = 0
        self.sum = 0
    # Read in the December spending data, row[2] is the $$, and need to format $$
    # Read in the December spending data, row[2] is the $$, and need to format $$
    def read_expenses(self,filename):
    def read_expenses(self,filename):
        with open(filename, newline='') as csvfile:
        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
            for row in csvreader:
                if '-' not in row[3]:
                if '-' not in row[3]:
                    continue
                    continue
                amount = float((row[3][2:]).replace(',',''))
                amount = float((row[3][2:]).replace(',',''))
                self.list.append(Expense(row[0],row[1], row[2], amount))
                self.list.append(Expense(row[0],row[1], row[2], amount))
                self.sum += amount
                self.sum += amount


    def categorize_set_comprehension(self):
        necessary_expenses = {x for x in self.list 
                            if x.category == 'Phone' or x.category == 'Auto and Gas' or 
                                x.category == 'Classes'  or x.category == 'Utilities' or 
                                x.category == 'Mortgage'}

        food_expenses = {x for x in self.list 
                            if x.category == 'Groceries' or x.category == 'Eating Out'}

        unnecessary_expenses = set(self.list) - necessary_expenses - food_expenses

        return [necessary_expenses, food_expenses, unnecessary_expenses]


    def categorize_for_loop(self):
    def categorize_for_loop(self):
            necessary_expenses2 = set()
            necessary_expenses2 = set()
            food_expenses2 = set()
            food_expenses2 = set()
            unnecessary_expenses2 = set()
            unnecessary_expenses2 = set()
            for i in self.list:
            for i in self.list:
                if (i.category == 'Phone'      or i.category == 'Auto and Gas' or 
                if (i.category == 'Phone'      or i.category == 'Auto and Gas' or 
                    i.category == 'Classes'  or i.category == 'Utilities' or 
                    i.category == 'Classes'  or i.category == 'Utilities' or 
                    i.category == 'Mortgage'): 
                    i.category == 'Mortgage'): 
                    necessary_expenses2.add(i)
                    necessary_expenses2.add(i)
                elif(i.category == 'Groceries' or i.category == 'Eating Out'):
                elif(i.category == 'Groceries' or i.category == 'Eating Out'):
                    food_expenses2.add(i)
                    food_expenses2.add(i)
                else:
                else:
                    unnecessary_expenses2.add(i)
                    unnecessary_expenses2.add(i)
            
            
            return [necessary_expenses2, food_expenses2, unnecessary_expenses2]