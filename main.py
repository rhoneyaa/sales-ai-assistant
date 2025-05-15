# main.py

def get_company_name():
    """Prompts the user to enter a company name."""
    company_name = input("Enter the target company's name: ")
    return company_name

if __name__ == "__main__":
    print("Sales AI Assistant - Initial Setup")
    target_company = get_company_name()
    print(f"Company to analyze: {target_company}")

    # We will add more functionality here later