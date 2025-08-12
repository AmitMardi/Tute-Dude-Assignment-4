# Task 2: Write and Append Data to a File

user_text = input("Enter text to write to the file: ")

file1 = open("output.txt", "w")
file1.write(user_text + "\n")
file1.close()
print("Data successfully written to output.txt \n")

append_text = input("Enter additional text to append: ")
file1 = open("output.txt", "a")
file1.write(append_text + "\n")
file1.close()
print("Data successfully appended.\n")

print("Final content of output.txt:")
file1 = open("output.txt", "r")
print(file1.read())
file1.close()