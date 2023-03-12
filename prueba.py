




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


