### Required Imports for Web Scraping And Converting To DataFrame


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bs4
from bs4 import BeautifulSoup
import requests
```

### Load the content using reuqests module convert it to html readable


```python
page = requests.get("https://www.imdb.com/search/title/?sort=num_votes,desc&start=1&title_type=feature&year=1950,2012")
contents = page.content
```

### Create a Static Html file of the same to use later and store it


```python
print(type(contents))
with open('IMDB_Movies_HTML_Page.html','ab') as fb:
    fb.write(contents)
```

    <class 'bytes'>
    

### Parse content using BeautifulSoup4's html.parse


```python
soup = BeautifulSoup(contents,"html.parser")
```

### Clean the data by removing unneccessary html tags and create dictionary to store data


```python
### Data_Clean_Soup=soup.find_all("div","lister-item mode-advanced")
Dict_Of_IMDB_Data = { 'Movie_Name' : [0,],'Duration_Minute':[0,],'Genre':[0,],'Rating':[0,],"Text":[0,],'Directores':[0,],'Stars_Heroes':[0,],'User_Votes':[0,],'Gross_In_Million':[0,]}
Dict_Of_IMDB_Data
```

### Use find_all or find to get required data from the parser


```python
#Data_Clean_Soup[0].find_all('a')[1].string                                  Movie Name
#Data_Clean_Soup[0].find_all('a')[13].string                                 Director
#Data_Clean_Soup[0].find_all('a')[14:]                                       all the heroes who worked in movie
#Data_Clean_Soup[0].find("span","runtime").string[:-4]                       duration
#Data_Clean_Soup[0].find("span","genre").string.strip('\n ')                 genre
#Data_Clean_Soup[0].find("span","value").string                              Rating
#Data_Clean_Soup[0].find_all('p')[1].string.strip('\n ')                     Text
#Data_Clean_Soup[0].find_all('span')[-4].string                              Vote
#Data_Clean_Soup[0].find_all('span')[-1].string[:-1]                         gross
#{ 'Movie_Name' : [],'Duration_Minute':[],'genre':[],'rating':[],"Text":[],'Directores':[],'Stars_Heroes':[],'User_Votes':[],'Gross_In_Million':[]}
```

### Convert Data to the List to Save in Dictionary


```python
Movie=[]
Genre=[]
Rating=[]
Text=[]
Directores=[]
User_Vote=[]
Gross=[]
Duration=[]
Stars=[]
get=[]
try:
    for i in range(len(Data_Clean_Soup)):
        get=i
        Movie.append(Data_Clean_Soup[i].find_all('a')[1].string)
        Genre.append(Data_Clean_Soup[i].find("span","genre").string.strip())
        Duration.append(Data_Clean_Soup[i].find("span","runtime").string[:-4])
        Rating.append(Data_Clean_Soup[i].find("span","value").string)
        Text.append(Data_Clean_Soup[i].find_all('p')[1].find(text=True).strip())
        Directores.append(Data_Clean_Soup[i].find_all('a')[13].string)
        User_Vote.append(Data_Clean_Soup[i].find_all('span')[-4].string)
        Gross.append(Data_Clean_Soup[i].find_all('span')[-1].string[:-1])
        list_actor =[]
        total_list = Data_Clean_Soup[i].find_all('a')[14:]
        for i in total_list:
            list_actor.append(i.string)
        Stars.append(','.join(list_actor))
except:
    print("Get Error on Line with Data index : ",get)
        
```

### Add data to the Dictionary


```python
Dict_Of_IMDB_Data['Movie_Name']=Movie
Dict_Of_IMDB_Data['Genre'] = Genre
Dict_Of_IMDB_Data['Duration_Minute'] =Duration
Dict_Of_IMDB_Data['Rating'] = Rating
Dict_Of_IMDB_Data['Text'] = Text
Dict_Of_IMDB_Data['Directores'] = Directores
Dict_Of_IMDB_Data['User_Votes'] = User_Vote
Dict_Of_IMDB_Data['Gross_In_Million'] = Gross
Dict_Of_IMDB_Data['Stars_Heroes']= Stars
```

### Create DataFrame Using Pandas 


```python
IMDB_Movie_Data = pd.DataFrame(Dict_Of_IMDB_Data)
IMDB_Movie_Data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Movie_Name</th>
      <th>Duration_Minute</th>
      <th>Genre</th>
      <th>Rating</th>
      <th>Text</th>
      <th>Directores</th>
      <th>Stars_Heroes</th>
      <th>User_Votes</th>
      <th>Gross_In_Million</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>The Shawshank Redemption</td>
      <td>142</td>
      <td>Drama</td>
      <td>9.3</td>
      <td>Two imprisoned men bond over a number of years...</td>
      <td>Frank Darabont</td>
      <td>Tim Robbins,Morgan Freeman,Bob Gunton,William ...</td>
      <td>2,244,893</td>
      <td>$28.34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>The Dark Knight</td>
      <td>152</td>
      <td>Action, Crime, Drama</td>
      <td>9</td>
      <td>When the menace known as the Joker wreaks havo...</td>
      <td>Christopher Nolan</td>
      <td>Christian Bale,Heath Ledger,Aaron Eckhart,Mich...</td>
      <td>2,213,479</td>
      <td>$534.86</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Inception</td>
      <td>148</td>
      <td>Action, Adventure, Sci-Fi</td>
      <td>8.8</td>
      <td>A thief who steals corporate secrets through t...</td>
      <td>Christopher Nolan</td>
      <td>Leonardo DiCaprio,Joseph Gordon-Levitt,Ellen P...</td>
      <td>1,967,796</td>
      <td>$292.58</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Fight Club</td>
      <td>139</td>
      <td>Drama</td>
      <td>8.8</td>
      <td>An insomniac office worker and a devil-may-car...</td>
      <td>David Fincher</td>
      <td>Brad Pitt,Edward Norton,Meat Loaf,Zach Grenier</td>
      <td>1,785,608</td>
      <td>$37.03</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Pulp Fiction</td>
      <td>154</td>
      <td>Crime, Drama</td>
      <td>8.9</td>
      <td>The lives of two mob hitmen, a boxer, a gangst...</td>
      <td>Quentin Tarantino</td>
      <td>John Travolta,Uma Thurman,Samuel L. Jackson,Br...</td>
      <td>1,758,151</td>
      <td>$107.93</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Forrest Gump</td>
      <td>142</td>
      <td>Drama, Romance</td>
      <td>8.8</td>
      <td>The presidencies of Kennedy and Johnson, the e...</td>
      <td>Robert Zemeckis</td>
      <td>Tom Hanks,Robin Wright,Gary Sinise,Sally Field</td>
      <td>1,731,046</td>
      <td>$330.25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>The Matrix</td>
      <td>136</td>
      <td>Action, Sci-Fi</td>
      <td>8.7</td>
      <td>A computer hacker learns from mysterious rebel...</td>
      <td>Lana Wachowski</td>
      <td>Lilly Wachowski,Keanu Reeves,Laurence Fishburn...</td>
      <td>1,610,651</td>
      <td>$171.48</td>
    </tr>
    <tr>
      <th>7</th>
      <td>The Lord of the Rings: The Fellowship of the Ring</td>
      <td>178</td>
      <td>Action, Adventure, Drama</td>
      <td>8.8</td>
      <td>A meek Hobbit from the Shire and eight compani...</td>
      <td>Peter Jackson</td>
      <td>Elijah Wood,Ian McKellen,Orlando Bloom,Sean Bean</td>
      <td>1,599,880</td>
      <td>$315.54</td>
    </tr>
    <tr>
      <th>8</th>
      <td>The Lord of the Rings: The Return of the King</td>
      <td>201</td>
      <td>Adventure, Drama, Fantasy</td>
      <td>8.9</td>
      <td>Gandalf and Aragorn lead the World of Men agai...</td>
      <td>Peter Jackson</td>
      <td>Elijah Wood,Viggo Mortensen,Ian McKellen,Orlan...</td>
      <td>1,586,333</td>
      <td>$377.85</td>
    </tr>
    <tr>
      <th>9</th>
      <td>The Godfather</td>
      <td>175</td>
      <td>Crime, Drama</td>
      <td>9.2</td>
      <td>The aging patriarch of an organized crime dyna...</td>
      <td>Francis Ford Coppola</td>
      <td>Marlon Brando,Al Pacino,James Caan,Diane Keaton</td>
      <td>1,548,695</td>
      <td>$134.97</td>
    </tr>
    <tr>
      <th>10</th>
      <td>The Dark Knight Rises</td>
      <td>164</td>
      <td>Action, Adventure</td>
      <td>8.4</td>
      <td>Eight years after the Joker's reign of anarchy...</td>
      <td>Christopher Nolan</td>
      <td>Christian Bale,Tom Hardy,Anne Hathaway,Gary Ol...</td>
      <td>1,463,652</td>
      <td>$448.14</td>
    </tr>
    <tr>
      <th>11</th>
      <td>The Lord of the Rings: The Two Towers</td>
      <td>179</td>
      <td>Adventure, Drama, Fantasy</td>
      <td>8.7</td>
      <td>While Frodo and Sam edge closer to Mordor with...</td>
      <td>Peter Jackson</td>
      <td>Elijah Wood,Ian McKellen,Viggo Mortensen,Orlan...</td>
      <td>1,433,177</td>
      <td>$342.55</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Se7en</td>
      <td>127</td>
      <td>Crime, Drama, Mystery</td>
      <td>8.6</td>
      <td>Two detectives, a rookie and a veteran, hunt a...</td>
      <td>David Fincher</td>
      <td>Morgan Freeman,Brad Pitt,Kevin Spacey,Andrew K...</td>
      <td>1,381,800</td>
      <td>$100.13</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Django Unchained</td>
      <td>165</td>
      <td>Drama, Western</td>
      <td>8.4</td>
      <td>With the help of a German bounty hunter, a fre...</td>
      <td>Quentin Tarantino</td>
      <td>Jamie Foxx,Christoph Waltz,Leonardo DiCaprio,K...</td>
      <td>1,298,785</td>
      <td>$162.81</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Gladiator</td>
      <td>155</td>
      <td>Action, Adventure, Drama</td>
      <td>8.5</td>
      <td>A former Roman General sets out to exact venge...</td>
      <td>Ridley Scott</td>
      <td>Russell Crowe,Joaquin Phoenix,Connie Nielsen,O...</td>
      <td>1,291,102</td>
      <td>$187.71</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Batman Begins</td>
      <td>140</td>
      <td>Action, Adventure</td>
      <td>8.2</td>
      <td>After training with his mentor, Batman begins ...</td>
      <td>Christopher Nolan</td>
      <td>Christian Bale,Michael Caine,Ken Watanabe,Liam...</td>
      <td>1,262,994</td>
      <td>$206.85</td>
    </tr>
    <tr>
      <th>16</th>
      <td>The Avengers</td>
      <td>143</td>
      <td>Action, Adventure, Sci-Fi</td>
      <td>8</td>
      <td>Earth's mightiest heroes must come together an...</td>
      <td>Joss Whedon</td>
      <td>Robert Downey Jr.,Chris Evans,Scarlett Johanss...</td>
      <td>1,232,323</td>
      <td>$623.28</td>
    </tr>
    <tr>
      <th>17</th>
      <td>The Silence of the Lambs</td>
      <td>118</td>
      <td>Crime, Drama, Thriller</td>
      <td>8.6</td>
      <td>A young F.B.I. cadet must receive the help of ...</td>
      <td>Jonathan Demme</td>
      <td>Jodie Foster,Anthony Hopkins,Lawrence A. Bonne...</td>
      <td>1,215,532</td>
      <td>$130.74</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Inglourious Basterds</td>
      <td>153</td>
      <td>Adventure, Drama, War</td>
      <td>8.3</td>
      <td>In Nazi-occupied France during World War II, a...</td>
      <td>Quentin Tarantino</td>
      <td>Brad Pitt,Diane Kruger,Eli Roth,Mélanie Laurent</td>
      <td>1,211,659</td>
      <td>$120.54</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Star Wars</td>
      <td>121</td>
      <td>Action, Adventure, Fantasy</td>
      <td>8.6</td>
      <td>Luke Skywalker joins forces with a Jedi Knight...</td>
      <td>George Lucas</td>
      <td>Mark Hamill,Harrison Ford,Carrie Fisher,Alec G...</td>
      <td>1,192,196</td>
      <td>$322.74</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Saving Private Ryan</td>
      <td>169</td>
      <td>Drama, War</td>
      <td>8.6</td>
      <td>Following the Normandy Landings, a group of U....</td>
      <td>Steven Spielberg</td>
      <td>Tom Hanks,Matt Damon,Tom Sizemore,Edward Burns</td>
      <td>1,187,343</td>
      <td>$216.54</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Schindler's List</td>
      <td>195</td>
      <td>Biography, Drama, History</td>
      <td>8.9</td>
      <td>In German-occupied Poland during World War II,...</td>
      <td>Oskar Schindler</td>
      <td>Steven Spielberg,Liam Neeson,Ralph Fiennes,Ben...</td>
      <td>1,166,863</td>
      <td>$96.90</td>
    </tr>
    <tr>
      <th>22</th>
      <td>The Departed</td>
      <td>151</td>
      <td>Crime, Drama, Thriller</td>
      <td>8.5</td>
      <td>An undercover cop and a mole in the police att...</td>
      <td>Martin Scorsese</td>
      <td>Leonardo DiCaprio,Matt Damon,Jack Nicholson,Ma...</td>
      <td>1,144,356</td>
      <td>$132.38</td>
    </tr>
    <tr>
      <th>23</th>
      <td>The Prestige</td>
      <td>130</td>
      <td>Drama, Mystery, Sci-Fi</td>
      <td>8.5</td>
      <td>After a tragic accident, two stage magicians e...</td>
      <td>Christopher Nolan</td>
      <td>Christian Bale,Hugh Jackman,Scarlett Johansson...</td>
      <td>1,137,253</td>
      <td>$53.09</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Star Wars: Episode V - The Empire Strikes Back</td>
      <td>124</td>
      <td>Action, Adventure, Fantasy</td>
      <td>8.7</td>
      <td>After the Rebels are brutally overpowered by t...</td>
      <td>Irvin Kershner</td>
      <td>Mark Hamill,Harrison Ford,Carrie Fisher,Billy ...</td>
      <td>1,119,676</td>
      <td>$290.48</td>
    </tr>
    <tr>
      <th>25</th>
      <td>The Green Mile</td>
      <td>189</td>
      <td>Crime, Drama, Fantasy</td>
      <td>8.6</td>
      <td>The lives of guards on Death Row are affected ...</td>
      <td>Frank Darabont</td>
      <td>Tom Hanks,Michael Clarke Duncan,David Morse,Bo...</td>
      <td>1,094,554</td>
      <td>$136.80</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Avatar</td>
      <td>162</td>
      <td>Action, Adventure, Fantasy</td>
      <td>7.8</td>
      <td>A paraplegic Marine dispatched to the moon Pan...</td>
      <td>James Cameron</td>
      <td>Sam Worthington,Zoe Saldana,Sigourney Weaver,M...</td>
      <td>1,092,654</td>
      <td>$760.51</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Memento</td>
      <td>113</td>
      <td>Mystery, Thriller</td>
      <td>8.4</td>
      <td>A man with short-term memory loss attempts to ...</td>
      <td>Christopher Nolan</td>
      <td>Guy Pearce,Carrie-Anne Moss,Joe Pantoliano,Mar...</td>
      <td>1,084,904</td>
      <td>$25.54</td>
    </tr>
    <tr>
      <th>28</th>
      <td>The Godfather: Part II</td>
      <td>202</td>
      <td>Crime, Drama</td>
      <td>9</td>
      <td>The early life and career of Vito Corleone in ...</td>
      <td>Francis Ford Coppola</td>
      <td>Al Pacino,Robert De Niro,Robert Duvall,Diane K...</td>
      <td>1,082,627</td>
      <td>$57.30</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Shutter Island</td>
      <td>138</td>
      <td>Mystery, Thriller</td>
      <td>8.1</td>
      <td>In 1954, a U.S. Marshal investigates the disap...</td>
      <td>Martin Scorsese</td>
      <td>Leonardo DiCaprio,Emily Mortimer,Mark Ruffalo,...</td>
      <td>1,079,456</td>
      <td>$128.01</td>
    </tr>
    <tr>
      <th>30</th>
      <td>American Beauty</td>
      <td>122</td>
      <td>Drama</td>
      <td>8.3</td>
      <td>A sexually frustrated suburban father has a mi...</td>
      <td>Sam Mendes</td>
      <td>Kevin Spacey,Annette Bening,Thora Birch,Wes Be...</td>
      <td>1,038,720</td>
      <td>$130.10</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Titanic</td>
      <td>194</td>
      <td>Drama, Romance</td>
      <td>7.8</td>
      <td>A seventeen-year-old aristocrat falls in love ...</td>
      <td>James Cameron</td>
      <td>Leonardo DiCaprio,Kate Winslet,Billy Zane,Kath...</td>
      <td>1,011,743</td>
      <td>$659.33</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Back to the Future</td>
      <td>116</td>
      <td>Adventure, Comedy, Sci-Fi</td>
      <td>8.5</td>
      <td>Marty McFly, a 17-year-old high school student...</td>
      <td>Robert Zemeckis</td>
      <td>Michael J. Fox,Christopher Lloyd,Lea Thompson,...</td>
      <td>1,005,323</td>
      <td>$210.61</td>
    </tr>
    <tr>
      <th>33</th>
      <td>American History X</td>
      <td>119</td>
      <td>Drama</td>
      <td>8.5</td>
      <td>A former neo-nazi skinhead tries to prevent hi...</td>
      <td>Tony Kaye</td>
      <td>Edward Norton,Edward Furlong,Beverly D'Angelo,...</td>
      <td>1,003,012</td>
      <td>$6.72</td>
    </tr>
    <tr>
      <th>34</th>
      <td>V for Vendetta</td>
      <td>132</td>
      <td>Action, Drama, Sci-Fi</td>
      <td>8.2</td>
      <td>In a future British tyranny, a shadowy freedom...</td>
      <td>James McTeigue</td>
      <td>Hugo Weaving,Natalie Portman,Rupert Graves,Ste...</td>
      <td>997,400</td>
      <td>$70.51</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Pirates of the Caribbean: The Curse of the Bla...</td>
      <td>143</td>
      <td>Action, Adventure, Fantasy</td>
      <td>8</td>
      <td>Blacksmith Will Turner teams up with eccentric...</td>
      <td>Gore Verbinski</td>
      <td>Johnny Depp,Geoffrey Rush,Orlando Bloom,Keira ...</td>
      <td>994,419</td>
      <td>$305.41</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Léon</td>
      <td>110</td>
      <td>Action, Crime, Drama</td>
      <td>8.5</td>
      <td>Mathilda, a 12-year-old girl, is reluctantly t...</td>
      <td>Luc Besson</td>
      <td>Jean Reno,Gary Oldman,Natalie Portman,Danny Ai...</td>
      <td>993,702</td>
      <td>$19.50</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Goodfellas</td>
      <td>146</td>
      <td>Biography, Crime, Drama</td>
      <td>8.7</td>
      <td>The story of</td>
      <td>Henry Hill</td>
      <td>Martin Scorsese,Robert De Niro,Ray Liotta,Joe ...</td>
      <td>976,570</td>
      <td>$46.84</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Kill Bill: Vol. 1</td>
      <td>111</td>
      <td>Action, Crime, Thriller</td>
      <td>8.1</td>
      <td>After awakening from a four-year coma, a forme...</td>
      <td>Quentin Tarantino</td>
      <td>Uma Thurman,David Carradine,Daryl Hannah,Micha...</td>
      <td>965,343</td>
      <td>$70.10</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Terminator 2: Judgment Day</td>
      <td>137</td>
      <td>Action, Sci-Fi</td>
      <td>8.5</td>
      <td>A cyborg, identical to the one who failed to k...</td>
      <td>James Cameron</td>
      <td>Arnold Schwarzenegger,Linda Hamilton,Edward Fu...</td>
      <td>964,096</td>
      <td>$204.84</td>
    </tr>
    <tr>
      <th>40</th>
      <td>WALL·E</td>
      <td>98</td>
      <td>Animation, Adventure, Family</td>
      <td>8.4</td>
      <td>In the distant future, a small waste-collectin...</td>
      <td>Andrew Stanton</td>
      <td>Ben Burtt,Elissa Knight,Jeff Garlin,Fred Willard</td>
      <td>963,143</td>
      <td>$223.81</td>
    </tr>
    <tr>
      <th>41</th>
      <td>The Usual Suspects</td>
      <td>106</td>
      <td>Crime, Mystery, Thriller</td>
      <td>8.5</td>
      <td>A sole survivor tells of the twisty events lea...</td>
      <td>Bryan Singer</td>
      <td>Kevin Spacey,Gabriel Byrne,Chazz Palminteri,St...</td>
      <td>957,047</td>
      <td>$23.34</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Braveheart</td>
      <td>178</td>
      <td>Biography, Drama, History</td>
      <td>8.3</td>
      <td>When his secret bride is executed for assaulti...</td>
      <td>Mel Gibson</td>
      <td>Mel Gibson,Sophie Marceau,Patrick McGoohan,Ang...</td>
      <td>933,060</td>
      <td>$75.60</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Star Wars: Episode VI - Return of the Jedi</td>
      <td>131</td>
      <td>Action, Adventure, Fantasy</td>
      <td>8.3</td>
      <td>After a daring mission to rescue Han Solo from...</td>
      <td>Richard Marquand</td>
      <td>Mark Hamill,Harrison Ford,Carrie Fisher,Billy ...</td>
      <td>918,129</td>
      <td>$309.13</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Finding Nemo</td>
      <td>100</td>
      <td>Animation, Adventure, Comedy</td>
      <td>8.1</td>
      <td>After his son is captured in the Great Barrier...</td>
      <td>Andrew Stanton</td>
      <td>Lee Unkrich,Albert Brooks,Ellen DeGeneres,Alex...</td>
      <td>918,050</td>
      <td>$380.84</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Iron Man</td>
      <td>126</td>
      <td>Action, Adventure, Sci-Fi</td>
      <td>7.9</td>
      <td>After being held captive in an Afghan cave, bi...</td>
      <td>Jon Favreau</td>
      <td>Robert Downey Jr.,Gwyneth Paltrow,Terrence How...</td>
      <td>912,090</td>
      <td>$318.41</td>
    </tr>
    <tr>
      <th>46</th>
      <td>The Lion King</td>
      <td>88</td>
      <td>Animation, Adventure, Drama</td>
      <td>8.5</td>
      <td>A lion cub prince is tricked by a treacherous ...</td>
      <td>Roger Allers</td>
      <td>Rob Minkoff,Matthew Broderick,Jeremy Irons,Jam...</td>
      <td>905,116</td>
      <td>$422.78</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Up</td>
      <td>96</td>
      <td>Animation, Adventure, Comedy</td>
      <td>8.2</td>
      <td>78-year-old Carl Fredricksen travels to Paradi...</td>
      <td>Pete Docter</td>
      <td>Bob Peterson,Edward Asner,Jordan Nagai,John Ra...</td>
      <td>900,381</td>
      <td>$293.00</td>
    </tr>
    <tr>
      <th>48</th>
      <td>The Truman Show</td>
      <td>103</td>
      <td>Comedy, Drama, Sci-Fi</td>
      <td>8.1</td>
      <td>An insurance salesman discovers his whole life...</td>
      <td>Peter Weir</td>
      <td>Jim Carrey,Ed Harris,Laura Linney,Noah Emmerich</td>
      <td>894,732</td>
      <td>$125.62</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Reservoir Dogs</td>
      <td>99</td>
      <td>Crime, Drama, Thriller</td>
      <td>8.3</td>
      <td>When a simple jewelry heist goes horribly wron...</td>
      <td>Quentin Tarantino</td>
      <td>Harvey Keitel,Tim Roth,Michael Madsen,Chris Penn</td>
      <td>885,154</td>
      <td>$2.83</td>
    </tr>
  </tbody>
</table>
</div>



### Now Save the DataFrame as a CSV file to use it later on Data Visualization
#### we have out csv file to perform the analysis. so, we can able to use it visualize and understand the data and their relations
##### Now we can able to use this data to create NLP Model or Machine learning for predictions


```python
IMDB_Movie_Data.to_csv("IMDB_MOVIES.csv")
```
