import bs4 as soup
import requests
import json

# Scraping nba.com/stats for NBA data based on passsed in player name, statistic, and year
class Scrape():
    
    base_url = "https://www.nba.com/stats/"

    def __init__(self, player, metric, year):
        self.player = player
        self.metric = metric
        self.year = year

    def get_player(self):
        return self.player

    def get_metric(self):
        return self.metric

    def get_year(self):
        return self.year

    def get_data(self):
        pass

    