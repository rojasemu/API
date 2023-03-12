from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
router = APIRouter (    
    prefix= "/k7341"
    #tags= ["Kmils"]
)

@router.get("/1/{psid}")
def K7341(psid):
    
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept     
        driver.delete_all_cookies()    
        
        
        wait = WebDriverWait(driver, 10)
    
        url= "https://webtraffic.datacollectionsite.com/mriweb/mriweb.dll?I.Project=P220751&ID="+psid+"**&smp=45&_k=7341&_s=444d22efab363d0f2c5fd2195e59fc4af04008d4983b1d90b9ab5e09b631e158&I.User6=Q2hyb21lIHx8IENocm9tZSAxMDIgfHwgV2luZG93cyAxMCB8fCBXaW5kb3dzIDEwIHx8IE4vQSB8fCBEZXNrdG9wL2xhcHRvcCB8fCBDT01QVVRFUiB8fCBGYWxzZSB8fCAwQkZCRDhBQi0yREY2LTRBM0ItODY3Ny1FRjk3QzY5RUUxQjU%3D#running"
        driver.get(url)
        #driver.set_page_load_timeout(10)    
        time.sleep(3)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ui-first-child"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()    
        
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("1996")
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ui-last-child"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ui-last-child"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()   
        
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("10104")
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()    
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()    
        
        wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q0_Q0"))).send_keys("amazon")
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Woodscapes')]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Kilz')]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Benjamin Moore')]"))).click()   
    
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Benjamin Moore')]"))).click()
        time.sleep(0.3)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(1)
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(1) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(2) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(3) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(4) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(5) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(6) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(7) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(8) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(9) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(10) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(11) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(12) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(13) .ui-radio:nth-child(3) > .ui-btn"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(14) .ui-radio:nth-child(3) > .ui-btn"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(15) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(16) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(17) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(18) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(19) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(20) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(21) .ui-radio:nth-child(3) .mrQuestionText"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(0.5) 
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Olympic')]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Messmers')]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Wolman')]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Flood')]"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()    
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //span[contains(text(), 'I prefer a product that can be applied to both horizontal ')]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //span[contains(text(), 'It’s poor quality')]"))).click()
        
        wait.until(ec.visibility_of_element_located((By.XPATH, " //span[contains(text(), 'It’s too expensive')]"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()      
        
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Yes, but I was eventually able to find it')]"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(0.5)     
        
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(1) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(2) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(3) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(4) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(5) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(6) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(7) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(8) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(9) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(10) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(11) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(12) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(13) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(14) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(15) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(16) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(17) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(18) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(19) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(0.5)
        
        #input('esperar') # por ide _Q0_C3
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'I have used previously and will use again in the future')]"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(1) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(2) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(3) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(4) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(5) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(6) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(7) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(8) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(9) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(10) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(11) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(1)
        
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(1) .ui-radio:nth-child(1) .mrQuestionText"))).click()

        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(2) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(3) .ui-radio:nth-child(1) .mrQuestionText"))).click()

        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(4) .ui-radio:nth-child(2) .mrQuestionText"))).click()

        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(5) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(0.5)
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(1) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(2) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(3) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(4) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(5) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(0.7)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(0.5)
        
        #aqui
        
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(1) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(2) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(3) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(1)   
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(4) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)   
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(5) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(6) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(7) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(8) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(9) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(10) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(11) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(12) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(13) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(14) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(15) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(16) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(17) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(18) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(19) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(0.5)  
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(1) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(2) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(3) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(4) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(5) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(6) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(7) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(1) 
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(8) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(9) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(10) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(11) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(12) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(13) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(14) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(15) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(16) .ui-radio:nth-child(2) > .ui-btn"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(17) .ui-radio:nth-child(1) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(18) .ui-radio:nth-child(2) .mrQuestionText"))).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(19) .ui-radio:nth-child(1) > .ui-btn"))).click()
        time.sleep(0.5)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click() 
        time.sleep(1.5) 
            
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Floor sander')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Mineral spirits')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Deck cleaner')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        time.sleep(0.5)    
            
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Benjamin Moore')]"))).click()
        time.sleep(0.1) 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Walmart')]"))).click()
        time.sleep(0.1) 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Home Depot')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        
        time.sleep(1)    
            
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Benjamin Moore')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Walmart')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(0.5)               
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Determining what product to buy')]"))).click()
        time.sleep(0.1) 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Sales staff not knowledgeable / helpful')]"))).click()
        time.sleep(0.1) 
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Adhering to my budget')]"))).click()
        time.sleep(0.1)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(1) 
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Determining what product to buy')]"))).click()
        time.sleep(0.2)
        wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
        time.sleep(2.5)
        jumper= driver.find_element(By.XPATH, "//a").get_attribute("href")
       
        
        #print(jumper)
            
            #time.sleep(5)    
            
        value= {"jumper":jumper}
            #json_compatible_item_data = jsonable_encoder(value)  
            
        time.sleep(0.5)    
        return  JSONResponse(content=value)  
        
    
    
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="7341 no encontrado Error 404")
        #pass
    
    
    finally:
    
        driver.quit() 
    
    
