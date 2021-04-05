# Shark Data Analysis
![alt text](https://github.com/FranLeston/shark_attack_data_analysis/blob/main/images/attacks_year_histoplot.png?raw=true)

Used the following libraries:

```bash
pip install pandas
pip install seaborn
pip install matplotlib
pip install numpy
pip install wordcloud
```

## Usage

```python
#Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image

#My Functions
import src.limpieza_texto as lt
#Sean B. Palmer script to calculate phases of the moon for a given date
import src.moonphase as moon

```

## Instructions
Given a data set about shark attacks, come up with some interesting visualizations and conclusions after analysing and cleaning the data. 
The link to the the dastaset may be found here: [Shark Attack Data](https://www.kaggle.com/teajay/global-shark-attacks). After downloading the .csv file,
place it in the data directory. You should first execute the code block in the "limpieza" jupyter notebook to clean the data. Afterwards, you can run the "visualization" 
to view the plots. 

## What I wanted to show
1. Did a Full Moon mean more shark attacks?
2. Show shark attacks by year since the year 1900 to present day.  
3. Did shark attacks increase since the film JAWS released?
4. Show the age distribution of the attacks. How many were male/female?
5. What activities resulted in the most shark attacks?
6. What species of shark is the most aggresive?
7. What are the fatality rates of shak attacks reported?
8. What were the most frequent injuries?
9. What were the countries with the most shark attacks?

## Preparing the data...

First thing on my list, was getting rid of all the columns in the dataset I know I am not going to need:
```python
df_cleaned = df.drop(columns=["Case Number","Unnamed: 22", "Unnamed: 23", "Name", "pdf", "href formula","href","original order","Case Number.1", "Case Number.2", "Investigator or Source"])
````
After that, some columns needed renaming for better clarity and accesibility.

Next, I checked for duplicate rows and rows with all NaN values:
```python
df_cleaned.dropna(axis = 0, how = 'all', inplace = True)
df_cleaned.drop_duplicates(subset=list(df_cleaned.columns), inplace = True)
```

The Age, Sex and Fatal columns needed some cleansingm so I applied some manual functions to each of those columns.
Also, I created a new column called Year Modern to save all the attacks that were post 1900. 
```python
df_cleaned['Age'] = df_cleaned['Age'].apply(lt.clean_age)
df_cleaned['Fatal'] = df_cleaned['Fatal'].apply(lt.clean_fatal)
df_cleaned['Sex'] = df_cleaned['Sex'].apply(lt.clean_sex)

# I dont really need to show years before the 1900's, so I'll create a new colum called Modern Year 
# and fill it in with the value from the year column:
df_cleaned['Year Modern'] = df_cleaned[df_cleaned['Year']>1900]['Year']
````

### Calculating the moon phases
I had to take all the valid dates in the dates column (day-month-year) and create a new Clean Dates Column.
Then create a new column for the moon phase during that day. Here I used a script by Sean B. Palmer, where given a date object
return the moon phase for that day in question. 

Thank you Sean B Palmer:
moonphase.py - Calculate Lunar Phase
Author: Sean B. Palmer, inamidst.com
Cf. http://en.wikipedia.org/wiki/Lunar_phase#Lunar_phase_calculation


```python
df_cleaned["Date Cleaned"] = df_cleaned['Date'].apply(lt.clean_date)
df_cleaned["Moon"] = df_cleaned['Date Cleaned'].apply(lt.get_moon)
```

Finally, reset the index and export clean data csv file to the data folder. 
```python
df_cleaned.to_csv("data/attacks_clean.csv")
```

## Plotting the data...
Mostly I used seaborn countplots, histplots, and pie charts to show my information. 
I had some fun using the Word Cloud library to show the frequency of injuries that appeared on the injuries data column.
The result was the following word cloud with an outline of a shark.

### Did Full Moons have something to do with the attacks?
![alt text](https://github.com/FranLeston/shark_attack_data_analysis/blob/main/images/moon_barplot.png?raw=true)

### WordCloud Injury Frequency
![alt text](https://github.com/FranLeston/shark_attack_data_analysis/blob/main/images/wordcloud_injuries.png?raw=true)

### Top activities resulting in the most shark attacks
![alt text](https://github.com/FranLeston/shark_attack_data_analysis/blob/main/images/activity_distribution_barplot.png?raw=true)

### Countries with most attacks
![alt text](https://github.com/FranLeston/shark_attack_data_analysis/blob/main/images/top_countries_barplot.png?raw=true)

### Age Distribution - Male vs Female
![alt text](https://github.com/FranLeston/shark_attack_data_analysis/blob/main/images/age_distribution_countplot.png?raw=true)

### Fatality Rate, Male vs Female, Types of Incidences
![alt text](https://github.com/FranLeston/shark_attack_data_analysis/blob/main/images/pie_charts.png?raw=true)

### Top shark attacks by species
![alt text](https://github.com/FranLeston/shark_attack_data_analysis/blob/main/images/species_barplot.png?raw=true)


