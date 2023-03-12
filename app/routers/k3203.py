from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
router = APIRouter (    
    prefix= "/k3203"
    #tags= ["Kmils"]
)




@router.get("/1/{psid}/{pid}/{ord}")
def k3203(psid, pid, ord):
    
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept  
        driver.delete_all_cookies()  
        action = ActionChains(driver)  
        wait = WebDriverWait(driver, 0.5)
        url= "https://eu2.qualtrics.com/jfe/form/SV_e9jNvyJvDT3H3IW?tid=&LS=&ac=&cintID=&cintid=&custom1=&EOLID=&EOL=&Location=&location=&YouGov_ID=&Fed=&ft=&ftouch=&Gender=&gid=&id=&ID=&sid=&invitation_id=&K2=&lang=&luth=&mcid=&mid=&owsid=&basic=&PID=&ppsid=&psid="+psid+"**&rid=&RISN=&V=D_API&rnid=&sesskey=&sid=&sn=&sname=&subsid=&uid=&uig=&user_id=&vid=&code=&country=&l=&m=&p=&Country=US&Hispanic=&iisID=&med=&MID=&name=&oldvid=&pid="+pid+"&ProjectToken=&QID=&race=&Segment=&rst=&Service=&study=&t=&Term=&password=&job=&ticket=&token=&UID=&WCE=&offer_click_id=&Preview=&sub_id=&respid=&projectid=&i_survey=&surveyID=SV_eJP53P9xZW0XnG6&opp=BookingTravelBrandTrack2023&p=&cmpid=&tk=&ejid=&TolunaEnc=51&qvs=&qvq2=&qvq=&qvc=&wspid=&GWSID=&viga=&CMRID=&Research_ID=&moid=&ppid=&ppgc1=&ppgc2=&ppgc3=&ppgc4=&pp=&s=&Q_TotalDuration=99&wave=&S=&transaction_id=&ref=&gc=1&term=screener1&orderNumber="+ord+"&tg="
        driver.get(url)
        time.sleep(1.5)
        #driver.execute_script("window.stop();") 
        #time.sleep(0.01)
        #pyautogui.press('esc') 
        #action.send_keys(Keys.ESCAPE)  
        #time.sleep(6)
        #jumper= wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='EndOfSurvey']/a"))).get_attribute("href")
        #print(jumper)    
            
        
        #input("pulsar enter para salir")
        jumper = driver.current_url           
        value= {"jumper":jumper}
        #json_compatible_item_data = jsonable_encoder(value)
        time.sleep(0.5)    
        return  JSONResponse(content=value)  
    except:
        time.sleep(0.5) 
        raise HTTPException(status_code=404, detail="K3203 no encontrado, Error 404")
    
    
    finally:
    
        driver.quit()   