import sqlite3
import re
import json

# Function to insert data into the Venue table
def insert_venue_data(conn, venue_data):

    print("writing venue data to DB")
    cursor = conn.cursor()

    for venue in venue_data:   
        cursor.execute('''INSERT INTO Venue (venue_id, city, name)
                     VALUES (?, ?, ?)''', (venue['venue_id'], venue['city'], venue['name']))
    
    conn.commit()

# Function to insert data into the Team table
def insert_team_data(conn, team_data):

    print("writing team data to DB")
    cursor = conn.cursor()

    for team in team_data:   
        cursor.execute('''INSERT INTO Team (team_id, Format, Prefix, TeamImage, teamname)
                     VALUES (?, ?, ?, ?, ?)''', (team['team_id'], team['Format'], team['Prefix'], team['TeamImage'], team['teamname']))
    
    conn.commit()

# Function to insert data into the Squad table
def insert_squad_data(conn, matchID, ballbyball_data):
    
    print("writing Squad data to DB")
    cursor = conn.cursor()

    for player in ballbyball_data['squad']:
        cursor.execute('''INSERT INTO Squad (
                            MatchID, Clubid, PlayerID, BattingOrder, isCaptain, isPlayed, isWK
                        ) VALUES (?,?,?,?,?,?,?)''',
                       (matchID, player['Clubid'], player['PlayerID'],player['BattingOrder'], player['isCaptain'],player['isPlayed'],player['isWK']))
    
    conn.commit()


# Function to insert data into the Player table
def insert_player_data(conn, player_data):

    print("writing player data to DB")
    cursor = conn.cursor()

    for player in player_data:
        cursor.execute('''INSERT INTO Player(
                    player_id
                    ,team_id
                    ,Battingtype
                    ,bowlingtype
                    ,DOB
                    ,Nationality
                    ,playername
                    ,refPlayerID
                    ,team_name
                    ,WK)
                    VALUES(?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?)''', (
                            player['Battingtype']
                            ,player['bowlingtype']
                            ,player['DOB']
                            ,player['Nationality']
                            ,player['player_id']
                            ,player['playername']
                            ,player['refPlayerID']
                            ,player['team_id']
                            ,player['team_name']
                            ,player['WK']
                        ))

    conn.commit()

# Function to insert data into the Fixture table
def insert_fixture_data(conn, fixture_data):
    
    print("writing fixture data to DB")
    cursor = conn.cursor()
    
    for fixture in fixture_data:

        #TODO: Capture CompetitionID from MatchInfo
        folder_path = '/workspaces/TFG-Data-Engineer-Task/England v Pakistan 2020/BallByBall'
        file_name = str(fixture['matchid'])

        # Parse each JSON file and insert data into the database
        file_path = f"{folder_path}/{file_name}.json"
        
        with open(file_path, 'r') as file:
            match_info_data = json.load(file)

        competition_id = match_info_data['MatchInfo']['CompetitionID']

        cursor.execute('''INSERT INTO Fixtures(
                     fixture_id
                    ,matchid
                    ,date
                    ,matchno
                    ,Matchtypeid
                    ,stage
                    ,teama
                    ,teama_id
                    ,teamb
                    ,teamb_id
                    ,time_ist
                    ,venue
                    ,venue_id)
                    VALUES(?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,?,?,?)''', (
                        competition_id
                        ,fixture['matchid']
                        ,fixture['date']
                        ,fixture['matchno']
                        ,fixture['Matchtypeid']
                        ,fixture['stage']
                        ,fixture['teama']
                        ,fixture['teama_id']
                        ,fixture['teamb']
                        ,fixture['teamb_id']
                        ,fixture['time_ist']
                        ,fixture['venue']
                        ,fixture['venue_id']
                        ))

    conn.commit()

# Function to insert data into the MatchInfo table
def insert_matchinfo_data(conn, matchID, ballbyball_data):

    print("writing matchinfo data to DB")

    cursor = conn.cursor()

    match_info_data = ballbyball_data['MatchInfo']
    cursor.execute('''INSERT INTO MatchInfo(
                     matchid
                    ,fixture_id
                    ,venue_id
                    ,Firstinn_RevisedOvers
                    ,FirstInngBatClubId
                    ,Secondinn_RevisedOvers
                    ,ClubA
                    ,ClubB
                    ,DayOrnight
                    ,KnockOut
                    ,ManOftheMatch
                    ,MatchDate
                    ,MatchTypeID
                    ,Result
                    ,RevisedTarget
                    ,Stage
                    ,Status
                    ,TossOpted
                    ,TossWin
                    ,WonClubid)
                    VALUES(?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,?,?,?,?,?,?,?,?,?,?)''', (
                    matchID
                    ,match_info_data['CompetitionID']
                    ,match_info_data['StadiumID']
                    ,match_info_data['1stinn RevisedOvers']
                    ,match_info_data['1stInngBatClubId']
                    ,match_info_data['2ndinn RevisedOvers']
                    ,match_info_data['ClubA']
                    ,match_info_data['ClubB']
                    ,match_info_data['DayOrnight']
                    ,match_info_data['KnockOut']
                    ,match_info_data['ManOftheMatch']
                    ,match_info_data['MatchDate']
                    ,match_info_data['MatchTypeID']
                    ,match_info_data['Result']
                    ,match_info_data['RevisedTarget']
                    ,match_info_data['Stage']
                    ,match_info_data['Status']
                    ,match_info_data['TossOpted']
                    ,match_info_data['TossWin']
                    ,match_info_data['WonClubid']
    ))

    conn.commit()


# Function to insert data into the MatchDetails table
def insert_matchdetails_data(conn, MatchID, data):

    print("writing matchdetails data to DB")

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

    print("writing Inningdetails data to DB")
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
                            MatchID, InningsNo, BatTeam, BowlTeam, Declared, FallofWicketStr,
                            FollowOn, TotalOvers, TotalRuns, TotalWickets, Extras
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (matchID, innings_no, batteam, bowlteam, declared, fallofwicketstr,
                        followon, total_overs, total_runs, total_wickets, extras))
        conn.commit()


# Function to insert data into the BattingCard table
def insert_battingcard_data(conn, matchID, data):

    print("writing battingcard data to DB")

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
                INSERT INTO BattingScorecard (matchID, inningsno, player_id, batteam, bowlteam,
                                     balls, _0s, _1s, _2s, _3s, _4s, _5s, _6s, dismissal, runs, sr)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (matchID, inningsno, player_data['id'], batteam, bowlteam,
                  player_data['balls'], player_data['_0s'],
                  player_data['_1s'], player_data['_2s'], player_data['_3s'],
                  player_data['_4s'], player_data['_5s'], player_data['_6s'],
                  player_data['dismissal'], player_data['runs'], player_data['sr'] ))

        # Insert data from ltdidnotbat list
        for player_data in inning['ltdidnotbat']:
            cursor.execute('''
                INSERT INTO BattingScorecard (matchID, inningsno, player_id, batteam, bowlteam)
                VALUES (?, ?, ?, ?, ?)
            ''', (matchID, inningsno, player_data['id'], batteam, bowlteam))

        # # Insert data from ltfallofwickets list
        # #TODO: Get player ID from their name and only fill ID 
        # #TODO: To come back
        # for wicket_data in inning['ltfallofwickets']:
        #     cursor.execute('''
        #         UPDATE BattingScorecard
        #         SET fallofwicketsstr = ?
        #         WHERE matchID = ? AND inningsno = ? AND player_id = ?
        #     ''', (wicket_data['overs'], matchID, inningsno, wicket_data['playername']))

    conn.commit()

# Function to insert data into the BowlingCard table 
def insert_bowlingcard_data(conn, matchID, data):
    print("writing bowlingcard data to DB")

    cursor = conn.cursor()

    for inning in data['ltinning']['ltinn']:
        batteam = inning['batteam']
        bowlteam = inning['bowlteam']
        followin = inning['followon']
        inningsno = int(inning['inningsno'])

        for player_data in inning['ltbowlingcard']:
            cursor.execute('''
                INSERT INTO BowlingScorecard (matchID, inningsno, player_id, batteam, bowlteam, boundary, dot, dotball, econ, extras, 
                maiden, nb, overs, runs, six, teamID, wd, wickets)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (matchID, inningsno, int(player_data['id']), batteam, bowlteam,               
                    int(player_data['boundary']),float(player_data['dot']),player_data['dotball'],float(player_data['econ']),
                    int(player_data['extras']),int(player_data['maiden']),int(player_data['nb']),
                    float(player_data['overs']),int(player_data['runs']),int(player_data['six']),
                    int(player_data['teamID']),int(player_data['wd']),int(player_data['wickets'])))

        conn.commit()


# Function to insert data into the PartnershipCard table 
def insert_partnershipcard_data(conn, matchID, data):
    print("writing partnership data to DB")

    cursor = conn.cursor()

    for inning in data['ltinning']['ltinn']:
        batteam = inning['batteam']
        bowlteam = inning['bowlteam']
        followin = inning['followon']
        inningsno = int(inning['inningsno'])

        #TODO: Get player 1 and player 2 ID from players table using names

        
        for player_data in inning['ltpartnershipcard']:
            
            #TODO: populate balls and totalruns fields
            balls1 = re.search(r'\((\d+)\)', player_data['Runs_Balls_1']).group(1)
            balls2 = re.search(r'\((\d+)\)', player_data['Runs_Balls_2']).group(1)

            totalballs = int(balls1)+int(balls2)
            totalruns = int(player_data['runs1'])+ int(player_data['runs2'])


            cursor.execute('''
                INSERT INTO PartnershipCard (matchID, inningsno, player1_id, player2_id, player1name, player2name, batteam, bowlteam, followin, balls1, balls2,
                                runs1, runs2, Runs_Balls_1, Runs_Balls_2, score, sr1, sr2, totalballs, totalruns, wkt2)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (matchID, inningsno, -1, -1, player_data['player1name'], player_data['player2name'], batteam, bowlteam, followin,               
                    balls1, balls2,
                    int(player_data['runs1']), int(player_data['runs2']), player_data['Runs_Balls_1'], player_data['Runs_Balls_2'],
                    player_data['score'], float(player_data['sr1']), float(player_data['sr2']), totalballs, 
                    totalruns, player_data['wkt2']))

        conn.commit()


#Function to parse JSON and insert data into BallByBall table
def insert_ballbyball_data(conn, matchID, ballbyball_data):
    print("writing ballbyball data to DB")

    cursor = conn.cursor()

    ltball = ballbyball_data['ltball']

    for ball in ltball:
        cursor.execute('''INSERT INTO BallByBall (
                            MatchID, InningsID, BallID, BallStopType, BatsmanInControlOutControl, BatSubject,
                            BatSubjectName, BattingClubID, BattingOrder, BattingType, BattingTypeID,
                            BowlerID, BowlerName, BowlingClubID, BowlingType, BowlingTypeID,
                            BowlSpeed, CatchType, CatchTypeName, CreaseMovement, CreaseMovementID,
                            DeliveryStyle, DeliveryStyleID, DirectHit, DirectHitName, DismissalFielderID1,
                            DismissalFielderID2, DismissalType, DismissalTypeID, DismissedPlayer,
                            DismissedPlayerName, EndID, Extras, ExtrasType, ExtrasTypeName, FieldPosition,
                            FieldPositionID, HeightX, HeightY, InterceptionPointX, InterceptionPointY,
                            InTheAir, IsDRS, IsFour, IsSix, ISTTime, IsWicket, LengthX, LengthY, Lofted,
                            MisRun, MRFielderID, MRFielderName, NonStrikerID, NonStrikerName,
                            OnOrOff, OverID, OverOrRound, OverOrRoundName, Overs, OverThrowRuns,
                            PaceOrSpin, PaceOrSpinName, PitchmapZone, PowerSurge, ReleasePointX,
                            ReleasePointY, Runs, SaveRun, ShotConnection, ShotConnectionName, SixDistance,
                            SRFielderName, SRFielderID, StrikerID, StrikerName, Stroke, StrokeID,
                            SubjectTag, SubjectTagName, SZZone, UmpireName, UmpireID, WagonWheelX,
                            WagonWheelY, WicketKeeperStandingPosition, WTO, WTOFielder, WTOFielderName,
                            WTOName, WTOBatsmanName, WTOPlayer, WTOType, WTOTypeName, WWZone
                        ) VALUES (?,
                                ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                                ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,
                                ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       (ball['MatchID'], ball['InningsID'], ball['BallID'], ball['BallStopType'], ball['Batsman InControl/OutControl'], ball['BatSubject'],
                        ball['BatSubjectName'], ball['BattingClubID'], ball['battingorder'], ball['BattingType'], ball['BattingTypeID'],
                        ball['bowlerid'], ball['bowlerName'], ball['BowlingClubID'], ball['BowlingType'], ball['BowlingTypeID'],
                        ball['bowlSpeed'], ball['CatchType'], ball['CatchType_Name'], ball['Creasemovement'], ball['CreaseMovementId'],
                        ball['DeliveryStyle'], ball['DeliveryStyleID'], ball['Directhit'], ball['Directhit_name'], ball['DismissalFielderID1'],
                        ball['DismissalFielderID2'], ball['dismissaltype'], ball['DismissalTypeId'], ball['Dismissedplayer'],
                        ball['Dismissedplayer_name'], ball['EndID'], ball['Extras'], ball['extrastype'], ball['ExtrasTypeName'], ball['fieldPosition'],
                        ball['fieldPositionid'], ball['HeightX'], ball['HeightY'], ball['InterceptionPoint_X'], ball['InterceptionPoint_Y'],
                        ball['InTheair'], ball['isDRS'], ball['isfour'], ball['issix'], ball['IST TIME'], ball['IsWicket'], ball['LengthX'], ball['LengthY'], ball['Lofted'],
                        ball['MisRun'], ball['MR_Fielderid'], ball['MR_FielderName'], ball['nonstrikerid'], ball['NonStrikerName'],
                        ball['OnorOff'], ball['overid'], ball['OverorRound'], ball['OverorRound_Name'], ball['overs'], ball['OverThrowRuns'],
                        ball['PaceorSpin'], ball['PaceorSpin_name'], ball['Pitchmap Zone'], ball['PowerSurge'], ball['ReleasePoint_X'],
                        ball['ReleasePoint_Y'], ball['Runs'], ball['saverun'], ball['ShotConnection'], ball['ShotConnectionName'], ball['SixDistance'],
                        ball['SR_Fielder_Name'], ball['SR_Fielderid'], ball['StrikerID'], ball['StrikerName'], ball['Stroke'], ball['StrokeID'],
                        ball['subjecttag'], ball['SubjectTagName'], ball['SZ Zone'], ball['umpire_name'], ball['umpireid'], ball['WagonWheelX'],
                        ball['WagonWheelY'], ball['WicketKeeper Standing position'], ball['WTO'], ball['Wto_Fielder'], ball['Wto_Fielder_name'],
                        ball['WTO_Name'], ball['wtoBatsman_name'], ball['wtoPlayer'], ball['WtoType'], ball['WtoType_Name'], ball['WW Zone']
                       ))

