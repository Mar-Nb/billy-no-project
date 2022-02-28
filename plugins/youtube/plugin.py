from copyreg import constructor
from select import select
import sys
from platform import release
from unicodedata import name
import webbrowser
import json
sys.path.append('../../')
from pluginDefault import PluginDefault

class PluginYoutube(PluginDefault):
    def response(self, sentence=""):
        file='list_music.json'
        if "jouer" in sentence:
            select = sentence.replace("youtube ", "").replace("jouer ", "")
            index = int(select)
            with open(file,'r+') as json_data:
                data_dict = json.load(json_data) 
                if index < len(data_dict["opening"]) or index == 0:
                    HI_string = "Nom: <input id=\'input-youtube-name\' /><br/>URL:<input id=\'input-youtube-url\' /><br/><button onclick=\'addURL()\' class=\'bibi_button_add\'>Ajouter</button>"
                    return HI_string
                else: 
                    name = data_dict["opening"][index-1]["name"]
                    URL=data_dict["opening"][index-1]["URL"]
                    webbrowser.open(URL)  # Go to example.com     
                    return "Je vous envoie sur l'URL de "+ name  
        elif "ajouter" in sentence:
            with open(file,'r+') as json_data:
                data_dict = json.load(json_data)
                name_url = sentence.split("|")
                name = name_url[0].replace("yt ", "").replace("ajouter ", "")
                url = name_url[1]
                data_dict["opening"].append({"name":name,"URL":url})
                json_data.seek(0)
                json.dump(data_dict, json_data, indent = 1,ensure_ascii=False)                
                return "Votre URL a bien été ajouté dans la liste" 
        else:
            file='list_music.json'
            dictionnaire = dict()
            dictionnaire["youtube"] = dict()
            with open(file,'r+') as json_data:
                data_dict = json.load(json_data)
                for i in range(0,len(data_dict["opening"])) :
                    opening = data_dict["opening"][i]
                    dictionnaire["youtube"][opening["name"]] = opening["URL"]
            json_string = json.dumps(dictionnaire, ensure_ascii=False).encode("utf8")
            return json_string.decode()


