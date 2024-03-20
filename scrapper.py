from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://result.npgc.in/")
time.sleep(3)
file=open("results.txt","w")
data=""

rollStart = int(input("Enter First Roll No: "))
rollEnd = int(input("Enter Last Roll No: "))

for roll in range(rollStart, rollEnd+1):
    roll = str(roll)
    time.sleep(1)
    driver.find_element(by="xpath", value="/html/body/form/div[3]/div[2]/div/div/article/div[5]/div[1]/input").clear()
    driver.find_element(by="xpath", value="/html/body/form/div[3]/div[2]/div/div/article/div[5]/div[1]/input").send_keys(roll)
    driver.find_element(by="xpath", value="/html/body/form/div[3]/div[2]/div/div/article/div[5]/div[2]/input").click()
    time.sleep(1)
    try:
        name=driver.find_element(by="xpath",value="/html/body/form/div[3]/div[2]/div/article/div[4]/table/tbody/tr[3]/td[3]/span").text
        text=driver.find_element(by="xpath",value="/html/body/form/div[3]/div[2]/div/article/div[7]/div/p/span").text
        print(roll,name,text)
        data=data+"\n"+roll+" "+name+" "+text
        driver.back()
    except:
        print("Roll no not registered")

file.write(data)
file.close()
        


