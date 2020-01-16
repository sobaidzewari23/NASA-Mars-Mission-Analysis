# NASA-Mars-Mission-Analysis
Web Scraping of NASA Mars Mission Data Using Python with Splinter, BeautifulSoup, and Flask, HTML, and MongoDB

NASA-Mars-Mission-Analysis
The goal of this project was to develop a webpage to present scraped data from several NASA Mars Mission websites. Python with Splinter, BeautifulSoup, and Pandas, and MongoDB were used to scrape and store the required data, and Python with Flask was used to automate those processes. HTML with Bootstrap CSS was used to generate and format the completed webpage presenting the scraped data.

Questions
Find and present the name and summary of the latest Mars news article.
Find and present the latest Mars featured image.
Find and present the latest Mars weather report.
Find and present the latest Mars facts.
Find and present the latest Mars hemisphere images.
Datasets
https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
https://twitter.com/marswxreport?lang=en
https://space-facts.com/mars/
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
Tasks
Web Scraping
Create a connection to the Google Chrome browser.
Auto-load the Mars news webpage in the browser and scrape the data.
Parse the HTML data, and extract the title and summary of the latest article.
Auto-load the Mars images webpage in the browser and scrape the data.
Parse the HTML data, and extract the link of the latest Mars featured image.
Auto-load the Mars weather Twitter webpage in the browser and scrape the data.
Parse the HTML data, and extract the text of the latest Mars weather report.
Auto-load the Mars facts webpage in the browser and scrape the data.
Parse the HTML data, and extract the table of the latest Mars facts.
Auto-load the Mars hemisphere webpages in the browser and scrape the data from each page.
Parse the HTML data from each page, and extract the links of the latest Mars hemisphere images.
Compile all of the extracted data into a Python dictionary.
Flask App Development
Create a connection to the MongoDB engine, and set the path to the appropriate database and collection.
Create a Scrape route that imports and calls the Python scraping code, and stores the outputted Python dictionary in MongoDB.
Create a Home route that loads the stored Python dictionary from MongoDB and passes it to the HTML webpage.
HTML Webpage Development
Create a navigation bar with a header and a button that calls the Scrape route from the Flask App.
Create a content card to display the name and summary of the latest Mars news article.
Create a content card to display the latest Mars featured image.
Create a content card to display the latest Mars weather report.
Create a content card to display the latest Mars facts.
Create a content card to display the latest Mars hemisphere images.
Results
http://localhost:5000/ (Python Flask App and MongoDB must be running on the local machine to enable full site functionality.)
