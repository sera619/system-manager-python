from http.server import executable
import sys
import os
from cx_Freeze import setup, Executable

files = ['models.py','ui_form.py','AANOTHERTAG.TTF', 'Icons.qrc', 'Icons_rc.py','form.ui']

target = Executable(script='main.py',
                    base = 'Win32GUI')

setup(
    name='M0W1Z',
    version='0.9.3',
    description="A System-Monitor for Tasks, Battery, System-Information, CPU, Memory, Storage.",
    author="S3R43o3",
    options={'build_exe': {'include_files': files}},
    executables= [target]
)