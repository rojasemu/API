from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.routers.schemas import *


router = APIRouter (    
    prefix= "/k11052"
    #tags= ["Kmils"]
)


@router.get("/1/{psid}", status_code=200)
def  k11052(psid) :
 
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept   
        driver.delete_all_cookies()   
        
        wait = WebDriverWait(driver, 10)
        url="http://survey.validators.nl/s3/30227ca813d6?PSID="+psid+"**&Age=22&Gender=1&Education=3&Groep=1&_k=11052"   
        driver.get(url)
        
        
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        time.sleep(1)
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sgE-90522568-315-869-box .sg-first-li > label"))).click()        
        
        wait.until(ec.visibility_of_element_located((By.ID, "sgE-90522568-315-873-element"))).send_keys("25")
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sgE-90522568-315-1252-box .sg-first-li > label"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sgE-90522568-315-1253-box li:nth-child(3) > label"))).click()
       
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
       
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Sports drinks')]"))).click()
      
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()        
        
        wait.until(ec.visibility_of_element_located((By.ID, "sgE-90522568-324-884-13218"))).send_keys("1")
        
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Coca-Cola')]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
       
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Coca-Cola')]"))).click()
       
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Coca-Cola')]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "label:nth-child(2)"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        
        
       #sgE-90522568-427-7061-box > legend > strong:nth-child(1)
        
        time.sleep(0.1)
      
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1219-12148"))):
            #print('presente 1219')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1219-12148"))).click()
          
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1220-12148"))):
            #print('presente 1220')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1220-12148"))).click()
       
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1221-12148"))):
            #print('presente 1221')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1221-12148"))).click()
           
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1222-12149"))):
            #print('presente 1222')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1222-12149"))).click()
              
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1223-12149"))):
            #print('presente 1223')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1223-12149"))).click()
                
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1224-12149"))):
            #print('presente 1224')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1224-12149"))).click()
              
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1225-12149"))):
            #print('presente 1225')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1225-12149"))).click()
                
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1226-12149"))):
            #print('presente 1226')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1226-12149"))).click()
                
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1227-12149"))):
            #print('presente 1227')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1227-12149"))).click()
                 
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1228-12149"))):
            #print('presente 1228')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1228-12149"))).click()
               
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1229-12149"))):
            #print('presente 1229')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1229-12149"))).click()
               
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1230-12149"))):
            #print('presente 1230')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1230-12149"))).click()
                
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1231-12149"))):
            #print('presente 1231')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1231-12149"))).click()
               
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1232-12149"))):
            #print('presente 1232')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1232-12149"))).click()
                 
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1233-12149"))):
            #print('presente 1233')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1233-12149"))).click()
              
        ''' if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1234-12149"))):
            print('presente 1234')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1234-12149"))).click()'''
                
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1235-12149"))):
            #print('presente 1235')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1235-12149"))).click() 
                
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1236-12149"))):
            #print('presente 1236')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1236-12149"))).click()
        ''' time.sleep(1.5)      
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1237-12149"))):
            print('presente 1237')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1237-12149"))).click() 
        time.sleep(1.5)      
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1239-12149"))):
            print('presente 1239')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1239-12149"))).click()
        time.sleep(1.5)       
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1240-12149"))):
            print('presente 1240')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-1240-12149"))).click()
        time.sleep(1.5)     
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-3709-12149"))):
            print('presente 3709')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-3709-12149"))).click()
        time.sleep(1.5)       
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-3710-12149"))):
            print('presente 3710')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-3710-12149"))).click()
        time.sleep(1.5)      
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-3711-12149"))):
            print('presente 3711')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-3711-12149"))).click()'''
                
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-3712-12149"))):
            #print('presente 3712')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-242-3712-12149"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        
        
        #//*[@id="sgE-90522568-242-684-meta"]
        #//label[@title='IE_Logo_CocaCola.png']
        #//*[@id="sgE-90522568-339-922-13839-image"]
        #sgE-90522568-252-789-13827
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@alt='IE_Logo_CocaCola.png']"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@alt='IE_Logo_CocaCola.png']"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@alt='IE_Logo_CocaCola.png']"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        
  
        time.sleep(0.1)
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4011-13237"))):
            #print('presente 4011')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4011-13237"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-3991-13237"))):
            #print('presente 3991')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-3991-13237"))).click()
            
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-3995-13238"))):
            #print('presente 3995')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-3995-13238"))).click()
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4780-13238"))):
            #print('presente 4780')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4780-13238"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4260-13238"))):
            #print('presente 4260')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4260-13238"))).click()
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-7952-13238"))):
            #print('presente 47952')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-7952-13238"))).click()
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-8207-13238"))):
            #print('presente 8207')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-8207-13238"))).click()
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4014-13238"))):
            #print('presente 4014')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4014-13238"))).click()
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4006-13238"))):
            #print('presente 4006')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4006-13238"))).click()
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-7954-13238"))):
            #print('presente 7954')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-7954-13238"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-7953-13238"))):
            #print('presente 7953')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-7953-13238"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4005-13238"))):
            #print('presente 4005')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4005-13238"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4013-13238"))):
            #print('presente 4013')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4013-13238"))).click()
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4004-13238"))):
            #print('presente 4004')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4004-13238"))).click()
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-7955-13238"))):
            #print('presente 7955')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-7955-13238"))).click()
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-7956-13238"))):
            #print('presente 7956')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-7956-13238"))).click()
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4777-13238"))):
            #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-327-4777-13238"))).click()       
        
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        
        
        
        
        
        
        '''  if  wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sgE-90522568-427-6573-box .sg-first-li > label"))):
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sgE-90522568-427-6573-box .sg-first-li > label"))).click()
            
        elif  wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sgE-90522568-427-6601-box .sg-first-li > label"))):
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sgE-90522568-427-6601-box .sg-first-li > label"))).click()
            
        elif  wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sgE-90522568-427-6628-box .sg-first-li > label"))):
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sgE-90522568-427-6628-box .sg-first-li > label"))).click()
            
        elif  wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sgE-90522568-427-7061-box .sg-first-li > label"))):
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sgE-90522568-427-7061-box .sg-first-li > label"))).click()
            
         '''
            
            #//*[@id="sgE-90522568-427-7061-box"]/div/ul/li[1]
            
         #//label[@for='sgE-90522568-427-6601-36912']  
            
       
        
        try:
            #I drink Lucozade Energy.
            #if wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6573-36830'] "))):
            #print(1)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6573-36830']"))).click()
            #I drink Lucozade Sport..        
            ''' elif wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6601-36912'] "))):
                print(1)
                wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6601-36912']"))).click()
            #I drink Lucozade Zero...   
            elif wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6628-36994'] "))):
                print(3)
                wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6628-36994']"))).click()
                
            #I drink Ribena..      
            elif wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-7061-38306'] "))):
                print(4)
                wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-7061-38306']"))).click() '''
            
        except:
            pass
        
        
        try:
            
            #if wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6601-36912'] "))):
            #print(2)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6601-36912']"))).click()
        
        except:
            pass
        
        
        try:
            
            #if wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6628-36994'] "))):
            #print(3)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6628-36994']"))).click()
                
        
        except:
            pass
        
        
        try:
            
            #if wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-7061-38306'] "))):
            #print(4)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-7061-38306']"))).click()
        
        except:
            pass
        
        
        
        
        
        
        
        
            '''  if wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6628-36994'] "))):
                print(2)
                wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6628-36994']"))).click()
                
            #I drink Ribena..    
            elif wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-7061-38306'] "))):
                print(2)
                wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-7061-38306']"))).click() 
        
               '''
        ''' 
        try:        
            if wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6628-36994'] "))):
                print(2)
                wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-6628-36994']"))).click()
        
        except:
                I drink Ribena..
            if wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-7061-38306'] "))):
                print(2)
                wait.until(ec.visibility_of_element_located((By.XPATH, "//label[@for='sgE-90522568-427-7061-38306']"))).click() '''
        
        
        '''   if wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'At breakfast')]"))):
            print(1)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'At breakfast')]"))).click()'''
       
        
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()       
        
      
        time.sleep(0.1)
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-458-8148-43649"))):
            #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-458-8148-43649"))).click()       
                
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-458-8149-43650"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-458-8149-43650"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-458-8150-43651"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-458-8150-43651"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-458-8151-43648"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-458-8151-43648"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-458-8152-43647"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-458-8152-43647"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-464-8184-43881"))):
            #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-464-8184-43881"))).click()       
                
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-464-8185-43884"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-464-8185-43884"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-464-8186-44048"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-464-8186-44048"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-464-8187-43880"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-464-8187-43880"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-464-8188-43882"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-464-8188-43882"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-465-8190-43927"))):
            #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-465-8190-43927"))).click()       
                
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-465-8191-43924"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-465-8191-43924"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-465-8192-43922"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-465-8192-43922"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-465-8193-43923"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-465-8193-43923"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-465-8194-43925"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-465-8194-43925"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-466-8196-43968"))):
            #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-466-8196-43968"))).click()       
                
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-466-8197-43967"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-466-8197-43967"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-466-8198-43969"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-466-8198-43969"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-466-8199-43965"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-466-8199-43965"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-466-8200-43966"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-466-8200-43966"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-467-8202-44008"))):
            #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-467-8202-44008"))).click()       
                
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-467-8203-44007"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-467-8203-44007"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-467-8204-44006"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-467-8204-44006"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-467-8205-44009"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-467-8205-44009"))).click()
        
        if wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-467-8206-44012"))):
                #print('presente 4077')
            wait.until(ec.presence_of_element_located((By.ID, "sgE-90522568-467-8206-44012"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()     
        #sgE-90522568-424-7688-box > div > table > tbody > tr.sg-even-row.row-7698 > td.sg-second-cell
        time.sleep(2)
        
        try:    
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sgE-90522568-424-7688-box > div > table > tbody > tr.sg-even-row.row-7698 > td.sg-second-cell"))).click()
        
        except:
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sgE-90522568-424-7688-box > div > table > tbody > tr.sg-even-row.row-7698 > td.sg-second-cell"))).click()
            
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "sgE-90522568-433-7879-element"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "sgE-90522568-433-7879-element"))).send_keys("14")
        wait.until(ec.visibility_of_element_located((By.ID, "sg_NextButton"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "sg_SubmitButton"))).click()
        time.sleep(0.2)
        
        
        
        
        ''' //*[@id="sgE-90522568-242-1219"]
        //*[@id="sgE-90522568-242-1220"]
        //*[@id="sgE-90522568-242-1221"]
        //*[@id="sgE-90522568-242-1222"]
        //*[@id="sgE-90522568-242-1223"]
        //*[@id="sgE-90522568-242-1224"]
        //*[@id="sgE-90522568-242-1225"]
        //*[@id="sgE-90522568-242-1226"]
        //*[@id="sgE-90522568-242-1227"]
        //*[@id="sgE-90522568-242-1228"]
        //*[@id="sgE-90522568-242-1229"]
        //*[@id="sgE-90522568-242-1230"]
        //*[@id="sgE-90522568-242-1231"]
        //*[@id="sgE-90522568-242-1232"]
        //*[@id="sgE-90522568-242-1233"]
        //*[@id="sgE-90522568-242-1234"]
        //*[@id="sgE-90522568-242-1235"]
        //*[@id="sgE-90522568-242-1236"]
        //*[@id="sgE-90522568-242-1237"]
        //*[@id="sgE-90522568-242-1239"]
        //*[@id="sgE-90522568-242-1240"]
        //*[@id="sgE-90522568-242-3709"]
        //*[@id="sgE-90522568-242-3710"]
        //*[@id="sgE-90522568-242-3711"]
        //*[@id="sgE-90522568-242-3712"] '''
                

       
      
        
             
        jumper = driver.current_url            
        value= {"jumper":jumper}
        
              
        time.sleep(0.5)    
        return  JSONResponse(content=value)  
        
    
    
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="Kmil no encontrado Error 404")
    
    
    finally:
    
        driver.quit() 
     
    
    
    
    
    
    
    
    
    
    
    
    
