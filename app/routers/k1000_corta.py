from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.routers.schemas import *
from concurrent.futures import ThreadPoolExecutor

router = APIRouter (    
    prefix= "/k1000"
    #tags= ["Kmils"]
)


@router.get("/1/{psid}/{pid}", status_code=200)
def  k1000C(psid, pid) :
 
   
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept   
        driver.delete_all_cookies()   
        
        wait = WebDriverWait(driver, 10)
        url="https://survey-au.dynata.com/survey/selfserve/53b/2202224?list=2&pid="+pid+"&psid="+psid+"**&C=2&W=1&decLang=english&sp=181&pp=0&sc=3&ppid="   
        driver.get(url)
        
        #params = {"status_code": 302, "url": url}
        #r = requests.get(url, params=params)
        
        
    
                
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".element:nth-child(4) .fir-selected"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()    
        time.sleep(0.5)
        
        wait.until(ec.visibility_of_element_located((By.ID, "ans30405.0.0"))).send_keys("35")
        time.sleep(0.5)

        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()
        time.sleep(0.5)
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Dior')]"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Chanel')]"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Oreal')]"))).click()
        time.sleep(0.5)

    
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()          
        jumper = driver.current_url            
        value= {"jumper":jumper}
        
              
        time.sleep(0.5)    
        return  JSONResponse(content=value)  
        
    
    
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="Kmil no encontrado Error 404")
    
    
    finally:
    
        driver.quit() 
     
    
    
    
    
    
    
    
    
    
    
    
    
