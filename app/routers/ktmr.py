from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import random
router = APIRouter (    
    prefix= "/ktmr"
    #tags= ["Kmils"]
)




@router.get("/1/{psid}")
def ktmr(psid):
    
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = interceptcint  
        driver.delete_all_cookies()      
        wait = WebDriverWait(driver, 10)
        url= "https://sz.ktrmr.com/mrIWeb/mrIWeb.srf?i.project=BTSWSATSP&s=CNT01&src=185&panelas=LFP01&pid="+psid+"&wv=12&bst=2&cintRespondent=1&panelId=10173&rdir=2&Id=1&useTest=1&i.test=1&_useDemoVars=0&korsid=F0960BB804DEE9498577486D95DC6EE4"
        driver.get(url)
   
        time.sleep(4)
   
   
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".fa-chevron-right"))).click()
        time.sleep(1.5)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) > div > div:nth-child(2)"))).click()
        time.sleep(1.5)
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).click()
        time.sleep(1.5)
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("35")
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(46) > div > div:nth-child(2)"))).click()
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) > div > div:nth-child(2)"))).click()
        time.sleep(4)       
        
        wait.until(ec.visibility_of_element_located((By.ID, "response"))).send_keys("cerveza")
        time.sleep(1.5)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sendBtn > .material-icons"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.ID, "response"))).send_keys("no")
        time.sleep(1.5)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#sendBtn > .material-icons"))).click()
          
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()        
        
        time.sleep(2)  
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) .\\__grid_col:nth-child(2) div:nth-child(2)"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(2) .\\__grid_col:nth-child(1) div:nth-child(2)"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".fa-chevron-right"))).click()
        time.sleep(2) 
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) .\\__grid_col:nth-child(2) div:nth-child(2)"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(2) .\\__grid_col:nth-child(1) div:nth-child(2)"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()
        time.sleep(2)     

        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_Q1']/div/div/div/div[1]/div/div[2]"))).click()
        time.sleep(1)       
         
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF1']/div/div/div/div[1]/div/div[2]"))).click()
       
        time.sleep(1) 
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) > div > div:nth-child(2)"))).click()
        
        time.sleep(1) 
        wait.until(ec.visibility_of_element_located((By.XPATH, ".//*[@id='container_BEH_CCF3']/div/div/div/div[1]/div/div[2]"))).click()
        
        time.sleep(1) 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF4']/div/div/div/div[1]/div/div[2]"))).click()
          
        
        time.sleep(2.5)  
        
        #input('esperando')
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_ANS_BEH_Q2a']/div/div/div/div[10]/div/div[2]"))).click() 
        
        except:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_ANS_BEH_Q2b']/div/div/div/div[9]/div/div[2]"))).click() 
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()  
        
        
        
        '''  try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_ANS_BEH_Q2b']/div/div/div/div[10]/div/div[2]"))).click()    
       
        except:
           wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_ANS_BEH_Q2a']/div/div/div/div[11]/div/div[2]"))).click()  '''
           
        #input('esperando')
        time.sleep(1)
        
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_ANS_BEH_Q2b']/div/div/div/div[9]/div/div[2]"))).click() 
            
        except:
            wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_ANS_BEH_Q2a']/div/div/div/div[10]/div/div[2]"))).click() 
          
            
        
        
          
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()  
        time.sleep(1.5)        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='_Q0_Q0_Q0']"))).send_keys("Cacique")
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()
            
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("1")
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()
        time.sleep(1.5)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF5']/div/div[2]/div/div/div[1]/div/div[2]"))).click() 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF5']/div/div[2]/div/div/div[1]/div/div[2]"))).click() 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF5']/div/div[2]/div/div/div[1]/div/div[2]"))).click() 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF5']/div/div[2]/div/div/div[1]/div/div[2]"))).click() 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF5']/div/div[2]/div/div/div[1]/div/div[2]"))).click() 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF5']/div/div[2]/div/div/div[1]/div/div[2]"))).click() 
        
        
        time.sleep(1.5)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) > div > div:nth-child(2)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) > div > div:nth-child(2)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) > div > div:nth-child(2)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) > div > div:nth-child(2)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) > div > div:nth-child(2)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) > div > div:nth-child(2)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) > div > div:nth-child(2)"))).click()
        
        
        #input('espera 1')
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_ANS_BEH_Q2b']/div/div/div/div[9]/div/div[2]"))).click()
        
        except:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_ANS_BEH_Q2a']/div/div/div/div[10]/div/div[2]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()
        
        #input('espera 2')
        
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_ANS_BEH_Q2b']/div/div/div/div[9]/div/div[2]"))).click()
        except:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_ANS_BEH_Q2a']/div/div/div/div[10]/div/div[2]"))).click()
            
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()  
        time.sleep(1.5)        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='_Q0_Q0_Q0']"))).send_keys("Cacique")
         
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()
              
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("1")
         
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()
        time.sleep(1.5)
        
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF5']/div/div[2]/div/div/div[1]/div/div[2]"))).click() 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF5']/div/div[2]/div/div/div[1]/div/div[2]"))).click() 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF5']/div/div[2]/div/div/div[1]/div/div[2]"))).click() 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF5']/div/div[2]/div/div/div[1]/div/div[2]"))).click() 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF5']/div/div[2]/div/div/div[1]/div/div[2]"))).click() 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_BEH_CCF5']/div/div[2]/div/div/div[1]/div/div[2]"))).click() 
        
        
        
        #input('espera 3')
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) > div > div:nth-child(2)"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".\\__grid_col:nth-child(1) > div > div:nth-child(2)"))).click()
       
        #input('espera 4')
        try:
        
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_ANS_BEH_Q7b']/div/div/div/div[9]/div/div[2]"))).click()
        
        except:
             wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_ANS_BEH_Q7a']/div/div/div/div[10]/div/div[2]"))).click()
        
        
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()
        time.sleep(1.5)
        
       
       
        try:
        
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container_ANS_BEH_Q7b']/div/div/div/div[10]/div/div[2]"))).click()
        
        except:
              wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_ANS_BEH_Q7a']/div/div/div/div[11]/div/div[2]"))).click()
        
        
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()
        
        
        try:
            
        
            wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_ANS_BEH_Q140b_L3M']/div/div/div/div[9]/div/div[2]"))).click()
        except:
            wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_ANS_BEH_Q140a_L3M']/div/div/div/div[10]/div/div[2]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()
        time.sleep(1.5)
        
        try:
        
            wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_ANS_BEH_Q140b_L3M']/div/div/div/div[10]/div/div[2]"))).click()
        
        except:
            wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_ANS_BEH_Q140a_L3M']/div/div/div/div[11]/div/div[2]"))).click()
            
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()
        time.sleep(1.5)
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()
        time.sleep(1.5)
        #input('espera 5')
        
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_PromptedAwareness_HT']/div/div[2]/div/div/div[1]/div/div[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_PromptedAwareness_HT']/div/div[2]/div/div/div[1]/div/div[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_PromptedAwareness_HT']/div/div[2]/div/div/div[1]/div/div[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_PromptedAwareness_HT']/div/div[2]/div/div/div[1]/div/div[2]"))).click()
        
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_PromptedAwareness_HT']/div/div[2]/div/div/div[1]/div/div[2]"))).click()
        except:
            pass
        #//*[@id="mrForm"]/div[1]/div[3]/div[2] //*[@id="mrForm"]/div[1]/div[3]/div[1]  
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_TBC_New_Hearing']/div/div[2]/div/div/div[11]/div/div[2]"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
       
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_TBC_New_Hearing']/div/div[2]/div/div/div[12]/div/div[2]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_TBC_New_Hearing']/div/div[2]/div/div/div[11]/div/div[2]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_TBC_New_Hearing']/div/div[2]/div/div/div[12]/div/div[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_TBC_New_Hearing']/div/div[2]/div/div/div[12]/div/div[2]"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        except:
            pass
        
        
        
        time.sleep(1.5)
    
        #input('espera 7')
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_MessageCheck_HT']/div/div[2]/div/div/div[5]/div/div[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_MessageCheck_HT']/div/div[2]/div/div/div[5]/div/div[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_MessageCheck_HT']/div/div[2]/div/div/div[5]/div/div[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_MessageCheck_HT']/div/div[2]/div/div/div[5]/div/div[2]"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        except:
            pass
        
        
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_MessageCheck_HT']/div/div[2]/div/div/div[5]/div/div[2]"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        except:
            pass
        
        
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_MessageCheck_HT']/div/div[2]/div/div/div[5]/div/div[2]"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        except:
            pass
        
        
        
        
        #input('espera 8')
        time.sleep(1.5)
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_IMAGERY_HT']/div/div[2]/div/div/div[5]/div/div[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_IMAGERY_HT']/div/div[2]/div/div/div[5]/div/div[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_IMAGERY_HT']/div/div[2]/div/div/div[5]/div/div[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_IMAGERY_HT']/div/div[2]/div/div/div[5]/div/div[2]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        
        
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_IMAGERY_HT']/div/div[2]/div/div/div[5]/div/div[2]"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        except:
            pass
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_IMAGERY_HT']/div/div[2]/div/div/div[5]/div/div[2]"))).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mrForm']/div[1]/div[3]/div[2]"))).click()
        except:
            pass
        
       
        #input('espera 9')
        time.sleep(1.5)
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_ES_Relationship']/div/div/div/div[6]/div/div[2]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='Cell.0.0']/label/span"))).click()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".tempNext"))).click()
        time.sleep(1.5)
        
        #input('espera 10')
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_QETH']/div/div/div/div[1]/div/div[2]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='container_BEH_SEG']/div/div/div/div[6]/div/div[2]"))).click()
        '''     
        input('esperar') 
        try:
            jumper= wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#mrEndLink"))).get_attribute("href")
            print(jumper)  
            
        except:
            jumper= wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@id='mrEndLink']"))).get_attribute("href")
            print(jumper)  
        #mrEndLink #mrEndLink  #//a[@id='mrEndLink']
        input('esperar') '''
        wait.until(ec.visibility_of_element_located((By.XPATH, " //*[@id='endLinkButton']"))).click()
        
   
   
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