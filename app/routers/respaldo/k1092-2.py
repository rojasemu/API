from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.routers.schemas import *



router = APIRouter (    
    prefix= "/k1092"
    #tags= ["Kmils"]
)



@router.get("/2/{psid}/{hash}")
def K1092mala(psid, hash):
        
    try:    
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept      
        driver.delete_all_cookies()    
            
            
        wait = WebDriverWait(driver, 5)    
        
            
    
        time.sleep(2)
            
        url= "https://www.surveys.com/start.aspx?SSID=5CAA66E2-BD74-4F45-91DE-A8805BD87C5C&IP_TargetGroup=3&EXTID="+psid+"**&EXTSupplierSourceID=1&_k=1092&_s="+hash+""
        driver.get(url)
        #driver.set_page_load_timeout(25)      
        time.sleep(27)
        
        
        try:
            wait.until(ec.visibility_of_element_located((By.ID, "l_1033_label"))).click()    
        except:
            wait.until(ec.visibility_of_element_located((By.ID, "l_1033_label"))).click()
                
        
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".prettycheckbox > a"))).click()    
        time.sleep(2.5)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
            
        time.sleep(1.5)
        a= driver.find_element(By.XPATH, "//*[@id='ScreenerKT1_text']/p[1]/span/b")
        
        #print(a.text)
        a=a.text
        
        time.sleep(0.3)
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
    
        
        #wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(2) .answerlabel"))).click()
        
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "GenderIdentity_1_label"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "Transgender_2_label"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "age_1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "age_1"))).send_keys("35")
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        time.sleep(0.5)
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(2) .answerlabel"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.ID, "EmpSt_1_label"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        #aqui
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.ID, "FFUse30D_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x1 #FFUse30D_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x2 #FFUse30D_header2"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x3 #FFUse30D_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgCT:nth-child(8) .answerlabel"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        
        time.sleep(1.5)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(1) .item:nth-child(2)"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(2) #FutRecomCMBiW_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(3) #FutRecomCMBiW_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(4) #FutRecomCMBiW_header3"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(1.5)
        
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "UseIntCMBiW_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(2) #UseIntCMBiW_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(3) #UseIntCMBiW_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(4) .item:nth-child(2)"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(0.5)   
        
        
        wait.until(ec.visibility_of_element_located((By.ID, "OEUBAComms_1"))).send_keys("whatsapp")
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        time.sleep(1.5)
        
    
        
        wait.until(ec.visibility_of_element_located((By.ID, "ABAComms_header1"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x1 #ABAComms_header2"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x2 #ABAComms_header3"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x3 #ABAComms_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x4 #ABAComms_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x5 #ABAComms_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x6 #ABAComms_header2"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x7 #ABAComms_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(0.5)    
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'WhatsApp')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Google Meet')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Zoom')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Skype')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(0.5)
        
        wait.until(ec.visibility_of_element_located((By.ID, "UIntComms_header2"))).click()
        time.sleep(0.1)   
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(2) #UIntComms_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(3) #UIntComms_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(4) #UIntComms_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(0.5)
        
    
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'WhatsApp')]"))).click()    
        time.sleep(0.1) 
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(0.5)
        
        
        wait.until(ec.visibility_of_element_located((By.ID, "UseComms_header3"))).click()
        time.sleep(0.5)
    
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x1 #UseComms_header4"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x2 #UseComms_header4"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x3 #UseComms_header4"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x4 #UseComms_header3"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x5 #UseComms_header2"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x6 #UseComms_header3"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x7 #UseComms_header1"))).click()    
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        
        
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//th[contains(text(), 'WhatsApp')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        time.sleep(2.5)
        wait.until(ec.visibility_of_element_located((By.ID, "FutRecomComms_header2"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(2) #FutRecomComms_header3"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(3) .item:nth-child(3)"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(4) .item:nth-child(2)"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(5) #FutRecomComms_header2"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(6) #FutRecomComms_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(7) #FutRecomComms_header2"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".bankedGridItem:nth-child(8) #FutRecomComms_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        time.sleep(1.5)
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(3) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(3) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(1) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(2) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(3) .item:nth-child(2) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".blockCurr .bankedGridItem:nth-child(4) .item:nth-child(1) > .banked-cover"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        #input('esperando')
        time.sleep(2.5)
        wait.until(ec.visibility_of_element_located((By.ID, "BMCommsiW_header2"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x1 #BMCommsiW_header3"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x2 #BMCommsiW_header1 > u"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x3 #BMCommsiW_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(2.5)
        
        
        
        wait.until(ec.visibility_of_element_located((By.ID, "CollabComms_header2"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x1 #CollabComms_header3"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x2 #CollabComms_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x3 #CollabComms_header1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        
        time.sleep(2)  #//label[contains(text(), 'Video calls (with individuals or groups)')]
        wait.until(ec.visibility_of_element_located((By.ID, "DetailUseCommsWork_7_label"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "DetailUseCommsWork_9_label"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "DetailUseCommsWork_1_label"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "DetailUseCommsWork_2_label"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(3)
        
        try:
        
            time.sleep(1)
            wait.until(ec.visibility_of_element_located((By.ID, "DetailUseCommsWork_7_label"))).click()
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.ID, "DetailUseCommsWork_6_label"))).click()
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.ID, "DetailUseCommsWork_5_label"))).click()
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click() 
            
        except:
            
            pass
            
            
        try:
        
            time.sleep(1)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Chat (text-based messaging)')]"))).click()
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Voice calls (with individuals or groups)')]"))).click()
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Share files or documents')]"))).click()
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
            time.sleep(1)
        except:
            
            pass
            
            
        
        try:
            time.sleep(1)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Chat (text-based messaging)')]"))).click()
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Voice calls (with individuals or groups)')]"))).click()
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Collaborate on documents in real time')]"))).click()
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()  
        
        except:
            
            pass
            
            
        
                
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'There is a primary solution, and access to other solutions is restricted')]"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(0.5)
            
        #aqui
    
    
        #aqui
        try:
            time.sleep(2)
            wait.until(ec.visibility_of_element_located((By.ID, "MemoOECommsx1"))).click()
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.ID, "MemoOECommsx1"))).send_keys("i like")
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
            time.sleep(0.5)
        except:
            pass
        
        
        
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), '4 overall positive')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), '4 very much')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(1.5)
        

        
        time.sleep(2)
            
        wait.until(ec.visibility_of_element_located((By.ID, "SponsoredComms_13_label"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
    

        try:
            time.sleep(3)
            wait.until(ec.visibility_of_element_located((By.ID, "SponsoredComms_99_label"))).click()
            time.sleep(0.3)
            wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
            time.sleep(0.5)
        except:
            pass
            
    
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".acc-ico-minus"))).click()
        time.sleep(0.1)    
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".acc-element:nth-child(1) .acc-ico-plus"))).click()
        
        try:
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.ID, "UseOS2iW_header1"))).click()
            
        except:
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.ID, "UseOS2iW_header5"))).click()
            
            
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".acc-element:nth-child(2) .acc-ico-plus"))).click()    
        try:
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".acc-items-show #UseOS2iW_header1"))).click()
            
        except:
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.ID, "UseOS2iW_header5"))).click()
            
        
            
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".acc-element:nth-child(3) .acc-ico-plus"))).click()    
        try:
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.ID, "UseOS2iW_header5"))).click()
            
        except:
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".acc-items-show #UseOS2iW_header1"))).click()
        
            
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".acc-element:nth-child(4) .acc-ico-plus"))).click()    
        try:
            time.sleep(0.1)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".acc-items-show #UseOS2iW_header1"))).click()
            
        except:
            wait.until(ec.visibility_of_element_located((By.ID, "UseOS2iW_header5"))).click()
            time.sleep(0.1)
        
        
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        
        
        
            
            
            
        time.sleep(1)    
        wait.until(ec.visibility_of_element_located((By.ID, "Industry_4_label"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        time.sleep(2)
        if driver.find_element(By.ID, "nav1"):
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "nav1"))).click()
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".box1a > .rg_text"))).click()   
        
        if driver.find_element(By.ID, "nav2"):
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "nav2"))).click()
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".box2a > .rg_text"))).click()   
            
    
        if driver.find_element(By.ID, "nav3"):
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "nav3"))).click()
            time.sleep(1)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".box3a > .rg_text"))).click()   
            
        if driver.find_element(By.ID, "nav4"):
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "nav4"))).click()
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".box4a > .rg_text"))).click()   
            
            
        if driver.find_element(By.ID, "nav5"):
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "nav5"))).click()
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".box5a > .rg_text"))).click()   
            
            
        if driver.find_element(By.ID, "nav6"):
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "nav6"))).click()
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".box6a > .rg_text"))).click()   
        
            
        if driver.find_element(By.ID, "nav7"):
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "nav7"))).click()
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".box7a > .rg_text"))).click()   
        
            
        if driver.find_element(By.ID, "nav8"):
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "nav8"))).click()
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".box8a > .rg_text"))).click()   
            
            
        if driver.find_element(By.ID, "nav9"):
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "nav9"))).click()
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".box9a > .rg_text"))).click()   
            
            
        if driver.find_element(By.ID, "nav10"):
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.ID, "nav10"))).click()
            time.sleep(0.5)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".box10a > .rg_text"))).click()
            
        
        
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='rg_nav']/div[10]"))).click() 
        time.sleep(0.5)   
        wait.until(ec.visibility_of_element_located((By.ID, "rl_confForward"))).click()     

        
    
        time.sleep(3)
        wait.until(ec.visibility_of_element_located((By.ID, "MarSt2_2_label"))).click()
        time.sleep(0.2)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".sgAll:nth-child(5) > .sgCT:nth-child(1) .answerlabel"))).click()
        time.sleep(0.2)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.ID, "SizeAgeHH2_2"))).click()
        time.sleep(0.1)   
        wait.until(ec.visibility_of_element_located((By.ID, "SizeAgeHH2_2"))).clear()     
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "SizeAgeHH2_2"))).send_keys("1")
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "SizeAgeHH2_5"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "SizeAgeHH2_5"))).clear()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "SizeAgeHH2_5"))).send_keys("1")
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.ID, "Ethnicity_2_label"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "EthnicityFollowUp_20_label"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        
        time.sleep(1.5)
        wait.until(ec.visibility_of_element_located((By.ID, "ZIPC1x1"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "ZIPC1x1"))).send_keys("28328")
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "AnnualHHInco_5_label"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "Educ2_4_label"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(1)
        
        
        
        #input('esperando')
        wait.until(ec.visibility_of_element_located((By.ID, "PrimeActOffiW2_header1"))).click()
        time.sleep(1.5)
        
        try:
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#acc-answers-0x1 #PrimeActOffiW2_header2"))).click()
            time.sleep(0.5)
        
        except:
            
            wait.until(ec.visibility_of_element_located((By.ID, "PrimeActOffiW2_header1"))).click()
            
            
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()    
        time.sleep(3)
        
        #input('esperando')
        try:
            time.sleep(2)
            wait.until(ec.visibility_of_element_located((By.ID, "FinalDecOffiW_2_label"))).click()
            
        except:
            time.sleep(2)
            wait.until(ec.visibility_of_element_located((By.ID, "HiInflOffiW_6_label"))).click()
            
        '''  except:
            time.sleep(2)
            wait.until(ec.visibility_of_element_located((By.ID, "FinalDecOffiW_1_label"))).click()
             '''
            
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(2)
        
        wait.until(ec.visibility_of_element_located((By.ID, "HybWorkiW_2_label"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(0.5)
        
        wait.until(ec.visibility_of_element_located((By.ID, "SurveyDev2_6_label"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
        time.sleep(1.5)
        
        wait.until(ec.visibility_of_element_located((By.ID, "comments"))).click()
        wait.until(ec.visibility_of_element_located((By.ID, "comments"))).send_keys("yes")
        time.sleep(0.3)
        
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