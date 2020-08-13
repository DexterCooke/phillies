from bs4 import BeautifulSoup as bs 
import requests
import re

URL = "https://questionnaire-148920.appspot.com/swe/data.html"
TOP_PLAYERS_COUNT = 125


def calculate_offer():
    """ 
     Uses the beautiful soup library to scrape the URL
     find all player salaries, clean the data and return
     a qualifying offer
    """
    r = requests.get(URL)
    soup = bs(r.content, "html.parser")
    raw_data = soup.find_all("td", attrs={"class": "player-salary"}, string=re.compile("$"))
    remove_invalid_salaries = [x.string for x in raw_data if '$' in x.string]
    remove_dollar_sign = [x.replace('$', '') for x in remove_invalid_salaries]
    convert_to_int = [int(x.replace(',', '')) for x in remove_dollar_sign]
    sort_top_players = sorted(convert_to_int, reverse=True)[:TOP_PLAYERS_COUNT]
    offer = sum(sort_top_players)/TOP_PLAYERS_COUNT

    return offer





