testData = [3, 4, 4, 2, 2, 2, 5, 6, 7, 7]
import math

class Stats:
    def __init__(self, dataset):
        if not isinstance(dataset, list):
            raise TypeError("Expected", type(dataset), "received", type(dataset))
        if dataset == []:
            raise ValueError("No data detected")
        self._dataset = sorted(dataset)
        self._sum = sum(dataset)
        self._mean = None
        self._median = None
        self._mode = None
        self._range = None
        self._variance = None
        self._standardDeviation = None

    def mean(self):
        if self._mean != None:
            return self._mean
        
        self._mean = self._sum/len(self._dataset)
        return self._mean

    def median(self):
        if self._median != None:
            return self._median
        
        if len(self._dataset)%2 == 0:
            halfLength = len(self._dataset)/2
            self._median = (self._dataset[int(halfLength-1)]+self._dataset[int(halfLength)])/2
        else:
            self._median = self._dataset[int((len(self._dataset)-1)/2)]
        return self._median

    def mode(self):
        frequencyDict = {}

        for v in self._dataset:
            if v in frequencyDict:
                frequencyDict[v] += 1
            else:
                frequencyDict[v] = 1

        highestFrequency = 1
        for value, frequency in frequencyDict.items():
            if frequency>highestFrequency:
                highestFrequency = frequency
                self._mode = value
            if highestFrequency == 1:
                self._mode = "No mode"
        return self._mode
    
    def variance(self):
        if self._mean == None:
            self.mean()
        
        varianceSum = 0

        for v in self._dataset:
            varianceSum += (v-self._mean) ** 2
        self._variance = varianceSum/(len(self._dataset)-1)
        
        return self._variance
        
        

    def standardDeviation(self):
        if self._standardDeviation != None:
            return self.standardDeviation
        if self._mean == None:
            self.mean()
        if self._variance == None:
            self.variance()

        self._standardDeviation = math.sqrt(self._variance)
        return self._standardDeviation



statsTest = Stats(testData)
print("Mean is:", statsTest.mean())
print("Mean is:", statsTest.median())
print("Mode is:", statsTest.mode())
print("Variance is", statsTest.variance())
print("Standard Deviation is", statsTest.standardDeviation())