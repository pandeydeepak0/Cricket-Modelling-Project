import json
import sqlite3
import os 

# Load data from JSON files
def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Create SQLite connection and cursor
conn = sqlite3.connect('cricket_data.db')
c = conn.cursor()

# Drop Tables
def drop_tables():

    c.execute("DROP TABLE IF EXISTS Fixture")
    c.execute("DROP TABLE IF EXISTS Team")
    c.execute("DROP TABLE IF EXISTS Venue")
    c.execute("DROP TABLE IF EXISTS BattingCard")
    c.execute("DROP TABLE IF EXISTS BowlingCard")
    c.execute("DROP TABLE IF EXISTS PartnershipCard")
    c.execute("DROP TABLE IF EXISTS InningsDetails")
    c.execute("DROP TABLE IF EXISTS MatchDetails")
    c.execute("DROP TABLE IF EXISTS Player")
    c.execute("DROP TABLE IF EXISTS BallByBall")


# Create tables
def create_tables():
    c.execute('''CREATE TABLE IF NOT EXISTS Fixture (
                 date TEXT,
                 matchid INTEGER PRIMARY KEY,
                 matchno INTEGER,
                 Matchtypeid INTEGER,
                 stage TEXT,
                 teama TEXT,
                 teama_id INTEGER,
                 teamb TEXT,
                 teamb_id INTEGER,
                 time_ist TEXT,
                 venue TEXT,
                 venue_id INTEGER
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Venue (
                 city TEXT,
                 name TEXT,
                 venue_id INTEGER PRIMARY KEY
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Team (
                 Format TEXT,
                 Prefix TEXT,
                 team_id INTEGER PRIMARY KEY,
                 TeamImage TEXT,
                 teamname TEXT
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Player (
                 Battingtype TEXT,
                 bowlingtype TEXT,
                 DOB TEXT,
                 Nationality TEXT,
                 player_id INTEGER PRIMARY KEY,
                 playername TEXT,
                 refPlayerID INTEGER,
                 team_id INTEGER,
                 team_name TEXT,
                 WK INTEGER
                 )''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS BattingCard (
            matchID TEXT,
            batteam TEXT,
            bowlteam TEXT,
            declared TEXT,
            fallofwicketsstr TEXT,
            followin TEXT,
            inningsno INTEGER,
            player TEXT,
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
            sr REAL,
            PRIMARY KEY (matchID, inningsno, player)
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS BowlingCard(
            matchID TEXT,
            batteam TEXT,
            bowlteam TEXT,
            followin TEXT,
            inningsno INTEGER,
            boundary INTEGER,
            dot REAL,
            dotball INTEGER,
            econ REAL,
            extras INTEGER,
            id INTEGER,
            maiden INTEGER,
            nb INTEGER,
            overs REAL,
            player TEXT,
            runs INTEGER,
            six INTEGER,
            teamID INTEGER,
            wd INTEGER,
            wickets INTEGER,
            wn TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS PartnershipCard (
            matchID TEXT,
            batteam TEXT,
            bowlteam TEXT,
            followin TEXT,
            inningsno INTEGER,
            balls1 INTEGER,
            balls2 INTEGER,
            player1name TEXT,
            player2name TEXT,
            runs1 INTEGER,
            runs2 INTEGER,
            Runs_Balls_1 ,
            Runs_Balls_2 ,
            score ,
            sr1 REAL,
            sr2 REAL,
            totalballs ,
            totalruns ,
            wkt2 TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS InningsDetails (
            MatchID TEXT,
            BatTeam TEXT,
            BowlTeam TEXT,
            Declared TEXT,
            FallofWicketStr TEXT,
            FollowOn TEXT,
            InningsNo TEXT,
            TotalOvers TEXT,
            TotalRuns TEXT,
            TotalWickets TEXT,
            Extras TEXT,
            PRIMARY KEY (MatchID, InningsNo)             
        )
    ''')

    c.execute('''CREATE TABLE IF NOT EXISTS MatchDetails (
                        MatchID TEXT PRIMARY KEY,
                        BatTeamName TEXT,
                        BatTeamOvers TEXT,
                        BatTeamRuns TEXT,
                        BatTeamWkts TEXT,
                        BwlTeamName TEXT,
                        CurrentInningsNo TEXT,
                        CurrentRunRate TEXT,
                        MatchStatus TEXT,
                        MaxOvers TEXT,
                        Partnership TEXT,
                        PrevOvers TEXT,
                        RecentOvers TEXT,
                        RemainingBalls TEXT,
                        RemainingOvers TEXT,
                        RequiredRunRate TEXT,
                        RequiredRuns TEXT,
                        State TEXT,
                        Status TEXT,
                        Target TEXT,
                        TeamAReview TEXT,
                        TeamBReview TEXT,
                        Extra TEXT,
                        Bowler1Name TEXT,
                        Bowler1Econ TEXT,
                        Bowler1Maidens TEXT,
                        Bowler1Overs TEXT,
                        Bowler1Runs TEXT,
                        Bowler1Wickets TEXT,
                        Bowler2Name TEXT,
                        Bowler2Econ TEXT,
                        Bowler2Maidens TEXT,
                        Bowler2Overs TEXT,
                        Bowler2Runs TEXT,
                        Bowler2Wickets TEXT,
                        Batsman1Name TEXT,
                        Batsman1Balls TEXT,
                        Batsman1Fours TEXT,
                        Batsman1Score TEXT,
                        Batsman1Sixes TEXT,
                        Batsman1StrikeRate TEXT,
                        Batsman2Name TEXT,
                        Batsman2Balls TEXT,
                        Batsman2Fours TEXT,
                        Batsman2Score TEXT,
                        Batsman2Sixes TEXT,
                        Batsman2StrikeRate TEXT,
                        LastWicketBatsman TEXT,
                        LastWicketBattingOrder TEXT,
                        LastWicketDismissal TEXT,
                        LastWicketFallOfWicket TEXT,
                        LastWicketRunsBalls TEXT
                    )''')

    # c.execute('''CREATE TABLE IF NOT EXISTS BallByBall (
    #                     BallID INTEGER PRIMARY KEY,
    #                     BallStopType TEXT,
    #                     BatsmanInControlOutControl TEXT,
    #                     BatSubject INTEGER,
    #                     BatSubjectName TEXT,
    #                     BattingClubID INTEGER,
    #                     BattingOrder INTEGER,
    #                     BattingType TEXT,
    #                     BattingTypeID INTEGER,
    #                     BowlerID INTEGER,
    #                     BowlerName TEXT,
    #                     BowlingClubID INTEGER,
    #                     BowlingType TEXT,
    #                     BowlingTypeID INTEGER,
    #                     BowlSpeed REAL,
    #                     CatchType TEXT,
    #                     CatchTypeName TEXT,
    #                     CreaseMovement TEXT,
    #                     CreaseMovementID INTEGER,
    #                     DeliveryStyle TEXT,
    #                     DeliveryStyleID INTEGER,
    #                     DirectHit TEXT,
    #                     DirectHitName TEXT,
    #                     DismissalFielderID1 INTEGER,
    #                     DismissalFielderID2 INTEGER,
    #                     DismissalType TEXT,
    #                     DismissalTypeID INTEGER,
    #                     DismissedPlayer TEXT,
    #                     DismissedPlayerName TEXT,
    #                     EndID TEXT,
    #                     Extras INTEGER,
    #                     ExtrasType INTEGER,
    #                     ExtrasTypeName TEXT,
    #                     FieldPosition TEXT,
    #                     FieldPositionID INTEGER,
    #                     HeightX INTEGER,
    #                     HeightY INTEGER,
    #                     InningsID INTEGER,
    #                     InterceptionPointX INTEGER,
    #                     InterceptionPointY INTEGER,
    #                     InTheAir INTEGER,
    #                     IsDRS INTEGER,
    #                     IsFour INTEGER,
    #                     IsSix INTEGER,
    #                     ISTTime TEXT,
    #                     IsWicket INTEGER,
    #                     LengthX INTEGER,
    #                     LengthY INTEGER,
    #                     Lofted INTEGER,
    #                     MatchID INTEGER,
    #                     MisRun INTEGER,
    #                     MRFielderID INTEGER,
    #                     MRFielderName TEXT,
    #                     NonStrikerID INTEGER,
    #                     NonStrikerName TEXT,
    #                     OnOrOff TEXT,
    #                     OverID INTEGER,
    #                     OverOrRound INTEGER,
    #                     OverOrRoundName TEXT,
    #                     Overs REAL,
    #                     OverThrowRuns INTEGER,
    #                     PaceOrSpin INTEGER,
    #                     PaceOrSpinName TEXT,
    #                     PitchmapZone INTEGER,
    #                     PowerSurge INTEGER,
    #                     ReleasePointX INTEGER,
    #                     ReleasePointY INTEGER,
    #                     Runs INTEGER,
    #                     SaveRun INTEGER,
    #                     ShotConnection INTEGER,
    #                     ShotConnectionName TEXT,
    #                     SixDistance REAL,
    #                     SRFielderName TEXT,
    #                     SRFielderID INTEGER,
    #                     StrikerID INTEGER,
    #                     StrikerName TEXT,
    #                     Stroke TEXT,
    #                     StrokeID INTEGER,
    #                     SubjectTag TEXT,
    #                     SubjectTagName TEXT,
    #                     SZZone INTEGER,
    #                     UmpireName TEXT,
    #                     UmpireID INTEGER,
    #                     WagonWheelX INTEGER,
    #                     WagonWheelY INTEGER,
    #                     WicketKeeperStandingPosition INTEGER,
    #                     WTO INTEGER,
    #                     WTOFielder TEXT,
    #                     WTOFielderName TEXT,
    #                     WTOName TEXT,
    #                     WTOBatsmanName TEXT,
    #                     WTOPlayer TEXT,
    #                     WTOType INTEGER,
    #                     WTOTypeName TEXT,
    #                     WWZone TEXT
    #                 )''')

# Function to parse JSON and insert data into BallByBall table
# def insert_BallByBall_data(conn, ballbyball_data):
#     cursor = conn.cursor()

#     ltball = ballbyball_data['ltball']

#     for ball in ltball:
#         cursor.execute('''INSERT INTO BallByBall (
#                             BallID, BallStopType, BatsmanInControlOutControl, BatSubject,
#                             BatSubjectName, BattingClubID, BattingOrder, BattingType, BattingTypeID,
#                             BowlerID, BowlerName, BowlingClubID, BowlingType, BowlingTypeID,
#                             BowlSpeed, CatchType, CatchTypeName, CreaseMovement, CreaseMovementID,
#                             DeliveryStyle, DeliveryStyleID, DirectHit, DirectHitName, DismissalFielderID1,
#                             DismissalFielderID2, DismissalType, DismissalTypeID, DismissedPlayer,
#                             DismissedPlayerName, EndID, Extras, ExtrasType, ExtrasTypeName, FieldPosition,
#                             FieldPositionID, HeightX, HeightY, InningsID, InterceptionPointX, InterceptionPointY,
#                             InTheAir, IsDRS, IsFour, IsSix, ISTTime, IsWicket, LengthX, LengthY, Lofted,
#                             MatchID, MisRun, MRFielderID, MRFielderName, NonStrikerID, NonStrikerName,
#                             OnOrOff, OverID, OverOrRound, OverOrRoundName, Overs, OverThrowRuns,
#                             PaceOrSpin, PaceOrSpinName, PitchmapZone, PowerSurge, ReleasePointX,
#                             ReleasePointY, Runs, SaveRun, ShotConnection, ShotConnectionName, SixDistance,
#                             SRFielderName, SRFielderID, StrikerID, StrikerName, Stroke, StrokeID,
#                             SubjectTag, SubjectTagName, SZZone, UmpireName, UmpireID, WagonWheelX,
#                             WagonWheelY, WicketKeeperStandingPosition, WTO, WTOFielder, WTOFielderName,
#                             WTOName, WTOBatsmanName, WTOPlayer, WTOType, WTOTypeName, WWZone
#                         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                        (ball['BallID'], ball['BallStopType'], ball['Batsman InControl/OutControl'], ball['BatSubject'],
#                         ball['BatSubjectName'], ball['BattingClubID'], ball['battingorder'], ball['BattingType'], ball['BattingTypeID'],
#                         ball['bowlerid'], ball['bowlerName'], ball['BowlingClubID'], ball['BowlingType'], ball['BowlingTypeID'],
#                         ball['bowlSpeed'], ball['CatchType'], ball['CatchType_Name'], ball['Creasemovement'], ball['CreaseMovementId'],
#                         ball['DeliveryStyle'], ball['DeliveryStyleID'], ball['Directhit'], ball['Directhit_name'], ball['DismissalFielderID1'],
#                         ball['DismissalFielderID2'], ball['dismissaltype'], ball['DismissalTypeId'], ball['Dismissedplayer'],
#                         ball['Dismissedplayer_name'], ball['EndID'], ball['Extras'], ball['extrastype'], ball['ExtrasTypeName'], ball['fieldPosition'],
#                         ball['fieldPositionid'], ball['HeightX'], ball['HeightY'], ball['InningsID'], ball['InterceptionPoint_X'], ball['InterceptionPoint_Y'],
#                         ball['InTheair'], ball['isDRS'], ball['isfour'], ball['issix'], ball['IST TIME'], ball['IsWicket'], ball['LengthX'], ball['LengthY'], ball['Lofted'],
#                         ball['MatchID'], ball['MisRun'], ball['MR_Fielderid'], ball['MR_FielderName'], ball['nonstrikerid'], ball['NonStrikerName'],
#                         ball['OnorOff'], ball['overid'], ball['OverorRound'], ball['OverorRound_Name'], ball['overs'], ball['OverThrowRuns'],
#                         ball['PaceorSpin'], ball['PaceorSpin_name'], ball['Pitchmap Zone'], ball['PowerSurge'], ball['ReleasePoint_X'],
#                         ball['ReleasePoint_Y'], ball['Runs'], ball['saverun'], ball['ShotConnection'], ball['ShotConnectionName'], ball['SixDistance'],
#                         ball['SR_Fielder_Name'], ball['SR_Fielderid'], ball['StrikerID'], ball['StrikerName'], ball['Stroke'], ball['StrokeID'],
#                         ball['subjecttag'], ball['SubjectTagName'], ball['SZ Zone'], ball['umpire_name'], ball['umpireid'], ball['WagonWheelX'],
#                         ball['WagonWheelY'], ball['WicketKeeper Standing position'], ball['WTO'], ball['Wto_Fielder'], ball['Wto_Fielder_name'],
#                         ball['WTO_Name'], ball['wtoBatsman_name'], ball['wtoPlayer'], ball['WtoType'], ball['WtoType_Name'], ball['WW Zone']
#                        ))

# Function to insert data into the MatchDetails table
def insert_matchdetails_data(conn, MatchID, data):

    cursor = conn.cursor()

    current_score = data['currentscore']['currentscoresdetail']
    extra = json.dumps(data['currentscore']['extra'])
    bowlers = data['currentscore']['bowlers']
    batsmen = data['currentscore']['batsmans']
    last_wicket = data['currentscore']['lastwicket']

    # Extracting bowlers' data
    bowler1 = bowlers[0]
    bowler2 = bowlers[1]

    # Extracting batsmen's data
    batsman1 = batsmen[0]
    batsman2 = batsmen[1]

    # Extracting last wicket's data
    last_wicket_data = last_wicket[0]

    cursor = conn.cursor()
    cursor.execute('''INSERT INTO MatchDetails (
                        MatchID, BatTeamName, BatTeamOvers, BatTeamRuns, BatTeamWkts,
                        BwlTeamName, CurrentInningsNo, CurrentRunRate, MatchStatus,
                        MaxOvers, Partnership, PrevOvers, RecentOvers, RemainingBalls,
                        RemainingOvers, RequiredRunRate, RequiredRuns, State, Status,
                        Target, TeamAReview, TeamBReview, Extra,
                        Bowler1Name, Bowler1Econ, Bowler1Maidens, Bowler1Overs, Bowler1Runs, Bowler1Wickets,
                        Bowler2Name, Bowler2Econ, Bowler2Maidens, Bowler2Overs, Bowler2Runs, Bowler2Wickets,
                        Batsman1Name, Batsman1Balls, Batsman1Fours, Batsman1Score, Batsman1Sixes, Batsman1StrikeRate,
                        Batsman2Name, Batsman2Balls, Batsman2Fours, Batsman2Score, Batsman2Sixes, Batsman2StrikeRate,
                        LastWicketBatsman, LastWicketBattingOrder, LastWicketDismissal, LastWicketFallOfWicket, LastWicketRunsBalls
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (MatchID, current_score['batteamname'], current_score['batteamovers'],
                    current_score['batteamruns'], current_score['batteamwkts'], current_score['bwlteamname'],
                    current_score['currentinningsno'], current_score['currentrunrate'], current_score['matchstatus'],
                    current_score['maxovers'], current_score['partnership'], current_score['prevovers'],
                    current_score['recentovers'], current_score['remainingballs'], current_score['remainingovers'],
                    current_score['requiredrunrate'], current_score['requiredruns'], current_score['state'],
                    current_score['status'], current_score['target'], current_score['teamareview'],
                    current_score['teambreview'], extra,
                    bowler1['bowlername'], bowler1['econ'], bowler1['maidens'], bowler1['overs'],bowler1['runs'], bowler1['wickets'],
                    bowler2['bowlername'], bowler2['econ'], bowler2['maidens'], bowler2['overs'],bowler2['runs'], bowler2['wickets'],
                    batsman1['striker'], batsman1['balls'], batsman1['fours'], batsman1['score'],batsman1['six'], batsman1['sr'],
                    batsman2['striker'], batsman2['balls'], batsman2['fours'], batsman2['score'],batsman2['six'], batsman2['sr'],
                    last_wicket_data['batsman'], last_wicket_data['battingorder'],
                    last_wicket_data['dismissal'], last_wicket_data['fallofwic'], last_wicket_data['runsballs']))
   


# Function to parse JSON and insert data into the InningsDetail table
def insert_inningsdetails_data(conn, matchID, data):
    cursor = conn.cursor()

    for inning in data['ltinning']['ltinn']:
        batteam = inning['batteam']
        bowlteam = inning['bowlteam']
        declared = inning['declared']
        fallofwicketstr = inning['fallofwicketsstr']
        followon = inning['followon']
        innings_no = inning['inningsno']
        total_overs = inning['totalovers']
        total_runs = inning['totalruns']
        total_wickets = inning['totalwickets']
        extras = json.dumps(inning['ltextras'])

        cursor.execute('''INSERT INTO InningsDetails (
                            MatchID, BatTeam, BowlTeam, Declared, FallofWicketStr,
                            FollowOn, InningsNo, TotalOvers, TotalRuns, TotalWickets, Extras
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (matchID, batteam, bowlteam, declared, fallofwicketstr,
                        followon, innings_no, total_overs, total_runs, total_wickets, extras))
        conn.commit()


# Function to insert data into the PartnershipCard table 
def insert_partnershipcard_data(conn, matchID, data):
    cursor = conn.cursor()

    for inning in data['ltinning']['ltinn']:
        batteam = inning['batteam']
        bowlteam = inning['bowlteam']
        followin = inning['followon']
        inningsno = int(inning['inningsno'])

        for player_data in inning['ltpartnershipcard']:
            cursor.execute('''
                INSERT INTO PartnershipCard (matchID, batteam, bowlteam, followin, inningsno, balls1, balls2, player1name, player2name,
                                runs1, runs2, Runs_Balls_1, Runs_Balls_2, score, sr1, sr2, totalballs, totalruns, wkt2)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (matchID, batteam, bowlteam, followin, inningsno,               
                    player_data['balls1'], player_data['balls2'], player_data['player1name'], player_data['player2name'],
                    int(player_data['runs1']), int(player_data['runs2']), player_data['Runs_Balls_1'], player_data['Runs_Balls_2'],
                    player_data['score'], float(player_data['sr1']), float(player_data['sr2']), player_data['totalballs'], 
                    player_data['totalruns'], player_data['wkt2']))

        conn.commit()


# Function to insert data into the BowlingCard table 
def insert_bowlingcard_data(conn, matchID, data):
    cursor = conn.cursor()

    for inning in data['ltinning']['ltinn']:
        batteam = inning['batteam']
        bowlteam = inning['bowlteam']
        followin = inning['followon']
        inningsno = int(inning['inningsno'])

        for player_data in inning['ltbowlingcard']:
            cursor.execute('''
                INSERT INTO BowlingCard (matchID, batteam, bowlteam, followin, inningsno, boundary, dot, dotball, econ, extras, 
                id, maiden, nb, overs, player, runs, six, teamID, wd, wickets, wn)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (matchID, batteam, bowlteam, followin, inningsno,               
                    int(player_data['boundary']),float(player_data['dot']),player_data['dotball'],float(player_data['econ']),
                    int(player_data['extras']),int(player_data['id']),int(player_data['maiden']),int(player_data['nb']),
                    float(player_data['overs']),player_data['player'],int(player_data['runs']),int(player_data['six']),
                    int(player_data['teamID']),int(player_data['wd']),int(player_data['wickets']),player_data['wn']))

        conn.commit()


# Function to insert data into the BattingCard table
def insert_battingcard_data(conn, matchID, data):
    cursor = conn.cursor()
    for inning in data['ltinning']['ltinn']:
        batteam = inning['batteam']
        bowlteam = inning['bowlteam']
        declared = inning['declared']
        fallofwicketsstr = inning['fallofwicketsstr']
        followin = inning['followon']
        inningsno = int(inning['inningsno'])

        # Insert data from ltbattingcard list
        for player_data in inning['ltbattingcard']:
            cursor.execute('''
                INSERT INTO BattingCard (matchID, batteam, bowlteam, declared, fallofwicketsstr, followin, inningsno,
                                        player, balls, _0s, _1s, _2s, _3s, _4s, _5s, _6s, dismissal, runs, sr)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (matchID, batteam, bowlteam, declared, '', followin, inningsno,
                  player_data['player'], player_data['balls'], player_data['_0s'],
                  player_data['_1s'], player_data['_2s'], player_data['_3s'],
                  player_data['_4s'], player_data['_5s'], player_data['_6s'],
                  player_data['dismissal'], player_data['runs'], player_data['sr'] ))

        # Insert data from ltdidnotbat list
        for player_data in inning['ltdidnotbat']:
            cursor.execute('''
                INSERT INTO BattingCard (matchID, batteam, bowlteam, declared, fallofwicketsstr, followin, inningsno,
                                        player)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (matchID, batteam, bowlteam, declared, '', followin, inningsno,
                  player_data['Playername']))

        # Insert data from ltfallofwickets list
        for wicket_data in inning['ltfallofwickets']:
            cursor.execute('''
                UPDATE BattingCard
                SET fallofwicketsstr = ?
                WHERE matchID = ? AND inningsno = ? AND player = ?
            ''', (wicket_data['overs'], matchID, inningsno, wicket_data['playername']))

    conn.commit()

# Function to parse the JSON file and insert data into the database
def parse_and_insert_data(conn, file_path):
    with open(file_path, 'r') as file:
        print(f"Starting parsing for: {file}")

        match_data = json.load(file)
        matchID = file_path.split('/')[-1].split('.')[0]  # Extract matchID from file name

        insert_battingcard_data(conn, matchID, match_data)
        insert_bowlingcard_data(conn, matchID, match_data)
        insert_partnershipcard_data(conn, matchID, match_data) 
        insert_inningsdetails_data(conn, matchID, match_data) 
        insert_matchdetails_data(conn, matchID, match_data)

# Insert data into tables
def insert_fixture_data(fixture_data):
    c.executemany('''INSERT INTO Fixture (date, matchid, matchno, Matchtypeid, stage, teama, teama_id, teamb, teamb_id, time_ist, venue, venue_id)
                     VALUES (:date, :matchid, :matchno, :Matchtypeid, :stage, :teama, :teama_id, :teamb, :teamb_id, :time_ist, :venue, :venue_id)''', fixture_data)

def insert_venue_data(venue_data):
    c.executemany('''INSERT INTO Venue (city, name, venue_id)
                     VALUES (:city, :name, :venue_id)''', venue_data)

def insert_team_data(team_data):
    c.executemany('''INSERT INTO Team (Format, Prefix, team_id, TeamImage, teamname)
                     VALUES (:Format, :Prefix, :team_id, :TeamImage, :teamname)''', team_data)

def insert_player_data(player_data):
    c.executemany('''INSERT INTO Player (Battingtype, bowlingtype, DOB, Nationality, player_id, playername, refPlayerID, team_id, team_name, WK)
                     VALUES (:Battingtype, :bowlingtype, :DOB, :Nationality, :player_id, :playername, :refPlayerID, :team_id, :team_name, :WK)''', player_data)


# Load data from JSON files
fixture_data = load_json('/workspaces/TFG-Data-Engineer-Task/England v Pakistan 2020/fixtures.json')['Fixture']
venue_data = load_json('/workspaces/TFG-Data-Engineer-Task/England v Pakistan 2020/venue.json')['Venue']
team_data = load_json('/workspaces/TFG-Data-Engineer-Task/England v Pakistan 2020/team.json')['Teams']
player_data = load_json('/workspaces/TFG-Data-Engineer-Task/England v Pakistan 2020/player.json')['Player']


# Create tables
drop_tables()
create_tables()

# Insert data into tables
insert_fixture_data(fixture_data)
insert_venue_data(venue_data)
insert_team_data(team_data)
insert_player_data(player_data)

folder_path = '/workspaces/TFG-Data-Engineer-Task/England v Pakistan 2020/ScoreCard'
file_names = os.listdir(folder_path)
print(file_names)

# Parse each JSON file and insert data into the database
for file_name in file_names:
    if file_name.endswith('.json'):
        file_path = os.path.join(folder_path, file_name)
        parse_and_insert_data(conn, file_path)


# folder_path = '/workspaces/TFG-Data-Engineer-Task/England v Pakistan 2020/BallByBall'
# file_names = os.listdir(folder_path)

# # Parse each JSON file and insert data into the database
# for file_name in file_names:
#     if file_name.endswith('.json'):
#         file_path = os.path.join(folder_path, file_name)
#         with open(file_path, 'r') as file:
#             ballbyball_data = json.load(file)
#             insert_BallByBall_data(conn, ballbyball_data)

#     break

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully into SQLite database.")
