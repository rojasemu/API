from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.routers.schemas import *


router = APIRouter (    
    prefix= "/k15293"
    #tags= ["Kmils"]
)


@router.get("/1/{psid}/{pid}", status_code=200)
def  k15293(psid, pid) :
 
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept   
        driver.delete_all_cookies()   
        
        wait = WebDriverWait(driver, 10)
        url="https://d444.keyingress.de/?i_survey=23__f88c1ce6d02632fac2527ad9b9f8c9b2&PSID="+psid+"**&PID="+pid+"&_k=15293"   
        driver.get(url)
        
        
        
        
        wait.until(ec.visibility_of_element_located((By.ID, "Q5A1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "Q5A1"))).send_keys("2")
        wait.until(ec.visibility_of_element_located((By.ID, "Q5A2"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "Q5A2"))).send_keys("0")
        wait.until(ec.visibility_of_element_located((By.ID, "Q5A3"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "Q5A3"))).send_keys("0")
        wait.until(ec.visibility_of_element_located((By.ID, "Q5A4"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "Q5A4"))).send_keys("2")
        wait.until(ec.visibility_of_element_located((By.ID, "Q5A5"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "Q5A5"))).send_keys("0")
        wait.until(ec.visibility_of_element_located((By.ID, "Q5A6"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "Q5A6"))).send_keys("0")
        wait.until(ec.visibility_of_element_located((By.ID, "btn_send_ahead"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "answer_td_text_Q8A1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_send_ahead"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "Q9A1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "Q9A1"))).send_keys("38")
        wait.until(ec.visibility_of_element_located((By.ID, "btn_send_ahead"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "inputQ11"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "inputQ11"))).send_keys("ca")
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "Q11A6"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_send_ahead"))).click()
        
            
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Marvel Universe')]"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_send_ahead"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "Q22A7_1_0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_send_ahead"))).click()
        

        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='answer_tr_Q24A1']/td[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='answer_tr_Q24A3']/td[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='answer_tr_Q24A2']/td[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='answer_td_form_Q24A4']"))).click()
            
        
        wait.until(ec.visibility_of_element_located((By.ID, "btn_send_ahead"))).click()
          

        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Hearthstone')]"))).click()
     
        wait.until(ec.visibility_of_element_located((By.ID, "btn_send_ahead"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Special offers')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'A more mature version of the game')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Lower price')]"))).click()
         
        wait.until(ec.visibility_of_element_located((By.ID, "btn_send_ahead"))).click()
    
        
        wait.until(ec.visibility_of_element_located((By.ID, "Q60A3"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_send_ahead"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "Q61A1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_send_ahead"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "answer_td_form_Q62A8"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_send_ahead"))).click()
        time.sleep(1.7)
        jumper = driver.current_url            
        value= {"jumper":jumper}
        
              
        time.sleep(0.5)    
        return  JSONResponse(content=value)  
        
    
    
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="Kmil no encontrado Error 404")
    
    
    finally:
    
        driver.quit() 
     
    
    
    
    
    
    
    
    
    
    
    
    
