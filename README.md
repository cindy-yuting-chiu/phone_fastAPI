# Building a small phone number lookup tool using FastAPI
This project is a demonstration of using AWS cloud tool to deploy a simple program using FastAPI framework. 

## Data 
The data comes from the source github: https://github.com/ravisorg/Area-Code-Geolocation-Database.
There are four different dataset in the github, we focused on the dataset us-area-code-cities.csv. 
This data is consist of columns including area code, city, state, longitude and latitude for citites in United States. We read in this data using python pandas dataframe and assign the corresponding column names for the data. 

## System Used
We developed the main python script using AWS Cloud9. We connected the Cloud9 environment with Github for version control. 
The application file is developed in FastAPI framework.
We then used EC2 to launch the instance so we can use non-local url when running the application. 
Last, we connected the application with AWS AppRunner. With AWS AppRunner, we can access the application directly using the public url.
In addition to Github, we also leveraged Github Action for continuous developement. The application will fail automatically without launching in AppRunner if there is error within the last update. 
The following is the diagram of system we used: 
<img width="924" alt="Screen Shot 2021-10-07 at 3 14 08 PM" src="https://user-images.githubusercontent.com/89810916/136485538-e54bf1be-a560-464c-941a-8960551c9045.png">

## Demo
A quick video demonstrating how to use the application and how the application is built can be found here: https://youtu.be/3_CvAED4EBo
