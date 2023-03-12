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
            
        url= "https://www.surveys.com/start.aspx?SSID=9910D3DA-1FCF-4656-961C-552F95893BC7&EXTID="+psid+"**&EXTSupplierSourceID=3&EXTSID="+pid+"&_k=1092"
        driver.get(url)
        #driver.set_page_load_timeout(25)      
        time.sleep(20)
        
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(1) .answerlabel"))).click()
        time.sleep(3.5)        
        
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".prettycheckbox > a"))).click()    
        time.sleep(3.5) 

        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(3.5) 

        a= driver.find_element(By.XPATH, "//*[@id='ScreenerKT1_text']/p[1]/span/b")
        
        #print(a.text)
        a=a.text
        #input('esperando')  
        time.sleep(3.5) 

        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
          
        
        
       
        
        
    
        time.sleep(3)
        b=driver.find_element(By.XPATH, "//label[@for='ScreenerKT2_1']")
        b=b.text
        
        c=driver.find_element(By.XPATH, "//label[@for='ScreenerKT2_2']")
        c=c.text
        
        d=driver.find_element(By.XPATH, "//label[@for='ScreenerKT2_3']")
        d=d.text
        
        e=driver.find_element(By.XPATH, "//label[@for='ScreenerKT2_4']")
        e=e.text
        
        f=driver.find_element(By.XPATH, "//label[@for='ScreenerKT2_5']")
        f=f.text
        
        g=driver.find_element(By.XPATH, "//label[@for='ScreenerKT2_6']")
        g=g.text
        
        h=driver.find_element(By.XPATH, "//label[@for='ScreenerKT2_7']")
        h=h.text
        
        i=driver.find_element(By.XPATH, "//label[@for='ScreenerKT2_8']")
        i=i.text
        
        j=driver.find_element(By.XPATH, "//label[@for='ScreenerKT2_9']")
        j=j.text
        
        
        
        
        
        if a == b:
            
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(1) .answerlabel"))).click()
    
        elif a == c:
            
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(2) .answerlabel"))).click()
    
        elif a == d:
            
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(3) .answerlabel"))).click()
        elif a == e:
            
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(4) .answerlabel"))).click()
    
        elif a == f:
            
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(5) .answerlabel"))).click()
    
        elif a == g :
            
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(6) .answerlabel"))).click()
    
        elif a == h:
            
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(7) .answerlabel"))).click()
    
        elif a == i:
            
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(8) .answerlabel"))).click()
    
        elif a == j:
            
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(9) .answerlabel"))).click()
    
        
        
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(3.5)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()       
        time.sleep(3.5)       
        wait.until(ec.visibility_of_element_located((By.ID, "GenderIdentity_1_label"))).click()
        time.sleep(3.5)
        wait.until(ec.visibility_of_element_located((By.ID, "Transgender_2_label"))).click()
        time.sleep(3.5)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(3.5)        
        wait.until(ec.visibility_of_element_located((By.ID, "age_1"))).send_keys("31")
        time.sleep(3.5)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(5)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(2) .answerlabel"))).click()
        time.sleep(3)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "EmpSt_1_label"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "FFUse30D_header1"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x1 #FFUse30D_header1"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x2 #FFUse30D_header2"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x3 #FFUse30D_header1"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "MarSt2_2_label"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgAll:nth-child(5) > .sgCT:nth-child(1) .answerlabel"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "SizeAgeHH2_2"))).click()
        time.sleep(3.5)   
        wait.until(ec.visibility_of_element_located((By.ID, "SizeAgeHH2_2"))).clear()     
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "SizeAgeHH2_2"))).send_keys("1")
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "SizeAgeHH2_5"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "SizeAgeHH2_5"))).clear()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "SizeAgeHH2_5"))).send_keys("1")
        time.sleep(25)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "ZIPC1x1"))).send_keys("90004")
        time.sleep(30)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "AnnualHHInco_5_label"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "Educ2_4_label"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(3.5) 
        
        wait.until(ec.visibility_of_element_located((By.ID, "SurveyDev2_1_label"))).click()
        time.sleep(3.5) 
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(3.5) 
        
        wait.until(ec.visibility_of_element_located((By.ID, "RandBDQ"))).send_keys("good")
        time.sleep(40)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(3.5)      
        wait.until(ec.visibility_of_element_located((By.ID, "comments"))).send_keys("good is very nice")
        time.sleep(45)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        
        
        
           
        
        
         
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