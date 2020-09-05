# from cx_Freeze import setup, Executable
import os.path
from os import path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
sprites_dir = path.join(path.dirname(__file__), 'sprites')
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
build_exe_options = {"packages": ["os", "pygame", "turtle"]}
options = {
    'build_exe': {
        'include_files': (
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            sprites_dir,
        ),
        "packages": ["os", "pygame", "turtle"]
    },
}

setup(
    name="Return to Eden",
    version="0.1",
    # options={"build_exe": build_exe_options},
    # description="",
    executables=[Executable("Intro.py")]

    )
