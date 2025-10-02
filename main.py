# %%
# -----------------------------
# IMPORTACIONES NECESARIAS
# -----------------------------
import sys
import subprocess as sub  # Ejecutar programas externos
import pyautogui as pyau  # Automatizar teclado, mouse, pantallas
import pywinauto as pywin  # Interactuar con GUI de Windows
from pywinauto import Desktop  # Acceder a la interfaz de Windows
import time  # Manejo de tiempos
import atexit  # Registrar funciones que se ejecuten al salir
import os
import pandas as pd
import numpy as np
import datetime as dt
import pyperclip as pc  # Acceso al portapapeles
import win32com.client as win32  # Automatización de aplicaciones de Office
import pygetwindow as gw  # Obtener y manejar ventanas activas

# %%
# -----------------------------
# RUTAS DE APLICACIONES A UTILIZAR
# -----------------------------
navegator = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
SQL20 = r"C:\Program Files (x86)\Microsoft SQL Server Management Studio 20\Common7\IDE\Ssms.exe"
Vscode = r"C:\Users\perezduran.11\AppData\Local\Programs\Microsoft VS Code\Code.exe"
#OutLook = r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"

# %%
# -----------------------------
# ABRIR WINDOWS MEDIA PLAYER
# -----------------------------
try:
    taskbar = Desktop(backend="uia").window(title='Barra de tareas')
    ssms_icon = taskbar.child_window(title_re='Windows Media Player', control_type='Button')
    ssms_icon.click_input(button='right')
    time.sleep(2)
    pyau.press('enter')  # Ejecuta la primera opción (reproducir, por lo general)
    time.sleep(1)
    print("Video de Windows Media Player Listo")
except Exception as ex:
    print("No se pudo abrir el reproductor de Windows Media por el error: ", ex)

# %%
# -----------------------------
# ABRIR MICROSOFT EDGE
# -----------------------------
try:
    sub.Popen(navegator)
    print("se logró abrir Navegador Edge")
    time.sleep(2)
except Exception as ex:
    print("No se pudo abrir el navegador Edge por el error: ", ex)

# %%
# -----------------------------
# ABRIR VISUAL STUDIO CODE
# -----------------------------
try:
    taskbar = Desktop(backend="uia").window(title='Barra de tareas')
    ssms_icon = taskbar.child_window(title_re='Visual Studio Code', control_type='Button')
    ssms_icon.click_input(button='Left')
    print("se logró abrir VS Code")
    time.sleep(5)
except Exception as ex:
    print("No se pudo abrir Visual Studio Code por el error: ", ex)

# %%
# -----------------------------
# ABRIR TEAMS
# -----------------------------
try:
    taskbar = Desktop(backend="uia").window(title='Barra de tareas')
    ssms_icon = taskbar.child_window(title_re='Microsoft Teams', control_type='Button')
    ssms_icon.click_input(button='Left')
    time.sleep(15)  # Espera a que Teams termine de cargar
    #pyau.hotkey('win', 'm')  # Minimiza todas las ventanas
    print("se logró abrir Teams")
    time.sleep(10)
except Exception as ex:
    print("No se pudo abrir Teams por el error: ", ex)

# %%
# -----------------------------
# ABRIR OUTLOOK
# -----------------------------
try:
    ###ejecuta la aplicacion indicada
    #sub.Popen(OutLook)
    ###espera antes de ejecutar el otro proceso
    #print("se logró abrir Outlook")
    #time.sleep(2)
    # Obtiene la barra de tareas de Windows
    taskbar = Desktop(backend="uia").window(title='Barra de tareas')
    # Encuentra el icono de SQL Server Management Studio en la barra de tareas
    ssms_icon = taskbar.child_window(title_re='Outlook ', control_type='Button')
    #ssms_icon = taskbar.child_window(title_re='Visual Studio Code', control_type='Button')
    # Haz clic derecho en el icono
    ssms_icon.click_input(button='Left')
    #pyau.click()
    time.sleep(15)
    #pyau.hotkey('win', 'm')
    print("se logró abrir Outlook")
    time.sleep(10)
except Exception as ex:
    print("No se pudo abrir Outlook por el error: ", ex)

# %%
# -----------------------------
# ABRIR SQL SERVER MANAGEMENT STUDIO Y CONECTAR AUTOMÁTICAMENTE
# -----------------------------
try:
    pyau.hotkey('win', 'm')  # Minimiza todo
    sub.Popen(SQL20)
    print("Ejecutando SQL Server Management Studio...")

    # Esperar hasta detectar la ventana de "Connect to Server"
    timeout = 360 ### 3 Minutos
    t0 = time.time()
    ventana_encontrada = False

    while time.time() - t0 < timeout:
        ventanas = gw.getWindowsWithTitle("Connect to Server")
        if ventanas:
            ventana_encontrada = True
            print("Ventana de conexión detectada.")
            break
        time.sleep(1)

    if not ventana_encontrada:
        raise Exception("No se detectó la ventana de conexión dentro del tiempo esperado.")

    time.sleep(1)
    pyau.press('enter')  # Confirmar la conexión
    print("Se conectó automáticamente.")

except Exception as ex:
    print("No se pudo abrir SQL por el error:", ex)


# -----------------------------
# ABRIR QUERY DESDE BARRA DE TAREAS EN SSMS
# -----------------------------
try:
    time.sleep(10)  # Dar tiempo a que SSMS esté listo
    taskbar = Desktop(backend="uia").window(title='Barra de tareas')
    ssms_icon = taskbar.child_window(title_re='SQL Server Management Studio', control_type='Button')
    ssms_icon.click_input(button='right')
    time.sleep(2)
    pyau.press('enter')  # Selecciona la primera opción del menú contextual
    time.sleep(1)
    print("Se dejó abierto el primer query de la lista")
except Exception as ex:
    print("No se pudo abrir Query por el error: ", ex)

# %%
# -----------------------------
# RESTAURAR CONSOLA FINAL AL TERMINAR TODO
# -----------------------------
try:
    pyau.hotkey('win', 'm')  # Minimiza todo de nuevo
    
    # Buscar la ventana del .exe
    #ventanas_console = gw.getWindowsWithTitle(r"C:\Users\perezduran.11\Desktop\AbrirAplicaciones.exe")
    ventanas_console = gw.getWindowsWithTitle("AbrirAplicacion")
    if ventanas_console:
        ventana = ventanas_console[0]
        ventana.restore()  # Restaurar la ventana si está minimizada
        ventana.activate()  # Llevarla al frente
        print("Se logró dejar la ventana de la consola visible.")
    else:
        print("No se encontró la ventana de la consola.")
    print(input("Presione Cualquier tecla para salir."))
except Exception as ex:
    print("No se pudo abrir la consola por el error:", ex)
