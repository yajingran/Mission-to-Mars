# Mission-to-Mars
Int his project, I have used Beautiful Soup, Splinter and Pandas to scrape NASA web pages related to Mars, and used MongoDB and Flask to display the results on the automated webpage.

<br />First, I imported all dependencies and connected to the chromedriver to open the page I need to scrape. Then, I used Beautiful Soup parse through the HTML and search for appropriate elements and classes that contain the information needed. To do this, I used '''soup.find_all(). 

<br />Second, to grad the featured_image, I used '''browser.click_link_by_partial_text() and time.sleep() to access the webpages. To find the relative images path, I then used '''soup.find_all() and '''.a['href'], and combined it withthe main URL to get the full-sized image.

<br />Next, I used Pandas to scrape for tables by typing '''pd.read_html(). Then, I renamed the columns and and set the index. At the end, I used '''df.to_html() to convert the dataframe into an HTML table.
