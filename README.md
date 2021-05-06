The DM Vault
=============
A web-based repository of useful books, supplements and other resources for players and dungeon masters looking for new useful material for their tabletop roleplaying games.

## UX

### Target Audiences
This website is aimed mainly at tabletop RPG enthusiastiasts looking for new and relevant books, maps and other resources to enhance their games.
There are many sites that provide this service within their own domain, such as [The DMs Guild](https://www.dmsguild.com/) or [Kobold Press](https://koboldpress.com/kpstore/),
but the difference with the DM Vault is that it is not tied to any specific shop platform so can contain content from across various sites, indexed and searchable under various categories.

### Design

#### Layout

##### Initial Concept

![Wireframe Image of Initial Desktop UX Layout](https://github.com/cfconor/rpg-book-repository/blob/main/static/img/desktop%20wireframe.png)

As seen by the mockups, the design strategy for this website prioritised delivering relevant information to the user quickly, without much navigating around
the site or having to do several clicks. The information is presented as soon as the homepage is shown, and for most users this may be the only thing they 
need to use the website for, so having this shown first makes sense.

***

![Wireframe Image of Initial Mobile UX Layout](https://github.com/cfconor/rpg-book-repository/blob/main/static/img/mobile%20wireframe.png)

Based on the assessment criteria, making the website responsive on different devices was not the top priority, however with the help of Materialize CSS
front-end framework a lot of the responsive functionality is built in, helping streamline that process and allowing me to focus on the back-end and database. 
The initial design for the mobile version of the app can be seen in the above wireframe.

***
##### Finalized Layout
![Image of completed Website Desktop Main Page](https://github.com/cfconor/rpg-book-repository/blob/main/static/img/desktop_final.PNG?raw=true)

The final user interface has a lot in common with the initial concept, a simple, consistent navbar across all pages, giving quick access to all features of the site 
a user might need, without navigating over several pages.

***

![Image of completed Website Mobile Main Page](https://github.com/cfconor/rpg-book-repository/blob/main/static/img/mobile_final.PNG?raw=true)

The mobile version also keeps the same priorities as the desktop version; simple, minimal design, with content being easy to get access to without too much looking
around and clicking on buttons and links.

#### User Stories

##### First Time Visitor
* I want to be able to find books, articles, maps and other resources that might be interesting to me.
* I want to search by keywords, or by entering the name of my favourite author, or game system (e.g. Dungeons and Dragons, Pathfinder, Star Wars, etc...)
* I want to filter only by certain types of content, like maps or tokens.
* I would like to use the website from my phone or tablet, rather than the desktop
* I have an article I have created for online purchase and would like to promote visibility on it.

###### Returning Visitor
* I would like to add my own articles, from my online store, to the site.
* I cannot find the category (book, map, token, etc.) I am looking for, and would like to add it.
* I cannot find the game system(Dungones and Dragons, Pathfinder, Star Wars, etc.) I am looking for, and would like to add it.
* I found some mistakes in created articles, categories or game systems, and would like to update them to fix the mistakes
* I would like to remove an article from the site, as its not longer being sold in its own online store.


## Features

### Existing Features

* Article Catalog
    * Each article created is viewable on the websites homepage, with a description of the author, the category and 
    which game system the article is intended for.
* Editable articles
    * Once registered and logged in, users can edit the existing articles, or delete them.
* Search function
    * The articles are indexed in such a way that a user can quickly search by article name keywords, or even by
    categories, or even game systems, providing powerful content filtering functionality.
* Editable categories
    * Once registered and logged in, users can add new categories, edit the existing categories, or delete them.
* Editable game systems
    * Once registered and logged in, users can add new game systems, edit the existing game systems, or delete them.
* user authentication
    * Users can register, log in or log out, and only users who have created accounts and are logged in can 
    add, edit or delete content.

### Features to Implement

* User Profile pages
    * Users will have their own profile pages, showing the articles they have created.
* Images on Article Cards
    * Users can provide images for their articles, which will add colour and variety to each entry in the catalog
* Admin privileges 
    * Divide users into regular users with restricted ability to edit and remove content, and admins with full permissions to add, edit or remove
    articles, categories, game_systems and users
* Tags on articles
    * Would allow additional granularity on filtering for certain topics and themes.

## Technologies Used

### Languages and Markups Used
* HTML (keeping with HTML5 best practices)
* CSS3
* Javascript
* Python
* Jinja (used to inject Python code snippets into the html pages)

### Data Management
* MongoDB used to create a non-relational database which could be accessed by users
via the user interface

### Frameworks and Libraries Added
* Python Flask framework to create the website tree, manage user input
and perform server-side logic, interacting between the user and the server
* Materialize frontend framework to implement friendly and responsive UX,
as well as add features such as drop down menus and clean page formatting
* JQuery used as part of Materialize implementation to allow for drop down menu functionality

### Python Modules
* click
* dnspython
* Flask
* Flask-PyMongo
* itsdangerous
* mysql
* mysqlclient
* pymongo
* PyMySQL
* Werkzeug

### Hosting
* Heroku

## Data Management

This was the first milestone project in the Full Stack Software Development course that focuses on creating and interacting with a database. 
As a starting point, a Data Model Diagram was done up, which showed required information as well as some nice-to-haves. Each entry in all collections 
(the MongoDB equivalent to a relational databases table) would have its own unique _id value, but variables such as article_category, game_system and created_by
would be important to link the collections together.

![Image of the database design strategy used in this project](https://github.com/cfconor/rpg-book-repository/blob/main/static/img/database%20design.png?raw=true)

In my submitted design, I have linked the collections via the category_name and system_name attributes, which in hindsight is not good design. Better would be to link
these foreign keys using their ObjectId, which is immutable, rather than a name string, which would break the link as soon as the name strings are changed.
Unfortunately I do not have time to overhaul this change in the time allowed for the project.

## Testing

The HTML and CSS were validated using W3C validators, the only error that was found during this testing was for CSS elements imported from the Materialize CSS Framework,
and as I do not see any actual issues arising from that reported error, I am satisfied that the HTML and CSS is up to acceptable validation standard.

### Testing User Stories

* First Time Visitor
    * I want to be able to find books, articles, maps and other resources that might be interesting to me.
        * The homepage shows the catalog of articles straight away, without need for scrolling or clicking anywhere, the content is shown as soon 
        as the homepage is loaded up, which is the route that most users will take to navigate to the site.
        * All entries are searchable by name, category or game system, so finding relevant documents is made as effortless as possible.
    * I want to search by keywords, or by entering the name of my favourite author, or game system (e.g. Dungeons and Dragons, Pathfinder, Star Wars, etc...)
        * There is a search function on the homepage that allows users to filter the catalog using search terms.
        * All entries are searchable by name, category or game system, so finding relevant documents is made as effortless as possible.
    * I want to filter only by certain types of content, like maps or tokens.
        * The search function on the homepage supports searching by attributes other than article name, like searching for a certain category,
        or game system. This allows users to search for only tokens, maps, books, etc.
    * I would like to use the website from my phone or tablet, rather than the desktop
        * Using Materialize CSS and some added styling, the site is responsive with full functionality at all resolutions.
    * I have an article I have created for online purchase and would like to promote visibility on it.
        * If a user registers and logs onto the website, they can add articles, categories and game systems,
        Allowing them to add their article to the catalog for others to view.

* Returning Visitor
    * I would like to add my own articles, from my online store, to the site.
        * If a user registers and logs onto the website, they can add articles, categories and game systems,
        Allowing them to add their article to the catalog for others to view.
    * I cannot find the category (book, map, token, etc.) I am looking for, and would like to add it.
        * If a user registers and logs onto the website, they can add articles, categories and game systems,
        Allowing them to add their article to the catalog for others to view.
    * I cannot find the game system(Dungones and Dragons, Pathfinder, Star Wars, etc.) I am looking for, and would like to add it.
        * If a user registers and logs onto the website, they can add articles, categories and game systems,
        Allowing them to add their article to the catalog for others to view.
    * I found some mistakes in created articles, categories or game systems, and would like to update them to fix the mistakes
        * Once a user has registered and logged in, they also have the ability to edit categories, articles and game systems, to 
        update any information on them, or fix mistakes.
    * I would like to remove an article from the site, as its not longer being sold in its own online store.
        * Once a user has registered and logged in, they also have the ability to delete categories, articles and game systems, to 
        remove any dead links or discontinued products.

### Further Testing
* The site was tested on Chrome, Safari and Firefox, and on various mobile devices, and the functionality was not affected.
* The responsiveness carried well on mobile devices, with a dropdown navbar replacing the horizontal navbar to allow full menu functions
on smaller screens

## Deployment

### Heroku
The project was deployed to Heroku using the following steps. You should already have a Github account, and have forked the *rpg-book-repository* to your own Github account.
Information on how to do this can be found on the Github Docs [here](https://docs.github.com/en/github/getting-started-with-github/quickstart).

1. Login to Heroku.
2. Choose **Create a new app**
3. Enter an app name and Choose a region (EU is faster if based in an EU country)
![Image showing an example of how to fill in the Create App Form in Heroku](https://github.com/cfconor/rpg-book-repository/blob/main/static/img/create_app_heroku.PNG?raw=true)
4. Once the new app loads up, navigate to *Deploy* > *Deployment method*
5. Select the **Github/Connect to Github** button
6. This should display the **Connect to Github** section below
7. Select the purple **Connect to Github** button at the bottom of the section
8. A popup will appear. enter your Github credentials, and authorize Heroku to connect
to your Github repositories
9. The **Connect to Github** Section of the previous page should now change to a similar layout to the screenshot below
![Image showing an example of a Github account linked to Heroku](https://github.com/cfconor/rpg-book-repository/blob/main/static/img/search_repo_heroku.PNG?raw=true)
10. Beside your username, you should see a search field. enter in the search term, *rpg-book-repository* (or whatever you called the project, if renamed)
11. The project will show in a results field below. Click on the **connect** button beside the correct search result.
12. The project is ready to be deployed, but first we need to set the environment variables.
13. At the horizontal menu under the Heroku project name, near the top of the page, navigate to the **Settings** tab.
14. Scroll down until you find the **Config Vars** field. 
15. You will need to create config vars for  IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME. These must correspond to the connection details
for the MongoDB databse, which have not been supplied in this Readme for security and privacy reasons.
16. Once these are added, navigate back to the **Deploy** tab on the horizontal menu at the top of the page.
17. Scroll down to the bottom, and hit **Deploy Branch**. 

If the config vars have been added, the Procfile and requirements.txt file will be read, and when the Flask app deploys, it will connect to the 
MongoDB database using the config details you have provided.

### Local Deploy
The project is built mostly using Python, so having Python installed on your system is vital. 
Information on installing and setting up Python for use on Windows, Linux or Mac can be found [on their website](https://www.python.org).


1. Navigate to the [rpg-book-repository github page](https://github.com/cfconor/rpg-book-repository) page.
2. Select the **Code** button, then **Download Zip**.
3. Download the zip file of the repository.
4. Extract the zipped file to a folder of your choice.
5. Open the root project file from your IDE.
6. Run the below command in the terminal. it will install all the necessary Python modules to deploy the project locally.
```
pip3 install -r requirements.txt
```
7. To deploy the website locally, type the following command
```
python3 app.py
```

## Credits

### Design
* The layout of the site was loosely inspired by the good people over at [The DMs Guild](https://www.dmsguild.com/).

### Code
* The implementation of Materialize CSS to structure the website layout was largely
due to seeing it's use in the Code Institute mini-project which focused on a data-centric
website

### Acknowledgements 
* My tutor for his advice and support through the project lifecycle
* My Dungeons and Dragons friends for helping to test the site and make suggestions