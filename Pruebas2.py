
import sys
import subprocess as sub
import pyautogui as pyau #me sirve para escribir cosas o hacer enterp 
import pywinauto as pywin #detector de ventanas
from   pywinauto import Desktop
import time
import atexit

navegator=      r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
OutLook=        r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"


# Obtiene la barra de tareas de Windows
taskbar = Desktop(backend="uia").window(title='Barra de tareas')

# Encuentra el icono de SQL Server Management Studio en la barra de tareas
ssms_icon = taskbar.child_window(title_re='Visual Studio Code', control_type='Button')

# Haz clic derecho en el icono
ssms_icon.click_input(button='Left')
#pyau.click()
print("se logró abrir VS Code")
time.sleep(5)

# Obtiene la barra de tareas de Windows
taskbar = Desktop(backend="uia").window(title='Barra de tareas')

# Encuentra el icono de SQL Server Management Studio en la barra de tareas
ssms_icon = taskbar.child_window(title_re='Microsoft Teams', control_type='Button')
#ssms_icon = taskbar.child_window(title_re='Visual Studio Code', control_type='Button')
# Haz clic derecho en el icono
ssms_icon.click_input(button='Left')
#pyau.click()
print("se logró abrir Teams Clasico")
time.sleep(10)

# Espera unos segundos para que aparezca la opción de abrir el nuevo Teams
time.sleep(5)

# Encuentra las coordenadas del botón en el que quieres hacer clic
#button_x, button_y = pyau.locateCenterOnScreen(r'C:\Users\perezduran.11\Desktop\Python Applications\NuevoTeams.PNG')
## Haz clic en las coordenadas identificadas
#pyau.click(button_x, button_y)
#print("se logró abrir Teams Nuevo")
#time.sleep(5)

#bajar todas las ventanas

# Obtiene la barra de tareas de Windows
taskbar = Desktop(backend="uia").window(title='Barra de tareas')

# Encuentra el icono de Windows Media Player en la barra de tareas
ssms_icon = taskbar.child_window(title_re='Windows Media Player', control_type='Button')

# Haz clic derecho en el icono
ssms_icon.click_input(button='right')

# Espera para que aparezca el menú contextual
time.sleep(2)

# Selecciona la primera opción (puede variar según la configuración)
#pyau.press('down')---> la idea es escoger el primero en la lista pero tuve que quitarlo porque elegia la segunda
pyau.press('enter')

# Espera antes de hacer clic izquierdo (puede variar según la velocidad de tu sistema)
time.sleep(1)

print("Video de Windows Media Player Listo")


pyau.hotkey('win', 'm')


# Haz clic izquierdo en la opción seleccionada
#pyau.click()
print("Todas las aplicaciones abiertas, que tengas feliz dia Edu")


print(input("Presione Cualquier tecla para salir."))


#sys.exit()
#atexit.register(minimize_windows)

