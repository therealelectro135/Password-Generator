# Import Modules

import random
import string
import time
from termcolor import colored
import pyfiglet
from colorama import Fore
import sqlite3
from datetime import datetime

# Variables

password_length = ""
colored_length = ""
username = ""
colored_username = ""
n_y_or_n = ""
sc_y_or_n = ""
yes_or_no = ""
add_to_db_y_or_n = ""
characters_type_num = ""
separator = "#" * 70
pass_structure = ""
password = ""
colored_password = ""
website = ""
colored_website = ""
website_y_or_n = ""
db_update_y_or_no = ""
show_y_or_no = ""
# Functions


def live_typing(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print("")


def db_commit_and_close():
    db.commit()
    db.close()


def yes_no_check(yornovar):
    while yornovar != "Y" and yornovar != "N":
        live_typing("Please Enter Y/N :")
        yornovar = input().strip().capitalize()
        print("")


# Password Generation Functions
def reg_pass(pass_length):
    pass_structure = string.ascii_uppercase + string.ascii_lowercase
    password = "".join(random.choice(pass_structure) for _ in range(pass_length))
    return password


def pass_with_num(pass_length):
    pass_structure = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = "".join(random.choice(pass_structure) for _ in range(pass_length))
    return password


def pass_with_sc(pass_length):
    pass_structure = (
        string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    )
    password = "".join(random.choice(pass_structure) for _ in range(pass_length))
    return password


def pass_with_everything(pass_length):
    pass_structure = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.punctuation
        + string.digits
    )
    password = "".join(random.choice(pass_structure) for _ in range(pass_length))
    return password


# Date And Time

current_datetime = datetime.now()

formatted_date = current_datetime.strftime("%d/%b/%Y")

formatted_time = current_datetime.strftime("%I:%M")


# # Welcome
time.sleep(0.5)
print(f"{Fore.CYAN}", pyfiglet.figlet_format("Password Generator"), f"{Fore.RESET}")
time.sleep(1)


live_typing("Hello There...", 0.05)
time.sleep(1)
live_typing("Here You Are, So You Want To Generate A Strong Password.", 0.05)
time.sleep(1)
live_typing("Let Me Help You :)", 0.05)
print("")
time.sleep(1)
print(colored(separator, "yellow"))
print("")
time.sleep(1)

live_typing("What Is Your Name ??", 0.02)
username = input().strip().capitalize()
colored_username = username
colored_username = colored(colored_username, "magenta")

print("")
time.sleep(1)
print(colored(separator, "yellow"))
print("")
time.sleep(1)

live_typing(
    f"Hi {colored_username}, Enter The Password Length [The Minimum Length Should Be 8]: ",
    0.02,
)
password_length = input().strip()
print("")


while 1:
    try:
        password_length = int(password_length)
        if password_length < 8:
            live_typing(
                "The Length Must Be 8 Or Greater, Please Enter Another Length: "
            )
            password_length = input().strip()
            print("")

        else:
            break
    except:
        live_typing(f"Sorry {colored_username}, Please Enter A Valid Number: ")
        password_length = input().strip()
        print("")


colored_length = password_length
colored_length = colored(colored_length, "blue")
live_typing(f"Now You Need {colored_length}-Characters Password, Is That Right ? [Y/N]")
yes_or_no = input().strip().capitalize()
print("")

while yes_or_no != "Y" and yes_or_no != "N":
    live_typing("Please Enter Y/N :")
    yes_or_no = input().strip().capitalize()
    print("")

while 1:
    if yes_or_no == "N":
        live_typing("Sorry, Please Try Again: ")
        password_length = input().strip()
        print("")
        colored_length = password_length
        colored_length = colored(colored_length, "blue")
        while True:
            try:
                password_length = int(password_length)
                if password_length < 8:
                    live_typing(
                        "The Length Must Be 8 Or Greater , Please Enter Another Length: "
                    )
                    password_length = input().strip()
                    print("")
                    colored_length = password_length
                    colored_length = colored(colored_length, "blue")

                else:
                    break
            except ValueError:
                live_typing(
                    f'Sorry "{colored_username}", Please Enter A Valid Number: '
                )
                password_length = input().strip()
                print("")
                colored_length = password_length
                colored_length = colored(colored_length, "blue")
        live_typing(
            f"Now You Need {colored_length}-Characters Password, Is That Right ? [Y/N]"
        )
        yes_or_no = input().strip().capitalize()
        print("")

        while yes_or_no != "Y" and yes_or_no != "N":
            live_typing("Please Enter Y/N :")
            yes_or_no = input().strip().capitalize()
            print("")

    elif yes_or_no == "Y":
        break
live_typing(f"OK, You Want {colored_length}-Characters Password")
time.sleep(1)
live_typing("Now, Password Must Be Contain Uppercase And Lowercase Characters, But ...")
time.sleep(1)
live_typing("Do You Need Numbers ? [Y/N]")
n_y_or_n = input().strip().capitalize()
print("")


while n_y_or_n != "Y" and n_y_or_n != "N":
    live_typing("Please Enter Y/N :")
    n_y_or_n = input().strip().capitalize()
    print("")


live_typing("Do You Need Special Characters ? [Y/N]")
sc_y_or_n = input().strip().capitalize()
print("")


while sc_y_or_n != "Y" and sc_y_or_n != "N":
    live_typing("Please Enter Y/N :")
    sc_y_or_n = input().strip().capitalize()
    print("")


time.sleep(1)

print("Please Wait ...")
print("")
separator = colored(separator, "yellow")
live_typing(separator, 0.1)
print("")


# Password Condition
if n_y_or_n == "N" and sc_y_or_n == "N":
    password = reg_pass(password_length)

elif n_y_or_n == "Y" and sc_y_or_n == "N":
    password = pass_with_num(password_length)

elif n_y_or_n == "N" and sc_y_or_n == "Y":
    password = pass_with_sc(password_length)

elif n_y_or_n == "Y" and sc_y_or_n == "Y":
    password = pass_with_everything(password_length)

# Printing The Password
colored_password = password
colored_password = colored(colored_password, "green", attrs=["bold"])

print(colored("This Is Your Password: ", "red"))
live_typing(colored_password, 0.1)
print("")

# Adding To Database
live_typing("Do You Want To Add It To Your Database ? [Y/N]")
add_to_db_y_or_n = input().strip().capitalize()
print("")

while add_to_db_y_or_n != "Y" and add_to_db_y_or_n != "N":
    live_typing("Please Enter Y/N :")
    add_to_db_y_or_n = input().strip().capitalize()
    print("")


if add_to_db_y_or_n == "Y":
    # Create To Database
    db = sqlite3.connect("app.db")
    cur = db.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Passwords (Name TEXT , Website TEXT , Password TEXT , Date TEXT , Time TEXT)"
    )
    live_typing("What Is The Name Of The Site For Which You Generated The Password? ")
    website = input().strip().capitalize()

    while True:
        if len(website) < 1:
            live_typing("Please Enter A Valid Website Name: ")
            website = input().strip().capitalize()
        else:
            break

    colored_website = website
    colored_website = colored(colored_website, "cyan")
    print("")
    live_typing(
        f"OK {colored_username}, Your Website Is {colored_website}, Is That Right ? [Y/N]"
    )
    website_y_or_n = input().capitalize()
    print("")

    while website_y_or_n != "Y" and website_y_or_n != "N":
        live_typing("Please Enter Y/N :")
        website_y_or_n = input().strip().capitalize()
        print("")

    while True:
        if website_y_or_n == "N":
            live_typing("Please Try Again Enter Your Site Name:")
            website = input().strip().capitalize()
            print("")
            colored_website = website
            colored_website = colored(colored_website, "cyan")
            live_typing(
                f"OK {colored_username}, Your Website Is {colored_website}, Is That Right ? [Y/N]"
            )
            website_y_or_n = input().capitalize()
            print("")

            while website_y_or_n != "Y" and website_y_or_n != "N":
                live_typing("Please Enter Y/N :")
                website_y_or_n = input().strip().capitalize()
                print("")

        elif website_y_or_n == "Y":
            break
    # Database Check And Insert
    cur.execute(
        f"SELECT Website FROM Passwords WHERE Website = '{website}' and Name = '{username}'"
    )
    result = cur.fetchone()

    if result != None:
        live_typing("Sorry, This Website Already Has A Password In Database")
        live_typing(f"Do You Want To Update {colored_website} Password ? [Y/N]")
        db_update_y_or_no = input().strip().capitalize()
        print("")
        while db_update_y_or_no != "Y" and db_update_y_or_no != "N":
            live_typing("Please Enter Y/N :")
            db_update_y_or_no = input().strip().capitalize()
            print("")
        if db_update_y_or_no == "Y":
            cur.execute(
                f"UPDATE Passwords SET Password = '{password}' , Date = '{formatted_date}' , Time = '{formatted_time}' WHERE Name = '{username}' and Website = '{website}' "
            )
            live_typing("Password Updated")
            print("")
        elif db_update_y_or_no == "N":
            live_typing("The Database Has Not Been Updated")

    else:
        # Insert To Database
        cur.execute(
            f"INSERT INTO Passwords values('{username}' , '{website}' , '{password}' , '{formatted_date}' , '{formatted_time}')"
        )
        live_typing(
            f'OK {colored_username}, You Added "{colored_password}" As A Password For {colored_website} Website To The Database'
        )
    print("")
    live_typing("Do You Want To Show What Is In Database ? [Y/N]")
    show_y_or_no = input().strip().capitalize()

    while show_y_or_no != "Y" and show_y_or_no != "N":
        live_typing("Please Enter Y/N :")
        show_y_or_no = input().strip().capitalize()
        print("")

    time.sleep(1)
    print("")
    print(colored(separator, "yellow"))
    print("")
    time.sleep(1)

    if show_y_or_no == "Y":
        cur.execute(f"SELECT * FROM Passwords WHERE Name = '{username}'")
        result = cur.fetchall()
        if len(result) == 1:
            pass_label = colored(" - You Have One Password", "red")
            live_typing(pass_label)
            print("")
        elif len(result) > 1:
            pass_label = colored(f" - You Have {len(result)} Passwords", "red")
            live_typing(pass_label)
            print("")

        for row in result:
            arrow = colored("==>", "red")
            colored_website = colored(row[1], "cyan")
            colored_password = colored(row[2], "green")
            live_typing(f" ---- {colored_website} {arrow} {colored_password}")
    else:
        live_typing(f"OK {colored_username}, I Will Not Show Your Passwords ;)")
    db_commit_and_close()
elif add_to_db_y_or_n == "N":
    live_typing("Nothing Added To Database")

time.sleep(1)
print("")
print(colored(separator, "yellow"))
print("")
time.sleep(1)
live_typing("Thanks For Using Password Generator :)")
time.sleep(1)
print("")
live_typing(f"Goodbye {colored_username} ^_^")
time.sleep(1)
