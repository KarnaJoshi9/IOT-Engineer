# Project Name
> IOT Simulation of Sensor Data.

## General Information
- For the initial stage I have executed a python program which can be used to acquire sensor data and convert the data into csv file format.
- For the next stage to make an Edge Program for transfering or uploading this file on server I tried different methods as follows:
- Using python I converted csv file to data frame in python using pandas.
- Then, for sending the data to server I used firstly my localhost host as my edge cloud server. I sent the csv data to my edge server in the form of HTML file.
- Drawback here is this method was not able for getting a continous loop of data transfer.
- For understanding http server connection I tried to send this csv data to server. I tried to use flask module in python
- Drawback- The entire data set was being sent in one go and not in single rows.
- I also learned socket connection with server and client python files containing socket connection program. Transmission of data was successful in this conncection.
- Overall for the above project I learned to acquire data from sensor, convert it into csv file, sent this csv file to edge server, learned to use flask module to send data to server, how to establish server connection between server and client using socket programming

## Technologies Used
- Python - 3.9
- Pycharm


