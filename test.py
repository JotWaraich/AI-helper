from openai import OpenAI

def aws():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    opt = Options()
    opt.add_experimental_option("debuggerAddress", "localhost:8989")
    driver = webdriver.Chrome(options=opt)
    wait = WebDriverWait(driver, 60)
    
    driver.get('https://us-east-2.console.aws.amazon.com/console/home?nc2=h_ct&region=us-east-2')
    wait.until(EC.url_to_be('https://us-east-2.console.aws.amazon.com/console/home?nc2=h_ct&region=us-east-2'))
    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/div/div/main/div/div[2]/div/div/div/div/div[4]/div[2]/div/div[65]/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/a"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/div/nav[2]/div[2]/div/div/ul[1]/li[4]/div/div[2]/ul/li[1]/a"))).click()

def gpt3():
    client = OpenAI(api_key="your api key")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    print(completion.choices[0].message)

def main():
    new_string = input("Enter a string: ")
    while True:
        if new_string == "exit":
            break
        if new_string == "aws":
            aws()
            new_string = input("Enter a string: ")
            continue
        gpt3(new_string)
        new_string = input("Enter a string: ")

if __name__ == "__main__":
    main()
