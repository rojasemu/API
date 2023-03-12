from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.routers.schemas import *



router = APIRouter (    
    prefix= "/k1092"
    #tags= ["Kmils"]
)



@router.get("/1/{psid}/{pid}")
def K1092(psid, pid):
        
    try:    
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept      
        driver.delete_all_cookies()    
            
            
        wait = WebDriverWait(driver, 5)    
        
            

        time.sleep(2)
            
        url= "https://www.surveys.com/start.aspx?SSID=09FB7825-06F7-451A-80F8-E077D7CF0F58&EXTID="+psid+"**&EXTSupplierSourceID=1&EXTSID="+pid+"&_k=1092"
        driver.get(url)
        time.sleep(20)
        
        #print(driver.current_url)
        time.sleep(1)
        cadena=driver.current_url
        ini = 90 #posición inicial de la subcadena
        fin = 126 #posición final de la subcadena (excluida)
        time.sleep(1)
        subcadena = cadena[ini:fin]
        
        
        url2="https://www.surveys.com/EndSurveyRedirect/return.aspx?SurveyName=UKC20120662SP&ID="+subcadena+"&rssc=20"
        driver.get(url2)
        #print(subcadena)
        
        time.sleep(2)
        #input('esperando')
        #driver.set_page_load_timeout(25)      
      
        
        
        
        
           
        
        
         
        jumper=driver.current_url
        print(jumper)
            
            #time.sleep(5)    
            
        value= {"jumper":jumper}
        #json_compatible_item_data = jsonable_encoder(value)  
        time.sleep(0.5)     
        return JSONResponse(content=value)  
        
    
    
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="K1092 no encontrado, Error 404")
    
    
    finally:
    
        driver.quit() 