## WebPy_HW10

The following has been completed in this task [^1]:

* Registration on the site and enter the site. 
* The ability to add a new author to the site, only for a registered user. 
* The ability to add a new quote to the site, indicating the author, only for a registered user. 
* You can go to the page of each author without user authentication 
* All quotes are viewable without user authentication
* Pagination. These are the next and previous buttons 
* To convert data from MongoDB to Django objects and store them in SQLite. In order to check if it works, the 
  following should be performed:
     1. Launch an interactive Python shell from a terminal:&nbsp;&nbsp;&nbsp;&nbsp;
     
                `python manage.py shell`
     2. Import models:&nbsp;&nbsp;&nbsp;&nbsp;
     
                `from quoteapp.models import Tag, Author, Quote`
     3. Run queries against the database to verify that the objects have been saved:&nbsp;&nbsp;&nbsp;&nbsp;
     
                `tags = Tag.objects.all()`
                 `print(tags)`



[^1]: Login -> Japan, 
      Password -> Seoul2023!
