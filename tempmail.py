from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time, BeautifulSoup

def open_link(link):
    browser2 = startBrowser()
    browser2.get(link)
    time.sleep(1)
    browser2.close()

def open_links(links):
    for link in links:open_link(link)
    
def startBrowser():
        return webdriver.PhantomJS()
        # chrome_options = Options()
        # chrome_options.add_argument("--disable-infobars")
        # return webdriver.Chrome(options=chrome_options)
        
def new_email():
    global browser
    try:a = browser
    except:browser = startBrowser()
    try:
        browser.get("https://www.guerrillamail.com/?fgt=1")
        email1 = browser.find_element_by_xpath('//*[@id="inbox-id"]').text
        email2 = browser.find_element_by_xpath('//*[@id="email-widget"]').text
        email2 = email2.split("@")[1]
        return email1 + "@" + email2
    except:return False

def get_links(body):
    links = []
    soup = BeautifulSoup.BeautifulSoup(body)
    for link in soup.findAll("a"):
        links.append(link.get("href"))
    return links

def get_mail():
    try:
        global browser
        mail = "There are no emails present in the inbox right now."
        while mail == "There are no emails present in the inbox right now.":
            mail = browser.find_element_by_xpath('//*[@id="email_list"]/tr/td').text
            time.sleep(1)
        browser.find_element_by_class_name("mail_row").click()
        time.sleep(2)
        title = browser.find_element_by_xpath("//*[@id='display_email']/div/div[2]/h3").text #title
        body = browser.find_element_by_xpath("//*[@id='display_email']/div/div[2]/div").get_attribute('innerHTML').strip() #body
        body = body.replace("<div>", "")
        body = body.replace("</div>", "")
        try:link = get_links(body)
        except Exception as e:
            link = None
            print(e)
        if link == []:link = None
        browser.close()
        return(title, body, link)
    except:return (False, False, False)
