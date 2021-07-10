# 1. Basic 1 

    //Path to chrome driver have been dowload
    PATH = r"C:\Users\DUYEN\Desktop\chromedriver.exe"
    
    // Type input search and get data return
    # elem = driver.find_element_by_name("q")
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)

    driver.close() // close one tab
    driver.quit() // close all tab

# Chapter 1:  Locating Elements From HTML

    driver.find_element_by_name("s")
    
    # Load source page
    driver.page_source

    main = driver.find_element_by_tag_name("main")
    print(main.text)

    find_elements_by_tag_name("article")  ==> element(s)

# Chapter 2: Navigation and Clicking

    <input type="text" name="passwd" id="passwd-id" />
    
    element = driver.find_element_by_id("passwd-id")
    element = driver.find_element_by_name("passwd")
    element = driver.find_element_by_xpath("//input[@id='passwd-id']")
    element = driver.find_element_by_css_selector("input#passwd-id")
    
    element.send_keys("some text")
    elem.send_keys(Keys.RETURN)
    element.clear()


    ### Select
    from selenium.webdriver.support.ui import Select
    select = Select(driver.find_element_by_name('name'))
    select.select_by_index(index)
    select.select_by_visible_text("text")
    select.select_by_value(value)

    # deselecting all the selected options:
    select = Select(driver.find_element_by_id('id'))
    select.deselect_all()

    # To get all available options:
    options = select.options
    
    #  list of all default selected options
    select = Select(driver.find_element_by_xpath("//select[@name='name']"))
    all_selected_options = select.all_selected_options
    

    ### Assume the button has the ID "submit" :)
    driver.find_element_by_id("submit").click()


    link = driver.find_element_by_link_text("Python Programming")
    link.click()

    driver.back()
    driver.forward()

    link_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    link_text.click()
    
# Locating by XPath
    
    <html>
     <body>
      <form id="loginForm">
       <input name="username" type="text" />
       <input name="password" type="password" />
       <input name="continue" type="submit" value="Login" />
       <input name="continue" type="button" value="Clear" />
      </form>
    </body>
    </html>
    
    login_form = driver.find_element_by_xpath("/html/body/form[1]")
    login_form = driver.find_element_by_xpath("//form[1]")
    login_form = driver.find_element_by_xpath("//form[@id='loginForm']")
   
    1. Absolute path (would break if the HTML was changed only slightly)
    2. First form element in the HTML
    3. The form element with attribute id set to loginForm

    username = driver.find_element_by_xpath("//form[input/@name='username']")
    username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
    username = driver.find_element_by_xpath("//input[@name='username']")
    
    1. First form element with an input child element with name set to username
    2. First input child element of the form element with attribute id set to loginForm
    3. First input element with attribute name set to username

    clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
    clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")


# Locating Hyperlinks by Link Text

    <html>
     <body>
      <p>Are you sure you want to do this?</p>
      <a href="continue.html">Continue</a>
      <a href="cancel.html">Cancel</a>
    </body>
    </html>
    
    continue_link = driver.find_element_by_link_text('Continue')
    continue_link = driver.find_element_by_partial_link_text('Conti')

# Locating Elements by CSS Selectors

    <html>
     <body>
      <p class="content">Site content goes here.</p>
    </body>
    </html>

    content = driver.find_element_by_css_selector('p.content')

# Locating Elements by Class Name and Tag name

    <html>
     <body>
      <p class="content">Site content goes here.</p>
    </body>
    </html>

    content = driver.find_element_by_class_name('content')
    content = driver.find_element_by_tag_name('p')

