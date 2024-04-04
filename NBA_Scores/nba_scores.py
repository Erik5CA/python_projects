from pprint import PrettyPrinter
from datetime import datetime
from requests import get
from api_key import API_KEY

now = datetime.now()
date = f'/{now.day}/{now.month}/{now.year}'

printer = PrettyPrinter()

url = "https://basketapi1.p.rapidapi.com/api/basketball/matches"

headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": "basketapi1.p.rapidapi.com"
}

def get_scoreboard():
    data = get(f'{url}{date}', headers=headers, timeout=5).json()

    games = data['events']
    games = games[:18]

    for game in games:
        home_team = game['homeTeam']['shortName']
        away_team = game['awayTeam']['shortName']
        if game['status']['type'] != 'notstarted':
            time = game['time']['played']
            period = game['time']['totalPeriodCount']
            score_home = game['homeScore']['current']
            score_away = game['awayScore']['current']
        else:
            time = 0
            period = 1
            sccore_home = 0
            sccore_away = 0
        print('-------------------------------------------------------')
        print(f'{home_team} vs {away_team}')
        print(f'{score_home} - {score_away}')
        print(f'{time} - {period}')

get_scoreboard()