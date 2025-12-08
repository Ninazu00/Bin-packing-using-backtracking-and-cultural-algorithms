import culturalAlgorithm
import gui
import time

GUI = gui.GUI()
#Backtracking testing


#Fine tuning variables for the cultural algorithm
populationSize = 50
mutationRate = 0.1
maxGenerations = 100
#Generates the list of items based on parameters given by the user
minBinSize = 3
maxBinSize = 7
numberOfItems = 25
totalItems = culturalAlgorithm.initializeTotalItems(minBinSize,maxBinSize,numberOfItems)
#User inputted value for the bin size
binSize = 10
bestBin = culturalAlgorithm.Individual()
#Starting time before running the cultural algorithm
startTimeCA = time.time()
#Calls the cultural algorithm
culturalAlgorithm.culturalAlgorithmFullSolve(populationSize,mutationRate,maxGenerations,totalItems,binSize,bestBin,GUI)
#Calculates the time it took the cultural algorithm to run
elapsedTimeCA = time.time()- startTimeCA
print("Time elapsed: ", elapsedTimeCA)

GUI.root.mainloop()