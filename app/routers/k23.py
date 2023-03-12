from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder



router = APIRouter (    
    prefix= "/k23"
    #tags= ["Kmils"]
)


@router.get("/1/{ids}/{psid}/{k2}/{pid}", status_code=200)
def  k23(ids, psid, k2, pid) :
 
   
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept   
        driver.delete_all_cookies()   
            
        wait = WebDriverWait(driver, 10)
        url="https://mcg.decipherinc.com/survey/selfserve/53b/g004/220666?list=33&supplier_id=33&idtype=0&country=US&decLang=english&IDS="+ids+"&PID="+pid+"&K2="+k2+"&VID=0&channel=2&ID="+psid+"**#paneles" 
        driver.get(url)
       
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='question_Hbrandassign']/div/div[3]/span/span[2]/label"))).click()    
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()         
        
        wait.until(ec.visibility_of_element_located((By.ID, "slidernumber_ans3066.0.0"))).click()    
        wait.until(ec.visibility_of_element_located((By.ID, "slidernumber_ans3108.0.0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "slidernumber_ans3125.0.0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "slidernumber_ans3142.0.0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "slidernumber_ans3159.0.0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "slidernumber_ans3176.0.0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "slidernumber_ans3193.0.0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "slidernumber_ans3210.0.0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "slidernumber_ans3227.0.0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()    
       
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()    
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//option[. = 'NY']"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "ans2549.0.0"))).send_keys("35")
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='question_Industry']/div/table/tbody/tr[2]/td[2]/table/tbody/tr[5]/td"))).click()
       
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, " //label[contains(text(), 'Male')] "))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'White/Caucasian')]"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "ans2599.0.0"))).send_keys("14225")
        #wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "2"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, " //label[contains(text(), 'No')] "))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, " //label[contains(text(), '5-Ok Experience')]"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()
        time.sleep(6)
        jumper = driver.current_url            
        value= {"jumper":jumper}
        
              
        time.sleep(0.5)    
        return  JSONResponse(content=value)  
        
    
    
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="Kmil no encontrado Error 404")
    
    
    finally:
    
        driver.quit() 
    


    
     
    
    
    
    
    
    
    

    
    
    
    
