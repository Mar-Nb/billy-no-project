import imp
from pluginDefault import PluginDefault
from plugins.alarm.plugin import PluginAlarm
from plugins.remote.plugin import PluginRemote
from plugins.opening.plugin import PluginOpening

class PluginFactory:

    def getPlugin(subject, typeS):
        themeName= subject.split(".")[0]    
        if themeName== "alarm":
            return PluginAlarm(subject, typeS)
        elif themeName== "remote":
            return PluginRemote(subject, typeS)
        elif themeName== "opening":
            return PluginOpening(subject, typeS)            
        return PluginDefault(subject, typeS)