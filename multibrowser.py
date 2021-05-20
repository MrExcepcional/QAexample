#! /usr/bin/env python3.9

from threading import Thread


from selenium import webdriver


browsers = [
    {
        "platform": "Windows 7 64-bit", 
        "browserName": "Internet Explorer",
        "version": "10", "name": "Python Parallel"
    },
    {
        "platform": "Windows 8.1",
        "browserName": "Chrome",
        "version": "50",
        "name": "Python Parallel"
    },
]

browsers_***REMOVED***ing = []

def get_browser_and_***REMOVED***(browser_data):
    print ("starting %s\n" % browser_data["browserName"])
    browser = get_browser(browser_data)
    browser.get("http://crossbrowsertesting.com")
    browsers_***REMOVED***ing.append(
        {"data": browser_data, "driver": browser}
    )
    print ("%s ready" % browser_data["browserName"])
    while len(browsers_***REMOVED***ing) < len(browsers):
        print ("working on %s.... please ***REMOVED***" % browser_data["browserName"])
        browser.get("http://crossbrowsertesting.com")
        time.sleep(3)

threads = []

for i, browser in enumerate(browsers):
    thread = Thread(target=get_browser_and_***REMOVED***, args=[browser])
    threads.append(thread)
    thread.start()
    for thread in threads:
        thread.join()
    print ("all browsers ready")

    for i, b in enumerate(browsers_***REMOVED***ing):
        print ("browser %s's title: %s" % (b["data"]["name"], b["driver"].title))
        b["driver"].quit()