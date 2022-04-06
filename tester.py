import json
import requests
url = "https://raw.githubusercontent.com/scythe-io/community-threats/master/Conti/Conti_scythe_threat.json"



r = requests.get(url)
rjson = r.json()


#print(rjson)

threatdict = rjson['threat']

#print(key1 + " TIME:")
#print(type(key1))
#print(rjson[key1])
#threatdict = rjson[key1]
print('Running the following campaign:')
print(threatdict['display_name'])
print(threatdict['description'])
#print(threatdict['script'])
#print(type(threatdict['script']))
executables = threatdict['script']

#print(executables)
for key2 in executables.keys():
    step = executables[key2]
    #print(step.keys())
    if 'request' in step:
        print(step['request'])
    
    '''
    for key3 in step.keys():
        print(key3)
        #print(step['request'])

'''
