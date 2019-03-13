
class serviceDictionary:
    def servicesState(self, tasks, counterName):
        self.dictCounter = {}
        counter = 0
        for task in tasks:            
            if counterName in task['Status']['State']:
                counter = counter+1
        self.dictCounter[counterName] = counter
        return  self.dictCounter

    def Info(self, service):               
        self.dictInfo = {}        
        self.dictInfo["replicas"] = self.servicesState(service.tasks(), "running")
        ServiceInfo = service.attrs["Spec"]
        TaskTemplate = ServiceInfo["TaskTemplate"]
        mMode = ServiceInfo["Mode"]
        if mMode != None:
            if "Global" in mMode:
                self.dictInfo["replicas"]["total"] = "Global"
            else:
                self.dictInfo["replicas"]["total"] = mMode["Replicated"]["Replicas"]
        self.dictInfo["deadContainers"] = self.servicesState(service.tasks(), "shutdown")["shutdown"]        
        mResources = TaskTemplate["Resources"]
        dictResource = {}
        if mResources != {}:
            if not mResources["Reservations"] == {} or not mResources["Limits"] == {}:
                dictResource["reservation"] = mResources["Reservations"]
                dictResource["limit"] = mResources["Limits"]
                self.dictInfo["resources"] = dictResource
        self.dictInfo["image"] = TaskTemplate["ContainerSpec"]["Image"].split('@')[0]
        self.dictInfo["version"] = self.dictInfo["image"].split(':')[1]        

        return self.dictInfo

class nodeDictionary:
    def servicesState(self, tasks, counterName):
        self.dictCounter = {}
        counter = 0
        for task in tasks:            
            if counterName in task['Status']['State']:
                counter = counter+1
        self.dictCounter[counterName] = counter
        return  self.dictCounter

    def Info(self, service):               
        self.dictInfo = {}        
        self.dictInfo["replicas"] = self.servicesState(service.tasks(), "running")
        ServiceInfo = service.attrs["Spec"]
        TaskTemplate = ServiceInfo["TaskTemplate"]
        mMode = ServiceInfo["Mode"]
        if mMode != None:
            if "Global" in mMode:
                self.dictInfo["replicas"]["total"] = "Global"
            else:
                self.dictInfo["replicas"]["total"] = mMode["Replicated"]["Replicas"]
        self.dictInfo["deadContainers"] = self.servicesState(service.tasks(), "shutdown")["shutdown"]        
        mResources = TaskTemplate["Resources"]
        dictResource = {}
        if mResources != {}:
            if not mResources["Reservations"] == {} or not mResources["Limits"] == {}:
                dictResource["reservation"] = mResources["Reservations"]
                dictResource["limit"] = mResources["Limits"]
                self.dictInfo["resources"] = dictResource
        self.dictInfo["image"] = TaskTemplate["ContainerSpec"]["Image"].split('@')[0]
        self.dictInfo["version"] = self.dictInfo["image"].split(':')[1]        

        return self.dictInfo