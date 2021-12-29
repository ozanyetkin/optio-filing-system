# OPTIO File Generator | Run this code to handle directory creation for you
import os

root_directory = os.getcwd()
land_no = input("Please Enter Land Number for the Project: ")
parcel_no = input("Please Enter Parcel Number for the Project: ")
project_name = input("Please Enter Short Name for the Project: ").upper()

while len(project_name) > 4:
    project_name = input("Please Use Max 4 Characters for Short Name: ").upper()

base_directory_name = land_no + "_" + parcel_no + "_" + project_name

try:
    os.mkdir(base_directory_name)
    os.chdir(base_directory_name)
except FileExistsError:
    os.chdir(base_directory_name)

disciplines = ["AR", "CE", "ME", "EE", "LA"]
phase_numbers = int(input("Please Enter Number of Phases for the Project: "))

for discipline in disciplines:
    discipline_directory_name = base_directory_name + "_" + discipline
    try:
        os.mkdir(discipline_directory_name)
        os.chdir(discipline_directory_name)
    except FileExistsError:
        os.chdir(discipline_directory_name)
    for i in range(phase_numbers):
        phase_name = discipline_directory_name + "_P" + str(i + 1)
        try:
            os.mkdir(phase_name)
        except FileExistsError:
            pass
    os.chdir("..")

special_folders = ["OTH", "DOC"]

for special in special_folders:
    special_directory_name = base_directory_name + "_" + special
    try:
        os.mkdir(special_directory_name)
    except FileExistsError:
        pass
    if special == "DOC":
        try:
            os.chdir(special_directory_name)
            os.mkdir(special_directory_name + "_" + "PHT")
        except FileExistsError:
            pass