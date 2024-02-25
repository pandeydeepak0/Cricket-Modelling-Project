import json
import sqlite3

# Load data from JSON files
def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Create SQLite connection and cursor
conn = sqlite3.connect('cricket_data.db')
c = conn.cursor()

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
fixture_data = load_json('C:\Projects\TFG_Data_Engineer_Task\TFG Data Engineer Task\England v Pakistan 2020\fixtures.json')['Fixture']
venue_data = load_json('C:\Projects\TFG_Data_Engineer_Task\TFG Data Engineer Task\England v Pakistan 2020\fixtures.json')['Venue']
team_data = load_json('C:\Projects\TFG_Data_Engineer_Task\TFG Data Engineer Task\England v Pakistan 2020\fixtures.json')['Teams']
player_data = load_json('C:\Projects\TFG_Data_Engineer_Task\TFG Data Engineer Task\England v Pakistan 2020\fixtures.json.json')['Player']

# Create tables
create_tables()

# Insert data into tables
insert_fixture_data(fixture_data)
insert_venue_data(venue_data)
insert_team_data(team_data)
insert_player_data(player_data)

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully into SQLite database.")
