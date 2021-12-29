# OPTIO File Namer | Run this code to handle file naming for you
import os
import re

base_directory = os.getcwd()
directories = os.listdir()


def get_directory_name():
    subdirectory_names = []
    for dir in directories:
        if os.path.isdir(dir):
            subdirectory_names.append(dir)
    return subdirectory_names


def enter_directory(directory):
    directory = os.chdir(os.path.join(os.getcwd(), directory))
    return directory


def get_files(directory):
    directory = enter_directory(directory)
    file_list = []
    directory_list = os.listdir()
    for dir in directory_list:
        if os.path.isfile(dir):
            file_list.append(dir)
    return file_list


def file_rename(files, file_type):
    file_no = 0
    for file in files:
        file_seeker = re.search(file_type + "$", file)
        if file_seeker != None:
            os.rename(file, dir_name + "_" + f"{file_no:03}" + file_type)
            file_no += 1


current_directory = get_directory_name()
all_subdirs = [x[0] for x in os.walk(current_directory[0])]

for dir in all_subdirs:
    dir_name = dir.split("/")[-1]
    files = get_files(base_directory + "/" + dir)
    file_rename(files, ".rvt")
    file_rename(files, ".3dm")
    file_rename(files, ".dwg")