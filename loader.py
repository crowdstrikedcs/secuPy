#Dataset Loader module
#Loads .binetflow from CTU Scenario 1 and stores relevant features

import netaddr, struct, sys
import numpy as np
import pickle

def load(fileName):
    #Save training data and dataset
    try:
        file = open(fileName, 'r')
        print("File opened successfully, reading...")
    except:
        print("Unable to load file")
        print("Usage: python loader.py 'filepath'")
        exit()
    trainData = []
    trainLabel = []
    testData = []
    testLabel = []
    flag = False
    normalCount=0
    botCount=0
    testNormal=0
    testBot=0

    #dicts to convert Argus protocols and state to integers
    protoDict = {'tcp': 0, 'udp': 1, 'rtp': 2, 'pim': 3, 'icmp': 4, 'arp': 5, 'ipx/spx': 6, 'rtcp': 7, 'igmp' : 8, 'ipv6-icmp': 9, 'ipv6': 10, 'udt': 11, 'esp': 12, 'unas': 13, 'rarp': 14, }

    file.readline()

    for line in file:
        #sd is a list where each element is a unique val from the csv line
        sd = line[:-1].split(',')
        #meat, this is what we are actually looking at per line
        # 2011/08/10 09:46:59.607825,1.026539,tcp,94.44.127.113,1577,   ->,147.32.84.59,6881,S_RA,0,0,4,276,156,flow=Background-Established-cmpgw-CVUT
        dur, proto, Sport, Dport, Sip, Dip, totP, totB, label= sd[1], sd[2], sd[4], sd[7], sd[3], sd[6], sd[11], sd[12], sd[14]
        try:
            #converts an IP to an 32 bit number, assuming this is easier to ~classify~
            Sip = int(netaddr.IPAddress(Sip))
        except:
            continue
        try:
            #converts an IP to an 32 bit number, assuming this is easier to ~classify~
            Dip = int(netaddr.IPAddress(Dip))
        except:
            continue
        #handle missing ports
        if Sport=='': continue
        if Dport=='': continue
        #back, nor, bot
        try:
            if "Background" in label:
                label=0

            elif "Normal" in label:
                label = 0

            elif "Botnet" in label:
                label = 1

            if flag==False:
                #Training Dataset
                #get some normal traffic
                if label==0 and normalCount<20001:
                    #what we are training on
                    trainData.append([float(dur), protoDict[proto], int(Sport), int(Dport), Sip, Dip, int(totP), int(totB)])
                    trainLabel.append(label)
                    normalCount+=1
                #get some bot traffic
                elif label==1 and botCount<20001:
                    trainData.append([float(dur), protoDict[proto], int(Sport), int(Dport), Sip, Dip, int(totP), int(totB)])
                    trainLabel.append(label)
                    botCount+=1
                #done, move to test dataset
                elif normalCount>19999 and botCount>19999:
                    flag=True

            else:
                #Test dataset
                if label==0 and testNormal<5001:
                    testData.append([float(dur), protoDict[proto], int(Sport), int(Dport), Sip, Dip, int(totP), int(totB)])
                    testLabel.append(label)
                    testNormal+=1
                elif label==1 and testBot<5001:
                    testData.append([float(dur), protoDict[proto], int(Sport), int(Dport), Sip, Dip, int(totP), int(totB)])
                    testLabel.append(label)
                    testBot += 1
                elif testNormal>4999 and testBot>4999:
                    break
        except:
            continue
    #pickle the dataset
    print("Dataset load complete, storing...")
    file = open('flowdata.pickle', 'wb')
    pickle.dump([np.array(trainData), np.array(trainLabel), np.array(testData), np.array(testLabel)], file)
    #return the training and the test dataset
    #return np.array(trainData), np.array(trainLabel), np.array(testData), np.array(testLabel)

if __name__ == "__main__":
    try:
        load(str(sys.argv[1]))
    except IndexError:
        print("Usage: python loader.py 'file'")
