from colorama import Style, Fore, Back
print(f"{Back.GREEN}{Fore.WHITE}Initiating GreenHouse...{Style.RESET_ALL}")

from app.green_house import GreenHouse

if __name__ == "__main__":
    green_house = GreenHouse()