Sumo Project

This is a project to analysis sumo data from the Makuuchi division, which is the top division of professional sumo in the Japan Sumo Association. This division typically entails 42 rikishi (wrestlers) engaged in six 15-day tournaments per year. This analysis covers every top-division match between January 1983 and July 2023.

Original data source: Mikhail Zhilkin at https://data.world/cervus/sumo-japan

This project will include the following features:

(1) Read TWO data files (JSON, CSV, Excel, etc.): The data files to be read are results.csv and banzuke.csv, both obtained from Mikhail Zhilkin at https://data.world/cervus/sumo-japan

(2a) Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set: I conduct heavy cleaning on the original results.csv file, merging numerous data sets together and calculating new values for wins, losses, matches, winning percentage, best rank, favorite kimarite (finishing move), and other data manupulation.

(2b) Clean your data and perform a SQL join with your data sets: I also use a SQL join to add the original banzuke.csv file with the other data.

(3) Make 3 matplotlib or seaborn (or another plotting library) visualizations to display your data. *TO BE ADDED*

(4a) Utilize a virtual environment and include instructions in your README on how the user should set one up: *TO BE ADDED*

(4b) Build a custom data dictionary: Featured in the file DATA_DICTIONARY.md

(5) Annotate your code with markdown cells in Jupyter Notebook, write clear code comments: I have documented every step I have taken in this project in markdown. These comments detail both my thought process in coding as well as my intentions on how to extract relevant information from the data to better explore the sport of sumo.

