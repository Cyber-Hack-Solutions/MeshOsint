# Tool designed by Cyber-Hack Solutions LLC
# For educational purposes only; use responsibly.

import subprocess
import os
from rich import box, print

get_current_dir = os.getcwd()

def clear_screen():
    """
    Permits the tool to run on all operating systems,
    Windows, MacOS, Linux
    """
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def input_field():
    """
    User Input Field
    """
    print(f"\n [bold][orange3] >> [/orange3][/bold]", end="")
