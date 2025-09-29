slambook = {}
def add_contact():
    name = input("enter name:  ").strip()
    if name in slambook:
        print("contact already exists!")
    else:
        number = input("enter number:  ").strip()
        slambook[name] = number
        print("contact {name} added successfully!")
def search_contact():
    name = input ("enter name to search:").strip()
    if name in slambook:
        print(f"{name}: {slambook[name]}")
    else:
        print("contact not found!")
def display_contacts():
    if slambook:
        print("slambook contacts:")
        for name, number in slambook.items():
            print(f"{name}: {number}")
    else:
        print("slambook is empty!")
def update_contact():
    name = input("enter name to update: ").strip()
    if name in slambook:
        number = input("enter new number: ").strip()
        slambook[name] = number
        print(f"contact {name} updated successfully!")
    else:
        print("contact not found!")
def delete_contact():
    name= input("enter name to delete:").strip()
    if name in slambook:
        del slambook[name]
        print(f"contact {name} deleted successfully!")  
    else:
        print("contact not found!")
def ask_question():
    name = input("what is your name ").strip()
    if name in slambook:
        hobby = input("enter your hobby: ").strip()
        slambook[name] = hobby
        print(f"thank you for sharing your hobby, {name}!")
    else:
        print("information already exists!")
def ask_question2():
    name = input("what is your name?").strip()
    if name in slambook:
        age = input("enter your age:").strip()
        slambook[name] = age
        print(f"thank you for sharing your age, {name}!")
def ask_question3():
    name = input("what is your name?").strip()
    if name in slambook :
         fav_color = input("enter your favorite color:").strip()
         slambook[name] = fav_color
         print(f"thank you for sharing your favorite color, {name}!")
def main():
    while True:
        print("slambook menu:")
        print("1. add contact")
        print("2. search contact")
        print("3. display contacts")
        print("4.update contact")
        print("5.delete contacts")
        print("6. exit")
        print("7. ask question 1,hobby")
        print("8. ask question 2,age")
        print("9. ask question 3,favorite color")
        choice = input("enter your choice (1-9): ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            display_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '7':
            ask_question()
        elif choice == '8':
            ask_question2()
        elif choice == '9':
            ask_question3()
        elif choice == '6':
            print("exiting slambook. goodbye!")

            break
        else:
            print("invalid choice. please try again.")
main() 