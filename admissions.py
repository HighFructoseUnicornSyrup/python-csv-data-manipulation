# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
# from typing import List
from itertools import zip_longest


def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True


# define your functions here
filename = "admission_algorithms_dataset.csv"
input_file = open(filename, "r")


def convert_row_type(q):
    float_data = []
    for i in range(0, len(q)):
        q[i] = float(q[i])
        float_data.append(q[i])


def main():

    student_scores = "student_scores.csv"
    chosen_students = "chosen_students.csv"
    outliers = "outliers.csv"
    chosen_improved = "chosen_improved.csv"
    better_improved = "better_improved.csv"
    composite_chosen = "composite_chosen.csv"


    write_ss = open(student_scores, "w")
    write_cs = open(chosen_students, "w")
    write_out = open(outliers, "w")
    write_improved = open(chosen_improved, "w")
    write_better = open(better_improved, "w")
    write_composite = open(composite_chosen, "w")
    data_lines = input_file.readlines()[0:]
    #print(data_lines)
    for line in data_lines:
        #print(line)
        split_line = line.split(',')
        #print(split_line)
        student_name = split_line[0]
        #print(student_name)
        student_data = split_line[1:]
        #print(student_data)
        convert_row_type(student_data)
        check_row_types(student_data)

        first_four = student_data[:4]
        last_four = student_data[4:]

        write_ss.write(f"{student_name},{calculate_score(first_four):.2f}\n")

        if calculate_score(first_four) >= 6:
            write_cs.write(f"{student_name}\n")

        if is_outlier(first_four) == True:
            write_out.write(f"{student_name}\n")

        if calculate_score(first_four) >= 6 or (is_outlier(first_four) == True and calculate_score(first_four) >=5):
            write_improved.write(f"{student_name}\n")

        if calculate_score_improved(first_four) == True:
            data_to_write = f"{student_name},{first_four[0]},{first_four[1]},{first_four[2]},{first_four[3]}\n"
            write_better.write(data_to_write)

    # This below line doesn't work. too many names are added. The functions all work and are approved by the autograder.
        if calculate_score(first_four) >= 6 or (calculate_score(first_four) >= 5 and ((is_outlier(first_four) == True or grade_outlier(last_four) == True or grade_improvement(last_four) == True))):
            write_composite.write(f"{student_name}\n")

    input_file.close()
    write_ss.close()
    write_cs.close()
    write_out.close()
    write_improved.close()
    write_better.close()
    write_composite.close()

def calculate_score(first_four):
    score = (((first_four[0] / 160) * 0.3) + ((first_four[1] * 2) * 0.4) + ((first_four[2]) * 0.1) + ((first_four[3]) * 0.2))
    return score


def is_outlier(first_four):
    norm_gpa = (first_four[1] * 2)
    norm_sat = (first_four[0] / 160)
    if first_four[2] == 0 or norm_gpa > (norm_sat + 2):
        return True
    else:
        return False


def calculate_score_improved(first_four):
    if is_outlier(first_four) == True or calculate_score(first_four) >= 6:
        return True
    else:
        return False


def grade_outlier(last_four):
    last_four = sorted(last_four)
    difference = (last_four[1] - last_four[0])
    if difference >= 20:
        return True
    else:
        return False


def grade_improvement(last_four):
    sem1 = last_four[0]
    sem2 = last_four[1]
    sem3 = last_four[2]
    sem4 = last_four[3]
    if sem1 <= sem2 <= sem3 <= sem4:
        return True
    else:
        return False


print("Processing " + filename + "...")
# grab the line with the headers
headers = input_file.readline()


# TODO: loop through the rest of the file

# TODO: make sure to close all files you've opened!

print("done!")


# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
