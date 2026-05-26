from modules.login import login
from modules.booking import book
from modules.captcha_solver import solve_captcha
from modules.scheduler import schedule_appointment


def main():
    print("Almaviva Bot - simple scaffold")
    while True:
        print("\n1) Login\n2) Book appointment\n3) Solve captcha\n4) Schedule appointment\n5) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            user = login(username, password)
            print("Logged in:", user)
        elif choice == "2":
            user_id = input("User ID: ")
            data = input("Appointment data: ")
            result = book(user_id, data)
            print("Booking result:", result)
        elif choice == "3":
            path = input("Captcha image path: ")
            solved = solve_captcha(path)
            print("Solved:", solved)
        elif choice == "4":
            user_id = input("User ID: ")
            when = input("Datetime (ISO): ")
            res = schedule_appointment(user_id, when)
            print("Scheduled:", res)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid option")

if __name__ == '__main__':
    main()
