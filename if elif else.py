role = input("Enter your role (admin/office/clerk): ")

if role == "admin":
    print("Welcome Admin!")
    print("You have full access.")

elif role == "office":
    print("Welcome Office Staff!")
    print("You can manage records.")

elif role == "clerk":
    print("Welcome Clerk!")
    print("You can view records only.")

else:
    print("Invalid role. Access denied.")
