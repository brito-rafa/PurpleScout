# PurpleScout

## Description
PurpleScout is an app that simplifies the scouting process for FRC teams. 
Data pipeline (from scouting to analysis) is as follows:

1. A Windows laptop runs a Python/Flask app that hosts a web form
2. Scouters collect data and input into the app
3. After each match, an HTML form is submitted that contains the data
4. Laptop recieves POST request
5. Data from scouts is combined and organized into a huge Excel file

(The below is if we can get internet connection to the laptop)
6. Excel file is periodically synced to Google Drive
7. Google Sheets runs analytics on the data and creates suggestions for the team
8?? Web dashboard accessible to admins to see data at-a-glance and make decisions

Currently the app is in development and is not ready for use.

## Creators
Team lead: Gabriel Tao
Lead developer: Soumik Chemdupati
nobody else :(