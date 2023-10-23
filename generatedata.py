#%%
import pandas as pd
import matplotlib as plt
import random
# %%
topics = ['turnto', 'problems','talkto','depending','xopen',
                 'xdeepdown', 'xtruecare', 'abandon','uneqcare']

# %%
relationtopics = topics.copy()
for i in range(len(relationtopics)):
    relationtopics[i] = 'r' + relationtopics[i]

generaltopics = topics.copy()
for i in range(len(generaltopics)):
    generaltopics[i] = 'g' + generaltopics[i]

print(relationtopics)
print(generaltopics)

#%%
demographics = ['age', 'gender']

#%%
surveycols = ['id','trial'] + relationtopics + generaltopics
print(len(surveycols))
# %%
democols = ['id'] + demographics
print(democols)
# %%
surveydata = pd.DataFrame(columns=surveycols)
print(surveydata)

demodata = pd.DataFrame(columns=democols)
print(demodata)

#%%
# demodata.loc[1] = [1, 15, 'Male']
# demodata.index = demodata.index + 1
# demodata = demodata.sort_index()
# print(demodata)
# print(demodata.shape)
# %%
def generateSurveydata():
    ans = [0] * 18
    for i in range(len(ans)):
        ans[i] = random.randint(1,5)
    return ans

def addTrial(id, trial = 1):
    data = generateSurveydata()
    data = [id, trial] + data
    #figure out where to put the row in into the df(could just put beginning)
    #can sort the rows by id and trial as well after insertion
