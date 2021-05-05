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
![Wireframe Image of Initial Desktop UX Layout](https://github.com/cfconor/rpg-book-repository/blob/main/static/img/desktop%20wireframe.png)
As seen by the mockups, the design strategy for this website prioritised delivering relevant information to the user quickly, without much navigating around
the site or having to do several clicks. The information is presented as soon as the homepage is shown, and for most users this may be the only thing they 
need to use the website for, so having this shown first makes sense.

![Wireframe Image of Initial Mobile UX Layout](https://github.com/cfconor/rpg-book-repository/blob/main/static/img/mobile%20wireframe.png)
Based on the assessment criteria, making the website responsive on different devices was not the top priority, however with the help of Materialize CSS
front-end framework a lot of the responsive functionality is built in, helping streamline that process and allowing me to focus on the back-end and database. 
The initial design for the mobile version of the app can be seen in the above wireframe.

#### Layout


#### User Stories




## Features

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


## Testing

## Deployment

## Credits

### Code
* The implementation of Materialize CSS to structure the website layout was largely
due to seeing it's use in the Code Institute mini-project which focused on a data-centric
website

### Acknowledgements 
* My tutor for his advice and support through the project lifecycle