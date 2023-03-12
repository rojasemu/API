from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
router = APIRouter (    
    prefix= "/k1000"
    #tags= ["Kmils"]
)


@router.get("/2/{psid}/{pid}")
def k1000(psid, pid):
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept      
        driver.delete_all_cookies()    
        
        
        wait = WebDriverWait(driver, 10)
    
        url= "https://survey-d.dynata.com/survey/selfserve/53c/2204164?list=2&psid="+psid+"**&pid="+pid+"&C=2&W=1&decLang=english&sp=181&pp=0&sc=3&ppid=#Paneles"
        #url= 'https://survey-d.dynata.com/survey/selfserve/53c/2204164?list=2&psid=jnlxvE9Cn7pmOtLfhwwto**&pid=304572439&C=2&W=1&decLang=english&sp=181&pp=0&sc=3&ppid=#Paneles'
        driver.get(url)
        
        time.sleep(2)
        try:
            wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()   
        
        except:
            wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()
        
        '''  driver.find_element(By.ID, "ans10098.0.0").click()
        time.sleep(2) '''
        wait.until(ec.visibility_of_element_located((By.XPATH, "//option[. = '48']"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click() 
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".element:nth-child(14) .fir-selected"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click() 
    
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'more')]"))).click()  
    
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click() 
    
        time.sleep(0.2)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".element:nth-child(4) label"))).click()    
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click() 
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(1) > .cell:nth-child(2)"))).click()    
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row-elements:nth-child(2) > .cell:nth-child(2)"))).click()   
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(3) > .cell:nth-child(3) .fir-selected"))).click()    
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(4) > .cell:nth-child(4) .fir-selected"))).click()     
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(5) > .cell:nth-child(5) .fir-selected"))).click()    
        
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()   
        time.sleep(0.2)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(1) > .cell:nth-child(2)"))).click()   
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row-elements:nth-child(2) > .cell:nth-child(2)"))).click()  
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(3) > .cell:nth-child(3) .fir-selected"))).click()    
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(4) > .cell:nth-child(4) .fir-selected"))).click()     
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(5) > .cell:nth-child(5) .fir-selected"))).click()    
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()    
        time.sleep(0.2)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".element:nth-child(3) .rounded"))).click()
    
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click() 
    
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".element:nth-child(8) .rounded"))).click()
    
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click() 

        wait.until(ec.visibility_of_element_located((By.ID, "ans7628.0.0"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "ans7628.0.0"))).send_keys("forex")
        
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click() 
    
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "img[title ='FOREX.com']"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click() 
    
        time.sleep(2)
        #quedamos aqui
        wait.until(ec.visibility_of_element_located((By.XPATH, "//td[2]"))).click()
    
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()    
        
        time.sleep(2) 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='question_Q4']/div[1]/div[1]/div[2]/ul/li[2]"))).click()
        
        time.sleep(2) 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='question_Q5']/div/div/div[2]/div[2]/span[10]"))).click()    
    
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click() 
    
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".sq-cardsort-bucket-item-c2").click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Next')]"))).click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".sq-cardsort-bucket-item-c2").click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Next')]"))).click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".sq-cardsort-bucket-item-c2").click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Next')]"))).click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".sq-cardsort-bucket-item-c2").click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Next')]"))).click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".sq-cardsort-bucket-item-c2").click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Next')]"))).click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".sq-cardsort-bucket-item-c2").click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Next')]"))).click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".sq-cardsort-bucket-item-c2").click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Next')]"))).click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, ".sq-cardsort-bucket-item-c2").click()    
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Next')]"))).click()
        time.sleep(3)
        '''  driver.find_element(By.CSS_SELECTOR, ".sq-cardsort-bucket-item-c2").click()    
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Next')]"))).click()
        '''
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "ans9877.0.0"))).send_keys("yes,ok")
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click() 
        time.sleep(0.5)    
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".odd .rounded"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click() 
    
        time.sleep(2)
        element = driver.find_element(By.ID, "btn_continue")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".odd label"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click() 
        
        time.sleep(3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".odd label"))).click()
        
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()          
        time.sleep(20)    

        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sq-cardsort-bucket-item-c5"))).click()
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sq-cardsort-bucket-item-c4"))).click()
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sq-cardsort-bucket-c5"))).click()
        time.sleep(6)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sq-cardsort-bucket-item-c4"))).click()
        time.sleep(4)
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()   
    
        time.sleep(0.5)
        
        wait.until(ec.visibility_of_element_located((By.ID, "btn_continue", ))).click()   
       
        jumper = driver.current_url
        #print(jumper)
                
               
                
        value= {"jumper":jumper}
        #json_compatible_item_data = jsonable_encoder(value)  
        time.sleep(0.5)        
        return JSONResponse(content=value)  
            
    
    
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="Kmil no encontrado Error 404")
    
    
    finally:
    
        driver.quit() 
    














'''   if wait.until( lambda driver: driver.current_url == "https://survey-d.dynata.com/survey/selfserve/53c/2204164#!)"):
          
        driver.execute_script("window.stop();")
        jumper= driver.find_element(By.XPATH, "//a").get_attribute("href")
        print(jumper)    
        
        return{"jumper":jumper} '''


    #driver.execute_script("window.stop();")
    #driver.execute_script("window.stop();")
    #driver.find_element(By.tagName("body")).sendKeys("Keys.ESCAPE");
    #time.sleep(10)
    #wait.until(ec.url_matches("/2204164?state"))
    #requests.post('https://survey-d.dynata.com/survey/selfserve/53c/2204164#!)',timeout=2.000).close()
   
   # wait.until(ec.url_matches("end"), driver.execute_script("window.stop();") ) 

#https://survey-d.dynata.com/survey/selfserve/53c/2204164?

#//dkr1.ssisurveys.com/projects/end?rst=1&psid=cwuLnLLgPGW4hn5H49vhfd**&high=13099526388689&_k=1000&_s=400bf2e366e60fa04a0bec150b7bee27a4ad258d
 #https://survey-d.dynata.com/survey/selfserve/53c/2204164
  #https://survey-d.dynata.com/survey/selfserve/53c/2204164
  #https://survey-d.dynata.com/survey/selfserve/53c/2204164#!)
#https://survey-d.dynata.com/survey/selfserve/53c/2204164?state=3dd2ce47-d035-4b8d-8f24-4837ad49ca41



#https://survey-d.dynata.com/survey/selfserve/53c/2204164?v2async=speederAutoCheckAPI&state=f04f04cb-2a3b-4724-a70f-9f7d3cf72f4f

#https://dkr1.ssisurveys.com/projects/end?rst=1&psid=4gbuSlIEXGxHJqoxFzh4edQ**&high=13366200336129&_k=1000&_s=48618572321ef9f14f3b37a80abf033c5a4396bb
