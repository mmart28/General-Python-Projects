#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Madeline Martine

#dictionary for all the car data
carActivities={'spider':{'oil changes':2,'bodywork incidents':7, 'agent id':0},
               'triangle':{'agent id':1,'oil changes':6},
               'shamrock':{'import/export waiver':1, 'agent id':1},
               'marty':{'bodywork incidents':3,'upgrades':1,'agent id':2}}

#agent list for reference later 
agentList=['Jake Connors','Ben Evans','Ariel Chen']

#function for aggregating data
def aggTotals(info):
    totalInfo=0
    for k,v in carActivities.items():
        totalInfo=totalInfo+v.get(info,0)
    return(totalInfo)    

#aggregation data for user to receive

activity=input('What information would you like to aggregate?\n')
totalActivity=aggTotals(activity)
print(str(activity)+'---->'+str(totalActivity))


print()

#section for individual car data

print()
carName=input('What is the name of the car you would like to check?\n')
print()
carAction=input('What action would you like a count for?\n')
#loop to look up the activity for the specific car
for k,v in carActivities.items():
    if k==carName:
        action=v.get(carAction,0)
        agent=v.get('agent id',0)
        print()
        print(carName+' had '+str(action)+' ' +carAction+' and the agent is '+agentList[int(agent)])
        #warning for too many oil changes
        if carAction=='oil changes' and action>5:
            print()
            print('WARNING: Your number of oil changes is greater than 5, please check your engine with a mechanic')
        print()
        

print()
print('Thank you and goodbye!')            


# In[ ]:




