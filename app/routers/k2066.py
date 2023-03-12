from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import random
router = APIRouter (    
    prefix= "/k2066"
    #tags= ["Kmils"]
)




@router.get("/1/{psid}")
def k2066(psid):
    
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept  
        driver.delete_all_cookies()      
        wait = WebDriverWait(driver, 10)
        url= "https://w-www.escalentsurvey.co/mrIWeb/mrIWeb.dll?I.Project=S230360_033&id="+psid+"**&panel=3&urlvar3=2&_k=2066"
        driver.get(url)
        time.sleep(3)
             
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
         
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q1_C1"))).click()
       
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
         
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C2"))).click()
       
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q1_C3"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
         
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
         
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
         
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q1_C2"))).click()
         
        wait.until(ec.visibility_of_element_located((By.ID, "_Q2"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "_Q2"))).send_keys("90006")
        
 
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
 
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C3"))).click()
        time.sleep(0.5)
        #input('esperando')
        #time.sleep(0.5) 
        #wait.until(ec.visibility_of_element_located((By.ID, "navnext"))).click()
        time.sleep(0.2) 
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
         
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C9"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
         
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q0_Q0_C0 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q1_Q0_C1 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q2_Q0_C2 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q3_Q0_C3 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q4_Q0_C4 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q5_Q0_C4 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q6_Q0_C4 > span"))).click()
       
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q7_Q0_C4 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        #input('esperando 1')
        
        
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
         
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C2"))).click()
      
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_C7 > img"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
      
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q0_Q0_C1 > span"))).click()
       
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q0_Q0_C0 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        #input('esperando55')
        time.sleep(0.2) 
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
       
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
     
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
       
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0_S0"))).click()
       
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C1_S5"))).click()
     
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C2_S0"))).click()
         
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
         
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q0_Q0"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q0_Q0"))).click()
     
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q0_Q2"))).click()
      
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q0_Q2"))).send_keys("1")
       
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q0_Q3"))).click()
  
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q0_Q3"))).send_keys("30")
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
       
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C1"))).click()
       
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
       
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
         
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
       
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "td"))).click()
     
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
      
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
       
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".myCode"))).click()
      
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
         
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q0_Q0_C0 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
         
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
         
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q0_Q0_C0 > span"))).click()
         
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        
        #input('esperando 2')
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q0_Q0_C0 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q1_Q0_C0"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q1_Q0_C1 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q2_Q0_C2 > span"))).click()
      
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q3_Q0_C2 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q4_Q0_C1 > span"))).click() 
     
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q4_Q0_C0 > span"))).click()
       
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q5_Q0_C0 > span"))).click()
      
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q6_Q0_C1 > span"))).click()
       
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q7_Q0_C1 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q8_Q0_C1 > span"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(0.2) 
        #input('esperando 2')
        time.sleep(0.5)
        '''   
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_Q5_Q0_C1 > span"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click() '''
        #wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q0_Q0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q0_Q0"))).send_keys("50")
        
        #wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q1_Q0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q1_Q0"))).send_keys("50")
       
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "td"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0_S0"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_Q0_Q0_C3"))).click()
         
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
       
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
      
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#span_Q0_C0 > i"))).click()
       
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0_S0"))).click()
         
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
       
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
       
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
         
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
       
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
     
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
      
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
       
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
       
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C0"))).click()
         
        #wait.until(ec.visibility_of_element_located((By.ID, "navnext"))).click()
        time.sleep(0.5) 
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
      
        wait.until(ec.visibility_of_element_located((By.ID, "span_Q0_C1"))).click()
       
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        #input ('esperando')
         
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='span_Q0_C1']"))).click()
        
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        #input('esperando 3')
        time.sleep(2)
       
        jumper = driver.current_url 
        value= {"jumper":jumper}
            #json_compatible_item_data = jsonable_encoder(value)
              
        time.sleep(0.5)    
        return  JSONResponse(content=value)  
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="K2066 no encontrado, Error 404")
    
    
    finally:
    
        driver.quit()   