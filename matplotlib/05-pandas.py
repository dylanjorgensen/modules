import pandas as pd
import matplotlib.pyplot as plt



# Generate a pandas dataframe
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
df = pd.DataFrame(data)

# Step2: Instantiate a figure
fig = plt.figure()

# Step3: Best practice is to do all your work inside a subplot
axes = fig.add_subplot(111) # The 111 defines we are working with 1 chart

# Step4: Plot our data in our subplot
axes.plot(df['wins'], df['losses'])

# Step5: Generate graph
plt.show()