from earliestyear import earliest_common_season
from scraper import get_data
import os
links = {
    'box_scores':'https://www.nba.com/stats/players/traditional?Season=',
    'assists':'https://www.nba.com/stats/players/passing?Season=',
    'height_weight':'https://www.nba.com/stats/players/bio?Season=',
    'touches':'https://www.nba.com/stats/players/touches?Season=',
    'drives':'https://www.nba.com/stats/players/drives?Season=',
    # 'shot_chart':'https://www.nba.com/stats/players/shooting?dir=D&sort=25-29+ft.+FGA&DistanceRange=By+Zone&Season=',
    'off_screen':'https://www.nba.com/stats/players/off-screen?SeasonYear=',
    'spot_up':'https://www.nba.com/stats/players/spot-up?SeasonYear=',
    'screen_assists':'https://www.nba.com/stats/players/hustle?Season=',
    'putback':'https://www.nba.com/stats/players/putbacks?SeasonYear=',
    'cut':'https://www.nba.com/stats/players/cut?SeasonYear=',
    'hand_off':'https://www.nba.com/stats/players/hand-off?SeasonYear=',
    'pnr_man':'https://www.nba.com/stats/players/roll-man?SeasonYear=',
    'pnr_handler':'https://www.nba.com/stats/players/ball-handler?SeasonYear=',
    'isolation':'https://www.nba.com/stats/players/isolation?SeasonYear=',
    'post_up':'https://www.nba.com/stats/players/tracking-post-ups?Season=',
    'catch_and_shoot':'https://www.nba.com/stats/players/catch-shoot?Season=',
}

earliest_common = 2015
# earliest_common = earliest_common_season(links)

path = os.getcwd()
seasons = []
for year in range(earliest_common, 2023):
    dir_name = str(year) + '-' + str(year + 1)[2:]
    if not os.path.exists(os.path.join(path, dir_name)):
        os.mkdir(os.path.join(path, dir_name))
    seasons.append(dir_name)

# for name, link in links.items():
#     print("Starting: " + name)
#     get_data(name, link, seasons)





