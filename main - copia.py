from fastapi import FastAPI, HTTPException

from pydantic import BaseModel
from webdriver import *
from webdriverusa import *
from webdriveruk import *
import os
import requests
from requests import get
import json
import pychrome
import urllib.request
import asyncio
app = FastAPI()
 
  

 
  
  
    

class Msg(BaseModel):
    msg: str
    secret: str
    
''' def enter_proxy_auth(PROXY_USER, PROXY_PASS):
    time.sleep(2)
    pyautogui.typewrite(PROXY_USER)
    pyautogui.press('tab')
    pyautogui.typewrite(PROXY_PASS)
    pyautogui.press('enter')
    
def open_a_page(driver, url):
    driver.get(url)   
'''


@app.middleware("http")
async def add_process_time_header(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(f'{process_time:0.4f} sec')
    return response

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}




@app.get("/wix/{psid}/{pid}")
async def wix(psid, pid):
    
    driver=iniciar_chrome_bots()
    driver.delete_all_cookies()      
    
    url= "https://online.ssisurveys.com/wix/4/p6845224.aspx?__extsid__=G7CtaTKM%2fMYgmAPZcDQRRxIlSjobyiOeVAPW5%2b7BZY6L7tUzHJfGmmACr%2fOcJzzdZroSh5Hf%2bFC7jttr1mxOc7LKmhgfnc7mP%2fFitX0hNuU%3d&PID="+pid+"&&psid="+psid+"**subpanelid=180&sc=11&country=27&l=&ORD=ORD-778918-L4N5"
    driver.get(url)
    
    #time.sleep(0.5)con proxy    
   
    driver.execute_script("window.stop();")    

    jumper = driver.current_url
    print(jumper)
    #input("pulsar enter para salir")     
   
    driver.close()    
    
    return{"jumper":jumper}



@app.get("/k3203/{psid}/{pid}")
async def k3203(psid, pid):
    
    driver=iniciar_chrome_bots()
    driver.delete_all_cookies()  
    action = ActionChains(driver)  
    wait = WebDriverWait(driver, 0.5)
    url= "https://eu2.qualtrics.com/jfe/form/SV_e9jNvyJvDT3H3IW?tid=&LS=&ac=&cintID=&cintid=&custom1=&EOLID=&EOL=&Location=&location=&YouGov_ID=&Fed=&ft=&ftouch=&Gender=&gid=&id=&ID=&sid=&invitation_id=&K2=&lang=&luth=&mcid=&mid=&owsid=&basic=&PID=&ppsid=&psid="+psid+"**&rid=&RISN=&V=D_API&rnid=&sesskey=&sid=&sn=&sname=&subsid=&uid=&uig=&user_id=&vid=&code=&country=&l=&m=&p=&Country=US&Hispanic=&iisID=&med=&MID=&name=&oldvid=&pid="+pid+"&ProjectToken=&QID=&race=&Segment=&rst=&Service=&study=&t=&Term=&password=&job=&ticket=&token=&UID=&WCE=&offer_click_id=&Preview=&sub_id=&respid=&projectid=&i_survey=&surveyID=SV_eJP53P9xZW0XnG6&opp=BookingTravelBrandTrack2023&p=&cmpid=&tk=&ejid=&TolunaEnc=51&qvs=&qvq2=&qvq=&qvc=&wspid=&GWSID=&viga=&CMRID=&Research_ID=&moid=&ppid=&ppgc1=&ppgc2=&ppgc3=&ppgc4=&pp=&s=&Q_TotalDuration=99&wave=&S=&transaction_id=&ref=&gc=1&term=screener1&orderNumber=ORD-792295-R6R2&tg="
    driver.get(url)
    driver.set_page_load_timeout(1)
    driver.execute_script("window.stop();") 
    #time.sleep(0.01)
    #pyautogui.press('esc') 
    #action.send_keys(Keys.ESCAPE)  
    time.sleep(6)
    jumper= wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='EndOfSurvey']/a"))).get_attribute("href")
    print(jumper)    
           
    
    #input("pulsar enter para salir")
    driver.quit()  
    value= {"jumper":jumper}  
     
    return json.dumps(value) 


@app.get("/k3715/{psid}")
async def k3715(psid):
    
    driver=iniciar_chrome_bots()
    driver.delete_all_cookies()  
    action = ActionChains(driver)  
    wait = WebDriverWait(driver, 0.5)
    url= "https://survey.az1.qualtrics.com/jfe/form/SV_5zI0gZnyf8BxYWO?psid="+psid+"**&_k=3715"
    driver.get(url)
    #driver.execute_script("window.stop();") 
    
    time.sleep(2)
    
    wait.until(ec.visibility_of_element_located((By.ID, "QID2-1-label"))).click()
    time.sleep(1)
    wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()
    time.sleep(4)
    #wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@choiceid='1']"))).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='QR~QID98~1']"))).click()
    time.sleep(1)
    wait.until(ec.visibility_of_element_located((By.ID, "NextButton"))).click()
    
    '''     t= driver.find_element(By.XPATH, "//strong")
    t=t.text
      
    //*[@id="QR~QID98~1"]
    
    #sky    
    a=wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='QID98-1-label']/img"))).get_attribute('alt')
    print(a)
    
    #Hamburger
    b=wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='QID98-4-label']/img"))).get_attribute('alt')
    print(b)
    #train
    c=wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='QID98-2-label']/img"))).get_attribute('alt')
    print(c)
    #dog
    d=wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='QID98-5-label']/img"))).get_attribute('alt')
    print(d) '''
    
    #if t in 'blue sky':
        
        
    '''   
    elif t==b:
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@choiceid='4']"))).click()
     
    elif t==c:
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@choiceid='2']"))).click()
     
    elif t==d:
        
        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@choiceid='5']"))).click()
    '''
     
     
    input("pulsar enter para salir")
     
     
     
     
     
     
     
    #action.send_keys(Keys.ESCAPE)  
    time.sleep(15)
    jumper= wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='EndOfSurvey']/a"))).get_attribute("href")
    print(jumper)    
           
    
    #input("pulsar enter para salir")
    driver.quit()  
    value= {"jumper":jumper}  
    return json.dumps(value) 



@app.get("/k2062/{psid}/{pid}/{ord}")
async def k2062(psid, pid, ord):
    
    driver=iniciar_chrome_bots()
    driver.delete_all_cookies()  
    action = ActionChains(driver)  
    wait = WebDriverWait(driver, 0.5)
    url= "https://ca1.qualtrics.com/jfe/form/SV_3ZO25bQavcRFA10?opp=Qual2751-0210-CXBenchmarking%20|%20Mr.%20Cooper&gc=1&&Country=&Location=&Wave=Q1%202023&email=&V=D_API&rid=&RISN=&uig=&gid=&sname=&uid=&PID="+pid+"&psid="+psid+"**&K2=&med=&id=&ppsid=&vid=&token=&sid=&EOLID=&password=&cintid=&ProjectToken=0a239158-0588-be97-c4d3-32147930d19c&job=&custom1=&YGID=&ID=&identifier=&pcid=&sesskey=&zid=&viga=&enc=&table=&tid=&usg=&ClientDuration=44&LS=&wspid=&ss=&ST=&pid=&k2=&spid=&CMRID=&EMI=&ss=&ClientDuration=&transaction_id=&cmpid=&digid=&ejid=&tk=&orderNumber="+ord+"&RE=&city=&tg=&sdv=&ERID=&ESID=&SVID=&PS="
    driver.get(url)
    driver.set_page_load_timeout(1.5)
    driver.execute_script("window.stop();")  
    #action.send_keys(Keys.ESCAPE)  
    time.sleep(6)
    jumper= wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='EndOfSurvey']/a"))).get_attribute("href")
    print(jumper)    
           
    
    #input("pulsar enter para salir")
    driver.quit()   
    return{"jumper":jumper} 


@app.get("/k1000/{psid}/{pid}")
async def k1000(psid, pid):
    
    driver=iniciar_chrome_bots()    
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
  
   
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".element:nth-child(4) label"))).click()    
    wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click() 
      
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(1) > .cell:nth-child(2)"))).click()    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row-elements:nth-child(2) > .cell:nth-child(2)"))).click()   
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(3) > .cell:nth-child(3) .fir-selected"))).click()    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(4) > .cell:nth-child(4) .fir-selected"))).click()     
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(5) > .cell:nth-child(5) .fir-selected"))).click()    
    
    wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()   
    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(1) > .cell:nth-child(2)"))).click()   
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row-elements:nth-child(2) > .cell:nth-child(2)"))).click()  
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(3) > .cell:nth-child(3) .fir-selected"))).click()    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(4) > .cell:nth-child(4) .fir-selected"))).click()     
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(5) > .cell:nth-child(5) .fir-selected"))).click()    
    wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()    
    
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
    time.sleep(15)    

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
    driver.set_page_load_timeout(60)  
    
    #driver.execute_script("window.stop();")
    #driver.execute_script("window.stop();")
    #driver.find_element(By.tagName("body")).sendKeys("Keys.ESCAPE");
    #time.sleep(10)
    #wait.until(ec.url_matches("/2204164?state"))
    #requests.post('https://survey-d.dynata.com/survey/selfserve/53c/2204164#!)',timeout=2.000).close()
   
   # wait.until(ec.url_matches("end"), driver.execute_script("window.stop();") ) 
    jumper = driver.current_url     
            
    print(jumper)    
    input('esperando')
    driver.quit()
    return{"jumper":jumper} 

    

'''   if wait.until( lambda driver: driver.current_url == "https://survey-d.dynata.com/survey/selfserve/53c/2204164#!)"):
          
        driver.execute_script("window.stop();")
        jumper= driver.find_element(By.XPATH, "//a").get_attribute("href")
        print(jumper)    
        
        return{"jumper":jumper} '''




#https://survey-d.dynata.com/survey/selfserve/53c/2204164?

#//dkr1.ssisurveys.com/projects/end?rst=1&psid=cwuLnLLgPGW4hn5H49vhfd**&high=13099526388689&_k=1000&_s=400bf2e366e60fa04a0bec150b7bee27a4ad258d
 #https://survey-d.dynata.com/survey/selfserve/53c/2204164
  #https://survey-d.dynata.com/survey/selfserve/53c/2204164
  #https://survey-d.dynata.com/survey/selfserve/53c/2204164#!)
#https://survey-d.dynata.com/survey/selfserve/53c/2204164?state=3dd2ce47-d035-4b8d-8f24-4837ad49ca41



#https://survey-d.dynata.com/survey/selfserve/53c/2204164?v2async=speederAutoCheckAPI&state=f04f04cb-2a3b-4724-a70f-9f7d3cf72f4f

#https://dkr1.ssisurveys.com/projects/end?rst=1&psid=4gbuSlIEXGxHJqoxFzh4edQ**&high=13366200336129&_k=1000&_s=48618572321ef9f14f3b37a80abf033c5a4396bb

@app.get("/7341/{psid}")
async def K7341(psid):
    
    driver=iniciar_chrome_bots()    
    driver.delete_all_cookies()    
    
    
    wait = WebDriverWait(driver, 10)
   
    url= "https://webtraffic.datacollectionsite.com/mriweb/mriweb.dll?I.Project=P220751&ID="+psid+"**&smp=45&_k=7341&_s=444d22efab363d0f2c5fd2195e59fc4af04008d4983b1d90b9ab5e09b631e158&I.User6=Q2hyb21lIHx8IENocm9tZSAxMDIgfHwgV2luZG93cyAxMCB8fCBXaW5kb3dzIDEwIHx8IE4vQSB8fCBEZXNrdG9wL2xhcHRvcCB8fCBDT01QVVRFUiB8fCBGYWxzZSB8fCAwQkZCRDhBQi0yREY2LTRBM0ItODY3Ny1FRjk3QzY5RUUxQjU%3D#running"
    driver.get(url)
    driver.set_page_load_timeout(10)    
    time.sleep(3)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ui-first-child"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()    
    
    wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("1996")
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ui-last-child"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".ui-last-child"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()   
    
    wait.until(ec.visibility_of_element_located((By.ID, "_Q0"))).send_keys("10104")
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()    
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()    
    
    wait.until(ec.visibility_of_element_located((By.ID, "_Q0_Q0_Q0"))).send_keys("amazon")
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Woodscapes')]"))).click()
    
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Kilz')]"))).click()
    
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Benjamin Moore')]"))).click()   
 
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Benjamin Moore')]"))).click()
    time.sleep(0.5)
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
    time.sleep(1) 
    
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
    time.sleep(1)      
    
    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(1) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(2) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(3) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(4) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(5) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(6) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(7) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(8) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(9) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(10) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(11) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(12) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(13) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(14) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(15) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(16) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(17) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(18) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(19) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    time.sleep(1)
    
    #input('esperar') # por ide _Q0_C3
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'I have used previously and will use again in the future')]"))).click()
    time.sleep(1)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    time.sleep(1)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(1) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(2) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(3) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(4) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(5) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(6) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(7) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(8) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(9) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(10) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(11) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    time.sleep(1)
    
    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(1) .ui-radio:nth-child(1) .mrQuestionText"))).click()

    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(2) .ui-radio:nth-child(2) .mrQuestionText"))).click()
 
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(3) .ui-radio:nth-child(1) .mrQuestionText"))).click()

    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(4) .ui-radio:nth-child(2) .mrQuestionText"))).click()

    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(5) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    time.sleep(1)
    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(1) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(1)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(2) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(3) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(4) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(5) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    time.sleep(1)
    
    
    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(1) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(1)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(2) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(3) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(4) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(5) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(6) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)  
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(7) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(8) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(9) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(10) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(11) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(12) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(13) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(14) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(15) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(16) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(17) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(18) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(19) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(0.5)    
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    
    time.sleep(1)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(1) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(1)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(2) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(3) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(4) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(5) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(6) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(7) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)    
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(8) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(9) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(10) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(11) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(12) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(13) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(14) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(15) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(16) .ui-radio:nth-child(2) > .ui-btn"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(17) .ui-radio:nth-child(1) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(18) .ui-radio:nth-child(2) .mrQuestionText"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".collapsible-button-group:nth-child(19) .ui-radio:nth-child(1) > .ui-btn"))).click()
    time.sleep(0.5) 
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click() 
    time.sleep(1.5) 
         
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Floor sander')]"))).click()
    
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Mineral spirits')]"))).click()
   
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Deck cleaner')]"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    
    time.sleep(1)    
        
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Benjamin Moore')]"))).click()
   
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Walmart')]"))).click()
    
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Home Depot')]"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    
    time.sleep(1)    
        
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Benjamin Moore')]"))).click()
    
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Walmart')]"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    time.sleep(1) 
    
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Determining what product to buy')]"))).click()
    
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Sales staff not knowledgeable / helpful')]"))).click()
    
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Adhering to my budget')]"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    time.sleep(1) 
    
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Determining what product to buy')]"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.NAME, "_NNext"))).click()
    time.sleep(0.2)
    if wait.until( lambda driver: driver.current_url == "https://webtraffic.datacollectionsite.com/mriweb/mriweb.dll#running"):
            
        driver.execute_script("window.stop();")
        jumper= driver.find_element(By.XPATH, "//a").get_attribute("href")
        print(jumper)    
        #input('esperando')
        return{"jumper":jumper}
    
    
    driver.quit() 
    #driver.close()
  






@app.get("/k1092/{psid}/{hash}")
async def K1092(psid, hash):
    driver=iniciar_chrome_bots()    
    driver.delete_all_cookies()    
    
    
    wait = WebDriverWait(driver, 5)    
   
          
   
    time.sleep(2)
    
    url= "https://www.surveys.com/start.aspx?SSID=5CAA66E2-BD74-4F45-91DE-A8805BD87C5C&IP_TargetGroup=3&EXTID="+psid+"**&EXTSupplierSourceID=1&_k=1092&_s="+hash+""
    driver.get(url)
     
    time.sleep(27)
    
    
    try:
        wait.until(ec.visibility_of_element_located((By.ID, "l_1033_label"))).click()    
    except:
        wait.until(ec.visibility_of_element_located((By.ID, "l_1033_label"))).click()
        
    
    wait.until(ec.visibility_of_element_located((By.ID, "forwardbutton"))).click()
    time.sleep(0.1)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".prettycheckbox > a"))).click()    
    time.sleep(0.1)
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
    wait.until(ec.visibility_of_element_located((By.ID, "age_1"))).send_keys("30")
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
        wait.until(ec.visibility_of_element_located((By.ID, "FinalDecOffiW_1_label"))).click()
         
         
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
    time.sleep(0.7) 
    driver.execute_script("window.stop();")
    jumper = driver.current_url    
    print(jumper)
    driver.quit()    
    return{"jumper":jumper}
       
       
       
       
       
@app.get("/k1000-2/{psid}/{pid}")
async def k1000C(psid, pid):
   
  
    driver=iniciar_chrome_bots()   
    driver.delete_all_cookies()   
    
    wait = WebDriverWait(driver, 10)
    
    url = "https://survey-au.dynata.com/survey/selfserve/53b/2202224?list=2&pid="+pid+"&psid="+psid+"**&C=2&W=1&decLang=english&sp=181&pp=0&sc=3&ppid="   
    #params = {"status_code": 302, "url": url}
    #r = requests.get(url, params=params)
    
    driver.get(url)
 
            
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".element:nth-child(4) .fir-selected"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()    
    time.sleep(0.5)
    
    wait.until(ec.visibility_of_element_located((By.ID, "ans30405.0.0"))).send_keys("35")
    time.sleep(0.5)

    wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()
    time.sleep(0.5)
    
    wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Dior')]"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Chanel')]"))).click()
    time.sleep(0.5)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Oreal')]"))).click()
    time.sleep(0.5)
   
    #input('esperando')
    
    #desired_url ='https://survey-au.dynata.com/survey/selfserve/53b/2202224'
    #response=requests.get(url) 
    #r = requests.head(url, allow_redirects=True)
   
    wait.until(ec.visibility_of_element_located((By.ID, "btn_continue"))).click()
    driver.set_page_load_timeout(1.5)
    #if wait.until(ec.url_changes(("https://survey-au.dynata.com/survey/selfserve/53b/2202224"))):    
    pyautogui.press('esc')
    #driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
    
    #if wait.until(ec.url_contains(("end"))):
        #driver.execute_script("window.stop();")
          
    #requests.get(url, allow_redirects=False)
    jumper = driver.current_url
    print(jumper)
          #http://www.w3.org/1999/xhtml
          
    #finalurl = res.geturl
    #print(finalurl)
    #response.history
    #print(r.history)
    
    
    
    time.sleep(20)
        
    
    
    #driver.execute_script("window.alert();")
    
    
    
    #driver.execute_script("window.stop();")
    
    
   
    #time.sleep(60)
    
    driver.quit()    
    #return{"jumper":jumper}    




    '''  def wait_for_correct_current_url(desired_url):
        wait.until(lambda driver: driver.current_url != desired_url)
        driver.execute_script("window.stop();")
    '''


   #<form id="primary" name="primary" method="post" action="/survey/selfserve/53b/2202224" enctype="application/x-www-form-urlencoded">

   #<input type="submit" name="continue" id="btn_continue" class="button continue" value="Continue >" onclick="var i = document.createElement('input'); i.setAttribute('type', 'hidden');i.setAttribute('value', '1');i.setAttribute('name', '__has_javascript');document.forms.primary.appendChild(i);">


  



  
    #content = requests.get('https://survey-au.dynata.com/survey/selfserve/53b/2202224?v2timing=48k7cwyp7j3rrj9p,w4ytaur3ea5rm7vc,294,411,411', params=params,  headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}, allow_redirects = False).content 
    #driver.execute_script("window.stop();")
    #params = {"status_code": 302}   
    #r = requests.get('https://survey-au.dynata.com/survey/selfserve/53b/2202224', allow_redirects=False)
   
   
   
'''  def  intercept(request):
       
       if request.url.starswith ("https://dkr1.ssisurveys.com"):
           request.abort
    
    driver.request_interceptor =intercept
     '''
   
    #driver.execute_script("window.stop();")   
    #input('esperando')
    
    #driver.find_element(By.CSS_SELECTOR, ".sq-cardsort-bucket-item-c2").click().execute_script("window.alert();") 
    #params= {'key':'AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw'}
    #content = requests.get('https://survey-au.dynata.com/survey/selfserve/53b/2202224', headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}, allow_redirects = False).content 


         
'''def  intercept(request):
           
        if request.driver.current_url.starswith("https://survey-au.dynata.com/survey/selfserve/53b/2202224"):
           request.abort()
    
    driver.request_interceptor =intercept
    
    driver.get("https://survey-au.dynata.com/survey/selfserve/53b/2202224")
    
    
    
    
    
     driver.current_url
    driver.execute_script("window.stop();")
    for request in driver.requests:
    print(request.url, request.response.status_code, request.response.headers['Content-Type']) '''
    
    #r1 = requests.get(content.headers[0])
    #print(content)    
    
   
   
   #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
   
    #r = requests.get(url, allow_redirects=false)    
        
    
    #print(r.history)
    #print(r.status_code)
    
    #driver.set_page_load_timeout(0.5)
    #time.sleep(10)
    # r = requests.get(url, params=params, allow_redirects=False)  
    #driver.set_page_load_timeout(10)
    #print (url.status_code)    
    #jumper= wait.until(ec.visibility_of_element_located((By.XPATH, "//a"))).get_attribute("href")
    
     #raise_for_status    
         
    #r=requests.get('https://survey-au.dynata.com/survey/selfserve/53b/2202224', allow_redirects=False)
    
''' POST https://survey-au.dynata.com/survey/selfserve/53b/2202224 HTTP/1.1
Host: survey-au.dynata.com
Connection: keep-alive
Content-Length: 154
Cache-Control: max-age=0
sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: https://survey-au.dynata.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://survey-au.dynata.com/survey/selfserve/53b/2202224
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,es;q=0.8,es-US;q=0.7
Cookie: IRIS_SESSION=pfzxjufx7pg1m9cs


HTTP/1.1 302 Found
Date: Tue, 07 Feb 2023 00:26:40 GMT
Server: Apache
X-Content-Type-Options: nosniff
Content-Length: 482
x-xss-protection: 1; mode=block
Expires: Wed, 14 Feb 1996 00:26:40 GMT
Location: //dkr1.ssisurveys.com/projects/end?rst=1&psid=9r0uSlIEXGxHJqoxFzhhwD**&basic=44455&_k=1000&_s=cfef0d548bd6be822679a8875359971ac28fb32b
Content-Type: text/html; charset=utf-8
Set-Cookie: IRIS_SESSION=pfzxjufx7pg1m9cs; expires=Thu, 09-Mar-2023 00:26:40 GMT; httpOnly; Path=/; secure;
Keep-Alive: timeout=60, max=94
Connection: Keep-Alive '''



     
    
       
                                         
                                                

#https://survey-au.dynata.com/survey/selfserve/53b/2202224#&
   
#POST https://survey-au.dynata.com/survey/selfserve/53b/2202224 HTTP/1.1

#https://survey-au.dynata.com/survey/selfserve/53b/2202224?v2timing=48k7cwyp7j3rrj9p,w4ytaur3ea5rm7vc,294,411,411


''' POST https://survey-au.dynata.com/survey/selfserve/53b/2202224 HTTP/1.1
Host: survey-au.dynata.com
Connection: keep-alive
Content-Length: 154
Cache-Control: max-age=0
sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: https://survey-au.dynata.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://survey-au.dynata.com/survey/selfserve/53b/2202224
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,es;q=0.8,es-US;q=0.7
Cookie: IRIS_SESSION=pfzxjufx7pg1m9cs


HTTP/1.1 302 Found
Date: Tue, 07 Feb 2023 00:26:40 GMT
Server: Apache
X-Content-Type-Options: nosniff
Content-Length: 482
x-xss-protection: 1; mode=block
Expires: Wed, 14 Feb 1996 00:26:40 GMT
Location: //dkr1.ssisurveys.com/projects/end?rst=1&psid=9r0uSlIEXGxHJqoxFzhhwD**&basic=44455&_k=1000&_s=cfef0d548bd6be822679a8875359971ac28fb32b
Content-Type: text/html; charset=utf-8
Set-Cookie: IRIS_SESSION=pfzxjufx7pg1m9cs; expires=Thu, 09-Mar-2023 00:26:40 GMT; httpOnly; Path=/; secure;
Keep-Alive: timeout=60, max=94
Connection: Keep-Alive
 '''




#@app.get("/Descalificador_Usa/{psid}")
@app.get("/Descalificador_Usa/{psid}")
async def Dusa(psid):
 
        
    driverusa=iniciar_chrome_usa()
    driverusa.delete_all_cookies()  
     
    time.sleep(3)
    Thread(target=enter_proxy_auth, args=(PROXY_USER, PROXY_PASS)).start()    
    Thread(target=open_a_page, args=(driverusa,"https://dkr1.ssisurveys.com/projects/pstart?psid="+psid+"&subpanelid=179")).start()     
    #Thread(target=open_a_page, args=(driverusa,"https://whoer.net")).start() 
    
    
    driverusa.execute_script("window.stop();")  
    #action.send_keys(Keys.ESCAPE)  
    time.sleep(12)
    #driverusa.delete_all_cookies() 
           
    
    #input("pulsar enter para salir")
    driverusa.quit()   
    return{"jumper":"Descalificación Exitosa"} 


@app.get("/Descalificador_Uk/{psid}")
async def Duk(psid):
    
    driveruk=iniciar_chrome_uk()
    driveruk.delete_all_cookies()  
     
    time.sleep(3)
    Thread(target=enter_proxy_auth, args=(PROXY_USER, PROXY_PASS)).start()    
    Thread(target=open_a_page, args=(driveruk,"https://dkr1.ssisurveys.com/projects/pstart?psid="+psid+"&subpanelid=179")).start()     
    #Thread(target=open_a_page, args=(driverusa,"https://whoer.net")).start() 
    
    
    driveruk.execute_script("window.stop();")  
    #action.send_keys(Keys.ESCAPE)  
    time.sleep(12)
    #driverusa.delete_all_cookies() 
           
    
    #input("pulsar enter para salir")
    driveruk.quit()   
    return{"jumper":"Descalificación Exitosa"} 