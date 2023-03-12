from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.routers.schemas import *


router = APIRouter (    
    prefix= "/k2001"
    #tags= ["Kmils"]
)


@router.get("/2/{psid}", status_code=200)
def  k2001mala(psid) :
 
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept   
        driver.delete_all_cookies()   
        
        wait = WebDriverWait(driver, 10)
        url="https://iq-dist-2.com/s/start/en-us/pPXZRYM1SCaFUcoxwyGizQ/woL-o6kCT4W0zZyTlmHIrA?&psid="+psid+"**&_k=2001"   
        driver.get(url)
        
        
        wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Start"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(3) .delta"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(2) .delta"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
       
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".mc-buttons-container"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(5) > label"))).click()
      
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(2) > label"))).click()
       
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(5) > label"))).click()
       
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
       
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(6) .delta"))).click()
       
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(4) > label"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
              
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Completed an online shopping order')]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(6) > input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(6) > input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(6) > input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(6) > input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(5) > td:nth-child(6) > input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(6) > input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(6) > input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(8) > td:nth-child(6) > input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(9) > td:nth-child(6) > input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(10) > td:nth-child(6) > input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(11) > td:nth-child(6) > input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(6) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(4) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Treasuries and other government notes')]"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(5) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'I am worried that cryptocurrencies are associated with criminal activity')]"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'I can use cryptocurrency to purchase products in a way that is faster or cheaper than paying with cash and credit / debit cards')]"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
       
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Kraken')]"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
    
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(6)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(6)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(6) > input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(6)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(5) > td:nth-child(6)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(6)"))).click()#5
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(6)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(8) > td:nth-child(6)"))).click()#3
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(9) > td:nth-child(6) > input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(2) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()    
                
       
             
        jumper = driver.current_url            
        value= {"jumper":jumper}
        
              
        time.sleep(0.5)    
        return  JSONResponse(content=value)  
        
    
    
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="Kmil no encontrado Error 404")
    
    
    finally:
    
        driver.quit() 
     
    
    
    
    
    
    
    
    
    
    
    
    
