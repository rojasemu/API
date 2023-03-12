
import os
#os.system('Xvfb :1 -screen 0 1600x1200x16  &')    # create virtual display with size 1600x1200 and 16 bit color. Color can be changed to 24 or 8
#os.environ['DISPLAY']=':1.0'    # tell X clients to use our virtual DISPLAY :1.0.

from fastapi import FastAPI, HTTPException


from webdriver import *
from webdriverusa import *
from webdriveruk import *


from app.routers import k1000_corta, hola, k3203, wix, k2062,  k1092, k7341, descalificador_usa, descalificador_uk, k23, k1098
from app.routers import k11052, k3906, k15293, k17564, k2066, k1091, ktmr


app = FastAPI()

#Saltador
app.include_router (hola.router)
app.include_router (wix.router)


#Bots
app.include_router (k1000_corta.router)
#app.include_router (k1000_larga.router)
app.include_router (ktmr.router)
app.include_router (k23.router)
app.include_router (k1091.router)
app.include_router (k1092.router)
app.include_router (k1098.router)
#app.include_router (k2001.router)
app.include_router (k2062.router)
app.include_router (k2066.router)
app.include_router (k3203.router)
app.include_router (k3906.router)
app.include_router (k7341.router)
app.include_router (k11052.router)
app.include_router (k15293.router)
app.include_router (k17564.router)

#Descalificadores
app.include_router (descalificador_usa.router)
app.include_router (descalificador_uk.router)
  
  
    


    







