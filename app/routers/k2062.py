from fastapi import APIRouter, HTTPException
from webdriver import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
router = APIRouter (    
    prefix= "/k2062"
    #tags= ["Kmils"]
)




@router.get("/1/{psid}/{pid}/{ord}")
def k2062(psid, pid, ord):
    
    try:
        driver=iniciar_chrome_bots()
        driver.request_interceptor = intercept  
        driver.delete_all_cookies()      
        wait = WebDriverWait(driver, 0.5)
        url= "https://ca1.qualtrics.com/jfe/form/SV_3ZO25bQavcRFA10?opp=Qual2751-0210-CXBenchmarking%20|%20Mr.%20Cooper&gc=1&&Country=&Location=&Wave=Q1%202023&email=&V=D_API&rid=&RISN=&uig=&gid=&sname=&uid=&PID="+pid+"&psid="+psid+"**&K2=&med=&id=&ppsid=&vid=&token=&sid=&EOLID=&password=&cintid=&ProjectToken=0a239158-0588-be97-c4d3-32147930d19c&job=&custom1=&YGID=&ID=&identifier=&pcid=&sesskey=&zid=&viga=&enc=&table=&tid=&usg=&ClientDuration=44&LS=&wspid=&ss=&ST=&pid=&k2=&spid=&CMRID=&EMI=&ss=&ClientDuration=&transaction_id=&cmpid=&digid=&ejid=&tk=&orderNumber="+ord+"&RE=&city=&tg=&sdv=&ERID=&ESID=&SVID=&PS="
        driver.get(url)
        time.sleep(1.5)
        #driver.execute_script("window.stop();")  
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
        raise HTTPException(status_code=404, detail="K2062 no encontrado, Error 404")
    
    
    finally:
    
        driver.quit()   