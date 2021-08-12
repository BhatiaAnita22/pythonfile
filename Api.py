import requests


def first_question():
    response = requests.get("https://my-json-server.typicode.com/typicode/demo/posts")
    data = response.json()
    datacomment = (requests.get("https://my-json-server.typicode.com/typicode/demo/comments")).json()
    finaldict = [];
    for unitd in data:
        for uc in datacomment:
            if(uc['id'] == unitd['id']):
                #print("matched first ",unitd ,"  and ",uc);
                tempdata = unitd;
                unitd.update(uc)
                print("uint is ",unitd)
                finaldict.append(unitd)
            else:
                print("not matched ");
    print(finaldict)
    #return finaldict;
def countPerson(data):
    s1 = set(['first_name', 'last_name'])
    count = 0;
    for unitdata in data:
        if s1.issubset(unitdata.keys()) == True:
            count += 1;
    return count;


    
def second_question():
    i = 1;
    count = 0;
    s = "https://reqres.in/api/users?page="
    while(i <= 12):
        response = requests.get(s+str(i))
        receivedtext = response.json()
        #print(receivedtext)
        if 'data' in receivedtext:
            count += countPerson(receivedtext['data']);
        i = i+1;
    print("total no of person are ",count)

first_question()
print("First Question Complted\n")
second_question()


        
    
