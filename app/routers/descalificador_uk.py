from fastapi import APIRouter, HTTPException
from webdriveruk import *
from fastapi.responses import JSONResponse
from threading import Thread
router = APIRouter (    
    prefix= "/Descalificador_Uk"
    #tags= ["Kmils"]
)
@router.get("/1/{ur}")
def Duk(ur):
   
    try:
        driveruk=iniciar_chrome_uk()
        driveruk.delete_all_cookies()  
        
        time.sleep(3)
        #Thread(target=enter_proxy_auth, args=(PROXY_USER, PROXY_PASS)).start()    
        #Thread(target=open_a_page, args=(driveruk,"https://dkr1.ssisurveys.com/projects/pstart?"+url)).start()     
        #Thread(target=open_a_page, args=(driverusa,"https://whoer.net")).start() 
        url= 'https://dkr1.ssisurveys.com/projects/pstart?'+ur
        
        driveruk.get(url)
        
        driveruk.execute_script("window.stop();")  
        #action.send_keys(Keys.ESCAPE)  
        time.sleep(2)
        #driverusa.delete_all_cookies() 
            
        
        #input("pulsar enter para salir")
          
        value={"jumper":"Descalificación Exitosa"}    
        #json_compatible_item_data = jsonable_encoder(value)  
        time.sleep(0.5)    
        return JSONResponse(content=value)  
        
    
    
    except:
        time.sleep(0.5)
        raise HTTPException(status_code=404, detail="Descalificación fallida, Error 404")
    
    
    finally:
    
        driveruk.quit() 