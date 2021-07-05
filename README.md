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
