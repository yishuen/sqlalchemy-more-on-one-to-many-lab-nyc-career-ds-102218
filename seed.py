from models import *
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///sports.db')

Session = sessionmaker(bind=engine)
session = Session()

# below we are reading the csv files to create the data we will need to create the players
# pandas returns a DataFrame object from reading the CSV
# we then tell the DataFrame object to turn each row into dictionaries
# by giving to_dict the argument "orient='records'"
# we are telling our DataFrame to make each row a dictionary using the column headers
# as the keys for the key value pairs in each new dictionary
# feel free to uncomment lines 18-21 to see each step of the process in your terminal
# ____ example ______
# la_dodgers0 = pd.read_csv('la_dodgers_baseball.csv')
# la_dodgers1 = pd.read_csv('la_dodgers_baseball.csv').to_dict()
# la_dodgers2 = pd.read_csv('la_dodgers_baseball.csv').to_dict(orient='records')
# import pdb; pdb.set_trace()
# __________________


dodgers = Team(name='LA Dodgers')
lakers = Team(name='LA Lakers')
knicks = Team(name='NY Knicks')
yankees = Team(name='NY Yankees')
basketball = Sport(name='Basketball', teams = [lakers, knicks])
baseball = Sport(name='Baseball', teams = [dodgers, yankees])
LA = City(name='LA', teams = [lakers, dodgers])
NY = City(name='NY', teams = [knicks, yankees])

la_dodgers = pd.read_csv('la_dodgers_baseball.csv').to_dict(orient='records')

dodgers.players = list(map(lambda d: Player(name=d['name'], number=d['number'],
height=d['height'], weight=d['weight']), la_dodgers))

la_lakers = pd.read_csv('la_lakers_basketball.csv').to_dict(orient='records')

lakers.players = list(map(lambda l: Player(name=l['name'], number=l['number'],
height=l['height'], weight=l['weight']), la_lakers))

ny_yankees = pd.read_csv('ny_yankees_baseball.csv').to_dict(orient='records')

yankees.players = list(map(lambda y: Player(name=y['name'],
height=y['height'], weight=y['weight']), ny_yankees))

ny_knicks = pd.read_csv('ny_knicks_basketball.csv').to_dict(orient='records')

knicks.players = list(map(lambda k: Player(name=k['name'], number=k['number'],
height=k['height'], weight=k['weight']), ny_knicks))


# LAKERS: {'number': 'None', 'name': 'Moritz Wagner', 'position': 'PF', 'age': 21, 'height': '7-0', 'weight': 241},
# {'number': '21', 'name': 'Travis Wear', 'position': 'SF', 'age': 27, 'height': '6-10', 'weight': 225},

# YANKEES [{'name': 'Miguel Andujar', 'age': 23, 'country': 'do', 'B': 'R', 'height': "6'0", 'weight': 215, 'birthdate': 'Mar 2 1995', 'Yrs': '2', 'G': 79, 'GS': 78, 'Batting': 79, 'Defense': 74, 'P': 0, 'C': 0, '1B': 0, '2B': 0, '3B': 74, 'SS': 0, 'LF': 0, 'CF': 0, 'RF': 0, 'OF': 0, 'DH': 6, 'PH': 1, 'PR': 0, 'WAR': '0.9'},
# {'name': 'Tyler Austin', 'age': 26, 'country': 'us', 'B': 'R', 'height': "6'2", 'weight': 220, 'birthdate': 'Sep 6 1991', 'Yrs': '3', 'G': 34, 'GS': 33, 'Batting': 34, 'Defense': 27, 'P': 0, 'C': 0, '1B': 27, '2B': 0, '3B': 0, 'SS': 0, 'LF': 0, 'CF': 0, 'RF': 0, 'OF': 0, 'DH': 7, 'PH': 0, 'PR': 0, 'WAR': '0.2'}]

# KNICKS: {'name': 'Enes Kanter', 'number': 0, 'position': 'C', 'height': '6-11', 'weight': 245, 'birthdate': 'MAY 20 1992', 'age': 26}
# now that we have the data for each player
# add and commit the players, teams, sports and cities below

session.add_all([dodgers, lakers, knicks, yankees, basketball, baseball, LA, NY])
session.commit()

# we will need to probably write at least one function to iterate over our data and create the players
# hint: it may be a good idea to creat the Teams, Cities, and Sports first
