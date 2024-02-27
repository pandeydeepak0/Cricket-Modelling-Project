<p style="text-align: center;">Made with markdown, please use MD viewer for best experience</p

---

### QUESTION1 :

>A big part of this role is to be able to design schema for sports that we model. Design a schema for the data attached - please produce a diagram to showcase your design. You can use any tool to produce this diagram, for example drawio.


###### Ans: To solve this problem, I started exploring the data available. We have total 6 dataset -- 

    Fixtures: details around the games in the series
    Player: details of all the players in the series
    Team: details of the teams involved in the series
    Venue: details of the stadium the series was played at
    Score Card: aggregate information about the match. The file names are the match IDs
    Ball by Ball: detailed information for every delivery in the match. The file names are the match IDs

###### Among these 6 datasets `Ball by Ball` contained Squad and MatchInfo details along with Ball by Ball breakup of the matches. 

###### Similarly the `Score Card` contained multiple difference dictionaries that could be translated into distinct entities with their own specific attributes. 


### Solution Discovery: 

###### To begin with I started creating few entities around this data namely, MatchInfo, Team, Fixture, Players. On closer investigation, I discovered few weak entities as well like Innings, matchdetails, batting and bowling scorecard, partnerships etc. 

###### Basis on this discovery I broke down this data into 12 distinct tables, with the intention to normalize the data and to minimize redundancy in records. Schema details below -  

    Venue: details of the stadium the series was played at
    Team: details of the teams involved in the series
    Squad: details of players invovled in the Match 
    Player: details of all players
    Fixtures: details around the games in the series
    MatchInfo: Information about the mataches played
    MatchDetails: additional information about the match
    InningsDetails: details about the innings in a match
    BattingScorecard: Batting Details of both innings in the match
    BowlingScorecard: Bowling details of both innings in the match
    PartnershipCard: Partnership detatils of both innings 
    BallbyBall: Ball by Ball breakup of entire match



###### The schema is designed keeping in mind efficient retrival and insertion of data. I have also setup primary key(s) in each table to maintain row level consistency.

### Solution: 


###### Post solution discovery i used `dbdiagram.io` to create the data model and ERD. The code used for the same is present in `schema.dbml` file. [To generate in realtime, please paste code in the Web editor] The ER diagram png is added in the folder.

> I have made the assumption here that the data will be used for both operational and analytical pruposes. Hence I have created an ERD diagram for the solution, which fits best in this usecase. The data can be further downstreamed to OLAP systems and we can further setup warehousing and dimensional models to prepare the data for analytical, reporting and ML usecases. 