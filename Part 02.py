Student_Progress_Count = 0  # count_calculation = 0 ,before running the programme
Student_Module_Trailer_Count = 0
Student_Exclude_Count = 0
Student_N_Module_Count = 0
Student_Total_Count = 0


def Range_Check(Input_01):  # function to check the range
    if Input_01 <= 120 and Input_01 >= 0 and Input_01 % 20 == 0:
        Stored_01 = True

    else:
        print("Out of range")
        Stored_01 = False
        return Stored_01


# --------------------------------------------------------------------------------------------------------------------------------------

print("")
print("****************************************************************************************************")
print("                                                                                                    ")
print("-----------------You Have Just Logged Onto The Student Progression Program----------------")
print("                                                                                                    ")
print("****************************************************************************************************")
# --------------------------------------------------------------------------------------------------------------------------------------
print("")
print("                        * LIMITATIONS FOR USERS *                     ")
print("")
print("01.Please use only 0  / 20 / 40 / 60 / 80 / 100 / 120 / q as inputs.")
print("")
print("02.Please do not use letters / symbols / special characters as inputs.")
# --------------------------------------------------------------------------------------------------------------------------------------

print("")

while True:
    Stored_02 = False
    while Stored_02 == False:

        Range = False
        while Range == False:
            try:
                Student_Pass_Mark = int(input("Please enter PASS credit :"))
                Range = Range_Check(Student_Pass_Mark)

            except ValueError:
                print("Integers required")
                Range = False

        Range = False
        while Range == False:
            try:
                Student_Defer_Mark = int(input("Please enter DEFER credit :"))
                Range = Range_Check(Student_Defer_Mark)

            except ValueError:
                print("Integers required")
                Range = False

        Range = False
        while Range == False:
            try:
                Student_Fail_Mark = int(input("Please enter FAIL credit:"))
                Range = Range_Check(Student_Fail_Mark)

            except ValueError:
                print("Integers required")
                Range = False
        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        Total_Mark_Students = Student_Pass_Mark + Student_Fail_Mark + Student_Defer_Mark
        if Total_Mark_Students == 120:  # Total calculated by the sum of 3 credit types
            Stored_02 = True
            print("")
        else:
            print("Total incorrect")
            print("_____________________________________________________________________")
            print("")
            Stored_02 = False

    if Student_Pass_Mark == 120:
        print("Progress")
        print("_____________________________________________________________________")
        print("")
        Student_Progress_Count = Student_Progress_Count + 1

    elif Student_Pass_Mark == 100:
        print("Progress–module trailer")
        print("_____________________________________________________________________")
        print("")
        Student_Module_Trailer_Count = Student_Module_Trailer_Count + 1

    elif Student_Fail_Mark >= 80:
        print("Exclude")
        print("_____________________________________________________________________")
        print("")
        Student_Exclude_Count = Student_Exclude_Count + 1

    else:
        print("Do not progress–module retriever")
        print("_____________________________________________________________________")
        Student_N_Module_Count = Student_N_Module_Count + 1

    Student_Total_Count = Student_N_Module_Count + Student_Exclude_Count + Student_Module_Trailer_Count + Student_Progress_Count
    input_command_for_exit = input(
        "Press 'q' to exit from the program. Press 'y' to check the progression outcome of another student  : ")
    if input_command_for_exit == "q":
        print("")
        break  # break used for stop the programme
    else:
        print("")
        continue

Vertical_histogram = max(Student_Progress_Count, Student_Module_Trailer_Count,
                     Student_N_Module_Count, Student_Exclude_Count)  # 0 to max is the range
print("Progress Trailing Retriever  Excluded")
for count in range(0, Vertical_histogram):

    if Student_Progress_Count > 0:  # I used for loop for vertical histogram.

        print("   *", end="         ")
        Student_Progress_Count -= 1  # these spaces kept for better align
    else:
        print("   ", end="          ")

    if Student_Module_Trailer_Count > 0:
        print("*", end="        ")
        Student_Module_Trailer_Count -= 1
    else:
        print("", end="         ")

    if Student_N_Module_Count > 0:
        print("*", end="          ")
        Student_N_Module_Count -= 1
    else:
        print("", end="           ")

    if Student_Exclude_Count > 0:
        print("*", end="\n")
        Student_Exclude_Count -= 1
    else:
        print("", end="\n")
print(Student_Total_Count,"Total Outcomes")        
