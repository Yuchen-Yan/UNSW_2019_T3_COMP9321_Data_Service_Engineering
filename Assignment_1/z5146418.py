import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def question_1():
    print("--------------- question_1 ---------------")
    df1 = pd.read_csv('Olympics_dataset1.csv')
    df2 = pd.read_csv('Olympics_dataset2.csv')
    #drop last row by row number
    df1 = df1.drop(df1.index[159])
    df2 = df2.drop(df2.index[159])
    #merge two dataframe
    df_final = pd.merge(df1, df2, on = 'Team')
    #drop the top row of two dataframes
    new_header = df_final.iloc[0] #grab the first row for the header
    df_final = df_final[1:] #take the data less the header row
    df_final.columns = new_header
    #rename the column
    df_final.columns = ["Country", "summer_rubbish", "summer_participation", "summer_gold", "summer_silver", "summer_bronze", "summer_total", "winter_participation" , "winter_gold", "winter_silver", "winter_bronze", "winter_total", "A", "B", "C", "D" ,"E"]
    #remove the last five columnns
    df_final = df_final.drop(['A', 'B', 'C', 'D', 'E'], axis = 1)
    #display 5 rows
    print(df_final.head(5).to_string())
    return df_final

def question_2(df_final):
    print("--------------- question_2 ---------------")
    #remove all of the () and [] in Country columns
    df_final['Country'] = df_final['Country'].str.replace(r"\(.*\)","")
    df_final['Country'] = df_final['Country'].str.replace(r"\[.*\]","")
    #df_final['Country'] = df_final['Country'].str.replace(r" ","")
    #set index as country name
    df_final = df_final.set_index('Country')
    #drop several columns
    df_final = df_final.drop(['summer_rubbish', 'summer_total', 'winter_total'], axis = 1)
    print(df_final.head(5).to_string())
    return df_final


def question_3(df_final):
    print("--------------- question_3 ---------------")
    df_final = df_final.dropna()
    print(df_final.tail(10).to_string())
    return df_final


def question_4(df_final):
    print("--------------- question_4 ---------------")
    df_final['summer_gold'] = df_final['summer_gold'].str.replace(r",","")
    df_final['summer_gold'] = df_final['summer_gold'].astype(float)
    print(df_final[df_final['summer_gold'] == df_final['summer_gold'].max()].index[0])


def question_5(df_final):
    print("--------------- question_5 ---------------")
    df_final['winter_gold'] = df_final['winter_gold'].astype(float)
    df_final['gold_diff'] = df_final['summer_gold'] - df_final['winter_gold']
    print(df_final[df_final['gold_diff'] == df_final['gold_diff'].max()].index[0])
    print(df_final['gold_diff'].max())
    df_final = df_final.drop(['gold_diff'], axis=1)
    return df_final


def question_6(df_final):
    print("--------------- question_6 ---------------")
    #convert columns to float number
    df_final['summer_silver'] = df_final['summer_silver'].astype(float)
    df_final['summer_bronze'] = df_final['summer_bronze'].astype(float)
    df_final['winter_gold'] = df_final['winter_gold'].astype(float)
    df_final['winter_silver'] = df_final['winter_silver'].astype(float)
    df_final['winter_bronze'] = df_final['winter_bronze'].astype(float)
    #sum them all
    df_final['metals'] = df_final['summer_gold'] + df_final['summer_silver'] + df_final['summer_bronze'] + df_final['winter_gold'] + df_final['winter_silver'] + df_final['winter_bronze']
    #sort by the metels
    df_final = df_final.sort_values(by=['metals'], ascending = False)
    #display them all
    print(df_final.head(5).to_string())
    print(df_final.tail(5).to_string())



def question_7(df_final):
    print("--------------- question_7 ---------------")
    #calculate the sum metals for summer and winter respectively
    df_final['summer_metals'] = df_final['summer_gold'] + df_final['summer_silver'] + df_final['summer_bronze']
    df_final['winter_metals'] = df_final['winter_gold'] + df_final['winter_silver'] + df_final['winter_bronze']
    #ordered by the metals
    df_final = df_final.sort_values(by=['metals'], ascending = False)
    
    #get the country names
    index = df_final[['metals', 'summer_metals', 'winter_metals']].head(10).index
    #get the summer and winter metals value
    summer_metals = [df_final['summer_metals'].head(10).values[i] for i in range(10)]
    winter_metals = [df_final['winter_metals'].head(10).values[i] for i in range(10)]

    #draw the plot
    N = 10
    y_pos = np.arange(N)
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.barh(y_pos, summer_metals, color = 'darkorange', align='center')
    ax.barh(y_pos, winter_metals, color = 'royalblue', align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(index)
    ax.set_title('Metals for Winter and Summer Games')

    summer_patch = matplotlib.patches.Patch(color='darkorange', label='Summer games')
    winter_patch = matplotlib.patches.Patch(color='royalblue', label='Winter games')
    
    plt.legend(handles=[winter_patch, summer_patch])
    plt.show()
    df_final = df_final.drop(['summer_metals', 'winter_metals', 'metals'], axis = 1)
    return df_final


def question_8(df_final):
    print("--------------- question_8 ---------------")
    #get the metal values of these countries
    countries = df_final.loc[[' United States  ', ' Australia  ', ' Great Britain  ', ' Japan ', ' New Zealand  '], ['winter_gold', 'winter_silver', 'winter_bronze']]
    
    #get the index and the metal quantities
    index = countries.index
    gold = countries['winter_gold']
    silver = countries['winter_silver']
    bronze = countries['winter_bronze']
    width = 0.25
    
    #draw the plot
    N = 5
    r1 = np.arange(N)
    r2 = [x + width for x in r1]
    r3 = [x + width for x in r2]
    
    #make the plot
    fig = plt.figure()
    plt.bar(r1, gold, color = 'blue', width = width, edgecolor = 'white', label = 'gold')
    plt.bar(r2, silver, color = 'orange', width = width, edgecolor = 'white', label = 'silver')
    plt.bar(r3, bronze, color = 'gray', width = width, edgecolor = 'white', label = 'bronze')
    
    #set the title
    fig.suptitle('Winter Games')
    plt.xticks([r + width for r in range(len(gold))], index)
    plt.legend()
    plt.show()



def question_9(df_final):
    print("--------------- question_9 ---------------")
    #get the summer metals
    df = df_final[['summer_participation','summer_gold','summer_silver','summer_bronze']]
    df = df.copy()
    df['summer_participation'] = df['summer_participation'].astype(float)
    #calculate the result
    df['point_per_par'] = (df['summer_gold'] * 5 + df['summer_silver'] * 3 + df['summer_bronze']) / df['summer_participation']
    df = df.sort_values(by=['point_per_par'], ascending = False)
    print(df['point_per_par'].head(5))



def question_10(df_final):
    print("--------------- question_10 ---------------")
    df = df_final.copy()
    df['summer_participation'] = df['summer_participation'].astype(float)
    df['winter_participation'] = df['winter_participation'].astype(float)
    
    #calculate the result
    df['point_per_par_s'] = (df['summer_gold'] * 5 + df['summer_silver'] * 3 + df['summer_bronze']) / df['summer_participation']
    df['point_per_par_w'] = (df['winter_gold'] * 5 + df['winter_silver'] * 3 + df['winter_bronze']) / df['winter_participation']
    df = df.fillna(0)

    #get the continent data
    continents = pd.read_csv('Countries-Continents.csv')
    continents = continents.set_index('Country')
    df.index = df.index.str.strip()
    df.index = df.index.str.rstrip()
    df = df.join(continents, how='outer')
    df = df.dropna(subset=['point_per_par_w'])
    
    #draw the plot
    fig, ax1 = plt.subplots(figsize=(8, 8))

    mapping = {'South America': 2, 'Europe': 3, 'Asia': 4, 'North America': 5, 'Oceania' :6, 'Africa' : 7}
    df = df.replace({'Continent': mapping})
    df['Continent'] = df['Continent'].fillna(1)
    ax1.scatter(df['point_per_par_s'], df['point_per_par_w'], c= df['Continent'], cmap=matplotlib.cm.brg)
    #draw the label
    index = df.index
    for i, txt in enumerate(index):
        ax1.annotate(txt,(df['point_per_par_s'][i], df['point_per_par_w'][i]))
    #set the title and lebals
    ax1.set_title('Summer vs Winter Rate')
    ax1.set_xlabel('Summer Rate')
    ax1.set_ylabel('Winter Rate')
    #removing top and right borders
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    plt.show()






if __name__ == "__main__":
    df_final = question_1()
    df_final = question_2(df_final)
    df_final = question_3(df_final)
    question_4(df_final)
    df_final = question_5(df_final)
    question_6(df_final)
    df_final = question_7(df_final)
    question_8(df_final)
    question_9(df_final)
    question_10(df_final)
