# scrape.py: example usage of the python TBA API, unused for now
import tbapy
import pprint

tba = tbapy.TBA('rZxJQVjP40eTtskoUbT3OWTKEnKNxk8McjB9QqRdU8mT78o8EN3OuzuMppJTADtV')

team = tba.team(418)

# Current event
EVENT = '2023txbel'

# Get the teams at the event
#teams = tba.event_teams(EVENT)

#print("There are {} teams at {}".format(len(teams), EVENT))
#for team in teams:
    #print(f"Team {team.team_number} ({team.nickname}) is from {team.city}, {team.state_prov}")

# Get the matches at the event
#matches = tba.event_matches(EVENT)

#print("There are {} matches at {}".format(len(matches), EVENT))
#for match in matches:
    #print(f"Match {match.key} is between {match.alliances['red']['team_keys']} and {match.alliances['blue']['team_keys']}")


example_match = tba.match('2023cmptx_f1m2')
pprint.pprint(example_match.score_breakdown)

# Data we can use:
"""
match.score_breakdown.[red/blue]

"""