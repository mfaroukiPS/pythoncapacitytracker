import json


with open('load.json',"r") as f:
    data = json.load(f) # read the file
f.close()


def loadchargeAll():
    #get all the information in data
    for item in data['datacharge']:
        print('the collaborator : {}'.format(item["nom"]))
        
        for k,v in item["charge"].items():
            #print (k,v)
            print('charge {} is {}'.format(k,v) )

        
def getcharge(name):
    #return charge for each team related to a collaborator
    # OK
    check = False
    charge={}
    for item in data['datacharge']:
        if item["nom"] == name:
            charge[name]=item["nom"]
            check = True
            for k,v in item["charge"].items():
                charge[k]=v
            return charge
    if check == False:
        return '{} does not existe'.format(name)


def getteamchargebyteam(team):
    #return charge for each collaborator in a team
    # we chose a team and the function return the charge by team
    # this function is ok 
    charge=[]
    type(charge)
    for item in data['datacharge']:
        for k,v in item["charge"].items():
            if k == team:
                charge.append({item["nom"]:v}) # add an object to the dict charge
    return charge


def modifycharge(nom,team,newcharge):
    # thi function modify the % of working for a given nom and team
    # OK
    tmp = data
    for item in tmp['datacharge']:
        if item["nom"] == nom:
            item['charge'][team] = newcharge

    with open('load.json', 'w') as f:
        json.dump(tmp, f, indent=2)
    return tmp

def getcollaborator():
    #this function return a tuple of collaborator
    listcollabo = []
    for item in data['datacharge']:
        listcollabo.append((item["nom"])) # add element in list
    return tuple(listcollabo) # convert the list tu tuple


getcollaborator()
# loadchargeAll()
#print(getcharge('nom2'))
# print(getteamchargebyteam('equipe2'))
#print(modifycharge("nom2", "equipe2", "100"))


