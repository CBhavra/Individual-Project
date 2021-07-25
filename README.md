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

[Continuous ntegration](Continuous-Integration)

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

          
          















