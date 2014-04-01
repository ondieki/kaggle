import csv
import collections 
import sys
import numpy

def readData():
    with open('train.csv', 'rU') as csvfile:
        reader = csv.reader(csvfile)
        #Skips the column headers --eg. latitude, longitude, crime location etc
        #reader.next()
        K = 20
        featureList = []
        labelList = []

        for row in reader:
            labels = row[:len(row)-1]
            features = row[len(row)-1]
            if K == 0: break;
            features = features.strip() #removes the leading space
            features = features.split(' ')  
            labels.append(features[0]) #append to label list for training example
            features = features[1:]    #we have ##:## tuples now
            #print labels ,"  =========  ",features
            K-=1
            featureList.append(features)
            labelList.append(labels)
    with open("trainlabels.txt", "a") as labelFile:
        for itemlabel in labelList:
            for category in itemlabel:
                labelFile.write(category + ',');
            labelFile.write('\n')   
    with open('trainfeatures.txt', "a") as featureFile:
            for itemFeatures in featureList:
                for tup in itemFeatures:
                    featureFile.write(tup + ',')
                featureFile.write('\n')
    labelFile.close()
    featureFile.close()

        
if __name__ == "__main__":
    readData();