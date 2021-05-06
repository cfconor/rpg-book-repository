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

### Shelved Features

* User Profile pages
    * Users will have their own profile pages, showing the articles they have created.
* Images on Article Cards
    * Users can provide images for their articles, which will add colour and variety to each entry in the catalog
* Admin privileges 
    * Divide users into regular users with restricted ability to edit and remove content, and admins with full permissions to add, edit or remove
    articles, categories, game_systems and users

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

![Image of the database design strategy used in this project](https://github.com/cfconor/rpg-book-repository/blob/main/static/img/mobile_final.PNG?raw=true)


## Testing

## Deployment

## Credits

### Code
* The implementation of Materialize CSS to structure the website layout was largely
due to seeing it's use in the Code Institute mini-project which focused on a data-centric
website

### Acknowledgements 
* My tutor for his advice and support through the project lifecycle