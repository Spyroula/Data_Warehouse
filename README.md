Introduction

Sparkify, is a fast growing music streaming startup. As their user and song databases are rapidly rise, Sparkify, decided to move their data and processes onto the cloud. Their database consist of JSON logs on the activity of the users of the app as well as JSON metadata on the songs in the app. All the data are securely stored in AWS S3 buckets. 

Sparkify, asked the data engineering team to help with the fast growing data and support the Analytics team with their main job, finding valuable insight on the songs that their users listen to. The main task for the Data Engineering team is to build an ETL Pipeline that extracts their data from S3 buckets, stags the data in AWS Redshift and finally transform the data into a set of fact and dimensional tables.

Project Datasets

Song Dataset

The song dataset is a subset of the Million Song Dataset(https://labrosa.ee.columbia.edu/millionsong/). Each JSON file obtains metadata on thesong and the artist of that song.
The files are seperated by the each song's track ID (first three letters). 
For instance:

    song_data/A/B/C/TRABCEI128F424C983.json
    song_data/A/A/B/TRAABJL12903CDCF1A.json

Here is an example of what a single JSON song file, TRAABJL12903CDCF1A.json, looks like:

    {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

Log Dataset

The log dataset consists of log JSON files, partitioned by month and year. 
For instance:

    log_data/2018/11/2018-11-12-events.json
    log_data/2018/11/2018-11-13-events.json

And below is an example of what a single log file, 2018-11-13-events.json, looks like.

    {"artist":"Pavement", "auth":"Logged In", "firstName":"Sylvie", "gender", "F", "itemInSession":0, "lastName":"Cruz", "length":99.16036, "level":"free", "location":"Klamath Falls, OR", "method":"PUT", "page":"NextSong", "registration":"1.541078e+12", "sessionId":345, "song":"Mercy:The Laundromat", "status":200, "ts":1541990258796, "userAgent":"Mozilla/5.0(Macintosh; Intel Mac OS X 10_9_4...)", "userId":10}

Schema 

A Star Schema is crucial for optimizing queries on song play queries.

Fact Table

Songplays:

    NextSong, songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

Dimension Tables

Users:

    users, user_id, first_name, last_name, gender, level

Songs:

    songs, song_id, title, artist_id, year, duration

Artists: 

    artists, artist_id, name, location, lattitude, longitude

Time: 

    start_time, hour, day, week, month, year, weekday

Project Architecture 

The project includes four python files:

1. `create_table.py`:
The script creates the staging, dimension and fact tables for the Star schema in Redshift.

2. `etl.py`:
The script loads data from S3 buckets into the staging tables in Redshift and then process the data into the analytics tables on Redshift.

3. `sql_queries.py`:
The script defines the SQL queries, which will be imported into the `create_table.py` and `etl.py` scripts.

4. README.md:
A detailed explanation of the project and the builted ETL pipeline.


Project instructions

1) Setup an AWS Redshift cluster with the right configurations and insert the details in dwh.cfg.
2) Run the `create_tables.py` script in order to create the required database structure.
3) Run the `etl.py` script in order to process the data from the S3 data buckets.