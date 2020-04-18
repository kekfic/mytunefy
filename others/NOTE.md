### Command for creating the .exe file

'pyinstaller -D --add-data="exe/ffmpeg.exe;exe" --add-data="exe/ffplay.exe;exe" --add-data="exe/ffprobe.exe;exe"                              --add-data="resources/gif/music1.gif;gif" --icon resources/icons/cuffie.ico .\mytunefy.py'


Note that: setuptools vs > 44.0 is creating trouble when creating the executable file. The error name is: * ModuleNotFoundError: No module named 'pkgresources.py2warn' [16320] *

When creating the executable, for the moment I am adding manually database folder, and resources/gif/ folder. 

I worked around the problem downgrading to 44.0 version. 


### Command for .ui file and .rc

pyside2-uic.exe .\gui_main.ui -o gui_main.py

pyside2-rcc.exe .\icons.qrc -o icon_rc.py

for some reasons, the icon_rc is not imported well in gui_main.py --> I correct it manually as: *from .import iconrc*