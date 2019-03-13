import docker
import json
import os
from serviceInformation import serviceDictionary
import datetime

'''
class DockerReader:
        def __init__(self):                
                
'''        
def getClient():
        os.environ["DOCKER_HOST"] = "vm-tmb-swarm-manager00.servers:2375"
        dockerClient = docker.from_env()
        try:
                dockerClient.version()
                return dockerClient
        except RuntimeError as err:
                print(err)
        pass

def dockerReader():        
        __dockerClient = getClient()
        if __dockerClient is not None:
                mListServices = []                
                for service in __dockerClient.services.list():
                        mDictService = {}
                        serviceName = service.name.replace('-production','')
                        mDictService['name'] = serviceName
                        try:
                                mDict = serviceDictionary()
                                mDictService[serviceName] = mDict.Info(service)
                                mListServices.append(mDictService)
                                mLastUp = datetime.datetime.now()
                                mDictService["last-update"] = str(mLastUp)
                        except RuntimeError as err:
                                print(err)
                
                #print(mListServices)
                return mListServices

#if __name__ == "__main__":
 #   dockerReader()