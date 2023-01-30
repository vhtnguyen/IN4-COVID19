### Computer networking

# IN4-COVID19

This is a `client-server` application tracking covid-19 information of all provinces in Vietnam using `Socket programming` with `TCP`.
The server fetches data from [this API](https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST) and automatically updates it every 60 minutes or when needed.

## For Ú-er

I attached my report so you guys can read the report for more details. I received 8.6 for this app. I think the main reason are I didn't use any database for this app, the messages struct was not good too, and spent too much time on the UI which was not important in this project.

## Usage

1. The client need to know the server's network address in the form of IP and Port number if needed (the default port is `8888`). eg: `192.168.1.5` or `192.168.1.5:8080`.

2.
   - To start the server, run `serverMain.py` in folder `server`. An available account to test: username `admin` and the password `admin`.
   - To start the client, run `clientMain.py` in folder `client`. Connect to the server address then login or signup for an account. An availible account to test has both is `1`.

The main processing is on `serverSocket.py` and `dataBase.py`.

## Demo

I used `PyQT5` to develop UI and made it a classic macOS UI.


![connect](screenshots/Screenshot%202023-01-30%20093815.png)
![login successfully](screenshots/Screenshot%202023-01-30%20063346.png)
![search result](screenshots/Screenshot%202023-01-30%20093312.png)
