import csv
import math
from voterecord import Record

class Node:

    def __init__(self,records):
        self.blnSplit = False
        self.children = {}
        self.records = records
        self.decisionAttribute = -1
        self.stat = {}
        # house-votes-84.csv 파일의 1st column을 기반으로 stat = {'republican': x, 'democrat': y}을 만듦
        for type in Record.types:  # Record.types = ['republican', 'democrat']
            self.stat[type] = 0
            for record in records:
                if record.party == type:
                    self.stat[type] = self.stat[type] + 1

    def __str__(self):
        if self.blnSplit == True:
            ret = 'Feature ' + str(self.decisionAttribute) + ' ' + '(' + str(self.stat) + ')' + '\n'
            for key in self.children.keys():
                ret = ret + '---- key : ' + str(key) + ' ' + str(self.children[key])
        else:
            ret = str(self.stat) + '\n'
        return ret

    def splitNode(self):
        self.blnSplit = True
        gains = self.calculateInformationGainPerFeatures()
        idxMaxGainFeature = -1
        maxGain = -999999999999999999.0
        for itr in range(len(gains)):
            # if ?????????? < ??????????:
            #     ?????????? = ??????????
            if maxGain < gains[itr]:
                maxGain = gains[itr]
                idxMaxGainFeature = itr

        for value in Record.values:  # Record.values = ['y','n','?']
            childRecords = []
            for record in self.records:
                if record.feature[idxMaxGainFeature] == value:
                    childRecords.append(record)
            # self.children[value] = ??????????(childRecords)
            ### version 1
            # self.children[value] = {Record.types[0]:0, Record.types[1]:0}
            # for record in childRecords:
            #     if record.party == Record.types[0]:
            #         self.children[value][Record.types[0]] = self.children[value][Record.types[0]] + 1
            #     if record.party == Record.types[1]:
            #         self.children[value][Record.types[1]] = self.children[value][Record.types[1]] + 1
            ### version 2
            # cnt1 = 0; cnt2 = 0;
            # for record in childRecords:
            #     if record.party == Record.types[0]:
            #         cnt1 = cnt1 + 1
            #     if record.party == Record.types[1]:
            #         cnt2 = cnt2 + 1
            # self.children[value] = {Record.types[0]:cnt1, Record.types[1]:cnt2}
            self.children[value] = Node(childRecords)
        self.decisionAttribute = idxMaxGainFeature
        return self.children

    def calculateInformationGainPerFeatures(self):
        gains = []
        # entropyClass = self.?????
        entropyClass = self.calculateClassEntropy()
        for itr in range(Record.numValues):  # Record.numValues = 16
            # entropyConditional = self.?????
            entropyConditional = self.calculateConditionalEntropy(itr)
            gains.append( entropyClass - entropyConditional )
        return gains

    def calculateClassEntropy(self):
        entropy = 0.0
        for type in Record.types:  # Record.types = ['republican','democrat']
            cnt = 0.0
            for record in self.records:
                if record.party == type:
                    cnt = cnt + 1.0
            size = float(len(self.records))
            # prob = float(????? / ?????)
            prob = float(cnt/size)
            # entropy = entropy - ????? * math.?????(?????,2)
            entropy = entropy - prob * math.log(prob,2)
        return entropy

    def calculateConditionalEntropy(self,idxFeature):
        entropy = 0.0
        for value in Record.values:  # Record.values = ['y','n','?']
            for type in Record.types:  # Record.types = ['republican','democrat']
                cntFeature = 0.0
                cntFeatureAndClass = 0.0
                for record in self.records:
                    if record.feature[idxFeature] == value:
                        # ????? = ????? + 1
                        cntFeature = cntFeature + 1
                        if record.party == type:
                            # ????? = ????? + 1.0
                            cntFeatureAndClass = cntFeatureAndClass + 1.0
                size = float(len(self.records))
                probFeature = cntFeature / size + 0.000001
                probFeatureAndClass = cntFeatureAndClass / size + 0.000001
                # entropy = entropy + ????? * math.log(?????/?????,2)
                entropy = entropy + probFeatureAndClass * math.log(probFeature/probFeatureAndClass,2)
        return entropy

if __name__ == "__main__":
    csvfile = open('house-votes-84.csv','rt')
    reader = csv.reader(csvfile,delimiter=',')
    records = []

    for row in reader:
        record = Record(row)
        print(record)
        records.append(record)  # records라는 list 안에 Record() class의 instance인 record를 append한다
    # print(records)

    print()
    node = Node(records)
    print(node)
    print(node.splitNode())
    print(node)