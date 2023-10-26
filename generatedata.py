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

#resets the dataframes (initializes them if not already)
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

def generateDemographicData():
    retdata = []
    gender = ['M', 'F', 'NB', 'NA']
    #80% chance of being M/F (arbitrary), equal chance being NB/NA if not M/F
    randomg = random.randint(1,10)
    if randomg <= 4:
        retdata.append(gender[0])
    elif randomg <= 8:
        retdata.append(gender[1])
    else:
        retdata.append(gender[randomg - 7]) #9/10 -> index 2/3
    
    age = random.randint(15,25)
    retdata.insert(0,age)
    
    return retdata

#adds the participant data to the demographic table (equivalent to saying they've join the study)
def addParticipant(id):
    global demodata

    #check if they're already in the study
    if (id in demodata['id'].unique()):
        print("Participant " + str(id) + " already in the study")
        return False
    
    toadd = generateDemographicData()
    toadd = [id] + toadd

    demodata.loc[-1] = toadd
    demodata.index = demodata.index + 1
    demodata.sort_values('id')


def generateSurveyData():
    ans = [0] * 18
    for i in range(len(ans)):
        ans[i] = random.randint(1,5)
    return ans

def addTrial(id, trial = 1):
    global surveydata
    global demodata

    #checks if the trial is too high
    if (trial > 6 or trial <= 0):
        print("Invalid trial number: " + str(trial))
        return False

    #checks if the id isn't present in demographic data (aka they haven't signed up for the study)
    if (id not in demodata['id'].unique()):
        print("Participant " + str(id) + " is not registered for the study")
        return False


    #checks if the id/trial pair is already in the dataframe

    #variable to check if the previous trial is present
    seenprevtrial = True if trial == 1 else False
    maxseentrial = 0

    for index,row in surveydata.iterrows():
        if (row['id'] == id and row['trial'] > maxseentrial):
            maxseentrial = row['trial']
        if (row['id'] == id and row['trial'] == trial):
            print("Trial " + str(trial) + " has already been completed for participant " + str(id))
            return False
        if (row['id'] == id and row['trial'] == trial - 1):
            seenprevtrial = True
    
    #replaces all the previous trials with -1 in each place
    #only if some of the trials were missed
    #resets trial to 0 if they haven't taken ANY trials
    #and takes their first trial now
    if maxseentrial == 0:#they haven't done any trials
        trial = 1
    if (not seenprevtrial):
        for i in range(maxseentrial+1, trial):
            toadd = [id, i] + ([-1] * 18)
            surveydata.loc[-1] = toadd
            surveydata.index = surveydata.index + 1
        
    
    data = generateSurveyData()
    data = [id, trial] + data
    surveydata.loc[-1] = data
    surveydata.index = surveydata.index + 1
    surveydata = surveydata.sort_values(by=['id','trial'])
    #figure out where to put the row in into the df(could just put beginning)
    #can sort the rows by id and trial as well after insertion

#%%
def printtables():
    print(demodata)
    print()
    print(surveydata)
# %%
#testing
addParticipant(1)
# print(demodata)
# print(surveydata)
addParticipant(2)
addParticipant(3)
addTrial(1, 1)
addTrial(1,4)
addTrial(2,2)#adds the 1st trial since person 2 hasn't taken
#ANY trials yet
addTrial(5,3)
printtables()
# %%
