testData = [3, 4, 4, 2, 2, 2, 5, 6, 7, 7]

class stats:
    def __init__(self, dataset):
        if dataset == []:
            raise Exception("No data detected")
        self.dataset = dataset

    def getSum(self, dataset):
        print("executing sum function")
        sum = 0
        print(sum)
        for i, v in enumerate(dataset):
            sum += v

    def getMean(self, dataset):
        self.checkDataset(dataset)
        if sum == None:
            self.getSum(dataset)
            print(sum)

        mean = sum/len(dataset)
        return mean

    def getMedian(self, dataset):
        self.checkDataset(dataset)

        if len(dataset)%2 == 0:
            halfLength = len(dataset)/2
            median = (dataset[int(halfLength-1)]+dataset[int(halfLength)])/2
        else:
            median = dataset[int((len(dataset)-1)/2)]
        return median

    def getMode(self, dataset):
        self.checkDataset(dataset)
        frequencyDict = {}

        for i, v in enumerate(dataset):
            if v in frequencyDict:
                frequencyDict[v] += 1
            else:
                frequencyDict[v] = 1

        highestFrequency = 1
        for value, frequency in frequencyDict.items():
            if frequency>highestFrequency:
                mode = value
        return mode

    print(getMean(testData))