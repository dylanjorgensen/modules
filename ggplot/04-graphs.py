from ggplot import *
import pandas as pd
import numpy as np




# Generate data
df = pd.read_csv("baseball-pitches-clean.csv")
df = df[['pitch_time', 'inning', 'pitcher_name', 'hitter_name', 'pitch_type',
         'px', 'pz', 'pitch_name', 'start_speed', 'end_speed', 'type_confidence']]
print df.head()
# print df.dtypes


# Strike "scatterplot"
# print ggplot(df, aes(x='px', y='pz')) + geom_point()

# Basic "histogram"
print ggplot(df, aes(x='start_speed')) + geom_histogram()

# Basic "facet wrap"
# print ggplot(aes(x='start_speed'), data=df) + geom_histogram() + facet_wrap('pitch_name')

# Basic "bar graph"
# print ggplot(aes(x='pitch_type'), data=df) + geom_bar()

# Basic "facet grid"  # This lines up the grid for comparison
# print ggplot(aes(x='start_speed'), data=df) + geom_histogram() + facet_grid('pitch_type')

# Basic  "geom density"  # To compare various categorical frequency's in the same field
# print ggplot(df, aes(x='start_speed')) + geom_density()
# print ggplot(df, aes(x='start_speed', color='pitch_name')) + geom_density()

