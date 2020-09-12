import csv

def writeIntoCsv(info_list):
    with open('studenInfo.csv', 'a', newline = '') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "ContactNo", "EmailID"])
        writer.writerow(info_list)

if __name__ == "__main__":
    condition = True
    studentNum = 1

    while(condition):
        studentInfo = input("Enter student #{} info in following format \n (Name Age ContactNo Email)"
                            .format(studentNum))
        print("Entered Student Information is: ",studentInfo)

        #split
        studentInfoList = studentInfo.split(" ")

        print("Entered Information\nName:{}\nAge:{}\nContactNo:{}\nEmailID:{}"
              .format(studentInfoList[0], studentInfoList[1], studentInfoList[2], studentInfoList[3]))

        choiceCheck = input("Is the entered information correct? Yes/No")

        if choiceCheck == "Yes" or choiceCheck == "yes":
            writeIntoCsv(studentInfoList)
            conditionCheck = input("Enter Yes/No if you want to add information  of another student")
            if conditionCheck == "Yes" or conditionCheck == "yes":
                condition = True
                studentNum += 1
            elif conditionCheck == "No" or conditionCheck == "no":
                condition = False

        elif choiceCheck == "No" or choiceCheck =="no":
            print("\nPlease Re-Enter values")

