Student_Progress_Count = 0  # count = 0 , Program not yet begun
Student_Module_Trailer_Count = 0
Student_Exclude_Count = 0
Student_N_Module_Count = 0
Student_Total_Count = 0


def Range_Check(input_01):  # range check function
    if input_01 <= 120 and input_01 >= 0 and input_01 % 20 == 0:
        Stored_01 = True

    else:
        print("range error")
        boolean_save_1 = False
        return Stored_01


def Histogram_Count():  # progression outcome function
    print("Progress ", Student_Progress_Count, ":  ", Student_Progress_Count * "*")
    print("\n")

    print("Trailing ", Student_Module_Trailer_Count, ":  ", Student_Module_Trailer_Count* "*")
    print("\n")

    print("Retriever ", Student_N_Module_Count, ": ",
          Student_N_Module_Count * "*")  # student_d_module_count_calculation meant for student do not progress-module retriever count calculation
    print("\n")

    print("Excluded ", Student_Exclude_Count, ":  ", Student_Exclude_Count * "*")
    print("\n")
    print("\n")
    print(Student_Total_Count, " total outcomes.")


# --------------------------------------------------------------------------------------------------------------------------------------

print("\n")
print("****************************************************************************************************")
print("-----------------You Have Oficially Logged Onto Student Progression Program----------------")
print("****************************************************************************************************")
# --------------------------------------------------------------------------------------------------------------------------------------
print("\n")
print("                            * Limitations For Users *                                  ")
print("01.Make Use Of The Values 0  / 20 / 40 / 60 / 80 / 100 / 120 / q in place of inputs.")
print("02.Restrict from using letters / symbols / special characters as inputs.")
# --------------------------------------------------------------------------------------------------------------------------------------

print("\n")

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
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        Total_Mark = Student_Pass_Mark + Student_Fail_Mark + Student_Defer_Mark
        if Total_Mark == 120:  # Total calculated by the sum of 3 credit types
            Stored_02 = True
            print("\n")
        else:
            print("Total incorrect")
            print("_____________________________________________________________________")
            print("\n")
            Stored_02 = False

    if Student_Pass_Mark == 120:
        print("Progress")
        print("_____________________________________________________________________")
        print("\n")
        student_progress_count = student_progress_count+ 1

    elif Student_Pass_Mark == 100:
        print("Progress–module trailer")
        print("_____________________________________________________________________")
        print("\n")
        Student_Module_Trailer_Count = Student_Module_Trailer_Count + 1

    elif Student_Fail_Mark >= 80:
        print("Exclude")
        print("_____________________________________________________________________")
        print("\n")
        Student_Exclude_Count = Student_Exclude_Count + 1

    else:
        print("Do not progress–module retriever")
        print("_____________________________________________________________________")
        Student_N_Module_Count = Student_N_Module_Count + 1

    Student_Total_Count = Student_N_Module_Count + Student_Exclude_Count + Student_Module_Trailer_Count + Student_Progress_Count
    input_command_for_exit = input(
        "Press 'q' to exit from the program. Press 'y' to check the progression outcome of another student  : ")
    if input_command_for_exit == "q":
        print("\n")
        break  # break used for stop the programme
    else:
        print("\n")
        continue

Histogram_Count()
