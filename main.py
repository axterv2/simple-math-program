import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# loader
def display_menu():
    print("""
 █████╗ ██╗  ██╗████████╗███████╗██████╗ 
██╔══██╗╚██╗██╔╝╚══██╔══╝██╔════╝██╔══██╗
███████║ ╚███╔╝    ██║   █████╗  ██████╔╝
██╔══██║ ██╔██╗    ██║   ██╔══╝  ██╔══██╗
██║  ██║██╔╝ ██╗   ██║   ███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    """)

    print("[!] Welcome to the Simple Math Program loader.")
    print("[1] Load the program")
    print("[2] Info")
    print("[3] Exit")


def loading_animation():
    print("[!] Loading", end="", flush=True)
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    time.sleep(1)
    clear_console()

def display_info():
    clear_console()
    print("""
 █████╗ ██╗  ██╗████████╗███████╗██████╗ 
██╔══██╗╚██╗██╔╝╚══██╔══╝██╔════╝██╔══██╗
███████║ ╚███╔╝    ██║   █████╗  ██████╔╝
██╔══██║ ██╔██╗    ██║   ██╔══╝  ██╔══██╗
██║  ██║██╔╝ ██╗   ██║   ███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    """)
    print("[!] Made by Axter - https://github.com/axterv2/simple-math-program")
    input("\n[!] Press Enter to return to the main menu.")

# math program
def run_math_program():
    import os

    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner(text):
        print(r"""
 █████╗ ██╗  ██╗████████╗███████╗██████╗ 
██╔══██╗╚██╗██╔╝╚══██╔══╝██╔════╝██╔══██╗
███████║ ╚███╔╝    ██║   █████╗  ██████╔╝
██╔══██║ ██╔██╗    ██║   ██╔══╝  ██╔══██╗
██║  ██║██╔╝ ██╗   ██║   ███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
        """)
        print(f"{text}\n")

    def addition():
        clear_console()
        print_banner("[!] Addition")
        try:
            num1 = float(input("[!] First number: "))
            num2 = float(input("[!] Second number: "))
            result = num1 + num2
            print(f"[!] The result of {num1} + {num2} is {result}\n")
        except ValueError:
            print("[!] Invalid input. Please enter numeric values.\n")

    def subtraction():
        clear_console()
        print_banner("[!] Subtraction")
        try:
            num1 = float(input("[!] First number: "))
            num2 = float(input("[!] Second number: "))
            result = num1 - num2
            print(f"[!] The result of {num1} - {num2} is {result}\n")
        except ValueError:
            print("[!] Invalid input. Please enter numeric values.\n")

    def multiplication():
        clear_console()
        print_banner("[!] Multiplication")
        try:
            num1 = float(input("[!] First number: "))
            num2 = float(input("[!] Second number: "))
            result = num1 * num2
            print(f"[!] The result of {num1} * {num2} is {result}\n")
        except ValueError:
            print("[!] Invalid input. Please enter numeric values.\n")

    def division():
        clear_console()
        print_banner("[!] Division")
        try:
            num1 = float(input("[!] First number: "))
            num2 = float(input("[!] Second number: "))
            if num2 != 0:
                result = num1 / num2
                print(f"[!] The result of {num1} / {num2} is {result}\n")
            else:
                print("[!] Cannot divide by zero.\n")
        except ValueError:
            print("[!] Invalid input. Please enter numeric values.\n")

    def main():
        while True:
            clear_console()
            print_banner("https://github.com/axterv2/simple-math-program")
            print("[!] Select an option:")
            print("[1] Addition")
            print("[2] Subtraction")
            print("[3] Multiplication")
            print("[4] Division")
            print("[5] Exit")

            choice = input("[!] Enter your choice (1-5): ")

            if choice == '1':
                addition()
            elif choice == '2':
                subtraction()
            elif choice == '3':
                multiplication()
            elif choice == '4':
                division()
            elif choice == '5':
                print("[:(] Goodbye...")
                break
            else:
                print("[!] Invalid choice. Please select a number between 1 and 5.\n")

            input("[!] Press Enter to continue...")

    if __name__ == "__main__":
        main()

def main():
    while True:
        clear_console()
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            loading_animation()
            run_math_program()
            break
        elif choice == '2':
            display_info()
        elif choice == '3':
            print("[:(] Goodbye...")
            break
        else:
            print("[!] Invalid choice. Please try again.")
            time.sleep(2)

if __name__ == "__main__":
    main()