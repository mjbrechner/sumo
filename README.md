git statusSumo Project

This is a project to analysis sumo data from the Makuuchi division, which is the top division of professional sumo in the Japan Sumo Association. This division typically entails 42 rikishi (wrestlers) engaged in six 15-day tournaments per year. This analysis covers every top-division match between January 1983 and July 2023.

Original data source: Mikhail Zhilkin at https://data.world/cervus/sumo-japan

The 227,773-line file results.csv goes line by line for every wrestler's individual top-division match results in every top-division match during the covered time period.

The 177,879-line file file bazuke.csv features a line for every wrestler in every tournament during the covered time period. This includes all wrestlers within the Japan Sumo Association at all levels, though my analysis will focus on those who are in the top division (as well as lower-division wrestlers who sometimes are called up to participate in top-division matches).

In this project, I will take each one of these .csv files, using each one to compile new dataframes. Whereas results.csv features rows for every single tournament match and banzuke.csv features rows for every wrestler in every tournament, my new dataframes will have one row for every wrestler, featuring statistics compiled from the original files. For instances, while results.csv features information on the winner of each individual match, my cleaned up file will show a wrestler's total wins over the entire 40-year time frame.

Once I have made these two new dataframes, I will combine them into the file analysis.csv and follow with further analysis and visualizations.



INSTRUCTIONS On RUNNING IN A VIRTUAL ENVIRONMENT

Create a virtual environment:

    python -m venv venv

Activate the virtual environment 
    
    Windows Users: venv\Scripts\activate
    MacIntosh/Linux Users: source venv/bin/activate

    pip install -r requirements.txt

Startup the Jupyter Notebook file

    main.ipynb (This file shows my step-by-step progress to clean up the first obtained data file, results.csv)
    banzuke_cleaning.ipynb (This file shows my step-by-step progress to clean up the second obtained file, banzuke.csv, then joining it to the first cleaned file)

When finished, deactivate as follows:

    deactivate

*which file to open, currently main2.ipynb, but also some in sql_join.ipynb*


This project will include the following features:

(1) Read TWO data files (JSON, CSV, Excel, etc.):
    
    The data files to be read are results.csv and banzuke.csv, both obtained from Mikhail Zhilkin at https://data.world/cervus/sumo-japan

(2a) Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set:
    
    I conduct heavy cleaning on the original results.csv file, merging numerous data sets together and calculating new values for wins, losses, matches, winning percentage, best rank, favorite kimarite (finishing move), and other data manupulation.

(2b) Clean your data and perform a SQL join with your data sets:
    
    I also use a SQL join to add the original banzuke.csv file with the other data.

(3) Make 3 matplotlib or seaborn (or another plotting library) visualizations to display your data:
    
    *TO BE ADDED*

(4a) Utilize a virtual environment and include instructions in your README on how the user should set one up:
    
    Featured earlier in this README.md

(4b) Build a custom data dictionary:
    
    Featured in the file DATA_DICTIONARY.md

(5) Annotate your code with markdown cells in Jupyter Notebook, write clear code comments:
    
    I have documented every step I have taken in this project in markdown. These comments detail both my thought process in coding as well as my intentions on how to extract relevant information from the data to better explore the sport of sumo.