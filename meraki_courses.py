### MERAKI SARAL COURSES INFORMATION 
from pprint import pprint
import os,json,requests
try:
    if os.path.exists('api.json'):
        f=open('api.json','r')
        json_data=json.load(f)
    else:
        res=requests.get("http://saral.navgurukul.org/api/courses").text
        json_data=json.loads(res)
        f=open('api.json','w')
        json.dump(json_data,f,indent=4)
        f.close()
finally: 
    num=1
    courses_list=[] 
    id_list=[]
    for v in json_data['availableCourses']:
        a=str(num)+'. '+v['name']
        print(a)
        courses_list.append(a)
        id_list.append(v['id'])
        num+=1
    ### FOR CHECKING
    #     for v1,v2 in zip(courses_list,id_list):
    #     print(v1+' id is= '+v2)
    n=int(input("Enter your course id:- "))
    print('##',courses_list[n-1])
    i=id_list[n-1]
    res1=requests.get("http://saral.navgurukul.org/api/courses/"+i+"/exercises").text
    b=json.loads(res1)
    num1=1
    list1=[]
    for c in b['data']:
        list2=[]
        d=str(num1)+'. '+c['name']
        print('     '+d)
        int_slug="http://saral.navgurukul.org/api/courses/"+i+"/exercise/getBySlug?slug="+c['slug']
        list2.append(int_slug)
        num2=1
        for d in c['childExercises']:
            e=str(num1)+'.'+str(num2)+' '+d['name']
            print('       '+e)
            float_slug="http://saral.navgurukul.org/api/courses/"+i+"/exercise/getBySlug?slug="+d['slug']
            list2.append(float_slug)
            dict2={str(num1)+'.'+str(num2):float_slug}
            list1.append(dict2)
            num2+=1
        dict1={num1:list2}
        list1.append(dict1)
        num1+=1
    n=input('Enter any sequence:- ')
    for g in list1:
        for h in g:
            try:
                if n==h:
                    res=requests.get(g[h]).text
                    res1=json.loads(res)
                    p=res1['content']
                    p1=json.loads(p)
                    print(p1[0]['value'])
                if int(n)==h:
                    c=0
                    for x in g[h]:
                        res=requests.get(x).text
                        res1=json.loads(res)
                        p=res1['content']
                        p1=json.loads(p)
                        print(str(c)+'. ',p1[0]['value'])
                        c+=1
            except:
                pass