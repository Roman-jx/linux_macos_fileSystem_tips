#Import modules
import enum        # Import module for numeration
# import sys       # Import module for systems
# import colorama  # Import module for color change
import time        # Import module for time
import click       # Import module for cli
import os          # Import module for operations
import json        # Import module to present data
import datetime    # Import module for time

#Takes value from modules 
from enum import Enum       # Take only Enum func to recalculate our arguments
# from sys import platform  # Take only platform func to check the user system
# from colorama import *    # Take all funcs to change the color output
from pathlib import Path    # Take only Path to chow absolute path to our file(s)
from os import *            # Take only walk to print all items in path
from pwd import *           # Take all funcs to work with paths

#Global values for click program
SAVE_SCRIPT_PATH = None
SAVE_RUN_PATH = None
SAVE_DEFINED_PATH = None
TEXT_FILE_NAME = None
CSV_FILE_NAME = None
JSON_FILE_NAME = None
HTML_FILE_NAME = None
GET_TASK_STATUS = "200"


#Main class
class Ls(Enum):
    #Class values
    SCRIPT_PATH = f"{Path('main.py').parent.absolute()}/"            #Default values
    RUN_PATH = f"{Path('main.py').parent.absolute()}/main.py"        #Default values
    DEFINED_PATH = f"{SAVE_DEFINED_PATH}"


    #Find our file in system
    def find_path(file_name: str, path: str = "/") -> str:
        for dpath, dname, fname in os.walk(path):
            if file_name in fname:
                return os.path.join(dpath, file_name)

    #Main func
    def get_path(mode: enum) -> str:                                # Takes three constants and returns the path depending on the value passed by the user
        return f"{mode.value}"

    #Additional def
    def ad_get_path(arg: str) -> str:
        return ", ".join(list(map(str, os.listdir(arg))))

    # Main func
    def get_content_list(path: str) -> list:                        # Return a list of files and folders along the path passed as the function argument
        return list(map(str, os.listdir(path)))

    # Main func
    def get_file_list(path: str) -> list:                            # Return only files along the path as the function argument
        return [fn for (dp, dn, fn) in walk(str(path))][0]

    # Main func
    def get_directory_list(path: str) -> list:                      # Return only folders along the path as the function argument
        return [dn for (dp, dn, fn) in walk(str(path))][0]

    # Main func
    def get_file_info(path: str) -> str:                           #Return the dict size, hash, modification date, file creation data
        d = {
            "Owner file": getpwuid(stat(str(path)).st_uid).pw_name,
            "Owner file in linux type": stat(path).st_uid,
            "Permissions": oct(stat(path).st_mode),
            "Files size in bytes": os.stat(str(path)).st_size,
            "File was created": datetime.datetime.utcfromtimestamp(stat(path).st_ctime),
            "File modified": datetime.datetime.utcfromtimestamp(stat(path).st_mtime),
            "File last accessed": datetime.datetime.utcfromtimestamp(stat(path).st_atime)
        }
        return ", ".join([f"{key}: {value}" for key, value in d.items()])

    # Main func
    def get_directory_info(path: str) -> str:                      #Return the dict size, hash, modification date, folder creation date
        d = {
            "Owner folder": getpwuid(stat(str(path)).st_uid).pw_name,
            "Owner folder in linux type": stat(path).st_uid,
            "Permissions": oct(stat(path).st_mode),
            "Folder size in bytes": os.stat(str(path)).st_size,
            "Folder was created": time.ctime(stat(path).st_ctime),
            "Folder modified": time.ctime(stat(path).st_mtime),
            "Folder last accessed": time.ctime(stat(path).st_atime)
        }
        return ", ".join([f"{key}: {value}" for key, value in d.items()])

    # Main func
    def save_as_txt(path: str, content: str = None) -> None:        #Save the found files and folder and information about them in a txt format
        if os.path.exists(path):
            with open(f"{path[:path.rfind('.')]}.txt", mode='w+') as file:
                with open(path, mode='r') as file2:
                    content = file2.read()
                    file.write(content)

    # Main func
    def save_as_csv(path: str, content: str = None) -> None:       #Save the found files and folder and information about them in a csv format
        if os.path.exists(path):
            with open(f"{path[:path.rfind('.')]}.csv", mode="w+") as file:
                with open(path, mode="r") as file2:
                    for line in file2:
                        file.write(line.rstrip("\n") + ",\n")

    # Main func
    def save_as_json(path: str, content: str = None) -> None:      #Save the found files and folder and information about them in a json format
        if os.path.exists(path):
            with open(f"{path[:path.rfind('.')]}.json", mode="w+") as file:
                with open(path, mode="r") as file2:
                    json.dump(file2.read().replace("\n", "").replace("  ", ""), file)

    # Main func
    def save_as_html(path: str, content: str = None) -> None:      #Save the found files and folder and information about them in a html format
        if os.path.exists(path):
            with open(f"{path[:path.rfind('.')]}.html", mode="w+") as file:
                with open(path, mode="r") as file2:
                    content = file2.read()
                    file.write(f"<html>\n<head>\n\t<title>Test data</title>\n</head>\n<body>\n\t<p>" + content.replace('\n', ' | ') + "</p>\n</body>\n</html>")

    # Main func
    def get_task_status(status: str) -> str:                        #Return the status on all executed tasks simply to extend term
        return f"{status}"

    # Main func
    def get_report_content(report_path: str) -> str:                #Return the contents of the file (csv, txt, json, html) in which the result is saved lists of files and folders and data about them
        return f"(Size): {os.path.getsize(report_path)}, (Changed): {datetime.datetime.utcfromtimestamp(os.path.getmtime(report_path))}, (Created): {datetime.datetime.utcfromtimestamp(os.path.getctime(report_path))}"


# Create cli program
@click.command()
@click.option("--script-path", "-sp", type=str, help="[spath] Path from which the script is called")
@click.option("--run-path", "-rp", type=str, help="[rpath] Path where the script is located")
@click.option("--defined-path", "-dp", type=str, help="[user input path] Path that is passed as the script argument.")
@click.option("--utc", "-uc", type=str, help="[user input file] Shows when the file and folder have changed")
@click.option("--unix", "-ux", type=str, help="[user input file] Shows file or directory time changes")
@click.option("--text", "-t", type=str, help="[user input file] Saves the file in txt format")
@click.option("--csv", "-cv", type=str, help="[user input file] Saves the file in csv format")
@click.option("--json", "-jn", type=str, help="[user input file] Saves the file in json format")
@click.option("--html", "-h", type=str, help="[user input file] Saves the file in html format")
@click.option("--file-info", "-fi", type=str, help="[user input file] Returns all information about the file")
@click.option("--get-files", "-gf", type=str, help="[user input path] Return all files which are in the path")
@click.option("--get-folders", "-gd", type=str, help="[user input path] Return all folders which are in the path")
@click.option("--get-files-info", "-gfi", type=str, help="[user input path] Return all info about files in the path")
@click.option("--get-folders-info", "-gdi", type=str, help="[user input path] Return all info about folders in the path")
def cli_program(script_path, run_path, defined_path, utc, unix, text, csv, json, html, file_info, get_files, get_folders, get_files_info, get_folders_info):
    '''
            The prototype is designed for LINUX and is still being tested to support other operating systems

            My github: https://github.com/Roman-jx
    '''

    #Set the value from the input to our variable
    SAVE_SCRIPT_PATH = script_path
    SAVE_RUN_PATH = run_path
    SAVE_DEFINED_PATH = defined_path
    TEXT_FILE_NAME = text
    CSV_FILE_NAME = csv
    JSON_FILE_NAME = json
    HTML_FILE_NAME = html

    #RUN options
    click.echo(
        f"[ {Ls.get_task_status(GET_TASK_STATUS)} ] Your script path is: {Ls.get_path(Ls.SCRIPT_PATH)}\nYour dir files and folders: {Ls.ad_get_path(Ls.get_path(Ls.SCRIPT_PATH))}" if (script_path == "spath" and script_path != None) else None
    )
    click.echo(
        f"[ {Ls.get_task_status(GET_TASK_STATUS)} ] Your run path is: {Ls.get_path(Ls.RUN_PATH)}" if (run_path == "rpath" and run_path != None) else None
    )
    click.echo(
        f"[ {Ls.get_task_status(GET_TASK_STATUS)} ] Your file path is: {Ls.find_path(SAVE_DEFINED_PATH)}\nYour dir files and folders: {Ls.ad_get_path(Ls.find_path(SAVE_DEFINED_PATH).strip(SAVE_DEFINED_PATH))}" if (defined_path != "./" and defined_path != None) else None
    )
    click.echo(
        f"[ {Ls.get_task_status(GET_TASK_STATUS)} ] Your date in utc format is: {datetime.datetime.utcfromtimestamp(os.path.getmtime(utc))}" if (utc != None) else None
    )
    click.echo(
        f"[ {Ls.get_task_status(GET_TASK_STATUS)} ] Your date in unix format is: {os.path.getmtime(unix)}" if (unix != None) else None
    )
    click.echo(
        f"[{Ls.save_as_txt(TEXT_FILE_NAME)}] [ {Ls.get_task_status(GET_TASK_STATUS)} ] Your file was saved as {TEXT_FILE_NAME[:TEXT_FILE_NAME.rfind('.')]}.txt\nCheck the current folder!" if (text != None) else None
    )
    click.echo(
        f"[{Ls.save_as_csv(CSV_FILE_NAME)}] [ {Ls.get_task_status(GET_TASK_STATUS)} ] Your file was saved as {CSV_FILE_NAME[:CSV_FILE_NAME.rfind('.')]}.csv\nCheck the current folder!" if (csv != None) else None
    )
    click.echo(
        f"[{Ls.save_as_json(JSON_FILE_NAME)}] [ {Ls.get_task_status(GET_TASK_STATUS)} ] Your file was saved as {JSON_FILE_NAME[:JSON_FILE_NAME.rfind('.')]}.json\nCheck the current folder!" if (json != None) else None
    )
    click.echo(
        f"[{Ls.save_as_html(HTML_FILE_NAME)}] [ {Ls.get_task_status(GET_TASK_STATUS)} ] Your file was saved as {HTML_FILE_NAME[:HTML_FILE_NAME.rfind('.')]}.html\nCheck the current folder!" if (html != None) else None
    )
    click.echo(
        f"[ {Ls.get_task_status(GET_TASK_STATUS)} ] Full info about file: {Ls.get_report_content(file_info)}" if (file_info != None) else None
    )
    click.echo(
        f"[ {Ls.get_task_status(GET_TASK_STATUS)} ] All files in the path: {Ls.get_file_list(get_files)}" if (get_files != None) else None
    )
    click.echo(
        f"[ {Ls.get_task_status(GET_TASK_STATUS)} ] All folders in the path: {Ls.get_directory_list(get_folders)}" if (get_folders != None) else None
    )
    click.echo(
        f"[ {Ls.get_task_status(GET_TASK_STATUS)} ] All files and their options in the path: {Ls.get_file_info(get_files_info)}" if (get_files_info != None) else None
    )
    click.echo(
        f"[ {Ls.get_task_status(GET_TASK_STATUS)} ] All folders and their options in the path: {Ls.get_directory_info(get_folders_info)}" if (get_folders_info != None) else None
    )


if __name__ == "__main__":
    cli_program()
