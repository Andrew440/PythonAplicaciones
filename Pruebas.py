import sys
import subprocess as sub
import pyautogui as pyau #me sirve para escribir cosas o hacer enterp 
import pywinauto as pywin #detector de ventanas
from   pywinauto import Desktop
import time
import atexit

#ruta del ejecutable del navegador o de la aplicacion
#navegator=      r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
##telegram =      r"C:\Users\perezduran.11\AppData\Roaming\Telegram Desktop\Telegram.exe"
#OneNote=        r"C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE"
#OutLook=        r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"
#Teams=          r"C:\Users\perezduran.11\AppData\Local\Microsoft\Teams\current\Teams.exe"
SQL=            r"C:\Program Files (x86)\Microsoft SQL Server Management Studio 19\Common7\IDE\Ssms.exe"
Vscode=         r"C:\Users\perezduran.11\AppData\Local\Programs\Microsoft VS Code\Code.exe"
#TerminadosBMS = r"\\TPCCP-AP35\People_Analytics\Nathalya Hernandez\Reporte de Seguridad\RPA Base de Terminados BMS"
#AplicativoEdgar= r"C:\Users\perezduran.11\OneDrive - Teleperformance\QUERY'S\Aplicativo Edgar.sql"

##ejecuta la aplicacion indicada
#sub.Popen(navegator)
##
###espera antes de ejecutar el otro proceso
#print("se logró abrir Navegador Edge")
#time.sleep(2)
##
###ejecuta la aplicacion indicada
##sub.Popen(telegram)
##
###espera antes de ejecutar el otro proceso
#print("se logró abrir Telegram")
#time.sleep(2)
##
###ejecuta la aplicacion indicada
#sub.Popen(OneNote)
##
###espera antes de ejecutar el otro proceso
#print("se logró abrir OneNote")
#time.sleep(10)
## Maximiza la ventana de OneNote
#pyau.hotkey('win', 'up')
##
###ejecuta la aplicacion indicada
#sub.Popen(OutLook)
#
##
###espera antes de ejecutar el otro proceso
#print("se logró abrir OutLook")
#time.sleep(25)
##
#
##bajar todas las ventanas
#pyau.hotkey('win', 'm')

#ejecuta la aplicacion indicada
#sub.Popen(SQL)
#
##espera antes de ejecutar el otro proceso
#print("se logró abrir SQL")
##
## esperar hasta que la ventana aparezca
#time.sleep(30)
#
#pyau.press('enter')
## esperar hasta que la ventana aparezca
time.sleep(5)


# Obtiene la barra de tareas de Windows
taskbar = Desktop(backend="uia").window(title='Barra de tareas')
#
#
# # Encuentra el icono de SQL Server Management Studio en la barra de tareas
ssms_icon = taskbar.child_window(title_re='SQL Server Management Studio 19', control_type='Button')
#
## Haz clic derecho en el icono
ssms_icon.click_input(button='right')
#main_window = pywin.w (title="SQL Server Management Studio 19")
#main_window.set_focus()
#main_window.type_keys("^o")  # Esto simula presionar Ctrl + O para abrir un archivo
#
## Esperar a que aparezca el cuadro de diálogo "Abrir archivo"
#open_dialog = pywin.window(title="Abrir archivo")
#
## Ingresa la ruta del archivo SQL que deseas abrir y presiona Enter
#archivo_sql = r"C:\Users\perezduran.11\OneDrive - Teleperformance\QUERY'S\Back Querys Tips.sql"
#open_dialog.type_keys(archivo_sql)
#open_dialog.type_keys("{ENTER}")
#

# Espera para que aparezca el menú contextual
time.sleep(2)

# Selecciona la primera opción (puede variar según la configuración)
pyau.press('down')
pyau.press('enter')

# Espera antes de hacer clic izquierdo (puede variar según la velocidad de tu sistema)
time.sleep(1)

# Obtiene la barra de tareas de Windows
taskbar = Desktop(backend="uia").window(title='Barra de tareas')

# Encuentra el icono de SQL Server Management Studio en la barra de tareas
ssms_icon = taskbar.child_window(title_re='Visual Studio Code', control_type='Button')

# Haz clic derecho en el icono
ssms_icon.click_input(button='Left')
pyau.click()
print("se logró abrir VS Code")
time.sleep(5)

# Obtiene la barra de tareas de Windows
taskbar = Desktop(backend="uia").window(title='Barra de tareas')

# Encuentra el icono de SQL Server Management Studio en la barra de tareas
ssms_icon = taskbar.child_window(title_re='Microsoft Teams classic', control_type='Button')
# Haz clic derecho en el icono
ssms_icon.click_input(button='Left')
pyau.click()
print("se logró abrir Teams")
time.sleep(5)

##ejecuta la aplicacion indicada
#ruta_archivo = r"\\TPCCP-AP35\People_Analytics\Nathalya Hernandez\Reporte de Seguridad\RPA Base de Terminados BMS\DescargaBMS.exe"


# Llamar y ejecutar el archivo .exe
#output = sub.check_output(ruta_archivo,creationflags=sub.CREATE_NEW_CONSOLE) #shell=True)
#print("El subprocesso se ejecutó correctamente.")

#espera antes de ejecutar el otro proceso
#print("se logró abrir PythonTerminadosBMS")
#time.sleep(10)

# Haz clic izquierdo en la opción seleccionada
#pyau.click()
print("Todas las aplicaciones abiertas, que tengas feliz dia Edu")


print(input("Presione Cualquier tecla para salir."))


#sys.exit()
#atexit.register(minimize_windows)
