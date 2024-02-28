import json
import sqlite3
import os 
import db_ddl
import db_dml

# Load data from JSON files
def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Create SQLite connection and cursor
conn = sqlite3.connect('cricket_data.db')
c = conn.cursor()


# Function to parse the JSON file and insert data into the database
def parse_and_insert_data(conn, file_path):
    with open(file_path, 'r') as file:
        print(f"Starting parsing for: {file}")

        if str(file_path.split('/')[-2]) == 'ScoreCard':
            
            match_data = json.load(file)
            matchID = file_path.split('/')[-1].split('.')[0]  # Extract matchID from file name

            db_dml.insert_battingcard_data(conn, matchID, match_data)
            db_dml.insert_bowlingcard_data(conn, matchID, match_data)
            db_dml.insert_partnershipcard_data(conn, matchID, match_data) 
            db_dml.insert_inningsdetails_data(conn, matchID, match_data) 
            db_dml.insert_matchdetails_data(conn, matchID, match_data)

        elif str(file_path.split('/')[-2]) == 'BallByBall':

            ballbyball_data = json.load(file)
            matchID = file_path.split('/')[-1].split('.')[0]  # Extract matchID from file name

            db_dml.insert_squad_data(conn, matchID, ballbyball_data)
            db_dml.insert_matchinfo_data(conn, matchID, ballbyball_data)
            db_dml.insert_ballbyball_data(conn, matchID, ballbyball_data)

# Function to scan folders for JSON filepaths
def parse_files_in_folder(folder_name):
    folder_path = f'/workspaces/TFG-Data-Engineer-Task/England v Pakistan 2020/{folder_name}'
    file_names = os.listdir(folder_path)

    # Parse each JSON file and insert data into the database
    for file_name in file_names:
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_path, file_name)
            parse_and_insert_data(conn, file_path)


if __name__ == "__main__":
    # Load data from JSON files
    venue_data = load_json('/workspaces/TFG-Data-Engineer-Task/England v Pakistan 2020/venue.json')['Venue']
    team_data = load_json('/workspaces/TFG-Data-Engineer-Task/England v Pakistan 2020/team.json')['Teams']
    player_data = load_json('/workspaces/TFG-Data-Engineer-Task/England v Pakistan 2020/player.json')['Player']
    fixture_data = load_json('/workspaces/TFG-Data-Engineer-Task/England v Pakistan 2020/fixtures.json')['Fixture']


    # Create tables
    db_ddl.drop_tables(conn)
    db_ddl.create_tables(conn)

    # Insert data into tables
    db_dml.insert_venue_data(conn, venue_data)
    db_dml.insert_team_data(conn, team_data)
    db_dml.insert_player_data(conn, player_data)
    db_dml.insert_fixture_data(conn, fixture_data)

    #JSON Folders
    data_folders = ['BallByBall', 'ScoreCard']
    for folder in data_folders:
        parse_files_in_folder(folder)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print("Data inserted successfully into SQLite database.")
