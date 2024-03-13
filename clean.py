import os
from driver import seasons
import pandas as pd


columns = {
    'box_scores': {'MIN':'MIN', 'FGA':'FGA', '3PA':'3PA', 'AST':'AST'},
    'assists': {'PassesMade':'PASSES MADE'},
    'height_weight': {'Height':'HEIGHT', 'Weight':'WEIGHT'},
    'touches': {'TOUCHES':'TOUCHES', 'FrontCTTouches':'FRONT CT TOUCHES', 'TimeOfPoss':'TIME OF POSS', 'AvgSecPerTouch':'AVG SEC PER TOUCH','AvgDribPerTouch':'AVG DRIB PER TOUCH', 'ElbowTouches':'ELBOW TOUCHES', 'PaintTouches':'PAINT TOUCHES'},
    'drives':{'DRIVES':'DRIVES', 'PASS':'PASS OFF DRIVE'},
    'off_screen': {'Freq%':'OFF SCREEN FREQ'},
    'spot_up':{'Freq%':'SPOT UP FREQ'},
    'screen_assists':{'ScreenAssists':'SCREEN ASSISTS'},
    'putback':{'Freq%':'PUTBACK FREQ'},
    'cut':{'Freq%':'CUT FREQ'},
    'hand_off':{'Freq%':'HANDOFF FREQ'},
    'pnr_man':{'Freq%':'PNR MAN FREQ'},
    'pnr_handler':{'Freq%':'PNR HANDLER FREQ'},
    'isolation':{'Freq%':'ISOLATION FREQ'},
    'post_up':{'PostUps':'POST UPS'},
    'catch_and_shoot':{'FGA':'CATCH AND SHOOT FGA', '3PA':'CATCH AND SHOOT 3PA'},
}

def preprocess():
    for name, new_columns in columns.items():
        print("Preprocessing: " + name)
        for season in seasons:
            path = os.path.join(os.getcwd(), season, name + '.csv')
            df = pd.read_csv(path)

            if 'Player' in df.columns:
                df = df.rename(columns={'Player':'PLAYER', 'Team':'TEAM'})

            df = df.rename(columns=new_columns)

            #remove all columns except for new_columns
            df.drop(columns=df.columns.difference(['PLAYER', 'TEAM'] + list(new_columns.values())), inplace=True)

            df.to_csv(path, index=False)
            print("Finished: " + name + " " + season)

preprocess()
            
# path = os.path.join(os.getcwd(), "2015-16", "box_scores" + '.csv')
# new_columns = columns["box_scores"]

# df = pd.read_csv(path)
# df = df.rename(columns=new_columns)

#remove all columns except for new_columns
# print(df.columns.difference(list(new_columns.values())))

# df.drop(columns=df.columns.difference(['PLAYER', 'TEAM'].append(list(new_columns.values()))), inplace=True)

# df.to_csv(path, index=False)
# print("Finished: " + name + " " + season)