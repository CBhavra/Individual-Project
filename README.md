# Individual Project 


## Contents

[Introduction](#Introduction)

[Objective](#Objective)

[Proposal](#Proposal)

[Architecture](#Architecture)

[Risk Assessment](#Risk-Assessment)

[Project Tracking](#Project-Tracking)

[Entity Realtionship Diagram](#Entity-Realtionship-Diagram)

[Testing Analysis](#Testing-Analysis)

[Continuous Integration](Continuous-Integration)

[Development](#Development)

[Front-End](#Front-End)

[Unit Tetsing](#Unit-Tetsing)

[Footer](#Footer)

[Future Implementations](#Future-Implementations)

[Author](#Author)

[Acknowledements](#Acknowledgements)


## Introduction

Cricket is an old but well-loved sport. It is played in many different countries and climates and has many forms some long (lasting whole days) and some small (lasting  only a few hours). It, like many other sports is comprised of two teams. One team tries to take ***wickets*** while the other team tries to score ***runs***. 
There are many ***Teams*** (and types of teams), ***players*** and ***statistics*** to record as that is just the nature of the sport. So a cricket fan would enjoy the ability to view, input, update or remove team or player statistics. 


### Ojectives

The core objective of this Project is to produce a CRUD application using the particuolar tools given to us for example:

- Creating the CRUD app with Python 3

- Front-end made using Flask

- Project tracking with Trello 

- Relational database

- Risk assessment

- Tetsing using pytest and automation using Jenkins


### Proposal 

As a fan of cricket I would enjoy an app that could show me all kinds of statistics of my favourite players or teams. So I know other fans would also like it. Fans should be able to view any stats they wish, create new stats for new players, update old stats and remove stats if they are 'fake' or have been put up as a joke.
The follwoing is an epic (a collection of User Stories that are the core requirements of the app.

***Create***
- As a cricket fan I want to be able to create statistics so that I view them at another later date 
- As a cricket fan I want to be able to create statistics so that other users can see them 

***Read***
- As a cricket fan I want to be able to view istics so that I can see the scores and runs of my favourite teams and players 

***Update***
- As a user of the app I wish to be able to change the statistics so that I can correct or update the stats 

***Delete***
- As a user of the app I want to be able to remove any 'fake' or 'joke' statistic inputs

## Architecture 


### Risk Assessment 

My risk assessment can be seen below:

<img src="https://github.com/CBhavra/Individual-Project/blob/main/images/Risk%20Assessment.jpg"/>

Throughout the project multiple risks came to me at different times. This was true for much of the rest of the projects aspects. The full risk assessment file can be found [here](https://github.com/CBhavra/Individual-Project/blob/main/Resources/Risk%20Assessment.xlsx).


### Project Tracking 

My project tracking method was to use Trello, it is useful and free-to-use and provided me with a friendly looking board to keep track of all requirements. It can be seen [here](https://github.com/CBhavra/Individual-Project/blob/main/Resources/Cricket%20App%20Kanban%20_%20Trello.html) or below:
<img src="https://github.com/CBhavra/Individual-Project/blob/main/images/Trello.jpg"/>


### Entity Relationship Diagram 

Version 1 and 2 of my ERD can be seen [here](https://github.com/CBhavra/Individual-Project/blob/main/Resources/ERD%20v1.drawio) or below:

<img src="https://github.com/CBhavra/Individual-Project/blob/main/images/ERD%20v1.jpg"/>

It is basic and then evolves from a basic one-to-many relational database to two one-to-many relationships. It works as one team can have many players and in the same way one player can have many statistics. 

My final revision can be seen [here](https://github.com/CBhavra/Individual-Project/blob/main/Resources/ERD%20v1.drawio) or below:

<img src="https://github.com/CBhavra/Individual-Project/blob/main/images/ERD%20v2.jpg"/>

As can be seen not much has changed from the original. I wanted to make one change, removing the format of the team table for the name of team. Whhich clearly makes more sense as the name of the team is fairly important. 


### Testing Analysis 

The project will only contain unit testing and automated testing in Jenkins. It's possible to use much better forms of testing however, as per the specification I was to use only what we had been given with reagrds to tools. Other forms of testing can involve non-functional testing and maintenance testing which could help to increase the viabiity of the app.


### Continuous Integration 

<img src="https://github.com/CBhavra/Individual-Project/blob/main/images/CI%20PIpeline.jpg"/>

The above is a visual representation of my CI pipeline, it shows all the toos used in the project and what happens at each stage until completeion.

The Jenkins script I used can be characterized in the following way:

- Installation of dependencies

`sudo apt-get install python3 python3-pip python3-venv`

- Installation of pip requirements 

`python3 -m venv venv 
source venv/bin/actiavte
pip3 install -r requirements.txt`

- Run the tests

`python3 -m pytest --cov=application`


## Development 

Development of this Cricket application can be broken down into two sections. Section one being the Front-End of the application, this corresponds to what the end-user will see. 


### Front-End 

The front-end of this Cricket application is in an extremely rudimentary stage and therefore has a very basic view and functionality. The app has been created following the CRUD format as follows:

<img src="https://github.com/CBhavra/Individual-Project/blob/main/images/Front-End%20Read.jpg"/>

The image above shows the read functionality working perfectly. As can be seen whilst following the `/home` URL a database of the current team(s) comes up. In it there are 3 attributes name, country and league of a team. 

<img src="https://github.com/CBhavra/Individual-Project/blob/main/images/Front-End%20Create.jpg"/>

This image is in regards to the create functionality. It has been implmented correctly as if your replace `/home` with `/create` you are given the ability to add a team set. 

<img src="https://github.com/CBhavra/Individual-Project/blob/main/images/Front-End%20Update%20.jpg"/>

The update functionality can be a littel trickier. This is because you are no longer adding a new id or viewing one. Instead you are trying to change an existing one so there is a requirement of knowing what you wish to change before doing so (i.e. you must know the id of which entry you wish to update). Entering `/update/<id>` (where id is known beforehand) in place of `/home` attains this.

The delete function is also avaiable. However, it is impossble to show. As soon as the function is input correctly the entry in the table disappears. Like the update function the id is required so placing `/delete/<id>` in the URL allows you to delete an entry.


### Unit Testing 

Unit testing is very basic but paramount to understanding the written codes' success or failure. the way `pytest` works is by taking your desired ouput and asserting through your code to see if the outcome has been met. These tests have been automated in Jenkins. It then provides a report of what passed or failed and what the coverage of code is. In this case the higher the better. 
When using VS Code 81% coverage was attained. Shown below:

<img src="https://github.com/CBhavra/Individual-Project/blob/main/images/VS%20Code%20Unit%20Test.jpg"/>

The same is true from running through Jenkins:

<img src="https://github.com/CBhavra/Individual-Project/blob/main/images/Jenkins%20test.jpg"/>

As seen above the coverage stayed the same and was still displayed regardless of the fact that the Jenkins build failed. 


## Footer 


### Future Implementations

I have many possible implementations that I could input:

- To begin with I would have like to have completed the stats table 

- I would definitely improve upon the Front-End of the application 

- I would have liked to have added buttons for ease of navigation 

- Addition of some form of integration testing such as selenium etc.


### Author 

Chasminder Bhavra


### Acknowledgements 

I would like to acknowledge and profusely thank the following for their aid and advice in this project:

- God
- Marius Saunders 

- Ryan Wright 

- Victoria Sacre 

- Oliver Nichols 







          
          















