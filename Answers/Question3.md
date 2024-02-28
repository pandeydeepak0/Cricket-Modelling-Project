<p style="text-align: center;">Made with markdown, please use MD viewer for best experience</p

---

### QUESTION3 :

>The data engineers within the team ensure our processes are automated on the cloud, what would you need to think about if automating and deploying this as a service that writes to a database?

###### Ans: To automate the ingestion process, we will have to setup a workflow and schedular. We can consider two scenarios for the ingestion to happen 
    
    1. Ingestion to happen as soon as new data is available (new JSON files)
    2. Ingestion can happen at certain fixed time of the day and the code can scan all new data 
    
###### Its not clear with the question, if the data for ongoing matches will be streamed to the JSON files or it needs to be captured from some external APIs, in those cases the solution need to be carefully designed keeping in mind the batch or real-time nature of the data. This phase of solution discovery will require more domain knowledge and insights into potential usage for this data. 

###### To simplify things, I will only talk about ingesting data from JSON files that are already available.

#### Approach 01
1. We will need to write JSON files in our storage, for GCP it can be the GCS buckets. Once we have setup GCS buckets, we can use cloud functions to detect new data in the source system storage and upload it in our bucket. 

2. We will want to run our ingestion.py script as soon as the new data is available, for this we can setup a trigger on our GCS bucket which causes a cloud function to execute, that runs our ingestion script. We can do case specific handling as and when required.

3. We might need to migrate from our SQLite3 DB to native RDBMS of the cloud platform. 

#### Approach 02 
Alternatively, we can also use cloud Composer (Airflow) or any other workflow tool to both schedule and manage the ingestion process, the python script can be uploaded to GCS bucket and composer can be used to control the run frequency.


###### This only covers a small portion of the entire end-to-end journey for this data, I am not sure if streaming solutions for this data, setting up message queues, DB design were in scope for this question. 
