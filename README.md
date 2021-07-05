# 1. Basic 1 

    //Path to chrome driver have been dowload
    PATH = r"C:\Users\DUYEN\Desktop\chromedriver.exe"
    
    // Type input search and get data return
    # elem = driver.find_element_by_name("q")
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)

# Chapter 1:  Locating Elements From HTML

    driver.find_element_by_name("s")
    
    # Load source page
    driver.page_source

    main = driver.find_element_by_tag_name("main")
    print(main.text)

    find_elements_by_tag_name("article")  ==> element(s)

# Chapter 2: Navigation and Clicking

    link = driver.find_element_by_link_text("Python Programming")
    link.click()

    driver.back()
    driver.forward()

    link_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    link_text.click()
