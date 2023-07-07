from datetime import datetime


def getBasicInfo():
    choice = input("""\t1. Add new income
    2. Add new expense
    3. Check current balance (income - expenses)
    4. Check specific month's balance
    5. Check specific month's income data
    6. Check specific month's expenses data
    7. Check total income by category
    8. Check total expenses by category
    9. Exit the program
    Choose an option (int): """)
    return choice


def addNewIncome():
    is_correct = True
    info = "New income was not added due to:"
    arr = []
    month_id = None
    amount = None

    name = str(input("Enter income name [str]: "))
    try:
        amount = int(input("Enter income amount [int]: "))
    except ValueError:
        info += "\nIncorrect datatype for amount."
        is_correct = False
    category = str(input("Enter income category [str]: "))
    datetime_str = str(input("Enter date & time of income (YYYY-MM-DD HH:MM:SS) or leave blank to add current date % "
                             "time [str]: "))
    if datetime_str == "":
        datetime_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if checkIfDateTimeIsValid(datetime_str):
        month_id = int(datetime_str[5:7])
    else:
        info += "\nIncorrect pattern for datetime field."
        is_correct = False

    arr.append(name)
    arr.append(amount)
    arr.append(category)
    arr.append(datetime_str)
    arr.append(month_id)
    arr.append(is_correct)
    arr.append(info)
    return arr


def addNewExpense():
    arr = addNewIncome()
    note = str(input("Enter note (optional) [str]: "))
    arr.insert(5, note)

    return arr


def getMonth(month):
    months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
              "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

    if isinstance(month, int):
        for name, month_id in months.items():
            if month_id == month:
                return name

    elif isinstance(month, str):
        month_id = months.get(month)
        return month_id


def checkForMonth(month):
    month_id = None

    if len(month) > 2:
        if getMonth(month.capitalize()) is not None:
            month_id = getMonth(month.capitalize())
        else:
            print("Incorrect month name input.")
    elif 2 >= len(month) > 0 and 1 <= int(month) <= 12:
        month_id = month
    else:
        print("Month with this ID does not exist.")

    return month_id


def checkIfDateTimeIsValid(datetime_str):
    try:
        datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False
