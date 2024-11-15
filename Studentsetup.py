import sys
from cx_Freeze import*
includefiles=["miraj.ico"]
excludes=[]
packages=[]
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
shortcut_table = [
    ("DesktopShortcut",  # Shortcut 
     "DesktopFolder",   # Directory
     "StudentManagementSystemComplete",  # Name
     "TARGETDIR", # Component
     "[TARGETDIR]\StudentManagementSystemComplete.exe", # Target
     None, # Arguments
     None, # Description
     None, # Hotkey
     None, # Icon
     None, # Icondex
     None, # ShowCmd
     "TARGETDIR",  # WkDir
     )
]

msi_data = {"Shortcut":shortcut_table}

bdist_msi_options = {'data': msi_data}
setup(
    version = "0.1",
    description = "Student Management System Developed by Miraj Miah",
    author = "Miraj Miah",
    name = "Student Management System",
    options = {'build_exe': {'include_files': includefiles}, "bdist_msi":bdist_msi_options ,},
    executables = [
        Executable(
        script = "StudentManagementSystemComplete.py",
        base = base,
        icon = 'miraj.ico',
        )    
    ]
)   