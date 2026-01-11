import time
from datetime import datetime
import os
import json

menu = [("1. Add expense"),
        ("2. Show all expenses"),
        ("3. Show summary"),
        ("4. Delete expense"),
        ("5. Exit")]
categories = ["FOOD","TRANSPORT","ENTERTAINMENT","BILLS","SHOPPING","OTHER"]
expenses = []
path = ("E:\\Set-Up\\expense_tracker\\expenses_data.json")



def valid_int(prompt , min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"\n❌ Please enter a number ({min_value},{max_value}): ")
                time.sleep(2)
        except ValueError:
            print(f"\n❌ Please enter a number ({min_value},{max_value}): ")
            time.sleep(2)
def valid_string(prompt):
    while True:
        value = input((prompt)).upper().strip()
        if value.isalpha():
            return value
        else:
            print(f"\n❌ Please enter valid category name: ")
            time.sleep(2) 
def valid_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print(f"\n❌ Please enter a valid number!")
                time.sleep(2)
        except ValueError:
            print(f"\n❌ Please enter a valid number!")
            time.sleep(2)
def valid_date(prompt):
    while True:
        date = input(prompt).strip()
        formats = ["%Y-%m-%d","%Y/%m/%d"]
        for fmt in formats:
            try:
                date_obj = datetime.strptime(date,fmt)
                return date_obj.strftime("%Y/%m/%d")
            except ValueError:
                continue
        print(f"\n❌ Please enter a valid date!")
        time.sleep(2)
def valid_description(prompt):
    while True:
            description = input(prompt).strip()
            if description:
                return description
            else:
                print(f"\n❌ Please enter a valid description!")
def valid_2Way_quest(prompt,ans_1,ans_2):
    while True:
        try:
            value = input(prompt).upper().strip()
            if value == ans_1 or value == ans_2:
                return value
            else:
                print(f"\n❌ Please answer {(ans_1)} or {ans_2}: ")
                time.sleep(2)
        except ValueError:
            print(f"\n❌ Please answer {(ans_1)} or {ans_2}: ")
            time.sleep(2) 
                        
            
             

        
    
def choice_maker():
    for i in menu:
        print (i)
    print()
    choice = valid_int("Choose from above👆: ",1,5)
    return choice    
def category_meny(prompt,categories):
    print(prompt)
    for i, cat in enumerate(categories, start=1):
        print(f"{i}. {cat}")
    category_num = valid_int("Choose from above(1-6)👆: ",1,6)
    return categories[category_num - 1]    
def dict_maker(expense_list):
    amount = valid_amount("How much did you spend💸: ")
    category = category_meny("What did you spend them on💰: ",categories)
    date = valid_date("What's the date of the purchase📅: ")
    description = valid_description("The description of your expense(one-word-only)📝: ")
    expense =({"Amount:": amount,
               "Category:": category,
               "Date:": date,
               "Description:": description})
    expense_list.append(expense)
    return expense_list
def show_expenses(expense_list):
    if len(expense_list) == 0:
        print("No expenses yet!📦")
    else:
        for i, expense in enumerate(expense_list, start=1):
            print(
            f"{i}. "
            f"{expense['Date:']} | "
            f"{expense['Category:']} | "
            f"{expense['Amount:']}€ | "
            f"{expense['Description:']}")
def show_summary(expense_list,categories):
    if len(expense_list) == 0:
        print("No expenses yet!📦")
    else:
        total_expenses = 0
        sum_categories = {}
        for i in categories:
            sum_categories[i] = 0 
        for i in expense_list:
            total_expenses += i.get("Amount:")
            if i.get("Category:") in categories:
                sum_categories[i.get("Category:")] += i.get("Amount:")
        for key,value in sum_categories.items():
            if value > 0:
                print(key,value)            
        print(f"You have bought {len(expense_list)} products/services!💰")
        print(f"Yor expenses summary is: {total_expenses}$")
def delete_expense(expense_list):
    if len(expense_list) == 0:
        print("No expenses yet!📦")
    else:
        while True:
            show_expenses(expense_list)
            selected_exp = valid_int("What do you want to delete💔: ",1,len(expense_list))
            safety_q = valid_2Way_quest("Are you sure you want to delete this? (YES✅/NO❌)", "YES", "NO")
            if safety_q == "YES":
                discards = expense_list.pop(selected_exp-1)
                print("Succesfully deleted from the store!🚫")
            if len(expense_list) > 0:      
                answer = valid_2Way_quest("Do you wish to delete more? (YES✅/NO❌): ", "YES", "NO")
            else:
                print("No more products inside the store!⛔")
                break
            if answer == "NO":
                print("As you wish! 🫸")
                print(20*("___"))
                break
def load_expenses():
    try:
        with open(path,"r") as f:
            data = json.load(f)
            print("All previous purchases have been loaded!▶️")
            return data   
    except (FileNotFoundError, json.JSONDecodeError):
        print("No expense_list have been made before!🆕🆕")
        return []  
def save_expenses(expense_list):
    try:
        with open(path,"w") as f:
            json.dump(expense_list, f, indent=4)
            print("Progress saved!📁")
    except Exception as e:
        print(f"❌ Error saving file: {e}")
def exit_programm(expense_list):
    save = valid_2Way_quest("Save before exit? (YES✅/NO❌): ", "YES", "NO")
    if save == "YES":
        save_expenses(expense_list)
        print("Thanks for using 🙏👋")
        print(20*("___"))
    else:
        print("Thanks for using 🙏👋")
        print(20*("___"))
        
        



expenses = load_expenses()
while True:
    print(20*("___"))
    choice = choice_maker()
    print(20*("__"))
    if choice == 1:
        expenses = dict_maker(expenses)
    if choice == 2:
        show_expenses(expenses)
    if choice == 3:
        show_summary(expenses,categories)
    if choice == 4:
        delete_expense(expenses)
    if choice == 5:
        exit_programm(expenses)
        break

