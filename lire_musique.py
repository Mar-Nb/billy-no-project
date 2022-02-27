import webbrowser
import json

file='list_music.json'
with open(file,'r+') as json_data:
    data_dict = json.load(json_data)
    print("0 - add music")
    for i in range(0,len(data_dict["opening"])) :
        opening = data_dict["opening"][i]
        print(str(i+1)+ " - "+opening["name"])
    index = int(input("saisiser le numero \n"))
    if index==0:
        name=input("donner le nom de l'opening \n")
        url=input("donner le nom de l'url \n")
        #add dans le JSON
        data_dict["opening"].append({"name":name,"URL":url})
        json_data.seek(0)
        json.dump(data_dict, json_data, indent = 1,ensure_ascii=False)
        print("le nom "+name+" a bien été ajouté")
        # message d'ajout
    else:
        URL=data_dict["opening"][index-1]["URL"]
        webbrowser.open(URL)  # Go to example.com