
import pandas as pd 
import matplotlib.pyplot as plt 


netflix_csv = pd.read_csv("/Users/nandhinivijayakumar/Desktop/Github_Projects/Netflix/archive (13)/netflix_data.csv")

netflix_subset = netflix_csv.loc[~(netflix_csv['type']=='TV Show')]
netflix_df = netflix_subset[["genre", "release_year", "duration", "type"]]
#print(netflix_df['genre'].unique())
short_movies = netflix_df.loc[netflix_df["duration"]<60]
colors=[]
print(netflix_df)
for movies in netflix_df.itertuples():
    genre_clr = movies.genre
    if  genre_clr=='Children':
        colors.append('Blue')
    elif genre_clr=='Documentaries':
        colors.append('Brown')
    elif genre_clr=='Anime Features':
        colors.append('Red')
    else:
        colors.append('Black')
    
fig = plt.figure()
plt.scatter(x='release_year',y= 'duration', data = netflix_df, color= colors )
plt.xlabel('Release Year')
plt.ylabel('Duration')
plt.title('Year of Release and the Movie Duration ')
plt.show()
plt.close()

   
    






