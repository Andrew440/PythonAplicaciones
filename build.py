# pip install pyinstaller
import PyInstaller.__main__

########IMPORTANTE: Copiar el archivo app.ico en la carpeta donde tenemos el proyecto antes de ejecutar. 


def build():
  PyInstaller.__main__.run([
    '--name=%s' % "AbrirAplicaciones",  #el nombre que llevará el .exe
    ['--onedir', '--onefile'][1], 
    '--noconfirm',
    ['--windowed', '--console'][1],
    '--paths=%s' % '.\\', # . is the dir of the entry file.
    '--hidden-import=pyodbc',
    # '--hidden-import=plyer'
    '--hidden-import=plyer.platforms.win.notification',
    # '--hidden-import=%s' % r'scripts.win32xl', # Manually add a package to handle module not found. Not necessary but an option to keep in mind.
    '--distpath=%s' % r'.\dist',   # where will you build the file
    '--workpath=%s' % r'.\build',   # where to put your output file
    # '--specpath=%s' % r'C:\py',
    '--exclude-module=matplotlib',
    '--exclude-module=qt5',
    '--exclude-module=qt4',
    '--exclude-module=ipython', # module name to exclude
    '--exclude-module=jedi', # module name to exclude
    # '--exclude-module=pandas',
    '--exclude-module=tkinter',
    # '--exclude-module=sqlalchemy',
    # '--exclude-module=sqlite3',
    '--icon=.\\Assasins.ico',
    # "--add-data=%s" % media_dir + ";media",    # where to copy from ; where to copy to
    # "--add-data=%s" % "./.env/Lib/site-packages/selenium/webdriver/remote;selenium/webdriver/remote",
    # "--add-binary=./geckodriver.exe;.", # External dependency setup
    #"--add-binary=.\\pifolderscanner\conn_string.txt;.", # External dependency setup
    # '--collect-all=%s' % r'auditor.py',
    # '--debug=imports',
    '.\\main.py',  # Entrance file

  ])

if __name__ == '__main__':
  build()
