from itertools import chain, combinations
from collections import defaultdict
from optparse import OptionParser


def returnsubsets(arr):
   
    return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])


def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet):
        _itemSet = set()
        localSet = defaultdict(int)

        for item in itemSet:
                for transaction in transactionList:
                        if item.issubset(transaction):
                                freqSet[item] += 1
                                localSet[item] += 1

        for item, count in localSet.items():
                support = float(count)/len(transactionList)

                if support >= minSupport:
                        _itemSet.add(item)

        return _itemSet


def returnJoinSet(itemSet, length):
        return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


def returnItemSetTransactionList(data_iterator):
    transactionList = list()
    itemSet = set()
    for record in data_iterator:
        transaction = frozenset(record)
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))             
    return itemSet, transactionList


def runApriori(data_iter, minSupport, minConfidence):
    itemSet, transactionList = returnItemSetTransactionList(data_iter)
    print"\n---Initeal CSET (C1)---\n"
    for i in itemSet:
        for item in i:
            print(item),
        print""
    print""       
    freqSet = defaultdict(int)
    largeSet = dict()
    assocRules = dict()
    oneCSet = returnItemsWithMinSupport(itemSet,
                                        transactionList,
                                        minSupport,
                                        freqSet)

    currentLSet = oneCSet
    print"\n---Initeal LSET (L1)---\n"
    for i in currentLSet:
        for item in i:
            print(item),
        print""
    print""   
    k = 2
    while(currentLSet != set([])):
        largeSet[k-1] = currentLSet
        currentLSet = returnJoinSet(currentLSet, k)
        print"---Current CSET (C"+str(k)+")--- \n"
        if(currentLSet==set([])):
            print "SET IS EMPTY"
        for i in currentLSet:
            for item in i:
                print(item),
            print""
        print""

        currentCSet = returnItemsWithMinSupport(currentLSet,
                                                transactionList,
                                                minSupport,
                                                freqSet)
        currentLSet = currentCSet
        print"---Current LSET (L"+str(k)+")---\n"
        if(currentLSet==set([])):
            print "SET IS EMPTY"
        for i in currentLSet:
            for item in i:
                print(item),
            print""   
        print""
        k = k + 1

    def returnSupport(item):
            return (float(freqSet[item])/len(transactionList))*100

    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), returnSupport(item))
                           for item in value])

    toRetRules = []
    for key, value in largeSet.items()[1:]:
        for item in value:
            _subsets = map(frozenset, [x for x in returnsubsets(item)])
            for element in _subsets:
                remain = item.difference(element)
                if len(remain) > 0:
                    confidence = returnSupport(item)/returnSupport(element)
                    if confidence >= minConfidence:
                        
                        toRetRules.append(((tuple(element), tuple(remain)),
                                           confidence*100))
    return toRetItems, toRetRules


def printResults(items, rules):
    print("---frequent itemsets sorted by support---\n")
    for item, support in sorted(items, key=lambda (item, support): support):
        print "item: %s , %.3f" % (str(item), support)
    print "\n---RULES sorted by confidence---\n"
    for rule, confidence in sorted(rules, key=lambda (rule, confidence): confidence):
        pre, post = rule
        print "Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence)


def dataFromFile(fname):
        file_iter = open(fname, 'rU')
        for line in file_iter:
                line = line.strip().rstrip(',')                         
                record = frozenset(line.split(','))
                yield record


if __name__ == "__main__":
   
    print "Running Apriori on first data set"
    
    dataFile="data1"
    inFile = dataFromFile(dataFile)
    minSupport =input("Please enter Minium Support: ")
    minConfidence =input("Please enter Maxium Confidence: ")
    if (minSupport > 1):
        minSupport=minSupport/100.0
    if(minConfidence > 1):
        minConfidence=minConfidence/100.0
    items, rules = runApriori(inFile, minSupport, minConfidence)    
    printResults(items, rules)
    
    print "Running Apriori on Second data set"
    
    dataFile="data2"
    inFile = dataFromFile(dataFile)
    minSupport =input("Please enter Minium Support: ")
    minConfidence =input("Please enter Maxium Confidence: ")
    if (minSupport > 1):
        minSupport=minSupport/100.0
    if(minConfidence > 1):
        minConfidence=minConfidence/100.0
    items, rules = runApriori(inFile, minSupport, minConfidence)    
    printResults(items, rules)
    
    print "Running Apriori on Third data set"
    
    dataFile="data3"
    inFile = dataFromFile(dataFile)
    minSupport =input("Please enter Minium Support: ")
    minConfidence =input("Please enter Maxium Confidence: ")
    if (minSupport > 1):
        minSupport=minSupport/100.0
    if(minConfidence > 1):
        minConfidence=minConfidence/100.0
    items, rules = runApriori(inFile, minSupport, minConfidence)    
    printResults(items, rules)
    
    print "Running Apriori on Forth data set"
    
    dataFile="data4"
    inFile = dataFromFile(dataFile)
    minSupport =input("Please enter Minium Support: ")
    minConfidence =input("Please enter Maxium Confidence: ")
    if (minSupport > 1):
        minSupport=minSupport/100.0
    if(minConfidence > 1):
        minConfidence=minConfidence/100.0
    items, rules = runApriori(inFile, minSupport, minConfidence)    
    printResults(items, rules)
    
    print "Running Apriori on Fifth data set"
    
    dataFile="data5"
    inFile = dataFromFile(dataFile)
    minSupport =input("Please enter Minium Support: ")
    minConfidence =input("Please enter Maxium Confidence: ")
    if (minSupport > 1):
        minSupport=minSupport/100.0
    if(minConfidence > 1):
        minConfidence=minConfidence/100.0
    items, rules = runApriori(inFile, minSupport, minConfidence)    
    printResults(items, rules)