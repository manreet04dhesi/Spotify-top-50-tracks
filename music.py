import numpy as np #for arrays
import pandas as pd #for manipulating data
import seaborn as sns #for visualization
import matplotlib.pyplot as plt #for the main set-up
from matplotlib.pyplot import figure
import plotly.express as px #easier code

#reading csv file
dt1 = pd.read_csv('spotifytoptracks.csv')

print(dt1.columns)

#Artist analysis: which singer had the most songs reach the top 50
song_count = px.histogram(dt1,x='artist',color='artist',text_auto='3s')
song_count.show()

#Genre analysis: what genre apeared the most in the top 50
genre_count = px.histogram(dt1, x='genre',color='genre',text_auto='3s')
genre_count.show()

#sorting the genres into the 6 main genres
main_genre = {'R&B/Soul':'R&B' , 'Alternative/Indie':'Alternative' , 'Hip-Hop/Rap':'Rap' , 'Dance/Electronic':'Electronic' ,
'Nu-disco':'Disco' , 'R&B/Hip-Hop alternative':'R&B' , 'Pop/Soft Rock':'Pop' , 'Pop':'Pop' , 'Pop rap':'Rap' , ' Electro-pop':'Electronic' ,
'Dance-pop/Disco':'Disco' , 'Disco-pop':'Disco' , 'Dreampop/Hip-Hop/R&B':'R&B' , 'Alternative/reggaeton/experimental':'Alternative' ,
'Chamber pop':'Pop' , 'Hip-Hop/Trap':'Rap'}

dt1['Main_Genre'] = dt1['genre'].apply(lambda x: main_genre[x])

#analysis of the 6 main genres
main = px.histogram(dt1,x='Main_Genre',color='Main_Genre',text_auto='3s',title='6 Main Genres Analysis')
main.show()

#sorting each artist into gender category
gender = {'The Weeknd':'Male' , 'Tones And I':'Female' , 'Roddy Ricch':'Male' , 'SAINt JHN':'Male' , 'Dua Lipa':'Female' , 'DaBaby':'Male' ,
 'Harry Styles':'Male', 'Powfu':'Male' , 'Trevor Daniel':'Male' , 'Lewis Capaldi':'Male' , 'KAROL G':'Male' , 'Arizona Zervas':'Male' ,
 'Post Malone':'Male' , 'Lil Mosey':'Male' , 'Justin Bieber':'Male' , 'Drake':'Male' , 'Doja Cat':'Female' , 'Maroon 5':'Group' , 'Future':'Male' ,
 'Jawsh 685':'Male' , 'Topic':'Male' , '24kGoldn':'Male' , 'Shawn Mendes':'Male' , 'Billie Eilish':'Female' , 'Cardi B':'Female' , 'Surfaces':'Group' ,
 'Eminem':'Male' , 'BTS':'Group' , 'BENEE':'Female' , 'Surf Mesa':'Male' , 'Lady Gaga':'Female' , 'Travis Scott':'Male' , 'Maluma':'Male' , 'Regard':'Male' ,
 'Black Eyed Peas':'Group' , 'THE SCOTTS':'Group' , 'Bad Bunny':'Male' , 'Juice WRLD':'Male' , 'Ariana Grande':'Female' , 'JP Saxe':'Male'}

dt1['Artist_Gender'] = dt1['artist'].apply(lambda x: gender[x])

#Gender analysis: Which gender was more dominant in the top 50
gender_count = px.histogram(dt1,x='Artist_Gender',color='Artist_Gender',text_auto='3s',title='Artist Gender analysis')
gender_count.show()

#to analyze the Dependence danceability has on the loudness of the song
plt.figure(figsize=(10,8))
sns.scatterplot(x='danceability', y='loudness', data=dt1, color='mediumpurple')
plt.title('Dependence Between Danceability And loudness', fontsize = 20)
plt.show()

#to analyze the spread between artist gender and the presence of words spoken in a song
scatter = px.scatter_polar(dt1,theta='Artist_Gender',r='speechiness',color ='speechiness',title='Spread of different Artist gender according length')
scatter.show()

#to analyze the spread between the genre of music and the danceability of the song
mix = px.scatter_polar(dt1,theta='Main_Genre',r='danceability',color ='danceability',title='Spread of main genres according to the danceability')
mix.show()
