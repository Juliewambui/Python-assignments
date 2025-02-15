citizenship = input("Are you an East African citizen? (yes/no): ").strip().lower()
age = int(input("Enter your age: "))
if citizenship == "yes" and age >=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
