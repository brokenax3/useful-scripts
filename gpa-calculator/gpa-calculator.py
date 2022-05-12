import csv

grade_list = []
grade_value = []
count = 0
summation = 0

sel = input("(G)PA or (C)GPA? (Default: G): ")

if(sel == ""):
    sel = "G"

with open("scores.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if count == 0:
            score_list = row
            count += 1
        else:
            credit_point_list = row
            count += 1

    if len(score_list) != len(credit_point_list):
        print("Length of score_list and credit_point_list does not match")
        exit(-1)

    credit_point_list_f = [float(item) for item in credit_point_list]

if(sel == "G"):
    for score in score_list:
        tmpscore = int(score)

        if(tmpscore >= 80):
            grade_list.append("HD")
            grade_value.append(4.0)
        elif(tmpscore < 80 and tmpscore >=70):
            grade_list.append("D")
            grade_value.append(3.0)
        elif(tmpscore < 70 and tmpscore >= 60):
            grade_list.append("C")
            grade_value.append(2.0)
        elif(tmpscore < 60 and tmpscore >= 50):
            grade_list.append("P")
            grade_value.append(1.0)
        elif(tmpscore < 50):
            grade_list.append("F")
            grade_value.append(0.3)
elif(sel == "C"):
    for score in score_list:
        tmpscore = int(score)

        if(tmpscore >= 80):
            grade_list.append("HD")
            grade_value.append(4.0)
        elif(tmpscore < 80 and tmpscore >=70):
            grade_list.append("D")
            grade_value.append(3.67)
        elif(tmpscore < 70 and tmpscore >= 60):
            grade_list.append("C")
            grade_value.append(2.85)
        elif(tmpscore < 60 and tmpscore >= 50):
            grade_list.append("P")
            grade_value.append(2.15)
        elif(tmpscore < 50):
            grade_list.append("F")
            grade_value.append(1.15)
else:
    print("Invalid Selection")
    exit(-1)

for index in range(0, len(grade_value)):
    product = grade_value[index] * credit_point_list_f[index]
    # print("{} x {} = {}".format(grade_value[index],credit_point_list_f[index],product))

    summation += product

# print("Summation is {}".format(summation))
# print("Total credit point of {}".format(sum(credit_point_list_f)))

gpa = summation / sum(credit_point_list_f)

print(gpa)
