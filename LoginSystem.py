import getpass
import mariadb

PURPLE = '\033[0;35m' 
RED = "\33[91m"
END = "\033[0m"
bannar = f"""
    {PURPLE}

    ___     __    __           __                      _ 
   /   |   / /   / /  ____    / /_   ____ _   ____    (_)
  / /| |  / /   / /  / __ \  / __ \ / __ `/  / __ \  / / 
 / ___ | / /   / /  / /_/ / / /_/ // /_/ /  / / / / / /  
/_/  |_|/_/   /_/   \____/ /_.___/ \__,_/  /_/ /_/ /_/  
        {END}
"""

print(bannar)

def connect_to_db():
    return mariadb.connect(
        user="", password="", host="", database=""  # add your user , password , host and database
    )


def register(username, password, is_admin=False):
    try:
        db = connect_to_db()
        cursor = db.cursor() 
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            print("Username already exists.")
            return False

        cursor.execute(
            "INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)",
            (username, password, is_admin),
        )
        db.commit()
        print("Registration successful.")
        return True

    except mariadb.Error as err:
        print("Error:", err)
        return False

    finally:
        cursor.close()
        db.close()


def login(username, password):
    try:
        db = connect_to_db()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password))
        user = cursor.fetchone()

        if user:
            print("username : ", user[1]) 
            print("Login successful.")
            return user
        else:
            print("Invalid username or password.: ", user)
            return None

    except mariadb.Error as err:
        print("Error:", err)
        return None

    finally:
        cursor.close()
        db.close()


def main():
    print("Welcome to the login system.")

    while True:
        choice = input("Choose an option: \n1. Register\n2. Login\n3. Exit\n")

        if choice == "1":
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            is_admin = input("Are you an admin? (yes/no): ").lower() == "yes"
            register(username, password, is_admin)

        elif choice == "2":
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            user = login(username, password)
            if user:
                if user[3]:
                    print(f"{RED}Welcome, admin!{END}")
                    break
                else:
                    print("Welcome, user!")
                    break
            else:
                print("Login failed.")

        elif choice == "3":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
