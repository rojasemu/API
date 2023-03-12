from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
router = APIRouter (    
    prefix= "/w"
    #tags= ["Kmils"]
)


@router.get("/wix/{psid}/{pid}/{ord}")
def wix(psid, pid, ord):
    
    try:
    
        driver=iniciar_chrome_bots()
        driver.delete_all_cookies()      
        url="https://online.ssisurveys.com/wix/4/p6845224.aspx?__extsid__=G7CtaTKM%2fMYgmAPZcDQRRxIlSjobyiOeVAPW5%2b7BZY6L7tUzHJfGmmACr%2fOcJzzdZroSh5Hf%2bFC7jttr1mxOc7LKmhgfnc7mP%2fFitX0hNuU%3d&PID="+pid+"&&psid="+psid+"**subpanelid=180&sc=11&country=27&l=&ORD="+ord 
        #url= "https://online.ssisurveys.com/wix/4/p6845224.aspx?__extsid__=G7CtaTKM%2fMYgmAPZcDQRRxIlSjobyiOeVAPW5%2b7BZY6L7tUzHJfGmmACr%2fOcJzzdZroSh5Hf%2bFC7jttr1mxOc7LKmhgfnc7mP%2fFitX0hNuU%3d&PID="+pid+"&&psid="+psid+"**subpanelid=180&sc=11&country=27&l=&ORD=ORD-778918-L4N5"
        driver.get(url)
        
        #time.sleep(0.5)con proxy    
    
        driver.execute_script("window.stop();")    

        jumper = driver.current_url
        #print(jumper)
        #input("pulsar enter para salir")     
        value= {"jumper":jumper}
        #json_compatible_item_data = jsonable_encoder(value)  
            
               
        time.sleep(0.5)    
        return  JSONResponse(content=value)  
    
    
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="Wix Fallido, Error 404")
    
    
    finally:
    
        driver.quit() 