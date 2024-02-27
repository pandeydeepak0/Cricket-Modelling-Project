import sqlite3

# Drop Tables
def drop_tables(conn):

    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Venue")
    c.execute("DROP TABLE IF EXISTS Team")
    c.execute("DROP TABLE IF EXISTS Squad")
    c.execute("DROP TABLE IF EXISTS Player")
    c.execute("DROP TABLE IF EXISTS Fixtures")
    c.execute("DROP TABLE IF EXISTS MatchInfo")
    c.execute("DROP TABLE IF EXISTS MatchDetails")
    c.execute("DROP TABLE IF EXISTS InningsDetails")
    c.execute("DROP TABLE IF EXISTS BattingScorecard")
    c.execute("DROP TABLE IF EXISTS BowlingScorecard")
    c.execute("DROP TABLE IF EXISTS PartnershipCard")
    c.execute("DROP TABLE IF EXISTS BallByBall")


# Create tables
def create_tables(conn):
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS Venue (
                   venue_id INTEGER [PRIMARY KEY]
                   ,city TEXT  
                   ,name TEXT
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Team (
                   team_id INTEGER [PRIMARY KEY]
                    ,Format TEXT
                    ,Prefix TEXT
                    ,TeamImage TEXT
                    ,teamname TEXT
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Squad (
                MatchID INTEGER [PRIMARY KEY],
                Clubid INTEGER [PRIMARY KEY],
                PlayerID INTEGER [PRIMARY KEY],
                BattingOrder INTEGER,
                isCaptain TEXT,
                isPlayed INTEGER,
                isWK TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Player (
                 player_id INTEGER [PRIMARY KEY]
                ,team_id INTEGER
                ,Battingtype TEXT
                ,bowlingtype TEXT
                ,DOB TEXT
                ,Nationality TEXT
                ,playername TEXT
                ,refPlayerID INTEGER
                ,team_name TEXT
                ,WK INTEGER
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Fixtures(
                 fixture_id INTEGER [PRIMARY KEY]
                ,matchid INTEGER
                ,date TEXT
                ,matchno INTEGER
                ,Matchtypeid INTEGER
                ,stage TEXT
                ,teama TEXT
                ,teama_id INTEGER
                ,teamb TEXT
                ,teamb_id INTEGER
                ,time_ist TEXT
                ,venue TEXT
                ,venue_id INTEGER
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS MatchInfo(
                 matchid INTEGER [PRIMARY KEY]
                ,fixture_id INTEGER
                ,venue_id INTEGER
                ,Firstinn_RevisedOvers INTEGER
                ,FirstInngBatClubId INTEGER
                ,Secondinn_RevisedOvers INTEGER
                ,ClubA INTEGER
                ,ClubB INTEGER
                ,DayOrnight TEXT
                ,KnockOut INTEGER
                ,ManOftheMatch INTEGER
                ,MatchDate TEXT
                ,MatchTypeID INTEGER
                ,Result TEXT
                ,RevisedTarget INTEGER
                ,Stage INTEGER
                ,Status TEXT
                ,TossOpted TEXT
                ,TossWin INTEGER
                ,WonClubid INTEGER
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS MatchDetails(
                MatchID INTEGER
                ,BatTeamName TEXT
                ,BatTeamOvers TEXT
                ,BatTeamRuns TEXT
                ,BatTeamWkts TEXT
                ,BwlTeamName TEXT
                ,CurrentInningsNo TEXT
                ,CurrentRunRate TEXT
                ,MatchStatus TEXT
                ,MaxOvers TEXT
                ,Partnership TEXT
                ,PrevOvers TEXT
                ,RecentOvers TEXT
                ,RemainingBalls TEXT
                ,RemainingOvers TEXT
                ,RequiredRunRate TEXT
                ,RequiredRuns TEXT
                ,State TEXT
                ,Status TEXT
                ,Target TEXT
                ,TeamAReview TEXT
                ,TeamBReview TEXT
                ,Extra TEXT
                ,Bowler1Name TEXT
                ,Bowler1Econ TEXT
                ,Bowler1Maidens TEXT
                ,Bowler1Overs TEXT
                ,Bowler1Runs TEXT
                ,Bowler1Wickets TEXT
                ,Bowler2Name TEXT
                ,Bowler2Econ TEXT
                ,Bowler2Maidens TEXT
                ,Bowler2Overs TEXT
                ,Bowler2Runs TEXT
                ,Bowler2Wickets TEXT
                ,Batsman1Name TEXT
                ,Batsman1Balls TEXT
                ,Batsman1Fours TEXT
                ,Batsman1Score TEXT
                ,Batsman1Sixes TEXT
                ,Batsman1StrikeRate TEXT
                ,Batsman2Name TEXT
                ,Batsman2Balls TEXT
                ,Batsman2Fours TEXT
                ,Batsman2Score TEXT
                ,Batsman2Sixes TEXT
                ,Batsman2StrikeRate TEXT
                ,LastWicketBatsman TEXT
                ,LastWicketBattingOrder TEXT
                ,LastWicketDismissal TEXT
                ,LastWicketFallOfWicket TEXT
                ,LastWicketRunsBalls TEXT
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS InningsDetails(
                MatchID INTEGER [PRIMARY KEY]
                ,InningsNo INTEGER [PRIMARY KEY]
                ,BatTeam TEXT
                ,BowlTeam TEXT
                ,Declared TEXT
                ,FallofWicketStr TEXT
                ,FollowOn TEXT
                ,TotalOvers TEXT
                ,TotalRuns TEXT
                ,TotalWickets TEXT
                ,Extras text 
                )''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS BattingScorecard (
            matchID INTEGER [PRIMARY KEY],
            inningsno INTEGER [PRIMARY KEY],
            player_id INTEGER [PRIMARY KEY],
            batteam TEXT,
            bowlteam TEXT,
            balls INTEGER,
            _0s INTEGER,
            _1s INTEGER,
            _2s INTEGER,
            _3s INTEGER,
            _4s INTEGER,
            _5s INTEGER,
            _6s INTEGER,
            dismissal TEXT,
            runs INTEGER,
            sr REAL        
            )
        ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS BowlingScorecard(
            matchID INTEGER [PRIMARY KEY]
            ,inningsno INTEGER [PRIMARY KEY]
            ,player_id INTEGER [PRIMARY KEY]
            ,batteam TEXT
            ,bowlteam TEXT
            ,boundary INTEGER
            ,dot REAL
            ,dotball INTEGER
            ,econ REAL
            ,extras INTEGER
            ,maiden INTEGER
            ,nb INTEGER
            ,overs REAL
            ,runs INTEGER
            ,six INTEGER
            ,teamID INTEGER
            ,wd INTEGER
            ,wickets INTEGER
            )''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS PartnershipCard (
            matchID INTEGER  [PRIMARY KEY]
            ,inningsno INTEGER [PRIMARY KEY]
            ,player1_id INTEGER [PRIMARY KEY] 
            ,player2_id INTEGER [PRIMARY KEY] 
            ,player1name TEXt
            ,player2name TEXT
            ,batteam TEXT
            ,bowlteam TEXT
            ,followin TEXT 
            ,balls1 INTEGER 
            ,balls2 INTEGER
            ,runs1 INTEGER
            ,runs2 INTEGER
            ,Runs_Balls_1 TEXT
            ,Runs_Balls_2 TEXT
            ,score TEXT
            ,sr1 REAL
            ,sr2 REAL
            ,totalballs INTEGER
            ,totalruns INTEGER
            ,wkt2 TEXT
            )''')

    c.execute('''CREATE TABLE IF NOT EXISTS BallByBall (
                        MatchID INTEGER [PRIMARY KEY],
                        InningsID INTEGER [PRIMARY KEY],
                        BallID INTEGER [PRIMARY KEY],
                        BallStopType TEXT,
                        BatsmanInControlOutControl TEXT,
                        BatSubject INTEGER,
                        BatSubjectName TEXT,
                        BattingClubID INTEGER,
                        BattingOrder INTEGER,
                        BattingType TEXT,
                        BattingTypeID INTEGER,
                        BowlerID INTEGER,
                        BowlerName TEXT,
                        BowlingClubID INTEGER,
                        BowlingType TEXT,
                        BowlingTypeID INTEGER,
                        BowlSpeed REAL,
                        CatchType TEXT,
                        CatchTypeName TEXT,
                        CreaseMovement TEXT,
                        CreaseMovementID INTEGER,
                        DeliveryStyle TEXT,
                        DeliveryStyleID INTEGER,
                        DirectHit TEXT,
                        DirectHitName TEXT,
                        DismissalFielderID1 INTEGER,
                        DismissalFielderID2 INTEGER,
                        DismissalType TEXT,
                        DismissalTypeID INTEGER,
                        DismissedPlayer TEXT,
                        DismissedPlayerName TEXT,
                        EndID TEXT,
                        Extras INTEGER,
                        ExtrasType INTEGER,
                        ExtrasTypeName TEXT,
                        FieldPosition TEXT,
                        FieldPositionID INTEGER,
                        HeightX INTEGER,
                        HeightY INTEGER,
                        InterceptionPointX INTEGER,
                        InterceptionPointY INTEGER,
                        InTheAir INTEGER,
                        IsDRS INTEGER,
                        IsFour INTEGER,
                        IsSix INTEGER,
                        ISTTime TEXT,
                        IsWicket INTEGER,
                        LengthX INTEGER,
                        LengthY INTEGER,
                        Lofted INTEGER,
                        MisRun INTEGER,
                        MRFielderID INTEGER,
                        MRFielderName TEXT,
                        NonStrikerID INTEGER,
                        NonStrikerName TEXT,
                        OnOrOff TEXT,
                        OverID INTEGER,
                        OverOrRound INTEGER,
                        OverOrRoundName TEXT,
                        Overs REAL,
                        OverThrowRuns INTEGER,
                        PaceOrSpin INTEGER,
                        PaceOrSpinName TEXT,
                        PitchmapZone INTEGER,
                        PowerSurge INTEGER,
                        ReleasePointX INTEGER,
                        ReleasePointY INTEGER,
                        Runs INTEGER,
                        SaveRun INTEGER,
                        ShotConnection INTEGER,
                        ShotConnectionName TEXT,
                        SixDistance REAL,
                        SRFielderName TEXT,
                        SRFielderID INTEGER,
                        StrikerID INTEGER,
                        StrikerName TEXT,
                        Stroke TEXT,
                        StrokeID INTEGER,
                        SubjectTag TEXT,
                        SubjectTagName TEXT,
                        SZZone INTEGER,
                        UmpireName TEXT,
                        UmpireID INTEGER,
                        WagonWheelX INTEGER,
                        WagonWheelY INTEGER,
                        WicketKeeperStandingPosition INTEGER,
                        WTO INTEGER,
                        WTOFielder TEXT,
                        WTOFielderName TEXT,
                        WTOName TEXT,
                        WTOBatsmanName TEXT,
                        WTOPlayer TEXT,
                        WTOType INTEGER,
                        WTOTypeName TEXT,
                        WWZone TEXT,
                        PRIMARY KEY (matchID, InningsID, BallID)
                    )''')