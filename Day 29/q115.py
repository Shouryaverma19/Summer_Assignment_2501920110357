choice = 0

while choice != 5:
    print("\n--- String Operations Menu ---")
    print("1. Concatenate Two Strings")
    print("2. Reverse a String")
    print("3. Check Palindrome")
    print("4. Find Substring Occurrence")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        s1 = input("Enter first string: ")
        s2 = input("Enter second string: ")
        print("Concatenated String:", s1 + s2)
    elif choice == 2:
        s = input("Enter string to reverse: ")
        rev = ""
        for char in s:
            rev = char + rev
        print("Reversed String:", rev)
    elif choice == 3:
        s = input("Enter string to check: ")
        length = 0
        for char in s:
            length += 1
        is_pal = True
        for i in range(length // 2):
            if s[i] != s[length - 1 - i]:
                is_pal = False
                break
        if is_pal:
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")
    elif choice == 4:
        main_str = input("Enter main string: ")
        sub_str = input("Enter substring to find: ")
        if sub_str in main_str:
            print("Substring exists inside the main string.")
        else:
            print("Substring does not exist.")
    elif choice == 5:
        print("Exiting String System.")
    else:
        print("Invalid choice.")