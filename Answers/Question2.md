<p style="text-align: center;">Made with markdown, please use MD viewer for best experience</p

---

### QUESTION2 :

>As a data science function we have scripts that ingest similar data to be used by our models. Implement a script(s) in a language of your choice to ingest the raw data and produce the tables in your data model. If you had more time, what adjustments or additions would you make to your ingestion script? 


###### Ans: Based on the data model and schema I designed earlier, I created a script in Python to parse JSON and ingest data in SQLite3 database, Tables created-- 
    
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

###### The main code is writtin in ingestion.py and two helper modules `db_ddl` and `db_dml` were created to manage and modularize the code. To run, execute below given commands in `Scripts` folder- 

```
pip install -r requirements.txt
python ingestion.py
```


###### SQLite3 was chosen, as its a lightweight, easy-to-setup database. 

###### The solution is not perfect and lacks many things that I would have attempted with more time in hand, some of these things that are on top of my mind were - 

1. More quality checks in ingestion scripts
2. column level checks and constraints 
3. DataType selection based on column information e.g. different lengths of varchars
2. Converting binary flags from text to 1/0 
3. Ensuring reduction in data size by only keeping relevant ids and removing actual data 
4. Code best practices: Exception Handling, logging and maintaining ingestion Feed key
