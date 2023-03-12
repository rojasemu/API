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
        url= "http://s.morpace.com/V230003_Q1?ID="+psid+"**&Source=2&IDTYPE=0&PASSWORD=0&_k=2066"
        driver.get(url)
        time.sleep(20)      
       
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.11 .mrMultipleText"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.0 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).click()
        num=random.randrange(1,100)
        print(num)
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys(num)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        time.sleep(4)
        #input('esprando') 
        if num >=1 and  num <=20:
            #wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='Cell.0.1']/label"))).click() #Construccion
            #wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='Cell.0.3']/label"))).click()  #Consumer Delivery / Last Mile 
            time.sleep(0.5)   
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Agriculture / Farming')]"))).click()      
            #wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.14 .mrSingleText"))).click()      
        elif num >20 and  num <=40:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Forestry / Lumber')]"))).click()
            
        elif num >40 and  num <=50:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Mining / Quarrying')]"))).click()
            
        elif num >50 and  num <=70:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Energy Services (Extraction, Refinement, Distribution of Oil & Gas, Solar, Wind, or Nuclear)')]"))).click()
            
        elif num >70 and  num <=100:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Utility Services (e.g., Public Utilities) ')]"))).click()
            
        '''         if num >=1 and  num <=20:
            #wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='Cell.0.1']/label"))).click() #Construccion
            #wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='Cell.0.3']/label"))).click()  #Consumer Delivery / Last Mile 
            time.sleep(0.5)   
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Manufacturing')]"))).click()      
            #wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.14 .mrSingleText"))).click()      
        elif num >20 and  num <=40:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Food & Beverage Processing and Distribution')]"))).click()
            
        elif num >40 and  num <=50:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'General Freight')]"))).click()
            
        elif num >50 and  num <=70:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Moving and Storage')]"))).click()
            
        elif num >70 and  num <=100:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Consumer Delivery / Last Mile')]"))).click() '''
            
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        #Cell\.0\.19 > label
        
        time.sleep(0.5)
        
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("1")
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.0 .mrSingleText"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.0 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.0 .mrSingleText"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.2 > label"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.1 .mrSingleText"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).click()
        time.sleep(2.5)
        
        
        if num >=1 and  num <=10:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("10/12/2001")
            wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
            #print('opcion1')
        elif num >10 and  num <=20:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("11/11/1999")
            wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
            #print('opcion2')
        elif num >20 and  num <=30:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("12/10/1975")
            wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
            #print('opcion3')
        elif num >30 and  num <=40:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("13/09/1980")
            wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
            #print('opcion4')
        elif num >40 and  num <=50:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("14/08/1996")
            wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
            #print('opcion4')
        elif num >50 and  num <=60:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("15/07/1986")
            wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
            #print('opcion5')
        elif num >60 and  num <=70:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("16/06/1970")
            wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
            #print('opcion6')
        elif num >70 and  num <=80:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("16/06/1965")
            wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
            
        elif num >80 and  num <=90:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("16/06/1980")
            wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
            #print('opcion7')
        elif num >90 and  num <=100:
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("16/06/1955")
            wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
      
       
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_C"))).click()
        dropdown = driver.find_element(By.ID, "_Q0_C")
        dropdown.find_element(By.XPATH, "//option[. = 'Chevrolet']").click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q1_C"))).click()
        dropdown = driver.find_element(By.ID, "_Q1_C")
        dropdown.find_element(By.XPATH, "//option[. = 'C/K Pickup']").click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q2_C"))).click()
        dropdown = driver.find_element(By.ID, "_Q2_C")
        dropdown.find_element(By.XPATH, "//option[. = '1-5 Vehicles']").click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".mrMultipleText"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.0 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("1")
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_C"))).click()
        dropdown = driver.find_element(By.ID, "_Q0_C")
        
        dropdown.find_element(By.XPATH, "//option[. = 'Chevrolet']").click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q1_C"))).click()
        dropdown = driver.find_element(By.ID, "_Q1_C")
        
        dropdown.find_element(By.XPATH, "//option[. = 'LCF 6500 XD']").click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "label:nth-child(3)"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        #input('esperando 2')
        #wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.10 > label"))).click()
        if num >=1 and  num <=20:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'GMC')]"))).click()
        elif num >20 and  num <=40:    
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'RAM')]"))).click()
        elif num >40 and  num <=60:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Ford')]"))).click()
        elif num >60 and  num <=80:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Tesla')]"))).click()
        else:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Arrival')]"))).click()
        #wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Chevrolet')]"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.3 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
       
       
       
       
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.1 #Cell\\.0\\.10 .scale_bttn_hgt"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.2 #Cell\\.0\\.10 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.3 #Cell\\.0\\.10 .scale_bttn_hgt"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.4 #Cell\\.0\\.10 .scale_bttn_hgt"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.5 #Cell\\.0\\.10 .scale_bttn_hgt"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.6 #Cell\\.0\\.10 > label > span:nth-child(1)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.7 #Cell\\.0\\.10 .scale_bttn_hgt"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.8 #Cell\\.0\\.10 .scale_bttn_hgt"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.9 #Cell\\.0\\.10 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.10 #Cell\\.0\\.10 > label > span:nth-child(1)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.11 #Cell\\.0\\.10 .scale_bttn_hgt"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.12 #Cell\\.0\\.10 .scale_bttn_hgt"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.13 #Cell\\.0\\.10 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.1\\.14 #Cell\\.0\\.10 .scale_bttn_hgt"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.7 .mrMultipleText"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.4 .mrMultipleText"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.4 .mrMultipleText"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.4 .mrMultipleText"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.4 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.4 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.4 .mrMultipleText"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.4 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.4 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.4 .mrMultipleText"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.4 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.4 .mrMultipleText"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.5 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.0 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.3 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.0 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        
       
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.10 .scale_bttn_hgt"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q0_Q0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q0_Q0"))).send_keys("1")
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q1_Q0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q1_Q0"))).send_keys("2")
        wait.until(ec.visibility_of_element_located((By.ID, "Cell.1.2"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q2_Q0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q2_Q0"))).send_keys("3")
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("1")
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.0 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.1 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "fieldset"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".mrQuestionTable"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.0 > label"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.3 .mrSingleText"))).click()
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("1")
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("90006")
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(5)
       
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