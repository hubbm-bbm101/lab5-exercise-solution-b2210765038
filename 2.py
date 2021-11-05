mail = str(input("Enter your e-mail"))
if "@" not in mail or "." not in mail:
    print("Sorry, you've entered a non-valid mail address.")
else:
    print("You're completely legal :)")
