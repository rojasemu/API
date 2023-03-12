from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.routers.schemas import *


router = APIRouter (    
    prefix= "/k3906"
    #tags= ["Kmils"]
)


@router.get("/1/{psid}", status_code=200)
def  k3906(psid) :
 
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept   
        driver.delete_all_cookies()   
        
        wait = WebDriverWait(driver, 10)
        url="https://nbcsportsresearch.iad1.qualtrics.com/jfe/form/SV_0pU7og5aqRgZJeC?psid="+psid+"**&_k=3906"   
        driver.get(url)
        
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#QID48-1-label > span"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        wait.until(ec.visibility_of_element_located((By.ID, "QID1-3-label"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(1) > .c4 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(2) > .c4 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(3) > .c4 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(4) > .c4 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(5) > .c4"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bottom > .c4 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "QR~QID49"))).click()
        dropdown = driver.find_element(By.ID, "QR~QID49")
        dropdown.find_element(By.XPATH, "//option[. = 'California']").click()
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'NFL live on TV')]"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(1) > .c4 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(2) > .c5 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(3) > .c5 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(4) > .c4 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bottom > .c4"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()
        
        time.sleep(1)   
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Barclays')]"))).click()
      
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()
        
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(1) > .c4 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(2) > .c5"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(3) > .c6 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(4) > .c7"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bottom > .c8 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()
        
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(1) > .c4"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(2) > .c5 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(3) > .c6 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(4) > .c7 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bottom > .c8"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()
        
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#QID5-5-label > span"))).click()    
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()  
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#QID55-1-label > span"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()  
        time.sleep(1)                                          
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(1) > .c4 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(2) > .c5"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(3) > .c6"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(4) > .c7"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bottom > .c8 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()   
           
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Barclays')]"))).click() 
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()
                                                 
        
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(1) > .c4 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(2) > .c5"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(3) > .c6"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(4) > .c7"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bottom > .c8 > .q-radio"))).click()                                         
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()  
        
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(1) > .c4 > .q-radio"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(2) > .c5"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(3) > .c6"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ChoiceRow:nth-child(4) > .c7"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bottom > .c8 > .q-radio"))).click()                                         
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()   
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#QID62-1-label > span"))).click() 
        wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()                                       
        time.sleep(3)    
             
        jumper = driver.current_url            
        value= {"jumper":jumper}
        
              
        time.sleep(0.5)    
        return  JSONResponse(content=value)  
        
    
    
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="Kmil no encontrado Error 404")
    
    
    finally:
    
        driver.quit() 
     
    
    
    
    
    
    
    
    
    
    
    
    
