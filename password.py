#program for checking password
for x in range(4):
    password = input("Enter password: ")
    if password == "1234":
        break
    print("error, this is not correct ... try again!")
else:
        print("the process is completed. Thanks!")
