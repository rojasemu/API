from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.routers.schemas import *


router = APIRouter (    
    prefix= "/k17564"
    #tags= ["Kmils"]
)


@router.get("/1/{psid}/{hash}", status_code=200)
def  k17564(psid, hash) :
 
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept   
        driver.delete_all_cookies()   
        
        wait = WebDriverWait(driver, 10)
        url="https://dkr1.ssisurveys.com/projects/end?rst=1&psid="+psid+"**&_k=17564&_s="+hash   
        driver.get(url)
        
             
        jumper = driver.current_url            
        value= {"jumper":jumper}
        
              
        time.sleep(0.5)    
        return  JSONResponse(content=value)  
        
    
    
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="Kmil no encontrado Error 404")
    
    
    finally:
    
        driver.quit() 
     
    
    
    
    
    
    
    
    
    
    
    
    
