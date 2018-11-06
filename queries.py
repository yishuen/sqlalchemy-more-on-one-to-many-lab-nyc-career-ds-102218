from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sports.db')

Session = sessionmaker(bind=engine)
session = Session()

def return_teams_for_new_york():
    return session.query(City).filter(City.name == 'NY')[0].teams

def return_players_for_la_dodgers():
    return session.query(Team).filter(Team.name == 'LA Dodgers')[0].players

def return_sorted_new_york_knicks():
    return session.query(Player).filter(Player.team == 'NY Knicks')
    # joined = Team.join(Team, Team.id == Player.team_id)
    # return session.query(joined).filter(Team.name == 'NY Knicks').
    # order_by(Player.number).players
    # here we want to return all the players on the New York Knicks
    # sorted in ascending (small -> big) order by their number

def return_youngest_basket_ball_player_in_new_york():
    # here we want to sort all the players on New York Knicks by age
    # and return the youngest player
    pass

def return_all_players_in_los_angeles():
    # here we want to return all players that are associated with
    # a sports team in LA
    pass

def return_tallest_player_in_los_angeles():
    # here we want to return the tallest player associted with
    # a sports team in LA
    pass

def return_team_with_heaviest_players():
    # here we want to return the city with the players that
    # have the heaviest average weight (total weight / total players)
    pass
