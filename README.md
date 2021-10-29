# Automation RPA Engineer test task for [Zoral](https://zorallabs.com/)

Using [Robot Framework](https://robotframework.org) and [SeleniumLibrary](https://github.com/robotframework/SeleniumLibrary/) implement following scenario:

* website: https://www.aihitdata.com
* goal:
  * login
  * search for mortgage companies located in US
  * scrape first 30 companies including following fields:
  * name
  * website
  * address
  * email
  * phone
  * collect scraping results to a single variable ${output}, it will be considered script output and assignment result
