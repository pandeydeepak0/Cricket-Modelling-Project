<p style="text-align: center;">Made with markdown, please use MD viewer for best experience</p

---

### QUESTION4 :

>We frequently work on projects building APIs for clients. Suppose a client wanted to know the outcome of every delivery in a future match as it happens. Please write a function to obtain this from your schema. How would you translate this into an API, please mention which technologies/packages you would use and why.

###### Ans: To fetch latest Ball data, we can take MatchID as input and further write a query to get latest `ballID` from latest `InningsID`, alternatively the same can be achieved with latest timestamp as well. I have written a small code for the same in main.py file. Execute below commands to run the server and test endpoint - 


```
cd Scripts 
pip install fastapi uvicorn
uvicorn main:app --reload
```

###### This is the enpoint `http://127.0.0.1:8000/latest_ball_info/{match_id}` and sample outcome

```
"{
   "bowlerName": "Chris Jordan", 
   "BowlingType": "Right-arm fast-medium", 
   "bowlSpeed": 0.0, 
   "DeliveryStyle": "Reverse Swing In", 
   "PaceOrSpinName": "Pace", 
   "InningsID": 1, 
   "overs": 18.5, 
   "Runs": 2, 
   "Extras": 0
}"
```

###### I do not work on API development on a regular basis, so I picked FastAPI as its easy to setup and comes with tons of tutorials online, I went through FastAPI documentation to create the API. Again, I used python for coding the entire solution.

###### This is a very crude version of how something like this will be done in production usecase - ofcourse we will need to also design solutions to hit API when an event is triggered, setup rate limits, API keys and secure endpoints etc.
