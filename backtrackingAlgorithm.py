import math
import copy
import time


def sortItems(itemsList):
    return sorted(itemsList, reverse=True)

def placeItem(item, binIndex, usedBins, binRemainingCapacities):
    usedBins[binIndex].append(item)
    binRemainingCapacities[binIndex] -= item

def removeItem(item, binIndex, usedBins, binRemainingCapacities):
    usedBins[binIndex].remove(item)
    binRemainingCapacities[binIndex] += item

def calculateLowerBound(remainingItems, binCapacity):

    totalSize = sum(remainingItems)
    return math.ceil(totalSize / binCapacity)



def copyBins(bins):
    return copy.deepcopy(bins)
  


def pruneBranch(usedBins, bestSolution, remainingItems, binCapacity):
    lowerBound = calculateLowerBound(remainingItems, binCapacity)
    if len(usedBins) + lowerBound >= len(bestSolution):
        return True

    return False


def initializeSolution(items, binCapacity):
    bins = []
    for item in items:
        placed = False
        for b in bins:
            if sum(b) + item <= binCapacity:
                b.append(item)
                placed = True
                break
        if not placed:
            bins.append([item])
    return bins

    pass

def findFeasibleBins(item, binRemainingCapacities):
    indices = []
    for i, remaining in enumerate(binRemainingCapacities):
        if item <= remaining:
            indices.append(i)
    return indices

def backtrack(currentIndex, usedBins, binRemainingCapacities, binCapacity, bestSolution, sortedItemsList):
    # Base case: all items have been placed
    if currentIndex == len(sortedItemsList):
        if len(usedBins) < len(bestSolution):
            bestSolution.clear()
            bestSolution.extend(copyBins(usedBins))
        return

    item = sortedItemsList[currentIndex]

    # Remaining items (including current item) for lower bound pruning
    remainingItems = sortedItemsList[currentIndex:]
    if pruneBranch(usedBins, bestSolution, remainingItems, binCapacity):
        return

    # Try placing in existing bins (all feasible choices)
    feasibleBins = findFeasibleBins(item, binRemainingCapacities)
    for i in feasibleBins:
        placeItem(item, i, usedBins, binRemainingCapacities)
        backtrack(currentIndex + 1, usedBins, binRemainingCapacities,
                  binCapacity, bestSolution, sortedItemsList)
        removeItem(item, i, usedBins, binRemainingCapacities)

    # Try placing in a new bin
    usedBins.append([item])
    binRemainingCapacities.append(binCapacity - item)
    backtrack(currentIndex + 1, usedBins, binRemainingCapacities, binCapacity, bestSolution, sortedItemsList)
    usedBins.pop()
    binRemainingCapacities.pop()


def solveBinPacking(items, binCapacity):
    if binCapacity <= 0:
        raise ValueError("binCapacity must be positive.")
    if any(item <= 0 for item in items):
        raise ValueError("All items must have positive size.")
    if any(item > binCapacity for item in items):
        raise ValueError("Item size cannot exceed binCapacity.")
    
    sortedItems = sortItems(items)
    bestSolution = initializeSolution(sortedItems, binCapacity)
    usedBins = []
    binRemainingCapacities = []
    start = time.time()
    backtrack(0, usedBins, binRemainingCapacities,
              binCapacity, bestSolution, sortedItems)
    end = time.time()
    execTime = (end - start) * 1000.0
    return bestSolution, execTime