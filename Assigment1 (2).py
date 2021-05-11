#!/usr/bin/env python
# coding: utf-8

# # Question no. 5 

# #### Q5.) Part1 - Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[34]:


from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd


# In[3]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page


# In[4]:


soup = BeautifulSoup(page.content)


# In[5]:


team_name1 = soup.find_all('span',class_="u-hide-phablet")


# In[6]:


team_name1


# In[7]:


team_name2 = []
for i in team_name1:
    team_name2.append(i.text)
team_name2


# In[8]:


team_name2 =team_name2[0:10]


# In[9]:


team_name2


# In[10]:


team_matches = soup.find('td',class_="rankings-block__banner--matches")


# In[11]:


team_matches.text            #matches of number 1 team


# In[12]:


#points of number 1 team
point1 = soup.find('td',class_="rankings-block__banner--points")
point1


# In[13]:


point1.text


# In[14]:


team_matches1 = soup.find_all('td',class_="table-body__cell u-center-text")


# In[15]:


team_matches1                    #contains both matches and rating 


# In[16]:


#seperating extra tags
matches1 = []
for i in team_matches1:
    matches1.append(i.text)
matches1


# In[17]:


#separating team points and matches
matches2 = matches1[0:18:2]
points = matches1[1:18:2]


# In[18]:


matches2.insert(0,'37')


# In[19]:


matches2                       #total number of matches


# In[20]:


points.insert(0,'4,455')


# In[21]:


points                #points of all teams


# #### Ratings of teams

# In[22]:


#rating of team at number 1 position
rating1 = soup.find('td',class_= "rankings-block__banner--rating u-text-right")
rating1.text.replace('\n','').replace('                            ','')


# In[23]:


#rating of other teams
rating2 = soup.find_all('td',class_ = "table-body__cell u-text-right rating")
rating2


# In[24]:


#extracting ratings
ratings = []
for i in rating2:
    ratings.append(i.text)
ratings


# In[25]:


#adding all ratings together
ratings.insert(0,'121')


# In[26]:


ratings1 = ratings[0:10]


# In[27]:


ratings1


# In[28]:


Mens_team = pd.DataFrame({})
Mens_team['Team Name'] = team_name2


# In[29]:


Mens_team['Matches'] = matches2
Mens_team['Points'] = points
Mens_team['Ratings'] = ratings1


# In[30]:


Mens_team


# In[31]:


Mens_team.to_csv("Men's top 10 ODI Team.csv",index = False)


# ### Q5.) Part2 - Top 10 ODI Batsmen in men along with the records of their team and rating.

# In[32]:


page2 = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")
page2


# In[33]:


soup1 = BeautifulSoup(page2.content)


# In[34]:


# Batsman name
name1 = soup1.find_all('div', class_ = "rankings-block__banner--name")
name1


# In[35]:


#extracting only batsmen name
name2 = name1[0]
name2.text


# In[36]:


name3 = soup1.find_all('td',class_ ="table-body__cell name")
name3


# In[37]:


player_name = []
for i in name3:
    for j in i.find_all("a"):
        player_name.append(j.text)
player_name                                             #contains names of all player


# In[38]:


Batsman_name = player_name[0:9]


# In[39]:


Batsman_name


# In[40]:


Batsman_name.insert(0,'Babar Azam')


# In[41]:


Batsman_name                     #contains names of all batsman


# In[42]:


#country name
country_name = soup1.find_all('span', class_ = "table-body__logo-text")
country_name


# In[43]:


def extract(category,class_name,main_matrics):
    matrix_name = soup1.find_all(category, class_ = class_name)
    for i in matrix_name:
        main_matrics.append(i.text)
    return main_matrics


# In[44]:


country_name1 = []
country_name_sorted = []
extract('span',"table-body__logo-text",country_name1)


# In[45]:


country_name1


# In[46]:


country_name = country_name1[0:9]
country_name


# In[47]:


#extracting country name of number 1 player
country_name2 = soup1.find('div', class_ ="rankings-block__banner--nationality")
country_name2.text


# In[48]:


c2=country_name2.text.replace('\n','').replace('                            ','').replace('865','')
c2


# In[49]:


country_name.insert(0,c2) 


# In[50]:


country_name                                #all the countries extracted


# In[51]:


#Ratings of the player


# In[52]:


#rating of number first player.
ratings1 = soup1.find('div', class_ ="rankings-block__banner--rating")
rat1 =ratings1.text
rat1                                   


# In[53]:


#ratings of other players
ratings2 = []
extract('td',"table-body__cell u-text-right rating",ratings2)


# In[54]:


#extracting top ten ratings
ratings = ratings2[0:9]
ratings


# In[55]:


#combining all ratings
ratings.insert(0,rat1)


# In[56]:


ratings


# In[57]:


#extracting rankings


# In[58]:


#ranking of number 1 player
rank1 = soup1.find('div',class_ = "rankings-block__banner--pos")
rank2=rank1.text.replace('This player has moved up in the rankings since the previous rankings update','').replace('\n','').replace('                        ','').replace('        ','')


# In[59]:


rank2


# In[60]:


#extracting others rating
ranking1 = soup1.find_all('td',class_ ="table-body__cell table-body__cell--position u-text-right")


# In[61]:


ranking2 = []
for i in ranking1:
    ranking2.append(i.text)
ranking2[0].replace('This player has moved down in the rankings since the previous rankings update\n\n','')


# In[62]:


ranking3 = ranking2[0:9]


# In[63]:


ranking3


# In[64]:


for i in range(0,9):
    ranking3[i] = ranking3[i].replace('This player has moved down in the rankings since the previous rankings update','')


# In[65]:


ranking3


# In[66]:


def filterfunc(elem1,elem2):
    for i in range(0,9):
        ranking3[i] = ranking3[i].replace(elem1,elem2)


# In[67]:


filterfunc('This player has moved up in the rankings since the previous rankings update','')


# In[68]:


ranking3


# In[69]:


filterfunc('\n','')
ranking3


# In[70]:


filterfunc('                                    ','')
ranking3


# In[71]:


filterfunc('        ','')


# In[72]:


ranking3


# In[73]:


ranking3[6] = '8'


# In[74]:


ranking3[8] = '10'


# In[75]:


ranking3


# In[76]:


ranking3.insert(0,rank2)


# In[77]:


ranking3


# In[78]:


ranking = ranking3


# In[79]:


ranking.remove('1')


# In[83]:


ranking.insert(0,'1')


# In[84]:


#creating data frame for batsmen ranking


# In[85]:


Batsmen = pd.DataFrame({})
Batsmen["Rankings"] = ranking
Batsmen["Player Name"] = Batsman_name
Batsmen["Country"] = country_name
Batsmen["Ratings"] = ratings


# In[86]:


Batsmen


# ### Q5.) Part3 - Top 10 ODI Bowlers in men along with the records of their team and rating.

# In[87]:


#players Name


# In[88]:


#extracting only batsmen name
Bowlers_name1 = name1[1]
Bowlers_name1.text


# In[89]:


Bowlers_name = player_name[9:18]


# In[90]:


Bowlers_name


# In[91]:


Bowlers_name.insert(0,Bowlers_name1.text)


# In[92]:


Bowlers_name


# In[93]:


#bowlers name extracted


# In[94]:


#Bowlers Country


# In[95]:


bowlers_country1 = soup1.find_all('div', class_ ="rankings-block__banner--nationality")


# In[96]:


bowlers_count = []
for i in bowlers_country1:
    bowlers_count.append(i.text)
bowlers_count


# In[97]:


bowlers_count1 = bowlers_count[1]


# In[98]:


bowlers_count1=bowlers_count1.replace('\n','').replace('                            ','').replace('737','')
bowlers_count1


# In[99]:


Bowlers_country = country_name1[9:18]
Bowlers_country.insert(0,bowlers_count1)


# In[100]:


Bowlers_country


# In[101]:


#bowlers country extracted


# In[102]:


#Extracting bolwers rating


# In[103]:


bowlers_ratings = ratings2[9:18]
bowlers_ratings


# In[104]:


bowlers_rating1 = soup1.find_all('div', class_ ="rankings-block__banner--rating")
bowlers_rat = []
for i in bowlers_rating1:
    bowlers_rat.append(i.text)
bowlers_rat


# In[105]:


bowlers_rat1 = bowlers_rat[1]
bowlers_rat1


# In[106]:


bowlers_ratings.insert(0,bowlers_rat1)


# In[107]:


bowlers_ratings


# In[108]:


#bowlers rating extracted


# In[109]:


#bowlers ranking


# In[110]:


#ranking of number 1 bowler
rank1_bowler = soup1.find('div',class_ = "rankings-block__banner--pos")
rank2_bowler=rank1_bowler.text.replace('This player has moved up in the rankings since the previous rankings update','').replace('\n','').replace('                        ','').replace('        ','')


# In[111]:


rank2_bowler


# In[112]:


ranking2_bowler = []
for i in ranking1:
    ranking2_bowler.append(i.text)
ranking2_bowler[9:18]


# In[113]:


ranking_bowler = ranking2_bowler[9:18]


# In[114]:


ranking_bowler


# In[115]:


def filterfunc(elem1,elem2):
    for i in range(0,9):
        ranking_bowler[i] = ranking_bowler[i].replace(elem1,elem2)


# In[116]:


filterfunc('This player has moved up in the rankings since the previous rankings update','')


# In[117]:


ranking_bowler


# In[118]:


filterfunc('This player has moved down in the rankings since the previous rankings update','')
ranking_bowler


# In[119]:


filterfunc('\n','')
ranking_bowler


# In[120]:


filterfunc('                                    ','')
filterfunc('        ','')


# In[121]:


ranking_bowler


# In[122]:


ranking_bowler.insert(0,rank2_bowler)


# In[123]:


ranking_bowler


# In[124]:


#creating dataframe for bowlers


# In[125]:


Bowler = pd.DataFrame({})
Bowler["Rankings"] = ranking_bowler
Bowler["Player Name"] = Bowlers_name
Bowler["Country"] = Bowlers_country
Bowler["Ratings"] = bowlers_ratings


# In[126]:


Bowler


# # Question no.6

# ### Q6.) Part1 - Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

# In[128]:


page4 = requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page4


# In[129]:


soupW = BeautifulSoup(page4.content)


# In[130]:


team_name3 = soupW.find_all('span',class_="u-hide-phablet")


# In[131]:


team_name3


# In[132]:


team_name4 = []
for i in team_name3:
    team_name4.append(i.text)
team_name4


# In[133]:


team_name4 =team_name4[0:10]


# In[134]:


team_name4


# In[135]:


team_matchesW = soupW.find('td',class_="rankings-block__banner--matches")


# In[136]:


team_matchesW.text            #matches of number 1 team


# In[137]:


#points of number 1 team
pointW1 = soupW.find('td',class_="rankings-block__banner--points")
pointW1


# In[138]:


pointW1.text


# In[139]:


team_matchesW1 = soupW.find_all('td',class_="table-body__cell u-center-text")


# In[140]:


team_matchesW1                    #contains both matches and rating 


# In[141]:


#seperating extra tags
matchesW1 = []
for i in team_matchesW1:
    matchesW1.append(i.text)
matchesW1


# In[142]:


#separating team points and matches
matchesW2 = matchesW1[0:18:2]
pointsW = matchesW1[1:18:2]


# In[143]:


matchesW2.insert(0,'18')


# In[144]:


matchesW2
pointsW.insert(0,'2955')
pointsW                #points of all teams


# #### Ratings of teams

# In[146]:


#rating of team at number 1 position
ratingW1 = soupW.find('td',class_= "rankings-block__banner--rating u-text-right")
ratingW1.text.replace('\n','').replace('                            ','')


# In[147]:


#rating of other teams
ratingW2 = soupW.find_all('td',class_ = "table-body__cell u-text-right rating")
ratingW2


# In[148]:


#extracting ratings
ratingsW = []
for i in ratingW2:
    ratingsW.append(i.text)
ratingsW


# In[149]:


#adding all ratings together
ratingsW.insert(0,'164')


# In[150]:


ratingsW


# In[151]:


Woman_team = pd.DataFrame({})
Woman_team['Team Name'] = team_name4


# In[152]:


Woman_team['Matches'] = matchesW2
Woman_team['Points'] = pointsW
Woman_team['Ratings'] = ratingsW


# In[153]:


Woman_team


# In[154]:


Woman_team.to_csv("Women's top 10 ODI TeamW.csv",index = False)


# ### Q6.) Part2 - Top 10 women’s ODI players along with the records of their team and rating.

# In[35]:


pageW2 = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
pageW2


# In[36]:


soupW1 = BeautifulSoup(pageW2.content)


# In[38]:


# Batsman name
nameW1 = soupW1.find_all('div', class_ = "rankings-block__banner--name")
nameW1


# In[39]:


#extracting only batsmen name
nameW2 = nameW1[0]
nameW2.text


# In[40]:


nameW3 = soupW1.find_all('td',class_ ="table-body__cell name")
nameW3


# In[41]:


player_nameW = []
for i in nameW3:
    for j in i.find_all("a"):
        player_nameW.append(j.text)
player_nameW        


# In[47]:


np.count_nonzero(player_nameW  )


# In[42]:


Batsman_nameW = player_nameW[0:9]


# In[43]:


Batsman_nameW


# In[44]:


Batsman_nameW.insert(0,nameW2.text)


# In[45]:


Batsman_nameW                     #contains names of all batsman


# In[48]:


#country name
country_nameW = soupW1.find_all('span', class_ = "table-body__logo-text")
country_nameW


# In[49]:


def extract(category,class_name,main_matrics):
    matrix_name = soupW1.find_all(category, class_ = class_name)
    for i in matrix_name:
        main_matrics.append(i.text)
    return main_matrics


# In[50]:


country_nameW1 = []
country_name_sortedW = []
extract('span',"table-body__logo-text",country_nameW1)


# In[51]:


country_nameW1


# In[169]:


country_nameW = country_nameW1[0:9]
country_nameW


# In[170]:


#extracting country name of number 1 player
country_nameW2 = soupW1.find('div', class_ ="rankings-block__banner--nationality")
country_nameW2.text


# In[171]:


c2=country_nameW2.text.replace('\n','').replace('                            ','').replace('765','')
c2


# In[172]:


country_nameW.insert(0,c2) 
country_nameW         


# In[52]:


#rating of number first player.
ratingsW1 = soupW1.find('div', class_ ="rankings-block__banner--rating")
ratW1 =ratingsW1.text
ratW1 


# In[53]:


#ratings of other players
ratingsW2 = []
extract('td',"table-body__cell u-text-right rating",ratingsW2)


# In[175]:


#extracting top ten ratings
ratingsW = ratingsW2[0:9]
ratingsW


# In[176]:


#combining all ratings
ratingsW.insert(0,ratW1)


# In[177]:


ratingsW


# In[178]:


#extracting rankings


# In[179]:


#ranking of number 1 player
rankW1 = soupW1.find('div',class_ = "rankings-block__banner--pos")
rankW2=rankW1.text.replace('This player has moved up in the rankings since the previous rankings update','').replace('\n','').replace('                        ','').replace('        ','')


# In[180]:


rankW2


# In[78]:


#extracting others rating
rankingW1 = soupW1.find_all('td',class_ ="table-body__cell table-body__cell--position u-text-right")


# In[182]:


rankingW2 = []
for i in rankingW1:
    rankingW2.append(i.text)
rankingW2[0].replace('This player has moved down in the rankings since the previous rankings update\n\n','')


# In[183]:


rankingW3 = rankingW2[0:9]


# In[184]:


rankingW3


# In[185]:


for i in range(0,9):
    rankingW3[i] = rankingW3[i].replace('This player has moved down in the rankings since the previous rankings update','')


# In[186]:


rankingW3


# In[54]:


def filterfunc(elem1,elem2):
    for i in range(0,9):
        rankingW3[i] = rankingW3[i].replace(elem1,elem2)


# In[188]:


filterfunc('This player has moved up in the rankings since the previous rankings update','')


# In[189]:


rankingW3


# In[190]:


filterfunc('\n','')
rankingW3
filterfunc('                                    ','')
rankingW3
filterfunc('        ','')


# In[191]:


rankingW3


# In[192]:


rankingW3.insert(0,rankW2)


# In[193]:


rankingW3


# In[194]:


rankingW = rankingW3


# In[195]:


#creating data frame for batsmen ranking


# In[196]:


BatsmenW = pd.DataFrame({})
BatsmenW["Rankings"] = rankingW
BatsmenW["Player Name"] = Batsman_nameW
BatsmenW["Country"] = country_nameW
BatsmenW["Ratings"] = ratingsW


# In[197]:


BatsmenW


# ### Q6.) Part3 - Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[55]:


#extracting allrounders record
Bowlers_nameW1 = nameW1[2]
Bowlers_nameW1.text


# In[58]:


Bowlers_nameW = player_nameW[18:27]


# In[59]:


Bowlers_nameW


# In[60]:


Bowlers_nameW.insert(0,Bowlers_nameW1.text)
Bowlers_nameW


# In[61]:


#Country


# In[62]:


bowlers_countryW1 = soupW1.find_all('div', class_ ="rankings-block__banner--nationality")


# In[63]:


bowlers_countW = []
for i in bowlers_countryW1:
    bowlers_countW.append(i.text)
bowlers_countW


# In[64]:


bowlers_countW1 = bowlers_countW[2]


# In[66]:


bowlers_countW1=bowlers_countW1.replace('\n','').replace('                            ','').replace('418','')
bowlers_countW1


# In[67]:


Bowlers_countryW = country_nameW1[18:27]
Bowlers_countryW.insert(0,bowlers_countW1)


# In[68]:


Bowlers_countryW


# In[69]:


#Extracting all rounder rating


# In[70]:


bowlers_ratingsW = ratingsW2[18:27]
bowlers_ratingsW


# In[71]:


bowlers_ratingW1 = soupW1.find_all('div', class_ ="rankings-block__banner--rating")
bowlers_ratW2 = []
for i in bowlers_ratingW1:
    bowlers_ratW2.append(i.text)
bowlers_ratW2


# In[72]:


bowlers_ratW2 = bowlers_ratW2[2]
bowlers_ratW2


# In[73]:



bowlers_ratingsW.insert(0,bowlers_ratW2)


# In[74]:


bowlers_ratingsW


# In[220]:


#allrounder ranking


# In[75]:


#ranking of number 1 bowler
rank1_bowlerW = soupW1.find('div',class_ = "rankings-block__banner--pos")
rank2_bowlerW=rank1_bowlerW.text.replace('This player has moved up in the rankings since the previous rankings update','').replace('\n','').replace('                        ','').replace('        ','')


# In[76]:


rank2_bowlerW


# In[79]:


ranking2_bowlerW = []
for i in rankingW1:
    ranking2_bowlerW.append(i.text)
ranking2_bowlerW[18:27]


# In[80]:


ranking_bowlerW = ranking2_bowlerW[18:27]


# In[81]:


ranking_bowlerW


# In[82]:


def filterfunc(elem1,elem2):
    for i in range(0,9):
        ranking_bowlerW[i] = ranking_bowlerW[i].replace(elem1,elem2)


# In[83]:


filterfunc('This player has moved up in the rankings since the previous rankings update','')


# In[84]:


ranking_bowlerW


# In[85]:


filterfunc('This player has moved down in the rankings since the previous rankings update','')
ranking_bowlerW


# In[86]:


filterfunc('\n','')
ranking_bowlerW
filterfunc('                                    ','')
filterfunc('        ','')


# In[91]:


ranking_bowlerW


# In[92]:


ranking_bowlerW.insert(0,rank2_bowlerW)
ranking_bowlerW.remove('\xa0\xa0')


# In[94]:


ranking_bowlerW.insert(1,'2')


# In[95]:


BowlerW = pd.DataFrame({})
BowlerW["Rankings"] = ranking_bowlerW
BowlerW["Player Name"] = Bowlers_nameW
BowlerW["Country"] = Bowlers_countryW
BowlerW["Ratings"] = bowlers_ratingsW


# In[96]:


BowlerW


# ## QUESTION No.1

# ### Write a python program to display all the header tags from ‘en.wikipedia.org/wiki/Main_Page’.

# In[241]:


pageT1 = requests.get('https://en.wikipedia.org/wiki/Main_Page')
pageT1


# In[242]:


soupT1 = BeautifulSoup(pageT1.content)


# In[243]:


soupT1


# In[244]:


headingsT1 = soupT1.find_all('h2', class_ = 'mp-h2')
headingsT1


# In[245]:


all_headingsT1 = []
for i in headingsT1:
    all_headingsT1.append(i.text)
all_headingsT1


# In[246]:


headT1 = soupT1.find('h1', class_ = 'firstHeading')


# In[247]:


headT1.text


# In[248]:


all_headingsT1.append(headT1.text)


# In[249]:


all_headingsT1


# In[250]:


all_headingsT1[1] = all_headingsT1[1].replace('\xa0','')


# In[251]:


all_headingsT1


# In[252]:


import pandas as pd


# In[253]:


HeadersT1 = pd.DataFrame({})
HeadersT1["Heading"] = all_headingsT1


# In[254]:


HeadersT1


# # Question no.2 

# ### Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. Name, IMDB rating, Year of release) and save it in form of a CSV file.

# In[255]:


pageIM = requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")
pageIM


# In[256]:


soupIM = BeautifulSoup(pageIM.content)


# In[257]:


soupIM


# In[258]:


titlesIM1 = soupIM.find_all('h3', class_="lister-item-header")
titlesIM1


# In[259]:


movie_titleIM = []
for i in titlesIM1:
    for j in i.find_all("a"):
          movie_titleIM.append(j.text)
movie_titleIM


# In[260]:


ratingsIM1 = soupIM.find_all('strong')
ratingsIM1


# In[261]:


rating_of_moviesIM = []
for i in ratingsIM1:
    rating_of_moviesIM.append(i.text)
rating_of_moviesIM


# In[262]:


yearIM1 = soupIM.find_all('span', class_="lister-item-year text-muted unbold")


# In[263]:


yearIM1


# In[264]:


movie_yearIM1 = []
for i in yearIM1:
    movie_yearIM1.append(i.text)
movie_yearIM1   


# In[265]:


pageIM2 = requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt")
pageIM2


# In[266]:


soupIM1 = BeautifulSoup(pageIM2.content)


# In[267]:


titleIM2 = soupIM1.find_all('h3', class_="lister-item-header")
titleIM2


# In[268]:


for i in titleIM2:
    for j in i.find_all("a"):
          movie_titleIM.append(j.text)
movie_titleIM


# In[269]:


ratingIM2 = soupIM1.find_all("strong")
for i in ratingIM2:
    rating_of_moviesIM.append(i.text)
rating_of_moviesIM


# In[270]:


rating_of_moviesIM.remove('Detailed')


# In[276]:



rating_of_moviesIM.remove('User Rating')
rating_of_moviesIM.remove('User Rating')


# In[277]:


final_ratingIM=rating_of_moviesIM
final_ratingIM


# In[278]:


yearIM2 = soupIM.find_all('span', class_="lister-item-year text-muted unbold")
yearIM2


# In[279]:


yearIM2


# In[280]:


for i in yearIM2:
    movie_yearIM1.append(i.text)
movie_yearIM1   


# In[281]:


def remove_brackets(list_name,e1,e2):
    for i in range(0,100):
        list_name[i] = list_name[i].replace(e1,'').replace(e2,'')
    return list_name


# In[282]:


remove_brackets(movie_yearIM1,'(',')')


# In[283]:


movie_titleIM


# In[284]:


Movie_detailsIM = pd.DataFrame({})
Movie_detailsIM["Movie Name"] = movie_titleIM
Movie_detailsIM["IMDb Rating"] = final_ratingIM
Movie_detailsIM["Year of release"] = movie_yearIM1


# In[285]:


Movie_detailsIM


# In[286]:


Movie_detailsIM.to_csv('IMDb Top 100 MoviesIM.csv', index=False)


# # Question no.3 

# ### Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. Name, IMDB rating, Year of release) and save it in form of a CSV file.

# In[287]:


pageIN = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
pageIN


# In[288]:


soupIN = BeautifulSoup(pageIN.content)


# In[289]:


titlesIN1 = soupIN.find_all('td', class_ = 'titleColumn')
titlesIN1


# In[290]:


movie_titleIN = []
for i in titlesIN1:
    for j in i.find_all("a"):
        movie_titleIN.append(j.text)
movie_titleIN


# In[291]:


ratingsIN = soupIN.find_all('strong')


# In[292]:


rating_of_moviesIN = []
for i in ratingsIN:
    rating_of_moviesIN.append(i.text)
rating_of_moviesIN


# In[293]:


yearIN = soupIN.find_all('span',class_="secondaryInfo")


# In[294]:


movie_year1IN = []
for i in yearIN:
    movie_year1IN.append(i.text)
movie_year1IN 


# In[295]:


#extracting details pf top 100 movies only
movie_title100IN = []
def top_movies(feature_name):
    for i in range(0,100):
        movie_title100IN.append(feature_name[i])
    return movie_title100IN


# In[296]:


movie_rating100IN = []
def top_rating(feature_name):
    for i in range(0,100):
        movie_rating100IN.append(feature_name[i])
    return movie_rating100IN


# In[297]:


movie_year100IN = []
def top_year(feature_name):
    for i in range(0,100):
        movie_year100IN.append(feature_name[i])
    return movie_year100IN


# In[298]:


top_movies(movie_titleIN)


# In[299]:


top_rating(rating_of_moviesIN)


# In[300]:


top_year(movie_year1IN)


# In[301]:


#removing extra brackets from year
def remove_brackets(list_name,e1,e2):
    for i in range(0,100):
        list_name[i] = list_name[i].replace(e1,'').replace(e2,'')
    return list_name


# In[302]:


remove_brackets(movie_year100IN,'(',')')


# In[303]:


# storing into dataframe


# In[304]:


Movie_detailsIN = pd.DataFrame({})
Movie_detailsIN["Movie Name"] = movie_title100IN
Movie_detailsIN["IMDb Rating"] = movie_rating100IN
Movie_detailsIN["Year of release"] = movie_year100IN


# In[305]:


Movie_detailsIN


# In[306]:


Movie_detailsIN.to_csv('Indian Top 100 MoviesIN.csv', index=False)


# # Question no.4 

# ### Write a python program to scrap book name, author name, genre and book review of any 5 books from ‘www.bookpage.com’

# In[307]:


pageBO = requests.get("https://bookpage.com/reviews/26195-rivers-solomon-sorrowland-fiction#.YJJItbUzZPY")
pageBO


# In[308]:


soupBO = BeautifulSoup(pageBO.content)
soupBO


# In[310]:


#first book title
titleBO = soupBO.find('h1',class_="italic")
titleBO.text


# In[311]:


titleS=titleBO.text.replace('\n★ ','').replace('\n','')
titleS


# In[313]:


#first book author name 
author1  = soupBO.find('h4',class_="sans")
author1.text


# In[314]:


authorS = author1.text.replace('\n','')
authorS


# In[315]:


#first book genre
genre1 = soupBO.find('p',class_="genre-links")
genre1.text


# In[316]:


genreS = genre1.text.replace('\n','')
genreS


# In[317]:


#first book review
review1 = soupBO.find('div',class_="article-body")
review1.text


# In[318]:


reviewS = review1.text.replace('\n','')
reviewS


# In[319]:


#Book 2
#title
page1BO = requests.get("https://bookpage.com/reviews/26191-maggie-shipstead-great-circle-fiction#.YJJMrLUzZPY")
page1BO


# In[321]:


soupG = BeautifulSoup(page1BO.content)


# In[322]:


title1G = soupG.find('h1',class_="italic")
title1G.text


# In[323]:


titleG=title1G.text.replace('\n★ ','').replace('\n','')
titleG


# In[326]:


#author
author2  = soupG.find('h4',class_="sans")
author2.text


# In[327]:


authorG = author2.text.replace('\n','')
authorG


# In[328]:


#genre
genre2 = soupG.find('p',class_="genre-links")
genre2.text


# In[329]:


genreG = genre2.text.replace('\n','')
genreG


# In[330]:


#review
review2 = soupG.find('div',class_="article-body")
review2.text


# In[331]:


reviewG = review2.text.replace('\n','').replace("\xa0\nALSO IN BOOKPAGE: Maggie Shipstead may not want to be a pilot, but she can’t help but explore that skyward impulse.",'').replace('\xa0','')
reviewG


# In[332]:


#Book 3
#title
page2G = requests.get("https://bookpage.com/reviews/26201-jhumpa-lahiri-whereabouts-fiction#.YJJxO7UzZPY")
page2G


# In[333]:


soup2G= BeautifulSoup(page2G.content)


# In[334]:


title2G = soup2G.find('h1',class_="italic")
title2G.text


# In[335]:


titleW=title2G.text.replace('\n★ ','').replace('\n','')
titleW


# In[336]:


#author
author3  = soup2G.find('h4',class_="sans")
author3.text


# In[338]:


authorW = author3.text.replace('\n','')
authorW


# In[341]:


#genre
genre3 = soup2G.find('p',class_="genre-links")
genre3.text


# In[342]:


genreW = genre2.text.replace('\n','')
genreW


# In[343]:


#review
review3 = soup2G.find('div',class_="article-body")
review3.text


# In[344]:


reviewW = review3.text.replace('\n','')
reviewW


# In[345]:


#book 4
page4 = requests.get("https://bookpage.com/reviews/26192-fiona-mozley-hot-stew-fiction#.YJJ0zbUzZPY")
page4


# In[346]:


soup4 = BeautifulSoup(page4.content)


# In[347]:


title4 = soup4.find('h1',class_="italic")
title4.text


# In[348]:


titleH=title4.text.replace('\n','')
titleH


# In[349]:


#author
author4  = soup4.find('h4',class_="sans")
author4.text


# In[367]:


authorH = author4.text.replace('\n','')
authorH


# In[350]:


#genre
genre4 = soup4.find('p',class_="genre-links")
genre4.text


# In[351]:


genreH = genre4.text.replace('\n','')
genreH


# In[ ]:





# In[352]:


#review
review4 = soup4.find('div',class_="article-body")
review4.text


# In[353]:


reviewH = review3.text.replace('\n','').replace('\xa0','')
reviewH


# In[354]:


#book 5
page5 = requests.get("https://bookpage.com/reviews/26198-chanel-cleeton-most-beautiful-girl-cuba-fiction#.YJd067UzZPY")
page5


# In[355]:


soup5 = BeautifulSoup(page5.content)


# In[356]:


title5 = soup5.find('h1',class_="italic")
title5.text


# In[357]:


titleTM=title5.text.replace('\n','')
titleTM


# In[358]:


#author
author5  = soup5.find('h4',class_="sans")
author5.text


# In[359]:


authorTM = author5.text.replace('\n','')
authorTM


# In[360]:


#genre
genre5 = soup5.find('p',class_="genre-links")
genre5.text


# In[361]:


genreTM = genre5.text.replace('\n','')
genreTM


# In[362]:


#review
review5 = soup5.find('div',class_="article-body")
review5.text


# In[363]:


reviewTM = review5.text.replace('\n','')
reviewTM


# In[364]:


Titles1 = [titleS,titleG,titleW,titleH,titleTM]


# In[365]:


Titles1


# In[368]:


Author = [authorS,authorG,authorW,authorH,authorTM]


# In[369]:


Genre = [genreS,genreG,genreW,genreH,genreTM]


# In[370]:


Review = [reviewS,reviewG,reviewW,reviewH,reviewTM]


# In[371]:


Books = pd.DataFrame({})


# In[372]:


Books["Title of the Book"] = Titles1
Books["Author Name"] = Author
Books["Book Genre"] = Genre
Books["Book Review"] = Review


# In[373]:


Books


# # QUESTION NO.8

# ### Write a python program to extract information about the local weather from the National Weather Service website of USA, https://www.weather.gov/ for the city, San Francisco. You need to extract data about 7 day extended forecast display for the city. The data should include period, short description, temperature and description.

# In[390]:


pageWE = requests.get("https://forecast.weather.gov/MapClick.php?lon=-122.40731529128576&lat=37.77610140364207#.YJdgFbUzZPa")


# In[391]:


pageWE


# In[392]:


soupWE = BeautifulSoup(pageWE.content)
soupWE


# In[393]:


#extracting period
periodWE1 = soupWE.find_all('div',class_ = 'col-sm-2 forecast-label')


# In[394]:


periodWE = []
for i in periodWE1:
    for j in i.find_all("b"):
        periodWE.append(j.text)
periodWE 


# In[395]:


#all periods extracted


# In[396]:


#short description


# In[397]:


description1 = soupWE.find_all('div',class_ = "col-sm-10 forecast-text")


# In[398]:


description = []
for i in description1:
    description.append(i.text)


# In[399]:


description


# In[400]:


short_description = description.copy()


# In[401]:


short_description


# In[402]:


short_description[0] = short_description[0].replace(', with a high near 77. Light and variable wind becoming west 9 to 14 mph in the morning. Winds could gust as high as 18 mph. ','')


# In[403]:


short_description[1] = short_description[1].replace(', with a low around 52. West wind 6 to 11 mph. ','')


# In[404]:


short_description[2] = short_description[2].replace(', with a high near 76. Light west southwest wind increasing to 11 to 16 mph in the afternoon. Winds could gust as high as 21 mph. ','')


# In[405]:


short_description[3] = short_description[3].replace(', with a low around 51. West wind 9 to 14 mph becoming light west southwest. ','')  


# In[406]:


short_description[4] = short_description[4].replace(', with a high near 69. Light west southwest wind increasing to 8 to 13 mph in the afternoon. ','')


# In[407]:


short_description[5] = short_description[5].replace(', with a low around 51.','')


# In[408]:


short_description[6] = short_description[6].replace(', with a high near 67.','')


# In[409]:


short_description[7] = short_description[7].replace(', with a low around 50.','')


# In[411]:


short_description[8] = short_description[8].replace(', with a high near 64.','')


# In[412]:


short_description[9] = short_description[9].replace(', with a low around 50.','')


# In[413]:


short_description[10] = short_description[10].replace(', with a high near 63.','')


# In[414]:


short_description[11] = short_description[11].replace(', with a low around 51.','')


# In[415]:


short_description[12] = short_description[12].replace(', with a high near 64.','')


# In[416]:


short_description


# In[417]:


#lower temperature
temperature= description.copy()


# In[418]:


temperature


# In[419]:


temperature[0] = temperature[0].replace('Sunny, with a ','').replace('near ','').replace('. Light and variable wind becoming west 9 to 14 mph in the morning. Winds could gust as high as 18 mph. ','')


# In[420]:


temperature[1] = temperature[1].replace('Mostly clear, with a ','').replace('around ','').replace('. West wind 6 to 11 mph. ','')


# In[422]:


temperature[2] = temperature[2].replace('Sunny, with a ','').replace('near ','').replace('. Light west southwest wind increasing to 11 to 16 mph in the afternoon. Winds could gust as high as 21 mph. ','')


# In[423]:


temperature[3] = temperature[3].replace('Mostly clear, with a ','').replace(' around','').replace('. West wind 9 to 14 mph becoming light west southwest. ','')


# In[424]:


temperature[4] = temperature[4].replace('Sunny, with a ','').replace('near ','').replace('. Light west southwest wind increasing to 8 to 13 mph in the afternoon. ','')


# In[425]:


temperature[5] = temperature[5].replace('Partly cloudy, with a ','').replace('around ','')


# In[426]:


temperature[6] = temperature[6].replace('Mostly sunny, with a ','').replace('near ','')


# In[427]:


temperature[7] = temperature[7].replace('Partly cloudy, with a ','').replace('around ','')


# In[428]:


temperature[8] = temperature[8].replace('Mostly sunny, with a ','').replace('near ','')


# In[429]:


temperature[9] = temperature[9].replace('Partly cloudy, with a ','').replace('around ','')


# In[430]:


temperature[10] = temperature[10].replace('Mostly sunny, with a ','').replace('near ','')


# In[435]:


temperature[11] = temperature[11].replace('low 50','low 51')


# In[433]:


temperature[12] = temperature[12].replace('Mostly sunny, with a ','').replace('near ','')


# In[436]:


temperature


# In[443]:


for i in range(5,13):
    temperature[i] = temperature[i].replace('.','')


# In[444]:


temperature


# In[445]:


Forecast1 = pd.DataFrame({})


# In[448]:


Forecast1["Period(From 9pm ,8th May)"] = periodWE
Forecast1["Short Description"] = short_description
Forecast1["Temperature (in Fahrenheit)"] = temperature
Forecast1["Detailed Description"] = description


# In[449]:


Forecast1


# # QUESTION NO.7

# ### Write a python program to scrape details of all the mobile phones under Rs. 20,000 listed on Amazon.in. The scraped data should include Product Name, Price, Image URL and Average Rating.

# In[8]:


pagear = requests.get("https://www.amazon.in/s?k=mobile+phone+under+20000+rupees&crid=17NMLVPARRUAF&sprefix=mobile+phone+under+20%2Caps%2C382&ref=nb_sb_ss_ts-doa-p_1_21")


# In[9]:


pagear


# In[10]:


soupaz = BeautifulSoup(pagear.content)


# In[11]:


soupaz


# In[12]:


names1A = soupaz.find_all('span',class_ = "a-size-medium a-color-base a-text-normal")
names1A


# In[13]:


phone_namesA = []
for i in names1A:
        phone_namesA.append(i.text)
phone_namesA


# In[15]:


#extracting prices
priceA = soupaz.find_all('span',class_ ="a-price-whole")
priceA


# In[17]:


phone_priceA = []
for i in priceA:
        phone_priceA.append(i.text)
phone_priceA


# In[18]:


phone_price1A = phone_priceA[4:20]


# In[19]:


phone_price1A


# In[20]:


#extracting ratings
ratingsA = soupaz.find_all('span',class_ ="a-icon-alt")
ratingsA


# In[21]:


ratings1A = []
for i in ratingsA:
    ratings1A.append(i.text)
ratings1A


# In[23]:


phone_ratingsA = ratings1A[0:20]


# In[24]:


phone_ratings1A = phone_ratingsA[4:20]
phone_ratings1A


# In[26]:


#image link
imagesA = soupaz.find_all('img')
imagesA


# In[27]:


image_link1A = []
for i in imagesA:
    link = i['src']
    image_link1A.append(link)
image_link1A


# In[28]:


image_linkA = image_link1A[3:23]


# In[29]:


image_link2A = image_linkA[4:20]


# In[30]:


image_link2A


# In[31]:


Amazon_phones_list = pd.DataFrame({})


# In[32]:


Amazon_phones_list["Phone Name"] = phone_namesA
Amazon_phones_list["Price of phone"] = phone_price1A
Amazon_phones_list["Ratings of phone"] = phone_ratings1A
Amazon_phones_list["Image link"] = image_link2A


# In[33]:


Amazon_phones_list


# In[ ]:




