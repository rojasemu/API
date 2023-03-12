from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.routers.schemas import *
#
from selenium.webdriver.common.action_chains import ActionChains

router = APIRouter (    
    prefix= "/k2001"
    #tags= ["Kmils"]
)


@router.get("/1/{psid}", status_code=200)
def  k2001(psid) :
 
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept   
        driver.delete_all_cookies()   
        
        wait = WebDriverWait(driver, 10)
        url="https://iq-dist-2.com/s/start/en-us/VyqPtST0Sl2wZEHOK6tDIA/4u7jhMXUQ1KjNvw35lcgYA?&psid="+psid+"**&_k=2001"   
        driver.get(url)
        
        
        wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Start"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(4) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "id_9424a10900c64f79a87d767d0d2d7003"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "id_9424a10900c64f79a87d767d0d2d7003"))).send_keys("90011")
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        #input('espera')
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(1) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(2) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(3) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(4) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(5) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(6) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(7) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(8) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        #input('esperar 0')
        #wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(6) .delta"))).click()
        
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(1) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(2) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(3) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(4) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(5) .delta"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(6) .delta"))).click()
        
        
        ''' wait.until(ec.visibility_of_element_located((By.XPATH, "//div[text()='Farmer’s market']"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[text()='Online floral delivery service (e.g., 1-800-Flowers, UrbanStems, FTD)']"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[text()='Grocery store / Supermarket (e.g., Kroger, Albertsons, Walmart)']"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[text()='Local florist']"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[text()='Home improvement store (e.g., Lowes)']"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[text()='Warehouse club or wholesale club (e.g., Costco, Sam's Club)']"))).click() '''
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(2) .has-tooltip"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(3) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(4) .has-tooltip"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(5) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "id_27a49b15bea4432994cd796d370e5da5:Customtoyou_arrangement"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".checkbox:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".delta:nth-child(2)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
       
        
        
        
        source1= driver.find_element(By.XPATH, "//*[@id='id_6a1ad8b8dec74085aae6c3805e2d91e3']/li[1]")
        target1 = driver.find_element(By.XPATH, "//*[@id='id_6a1ad8b8dec74085aae6c3805e2d91e3-dest']")
        action = ActionChains(driver)        
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2) 
        source1= driver.find_element(By.XPATH, "//*[@id='id_6a1ad8b8dec74085aae6c3805e2d91e3']/li[1]")
        target1 = driver.find_element(By.XPATH, "//*[@id='id_6a1ad8b8dec74085aae6c3805e2d91e3-dest']")
        action = ActionChains(driver)        
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2)
        source1= driver.find_element(By.XPATH, "//*[@id='id_6a1ad8b8dec74085aae6c3805e2d91e3']/li[1]")
        target1 = driver.find_element(By.XPATH, "//*[@id='id_6a1ad8b8dec74085aae6c3805e2d91e3-dest']")
        action = ActionChains(driver)        
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()       
        
    
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        
        
        #wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[text()='Farmer’s market']"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        
            
        source1= driver.find_element(By.XPATH, "//*[@id='id_31cc54d6e49345e9b9e21c97b17582fd']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_31cc54d6e49345e9b9e21c97b17582fd-dest']")
        action = ActionChains(driver)        
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2) 
        source1= driver.find_element(By.XPATH, "//*[@id='id_31cc54d6e49345e9b9e21c97b17582fd']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_31cc54d6e49345e9b9e21c97b17582fd-dest']")
        action = ActionChains(driver)        
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2)
        source1= driver.find_element(By.XPATH, "//*[@id='id_31cc54d6e49345e9b9e21c97b17582fd']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_31cc54d6e49345e9b9e21c97b17582fd-dest']")
        action = ActionChains(driver)       
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        source1= driver.find_element(By.XPATH, "//*[@id='id_31cc54d6e49345e9b9e21c97b17582fd']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_31cc54d6e49345e9b9e21c97b17582fd-dest']")
        action = ActionChains(driver)        
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2) 
        source1= driver.find_element(By.XPATH, "//*[@id='id_31cc54d6e49345e9b9e21c97b17582fd']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_31cc54d6e49345e9b9e21c97b17582fd-dest']")
        action = ActionChains(driver)        
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2)
        source1= driver.find_element(By.XPATH, "//*[@id='id_31cc54d6e49345e9b9e21c97b17582fd']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_31cc54d6e49345e9b9e21c97b17582fd-dest']")
        action = ActionChains(driver)       
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2)
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click() 
        #input('esperar 2')  
        time.sleep(1.5)    
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "./html/body/main/form/input[3]"))).click() 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='qc7e582f4b624486b937df6b878cba1e9']/ul[1]/li[5]/label"))).click()        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click() 
        
        '''   try:
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click() 
        except: '''
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        
        #input('esperar 2') 
        try:
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(2) > label"))).click()
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()  
        except:
            pass
              
             
        #input('esperar 2')
        try:
            time.sleep(1.5) 
            wait.until(ec.visibility_of_element_located((By.XPATH, "./html/body/main/form/input[3]"))).click()  
        except:
            pass
         
        #input('esperar 2')
        
        #//*[@id="q8fff763445ed42bbb690f924254011b5"]/table/tbody/tr[4]/td[1]/input
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='8fff763445ed42bbb690f924254011b5.Rose_bunch']"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='8fff763445ed42bbb690f924254011b5.Fresh_cut_flower_bunch']"))).click()  
            wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='8fff763445ed42bbb690f924254011b5.Customtoyou_arrangement']"))).click()  
            wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='8fff763445ed42bbb690f924254011b5.Rose_bouquet']"))).click()  
            wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='8fff763445ed42bbb690f924254011b5.Readymade_arrangement']"))).click()  
            wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='8fff763445ed42bbb690f924254011b5.Nonrose_bouquet']"))).click()        
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        except:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='qc7e582f4b624486b937df6b878cba1e9']/ul[1]/li[5]/label"))).click()        
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
            
            
            
        #input('esperar 3')
                       
        source1= driver.find_element(By.XPATH, "//*[@id='id_76aa50da43f04a7e8aefdd44ce280386']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_76aa50da43f04a7e8aefdd44ce280386-dest']")
        action = ActionChains(driver)        
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2) 
        source1= driver.find_element(By.XPATH, "//*[@id='id_76aa50da43f04a7e8aefdd44ce280386']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_76aa50da43f04a7e8aefdd44ce280386-dest']")
        action = ActionChains(driver)        
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2)
        source1= driver.find_element(By.XPATH, "//*[@id='id_76aa50da43f04a7e8aefdd44ce280386']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_76aa50da43f04a7e8aefdd44ce280386-dest']")
        action = ActionChains(driver)       
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2)
        source1= driver.find_element(By.XPATH, "//*[@id='id_76aa50da43f04a7e8aefdd44ce280386']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_76aa50da43f04a7e8aefdd44ce280386-dest']")
        action = ActionChains(driver)       
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2)
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()   
        
        try:
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        except:
            pass
            
        
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[1]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[2]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[3]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[4]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[5]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[6]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[7]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[8]/td[5]/input"))).click()
        
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        time.sleep(1.5)
        b=driver.find_element(By.XPATH, "//*[@id='q76aa50da43f04a7e8aefdd44ce280386']/h3/div/b")
        b=b.text
        #print(b)
        #input('esperar 4')
       
        #exactly
        '''  try:
             
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q152ff13c2ad343acbc23af194497e88f']/ul[1]/li[5]/label"))).click() 
        except:
            pass        '''
            
            
        if b=='exactly':
            source1= driver.find_element(By.XPATH, "//*[@id='id_76aa50da43f04a7e8aefdd44ce280386']/li[1]")
            target1 = driver.find_element(By.XPATH, " //*[@id='id_76aa50da43f04a7e8aefdd44ce280386-dest']")
            action = ActionChains(driver)        
            action.drag_and_drop(source1,target1).perform()
            time.sleep(0.2) 
            source1= driver.find_element(By.XPATH, "//*[@id='id_76aa50da43f04a7e8aefdd44ce280386']/li[1]")
            target1 = driver.find_element(By.XPATH, " //*[@id='id_76aa50da43f04a7e8aefdd44ce280386-dest']")
            action = ActionChains(driver)        
            action.drag_and_drop(source1,target1).perform()
            time.sleep(0.2)
            source1= driver.find_element(By.XPATH, "//*[@id='id_76aa50da43f04a7e8aefdd44ce280386']/li[1]")
            target1 = driver.find_element(By.XPATH, " //*[@id='id_76aa50da43f04a7e8aefdd44ce280386-dest']")
            action = ActionChains(driver)       
            action.drag_and_drop(source1,target1).perform()
            time.sleep(0.2)
            source1= driver.find_element(By.XPATH, "//*[@id='id_76aa50da43f04a7e8aefdd44ce280386']/li[1]")
            target1 = driver.find_element(By.XPATH, " //*[@id='id_76aa50da43f04a7e8aefdd44ce280386-dest']")
            action = ActionChains(driver)       
            action.drag_and_drop(source1,target1).perform()
            time.sleep(0.2)
        
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        #input('esperar 5')
        ''' try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table[2]/tbody/tr[1]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table[2]/tbody/tr[2]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table[2]/tbody/tr[3]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table[2]/tbody/tr[4]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table[2]/tbody/tr[5]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table[2]/tbody/tr[6]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table[2]/tbody/tr[7]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table[2]/tbody/tr[8]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table[2]/tbody/tr[9]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table[2]/tbody/tr[10]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table[2]/tbody/tr[11]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table[2]/tbody/tr[12]/td[6]/input"))).click()
            
        except:
            pass   
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[1]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[2]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[3]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[4]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[5]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[6]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[7]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[8]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[9]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[10]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[11]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[12]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[13]/td[6]/input"))).click()
        except:
            pass   
        
        
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[1]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[2]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[3]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[4]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[5]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[6]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[7]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[8]/td[5]/input"))).click()
        except:
            pass  '''
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[1]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[2]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[3]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[4]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[5]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[6]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[7]/td[5]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[8]/td[5]/input"))).click()
        #input('esperar 6')
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        ''' try:
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()        
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        except:
            pass '''
        
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q152ff13c2ad343acbc23af194497e88f']/ul[1]/li[5]/label"))).click()
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        except:
            
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        #input('esperar 7')    
        
        #input('esperar 8')
        ''' try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[1]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[2]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[3]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[4]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[5]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[6]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[7]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q2898499a265b4988a11264c0fee2d9cd']/table/tbody/tr[8]/td[5]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q152ff13c2ad343acbc23af194497e88f']/ul[1]/li[5]/label"))).click()
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        except:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[1]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[2]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[3]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[4]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[5]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[6]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[7]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[8]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[9]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[10]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[11]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[12]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[13]/td[6]/input"))).click()
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
            time.sleep(3)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click() '''
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[1]/td[6]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[2]/td[6]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[3]/td[6]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[4]/td[6]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[5]/td[6]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[6]/td[6]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[7]/td[6]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[8]/td[6]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[9]/td[6]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[10]/td[6]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[11]/td[6]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[12]/td[6]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q3c8c561a286846e0b858924657499e6f']/table/tbody/tr[13]/td[6]/input"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        time.sleep(1.5)
        wait.until(ec.visibility_of_element_located((By.XPATH, "./html/body/main/form/input[3]"))).click() 
        
        
        ''' try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='q152ff13c2ad343acbc23af194497e88f']/ul[1]/li[5]/label"))).click()
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        except:
            pass '''
        
        
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()
        
        #input('esperar 9')
        source1= driver.find_element(By.XPATH, "//*[@id='id_8cb164a26d454b72a5d2f59aa378b4ca']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_8cb164a26d454b72a5d2f59aa378b4ca-dest']")
        action = ActionChains(driver)        
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2)
        source1= driver.find_element(By.XPATH, "//*[@id='id_8cb164a26d454b72a5d2f59aa378b4ca']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_8cb164a26d454b72a5d2f59aa378b4ca-dest']")
        action = ActionChains(driver)        
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2)
        source1= driver.find_element(By.XPATH, "//*[@id='id_8cb164a26d454b72a5d2f59aa378b4ca']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_8cb164a26d454b72a5d2f59aa378b4ca-dest']")

        action = ActionChains(driver)       
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2)
        source1= driver.find_element(By.XPATH, "//*[@id='id_8cb164a26d454b72a5d2f59aa378b4ca']/li[1]")
        target1 = driver.find_element(By.XPATH, " //*[@id='id_8cb164a26d454b72a5d2f59aa378b4ca-dest']")

        action = ActionChains(driver)       
        action.drag_and_drop(source1,target1).perform()
        time.sleep(0.2)
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()   
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()     
             
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='qf472133a946244c6ac24a32097d5a086']/ul[1]/li[11]/label"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "id_cb915363192743618de34a9be03999ea"))).send_keys("1")             
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()   
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()     
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(1) > label"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click()    
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".radio:nth-child(5) .delta"))).click()  
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button1"))).click() 
        jumper = driver.current_url            
        value= {"jumper":jumper}
        
              
        time.sleep(0.5)    
        return  JSONResponse(content=value)  
        
    
    
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="K2001 no encontrado Error 404")
    
    
    finally:
    
        driver.quit() 
     
    
    
    
    
    
    
    
    
    
    
    
    
