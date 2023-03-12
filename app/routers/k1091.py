from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import random
router = APIRouter (    
    prefix= "/k1091"
    #tags= ["Kmils"]
)




@router.get("/1/{psid}/{pid}")
def k1091(psid, pid):
    
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept  
        driver.delete_all_cookies()      
        wait = WebDriverWait(driver, 10)
        url= "https://survey.us.confirmit.com/wix/6/p229027202226.aspx?SAMID=DYN&psid="+psid+"**&pid="+pid+"&_k=1091"
        driver.get(url)
        
        wait.until(ec.visibility_of_element_located((By.ID, "l_10_label"))).click()
        #wait.until(ec.visibility_of_element_located((By.ID, "l_9_label"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CQSTATE"))).click()
        dropdown = driver.find_element(By.ID, "CQSTATE")
        dropdown.find_element(By.XPATH, "//option[. = 'California']").click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "fieldset_QAGE"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "QAGE"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "QAGE"))).send_keys("33")
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "QGENDER_3_label"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "l7_2_label"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "l9_2_label"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "QHHI_8_label"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(1)"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "Demo13_2"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "Demo14_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "QLANG_2"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
         #//*[@id="Demo18c_59_label"]
        wait.until(ec.visibility_of_element_located((By.ID, "Demo17_3"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "Demo18c_59_label"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        #input('esperar 1')
        
        
        wait.until(ec.visibility_of_element_located((By.ID, "Demo19b_1_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "Demo19b_2_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "Demo20_2_label"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        
        wait.until(ec.visibility_of_element_located((By.ID, "CI1_4"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        
        #//*[@id="yui_3_14_1_1_1677954896601_72"]
        
        #//*[@id="yui_3_14_1_1_1677954896601_72"]
        #//*[@id="yui_3_14_1_1_1677954896601_417"]
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_19_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_71_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_17_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_13_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_51_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_57_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_64_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_37_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_52_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_31_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_8_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_44_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_70_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_24_1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_1_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_62_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_49_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_9_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_50_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_5_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_55_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_21_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_42_2"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_39_2"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_28_2"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_59_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_68_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_12_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_29_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_34_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_60_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_16_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_10_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_33_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_63_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_58_2"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_53_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_47_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_61_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_32_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_56_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_22_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_14_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_43_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_46_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_25_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_38_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_65_2"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_54_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_41_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_40_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_18_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_20_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_69_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_27_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_67_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_3_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_35_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_26_1"))).click()        
        wait.until(ec.visibility_of_element_located((By.ID, "CI2_15_2"))).click()   
        #input('esperar 2')
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_14_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_3_3"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_4_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_5_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_6_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_7_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_8_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_9_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_10_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_11_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_12_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_1_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_2_1"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "CI3_13_1"))).click()
        
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()   
        
        
        input('esperar 3')
        
       #//td[@headers='CI4_header1']
        
        try:
            #if wait.until(ec.visibility_of_element_located((By.ID, "//tr[@class='carousel-scale-row carousel-inactive']"))):
            #wait.until(ec.visibility_of_element_located((By.XPATH, "//td[@headers='CI4_header1']"))).click()             
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[text()='Mucha influencia']"))).click()             
                               
        except:
             pass
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[text()='Mucha influencia']"))).click()   
        except:
             pass
        try:
           wait.until(ec.visibility_of_element_located((By.XPATH, "//label[text()='Mucha influencia']"))).click()   
        except:
           pass  
       
        input('esperar 4')
        try:
            #if wait.until(ec.visibility_of_element_located((By.ID, "//tr[@class='carousel-scale-row carousel-current']"))):
            wait.until(ec.visibility_of_element_located((By.XPATH, "//td[@headers='CI4_header1']"))).click()             
                               
        except:
             pass
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//td[@headers='CI4_header1']"))).click()
        except:
             pass
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//td[@headers='CI4_header1']"))).click() 
        except:
           pass  
        
        if driver.find_element(By.XPATH, "//tr[@class='carousel-scale-row carousel-current']") and driver.find_element(By.ID, "yui_3_14_1_1_1678040980907_1251"):
            
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
            
    
          
        elif driver.find_element(By.XPATH, "//tr[@class='carousel-scale-row carousel-current']") and driver.find_element(By.ID, "yui_3_14_1_1_1678040980907_1231"):
            
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Algo de influencia')]"))).click()
            
    
          
        elif driver.find_element(By.XPATH, "//tr[@class='carousel-scale-row carousel-current']") and driver.find_element(By.ID, "yui_3_14_1_1_1678040980907_1235"):
            
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Neutral')]"))).click()
            
    
          
          
        elif driver.find_element(By.XPATH, "//tr[@class='carousel-scale-row carousel-current']") and driver.find_element(By.ID, "yui_3_14_1_1_1678040980907_1239"):
            
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
            
    
          
        elif driver.find_element(By.XPATH, "//tr[@class='carousel-scale-row carousel-current']") and driver.find_element(By.ID, "yui_3_14_1_1_1678040980907_1243"):
            
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
            
    
          
        elif driver.find_element(By.XPATH, "//tr[@class='carousel-scale-row carousel-current']") and driver.find_element(By.ID, "yui_3_14_1_1_1678040980907_1247"):
            
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
            
    
          
        elif driver.find_element(By.XPATH, "//tr[@class='carousel-scale-row carousel-current']") and driver.find_element(By.ID, "yui_3_14_1_1_1678040980907_1255"):
            
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
            
    
          
        elif driver.find_element(By.XPATH, "//tr[@class='carousel-scale-row carousel-current']") and driver.find_element(By.ID, "yui_3_14_1_1_1678040980907_1259"):
            
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
            
    
          
        elif driver.find_element(By.XPATH, "//tr[@class='carousel-scale-row carousel-current']") and driver.find_element(By.ID, "yui_3_14_1_1_1678040980907_1263"):
            
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
            
    
        elif driver.find_element(By.XPATH, "//tr[@class='carousel-scale-row carousel-current']") and driver.find_element(By.ID, "yui_3_14_1_1_1678040980907_1267"):
            
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
            
    
        elif driver.find_element(By.XPATH, "//tr[@class='carousel-scale-row carousel-current']") and driver.find_element(By.ID, "yui_3_14_1_1_1678040980907_1271"):
            
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
            
    
        elif driver.find_element(By.XPATH, "//tr[@class='carousel-scale-row carousel-current']") and driver.find_element(By.ID, "yui_3_14_1_1_1678040980907_1275"):
            
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
            
    
        elif driver.find_element(By.XPATH, "//tr[@class='carousel-scale-row carousel-current']") and driver.find_element(By.ID, "yui_3_14_1_1_1678040980907_1279"):
            
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
            
    
          
        
        input ('esperando')   
          
          
          
          
          
          
        '''    
           
        # Beauty, Television shows,  Food,   Movies, Politics, Health and Wellness, Haircare, Art, Technology, Fashion, Music, Sports, Dance

        driver.find_element(By.CSS_SELECTOR, ".page").click()
       
        time.sleep(5)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
        wait.until(ec.element_to_be_clickable((By.XPATH, "//label[contains(text(),  'Neutral')]"))).click()
        time.sleep (1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Algo de influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Neutral')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Neutral')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Ninguna influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Ninguna influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Algo de influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Algo de influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Algo de influencia')]"))).click()  
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Algo de influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Neutral')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Algo de influencia')]"))).click()        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Neutral')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Ninguna influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Ninguna influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Algo de influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Algo de influencia')]"))).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(),  'Mucha influencia')]"))).click()    
        '''
       
       
       
       
       
       
       
       
       
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#Cell\\.0\\.11 .mrMultipleText"))).click()

       
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