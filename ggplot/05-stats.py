from ggplot import *
import pandas as pd
import numpy as np


df = pd.read_csv("./baseball-pitches-clean.csv")
df = df[['pitch_time', 'inning', 'pitcher_name', 'hitter_name', 'pitch_type',
         'px', 'pz', 'pitch_name', 'start_speed', 'end_speed', 'type_confidence']]
# print df.head()


df['game_date'] = df.pitch_time.str.slice(0, 10)  # Takes first 10 chars of date string
df['pitch_count'] = 1  # New field with all 1s

df['pitch_count'] = df.groupby(["pitcher_name", "game_date"]).pitch_count.cumsum()  # Sums how many times each pitcher threw pitches


# From messy blob...
# print ggplot(aes(x='pitch_count', y='start_speed'), data=df) + geom_point()  # Blob

# To smooth curve: Performes localized regression
# print ggplot(aes(x='pitch_count', y='start_speed'), data=df) + stat_smooth()

# Adjust how many points are considered in the regression with the span=0.3
# print ggplot(aes(x='pitch_count', y='start_speed'), data=df) + stat_smooth(span=0.3)

# Uses local moving average instead of regression
# print ggplot(aes(x='pitch_count', y='start_speed'), data=df) + stat_smooth(method='lm')

#  Remove the bounderies and split by color
print ggplot(aes(x='pitch_count', y='start_speed', color='pitch_name'), data=df) + stat_smooth(se=False)
