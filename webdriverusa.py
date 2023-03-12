# para instalar automaticamnete chormedriver
from webdriver_manager.chrome import ChromeDriverManager

#driver de selenium
from selenium.webdriver.common.keys import Keys
#from selenium import webdriver as webdriverusa
from selenium.webdriver.chrome.service import Service
from seleniumwire  import webdriver as webdriverusa
import seleniumwire.undetected_chromedriver as uc
#para modificar las opciones de webdriver en Chrome
from selenium.webdriver.chrome.options import Options

# para definir el tipo de busqueda del elemento
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait # para esperar por elementos en selenium
from selenium.webdriver.support import expected_conditions as ec  # para condiciones en selenium
from selenium.common.exceptions import TimeoutException # excepcion de timeot en selenium
#Ventana virtual


#import pyautogui
from threading import Thread
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
from selenium.webdriver.common.action_chains import ActionChains
import time  

PROXY_HOST = '216.185.48.166'  # rotating proxy or host
PROXY_PORT = '50100' # port
PROXY_USER = 'Seljesusvirus2007' # username
PROXY_PASS = 'JesusMata2323' # password    

def iniciar_chrome_usa():
    
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "normal" 
    #capa ['acceptInsecureCerts'] = True
    # Iniciamos Chorme con los parametros indicados y devuelve el driver
    
    #instalamos la version de chromedriver correspondiente. Nos devuelve la ruta completa del ejecutable
    ruta= ChromeDriverManager(path='./chromedriver').install()# añadimos el Log_level para tener un salida limpia en la terminal
    #ruta= '  C:\\Users\\Rojasemu\\Downloads\\chromedriver_win32\\chromedriver.exe'
    #Opciones de Chrome:
    ''' load_dotenv(find_dotenv()) 
    PROXY_CHEAP_USER = os.environ.get("PROXY_CHEAP_USER")
    PROXY_CHEAP_PW= os.environ.get("PROXY_CHEAP_PW")
    PROXY_HOST = 'proxyhost.com'  # rotating proxy or host
    PROXY_PORT = port # port
    PROXY_USER = PROXY_CHEAP_USER # username
    PROXY_PASS = PROXY_CHEAP_PW # password '''

    options = Options()
    user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")#define un user agent personalizado
    options.add_argument("--disable-popup-blocking"); #deshabilitará el bloqueo de ventanas emergentes,
    #options.add_argument('--headless')
    options.add_argument("--start-maximized")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-web-security")# deshabilita la politica del mismo origen o Same Origin Policy   
    options.add_argument("--incognito")#Navegador Modo incognito
    options.add_argument("--disable-extensions")# para que no cargue las extensiones de chrome
    options.add_argument("--disable-notifications")# para bloquear las notificaciones de chrome
    options.add_argument("--ignore-certificate-errors")# para ignorar el aviso "su conexion no es privada"
    options.add_argument("--no-sandbox") # deshabilita el modo sandbox
    options.add_argument("--log-level=3") # para que chormedriver no muestre nada en la terminal
    options.add_argument("--allow-running-insecure-content")# desactiva el aviso de "contenido no seguro"
    options.add_argument("--no-default-browser-check")# Evita el aviso de que chorme no es el navegador predeterminado
    options.add_argument("--no-firts-run") # evita la ejecucion de ciertas tareas que se realizan al iniciar el chorme por primera vez
    #options.add_argument("--no-proxy-server")# para no usar proxy sino conexiones directas
    #options.add_argument('--blink-settings=imagesEnabled=false') # deshabilitar la carga de imagenes
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")# Evita que seleniun sea detectado en el navegador  con f12 en consola  chequear navigator.webdriver
    options.add_argument('--disable-gpu')
    options.add_argument("--use-gl=desktop, angle=none")# Evita uso de la gpu
    options.add_argument("--lang=en-US") # aceptar lenguaje en ingles
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
    
    options_seleniumWire = {
        'proxy': {
            'https': 'https://Seljesusvirus2007:JesusMata2323@216.185.48.166:50100',
        }
    }
   
    
    s= Service(ruta)
    #instanciamos webdriver de selenium con chorme
    driverusa= webdriverusa.Chrome(service=s, options=options, seleniumwire_options=options_seleniumWire , desired_capabilities=capa) # añadimos el argumento OPTIONS  desired_capabilities=capa
    #devolvemos el driver
    
    return driverusa


    
#def open_a_page(driverusa, url):
#    driverusa.get(url)