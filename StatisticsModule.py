testData = [3, 4, 4, 2, 2, 2, 5, 6, 7, 7]

class Stats:
    def __init__(self, dataset):
        if not isinstance(dataset, list):
            raise TypeError("Expected", type(dataset), "received", type(dataset))
        if dataset == []:
            raise ValueError("No data detected")
        self._dataset = sorted(dataset)
        self._sum = sum(dataset)

    def mean(self):
        mean = self._sum/len(self._dataset)
        return mean

    def median(self):
        if len(self._dataset)%2 == 0:
            halfLength = len(self._dataset)/2
            median = (self._dataset[int(halfLength-1)]+self._dataset[int(halfLength)])/2
        else:
            median = self._dataset[int((len(self._dataset)-1)/2)]
        return median

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
                mode = value
            if highestFrequency == 1:
                mode = "No mode"
        return mode

statsTest = Stats(testData)
print("Mean is:", statsTest.mean())
print("Mean is:", statsTest.median())
print("Mode is:", statsTest.mode())