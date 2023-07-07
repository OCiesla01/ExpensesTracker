import pymysql
from dotenv import load_dotenv
import os
from datetime import datetime

from programMethods import *

load_dotenv()

connection = pymysql.connect(
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    host='localhost',
    database='expenses_tracker'
)

cursor = connection.cursor()



while True:
    choice = int(getBasicInfo())
    if choice == 1:
        income = addNewIncome()
        if income[5]:
            add_new_income_query = "INSERT INTO income (name, amount, category, date_time, month_id) " \
                                   f" VALUES ('{income[0]}', {income[1]}, '{income[2]}', '{income[3]}', {income[4]})"
            cursor.execute(add_new_income_query)
            connection.commit()
            print("New income has been successfully added to database.")
        else:
            print(income[6])

    elif choice == 2:
        expense = addNewExpense()
        if expense[6]:
            add_new_expense_query = "INSERT INTO expenses (name, amount, category, date_time, month_id, note) " \
                                    f" VALUES ('{expense[0]}', {expense[1]}, '{expense[2]}', '{expense[3]}', {expense[4]}," \
                                    f" '{expense[5]}')"
            cursor.execute(add_new_expense_query)
            connection.commit()
            print("New expense has been successfully added to database.")
        else:
            print(expense[7])

    elif choice == 3:
        all_income_query = "SELECT * FROM income"
        all_expenses_query = "SELECT * FROM expenses"
        sum_income = 0
        sum_expenses = 0

        cursor.execute(all_income_query)
        for i in cursor:
            sum_income += i[2]

        cursor.execute(all_expenses_query)
        for i in cursor:
            sum_expenses += i[2]

        balance = sum_income - sum_expenses
        print(f"Current balance: {balance}$")

    elif choice == 4:
        month = input("Enter month name or id: ")
        month_id = checkForMonth(month)

        if month_id is not None:
            all_income_by_month_query = "SELECT * FROM income" \
                                        f" WHERE month_id = {month_id}"
            all_expenses_by_month_query = "SELECT * FROM expenses" \
                                          f" WHERE month_id = {month_id}"
            sum_income = 0
            sum_expenses = 0
            cursor.execute(all_income_by_month_query)

            for i in cursor:
                sum_income += i[2]

            cursor.execute(all_expenses_by_month_query)

            for i in cursor:
                sum_expenses += i[2]

            balance = sum_income - sum_expenses
            print(f"{getMonth(int(month_id))}'s balance: {balance}$")

    elif choice == 5:
        month = input("Enter month name or id: ")
        month_id = checkForMonth(month)

        if month_id is not None:
            all_income_by_month_query = "SELECT * FROM income" \
                                        f" WHERE month_id = {month_id}"
            sum_income = 0
            cursor.execute(all_income_by_month_query)

            for i in cursor:
                sum_income += i[2]
                print(f"Transaction ID: {i[0]}\n"
                      f"Transaction name: {i[1]}\n"
                      f"Transaction amount: {i[2]}\n"
                      f"Transaction category: {i[3]}\n"
                      f"Transaction date & time: {i[4]}\n")

            print(f"{getMonth(int(month_id))}'s total income: {sum_income}$")

    elif choice == 6:
        month = input("Enter month name or id: ")
        month_id = checkForMonth(month)

        if month_id is not None:
            all_expenses_by_month_query = "SELECT * FROM expenses" \
                                        f" WHERE month_id = {month_id}"
            sum_expenses = 0
            cursor.execute(all_expenses_by_month_query)

            for i in cursor:
                sum_expenses += i[2]
                print(f"Transaction ID: {i[0]}\n"
                      f"Transaction name: {i[1]}\n"
                      f"Transaction amount: {i[2]}\n"
                      f"Transaction category: {i[3]}\n"
                      f"Transaction date & time: {i[4]}\n"
                      f"Transaction note: {i[6]}\n")

            print(f"{getMonth(int(month_id))}'s total expenses: {sum_expenses}$")

    elif choice == 7:
        category = str(input("Enter income category: "))
        all_income_by_category_query = "SELECT * FROM income" \
                                       f" WHERE category = '{category}'"
        sum_income = 0
        cursor.execute(all_income_by_category_query)

        for i in cursor:
            sum_income += i[2]

        print(f"Total income by category - {category}: {sum_income}$")

    elif choice == 8:
        category = str(input("Enter income category: "))
        all_expenses_by_category_query = "SELECT * FROM expenses" \
                                       f" WHERE category = '{category}'"
        sum_expenses = 0
        cursor.execute(all_expenses_by_category_query)

        for i in cursor:
            sum_expenses += i[2]

        print(f"Total expenses by category - {category}: {sum_expenses}$")
    elif choice == 9:
        break
    else:
        print("Invalid input. Try again.")

connection.close()
cursor.close()
