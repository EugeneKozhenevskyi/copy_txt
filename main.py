def copy_file():
    user_input = input("Enter text: ")

    with open("text.txt", "w") as file1:
        file1.write(user_input)

    with open("text.txt", "r") as file2:
        result = file2.read()

    with open("text2.txt", "w") as file3:
        file3.write(result)

    file1.close()
    file2.close()
    file3.close()

    print("The file has been copied")


copy_file()
