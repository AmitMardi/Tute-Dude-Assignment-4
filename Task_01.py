# Task 1: Read a File and Handle Errors
try:
    file1 = open('sample.txt', 'r')
    line1 = file1.readline().strip()
    line2 = file1.readline().strip()
    print("Reading file content:")
    print("Line 1:", line1)
    print("Line 2:", line2)
    file1.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
