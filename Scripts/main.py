from fastapi import FastAPI, HTTPException
import sqlite3
import json

app = FastAPI()

# Function to get max BallID of latest innings for a given match ID
def get_max_ballid_latest_innings(match_id):
    try:
        conn = sqlite3.connect('cricket_data.db')
        cursor = conn.cursor()

        #TODO: Utilize timestamp to grab latest delivery 
        #Behavior - on screen refrsh hit an API that checks if latest timestamp fetched from ballbyball
        cursor.execute('''SELECT MAX(BallID) FROM BallByBall WHERE MatchID = ? AND InningsID = (SELECT MAX(InningsID) FROM BallByBall WHERE MatchID = ?)''', (match_id, match_id))
        max_ballid = cursor.fetchone()[0]
        conn.close()
        return max_ballid
    except Exception as e:
        raise e 

# Function to get ball info based on max BallID for a given match ID
def get_ball_info(match_id, max_ballid):
    try:
        conn = sqlite3.connect('cricket_data.db')
        cursor = conn.cursor()

        # We can extract more info if needed
        cursor.execute('''SELECT bowlerName, BowlingType, bowlSpeed, DeliveryStyle, 
            PaceOrSpinName, InningsID, overs, Runs, Extras FROM BallByBall WHERE MatchID = ? AND BallID = ?''', (match_id, max_ballid))
        ball_info = cursor.fetchone()
        conn.close()
        return ball_info
    except Exception as e:
        raise e

# Convert ball info to JSON format
def ball_info_to_json(ball_info):
    if ball_info:
        return {
            "bowlerName": ball_info[0],
            "BowlingType": ball_info[1],
            "bowlSpeed": ball_info[2],
            "DeliveryStyle": ball_info[3],
            "PaceOrSpinName": ball_info[4],
            "InningsID": ball_info[5],
            "overs": ball_info[6],
            "Runs": ball_info[7],
            "Extras": ball_info[8]
            # We can add other fields here if needed
        }
    else:
        return {}

# Setting up the API endpoint
@app.get("/latest_ball_info/{match_id}")
def latest_ball_info(match_id: int):
    try:
        max_ballid = get_max_ballid_latest_innings(match_id)
        ball_info = get_ball_info(match_id, max_ballid)
        return (ball_info_to_json(ball_info))
    except HTTPException as e:
        return e
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
