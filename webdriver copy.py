# para instalar automaticamnete chormedriver

from webdriver_manager.chrome import ChromeDriverManager
 #browserproxy

#antibot
#import seleniumwire.undetected_chromedriver as uc
#driver de selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service

#para modificar las opciones de webdriver en Chrome
from selenium.webdriver.chrome.options import Options

# para definir el tipo de busqueda del elemento
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait # para esperar por elementos en selenium
from selenium.webdriver.support import expected_conditions as ec  # para condiciones en selenium
from selenium.common.exceptions import TimeoutException # excepcion de timeot en selenium
#Ventana virtual

import requests
import pyautogui
from threading import Thread
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
from selenium.webdriver.common.action_chains import ActionChains
import time  

''' PROXY_HOST = '192.155.88.198'  # rotating proxy or host
PROXY_PORT = '8728' # port
PROXY_USER = 'MontBlanc17' # username
PROXY_PASS = 'H8vcMWNFjD' # password '''

def iniciar_chrome():
    
    
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "eager" 
    
    # Iniciamos Chorme con los parametros indicados y devuelve el driver
    
    #instalamos la version de chromedriver correspondiente. Nos devuelve la ruta completa del ejecutable
    ruta= ChromeDriverManager(path='./chromedriver').install()# añadimos el Log_level para tener un salida limpia en la terminal
    #ruta= '  C:\\Users\\Rojasemu\\Downloads\\chromedriver_win32\\chromedriver.exe'
    #Opciones de Chrome:
    
   
    options =Options() # instanciamos las opciones de Chrome
    
    user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")#define un user agent personalizado
    
    #options.add_argument("--window-size=1000,1000")# Para configurar el alto y ancho de la ventana donde abriar ael chrome
    #options.add_experimental_option("detach", True)
    ##options.add_argument("--headless")# para que se ejecute chorme sin abrir la ventana
    options.add_argument("--start-maximized") # para maximizar la ventana del chorme
    options.add_argument("--disable-web-security")# deshabilita la politica del mismo origen o Same Origin Policy
    #options.add_argument('--proxy-server={}'.format(PROXY_HOST + ":" + PROXY_PORT)) # Credenciales del proxy
    #options.add_argument("--proxy-server={0}".format(proxy.proxy))
    options.add_argument("--incognito")#Navegador Modo incognito
    #options.add_argument("--disable-extensions")# para que no cargue las extensiones de chrome
    options.add_argument("--disable-notifications")# para bloquear las notificaciones de chrome
    options.add_argument("--ignore-certificate-errors")# para ignorar el aviso "su conexion no es privada"
    options.add_argument("--no-sandbox") # deshabilita el modo sandbox
    options.add_argument("--log-level=3") # para que chormedriver no muestre nada en la terminal
    options.add_argument("--allow-running-insecure-content")# desactiva el aviso de "contenido no seguro"
    options.add_argument("--no-default-browser-check")# Evita el aviso de que chorme no es el navegador predeterminado
    options.add_argument("--no-firts-run") # evita la ejecucion de ciertas tareas que se realizan al iniciar el chorme por primera vez
    options.add_argument("--no-proxy-server")# para no usar proxy sino conexiones directas
    #options.add_argument('--blink-settings=imagesEnabled=false') # deshabilitar la carga de imagenes
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")# Evita que seleniun sea detectado en el navegador  con f12 en consola  chequear navigator.webdriver
    options.add_argument('--disable-gpu')
    options.add_argument("--use-gl=desktop, angle=none")# Evita uso de la gpu
    options.add_argument("--lang=en-US") # aceptar lenguaje en ingles
    #options.add_argument("--use-angle=swiftshader") #Evita uso de la gpu
    options.add_argument("--disable-3d-apis")
    #options.add_argument("--")
    ''' prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs) '''
    #PARAMETROS A OMITIR EN EL INICIO DE CHORME DRIVER
    
    exp_opt = [
        
        'enable-automation', #para que no muestrre la notificacion  "un Software automatizado de prueba esta en chorme"
        'ignore-certificate-errors', #para ignorar errores de certificados (a veces esta caducados)
        'enable-loggin' # para que nos e muestre en la terminal "DevTools  Listening on..."
        ]
    
    options.add_experimental_option ("excludeSwitches" , exp_opt)
    
    # PARAMETROS QUE DEFINEN PREFERENCIAS EN CHORMEDRIVER
    
    prefs= {
        
        "profile.default_content_setting_values.notifications": 2, #notificaciones : 0= preguntar"| 1= permitir | 2= no permitir
        "intl.accept_languages": ['en,en_US'], #para definir el idioma del navegador
        "credentials_enable_service": False # para evitar que chrome nos pregunte si queremos  guadar la contraseña al loguearnos 
        }
    options.add_experimental_option("prefs", prefs )
    
    '''  
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    options.add_experimental_option('excludeSwitches', ['ignore-certificate-errors']) '''
   
    # instanciamos el servicio de chromedriver
    
   
    s= Service(ruta)
    #instanciamos webdriver de selenium con chorme
    driver= webdriver.Chrome(service=s, options=options, desired_capabilities=capa) # añadimos el argumento OPTIONS  desired_capabilities=capa
    #devolvemos el driver
   
    return driver

