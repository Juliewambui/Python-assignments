def main():
    # Prompt the user to enter names
    names_input = input("Enter a list of names separated by commas: ")
    
    # Split the input into a list of names, removing any extra spaces
    names_list = [name.strip() for name in names_input.split(',')]
    
    # Remove duplicates by converting the list to a set and then back to a list
    unique_names = list(set(names_list))
    
    # Sort the list alphabetically
    unique_names.sort()
    
    # Display the final sorted list
    print("\nSorted list of unique names:")
    print(unique_names)
    
    # Count and display the total number of names entered
    total_names = len(names_list)
    print(f"\nTotal number of names entered: {total_names}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
