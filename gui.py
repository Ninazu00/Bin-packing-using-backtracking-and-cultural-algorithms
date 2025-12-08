import tkinter as tk
import time
import culturalAlgorithm
import backtrackingAlgorithm
from tkinter import ttk, messagebox

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("1D Bin Packing Solver")
        self.root.geometry("1920x1080")
        #Graph frame
        self.binGraphFrame = tk.Frame(self.root)
        #Left graph for backtracking
        self.leftFrame = tk.Frame(self.binGraphFrame)
        self.leftFrame.pack(side="left", padx=20)
        self.leftLabel =  tk.Label(self.leftFrame, text="Backtracking algorithm result", font=("Courier", 16))
        self.leftLabel.pack()
        self.binGraphLeft = tk.Text(self.leftFrame, font=("Courier", 16), width=45)
        self.binGraphLeft.pack(padx=20, pady=20)
        #Right graph for cultural algorithm
        self.rightFrame = tk.Frame(self.binGraphFrame)
        self.rightFrame.pack(side="left", padx=20)
        self.rightLabel = tk.Label(self.rightFrame, text="Cultural algorithm result", font=("Courier", 16))
        self.rightLabel.pack()
        self.binGraphRight = tk.Text(self.rightFrame, font=("Courier", 16), width=45)
        self.binGraphRight.pack(padx=20, pady=20)

        # Container for all controls (instructions + inputs + dropdown)
        self.topFrame = tk.Frame(self.root)
        self.topFrame.pack(side="top", pady=20)
        #Container for all algorithm graphs
        self.binGraphFrame.pack(expand=True)
        # Instructions
        self.instructions = tk.Label(
            self.topFrame,
            text=("1D Bin Packing Solver\nEnter the minimum and maximum item sizes, then choose an algorithm to run.\nThe solver will pack items into bins of fixed capacity and show the bin usage."),
            font=("Helvetica", 14),
            justify="center")
        self.instructions.pack(pady=10)

        # Min/Max inputs
        self.inputFrame = tk.Frame(self.topFrame)
        self.inputFrame.pack(pady=10)

        tk.Label(self.inputFrame, text="Min Item Size:").grid(row=0,column=0, padx=10)
        self.entMinSize = tk.Entry(self.inputFrame, width=10)
        self.entMinSize.grid(row=0, column=1,padx=10)
        tk.Label(self.inputFrame, text="Max Item Size:").grid(row=0,column=2, padx=10)
        self.entMaxSize = tk.Entry(self.inputFrame, width=10)
        self.entMaxSize.grid(row=0, column=3,padx=10)
        tk.Label(self.inputFrame, text="Number of Items:").grid(row=0, column=4, padx=10)
        self.itemNumber = tk.Entry(self.inputFrame, width=10)
        self.itemNumber.grid(row=0, column=5, padx=10)

        # Dropdown menu for algorithms
        self.algoFrame = tk.Frame(self.topFrame)
        self.algoFrame.pack(pady=10)
        tk.Label(self.algoFrame,text="Select Algorithm:").pack()

        # variable to hold selected algorithm
        self.selectedAlgo = tk.StringVar(self.root)
        self.selectedAlgo.set("Backtracking Algorithm") # default
        self.algoOptions = ["Backtracking Algorithm","Cultural Algorithm","Both"] # List of options

        # remember last selection
        self.lastSelection = {"value": self.selectedAlgo.get()}

        self.algoDropdown = ttk.OptionMenu(
            self.algoFrame,
            self.selectedAlgo,
            self.selectedAlgo.get(), # default shown value
            *self.algoOptions,
            command=self.whenAlgoChange)
        self.algoDropdown.pack(pady=5)

        self.runButton = tk.Button(self.topFrame, text="Run", font=("Helvetica", 14), command=self.runAlgorithm)
        self.runButton.pack(pady=20)

        self.btTimeLabel = tk.Label(self.leftFrame, text="Backtracking time: 0 ms")
        self.btTimeLabel.pack()
        self.btBinsLabel = tk.Label(self.leftFrame, text="Backtracking bins: 0")
        self.btBinsLabel.pack()

        self.caTimeLabel = tk.Label(self.rightFrame, text="Cultural Algorithm time: 0 ms")
        self.caTimeLabel.pack()
        self.caBinsLabel = tk.Label(self.rightFrame, text="Cultural Algorithm bins: 0")
        self.caBinsLabel.pack()
    
    def whenAlgoChange(self, choice):
        # choice is the new value selected from the dropdown
        if choice == self.lastSelection["value"]:
            return # the same option is selected again, nothing will change
        # update selection value
        self.lastSelection["value"] = choice
        self.selectedAlgo.set(choice)

    def drawBinFillLeft(self,fillRate, binNumber):
        barlength = 20
        filled = int(fillRate*barlength)
        empty = barlength - filled
        bar = f"Bin {binNumber} : "
        bar += "|" + ("█"*filled) + ("-"*empty) + "| " + str(fillRate*100) + "%"
        newText = "\n" + bar
        self.binGraphLeft.config(state="normal")
        self.binGraphLeft.insert("end", newText + "\n")
        self.binGraphLeft.config(state="disabled")
        self.binGraphLeft.see("end")
        return bar
    
    def drawBinFillRight(self, bestSolution):
        for binNumber, binItems in enumerate(bestSolution, start=1):
            binCapacityUsed = sum(binItems)
            binCapacityTotal = self.binCapacity 
            barlength = 20
            fillRate = binCapacityUsed / binCapacityTotal
            filled = int(fillRate * barlength)
            empty = barlength - filled
            bar = f"Bin {binNumber} : "
            bar += "|" + ("█"*filled) + ("-"*empty) + "| " + f"{fillRate*100:.1f}%"
            self.binGraphRight.insert("end", bar + "\n")        
        self.binGraphRight.config(state="disabled")
        self.binGraphRight.see("end")
        return bar

    def runAlgorithm(self):
        minSize = int(self.entMinSize.get())
        maxSize = int(self.entMaxSize.get())
        numItems = int(self.itemNumber.get())
        binSize = 10
        choice =  self.algoDropdown = ttk.OptionMenu.get()

        items = culturalAlgorithm.initializeTotalItems(minSize, maxSize, numItems)

        if choice == "Backtracking":
            start = time.time()
            solBT = backtrackingAlgorithm.solveBinPacking(items, binSize)
            end = time.time()
            btTime = (end - start) * 1000.0

            test.btTimeLabel.config(text=f"Backtracking time: {btTime:.2f} ms")
            test.btBinsLabel.config(text=f"Backtracking bins: {len(solBT)}")

        elif choice == "Cultural Algorithm":
            start = time.time()
            solCA = culturalAlgorithm.generateBinCulturalAlgorithm(100, 50, 0.2, numItems, binSize)
            end = time.time()
            caTime = (end - start) * 1000.0

            test.caTimeLabel.config(text=f"Cultural Algorithm time: {caTime:.2f} ms")
            test.caBinsLabel.config(text=f"Cultural Algorithm bins: {len(solCA)}")

        else:  

            startBT = time.time()
            solBT = backtrackingAlgorithm.solveBinPacking(items, binSize)
            endBT = time.time()

            startCA = time.time()
            solCA = culturalAlgorithm.generateBinCulturalAlgorithm(100, 50, 0.2, numItems, binSize)
            endCA = time.time()

            btTime = (endBT - startBT) * 1000.0
            caTime = (endCA - startCA) * 1000.0

            test.btTimeLabel.config(text=f"Backtracking time: {btTime:.2f} ms")
            test.btBinsLabel.config(text=f"Backtracking bins: {len(solBT)}")

            test.caTimeLabel.config(text=f"Cultural Algorithm time: {caTime:.2f} ms")
            test.caBinsLabel.config(text=f"Cultural Algorithm bins: {len(solCA)}")

    
    

test = GUI()

# Container for all controls (instructions + inputs + dropdown)
topFrame = tk.Frame(test.root)
topFrame.pack(side="top", pady=20)

# Instructions
instructions = tk.Label(
    topFrame,
    text=("1D Bin Packing Solver\nEnter the minimum and maximum item sizes, then choose an algorithm to run.\nThe solver will pack items into bins of fixed capacity and show the bin usage."),
    font=("Helvetica", 14),
    justify="center")
instructions.pack(pady=10)

# Min/Max inputs
inputFrame = tk.Frame(topFrame)
inputFrame.pack(pady=10)

tk.Label(inputFrame, text="Min Item Size:").grid(row=0,column=0, padx=10)
entMinSize =tk.Entry(inputFrame, width=10)
entMinSize.grid(row=0, column=1,padx=10)
tk.Label(inputFrame, text="Max Item Size:").grid(row=0,column=2, padx=10)
entMaxSize = tk.Entry(inputFrame, width=10)
entMaxSize.grid(row=0, column=3,padx=10)

# Dropdown menu for algorithms
algoFrame = tk.Frame(topFrame)
algoFrame.pack(pady=10)
tk.Label(algoFrame,text="Select Algorithm:").pack()

# variable to hold selected algorithm
selectedAlgo = tk.StringVar(test.root)
selectedAlgo.set("Backtracking Algorithm")  # default
algoOptions = ["Backtracking Algorithm","Cultural Algorithm","Both"] # List of options


# remember last selection
lastSelection = {"value": selectedAlgo.get()}

def whenAlgoChange(choice):
    # choice is the new value selected from the dropdown
    if choice == lastSelection["value"]:
        return # the same option is selected again, nothing will change
    # update selection value
    lastSelection["value"] = choice
    selectedAlgo.set(choice)

algoDropdown = ttk.OptionMenu(
    algoFrame,
    selectedAlgo,
    selectedAlgo.get(), # default shown value
    *algoOptions,
    command=whenAlgoChange)
algoDropdown.pack(pady=5)

test.root.mainloop()
'''
    def drawBinFillRight(self,bestSolution):
        for binNumber, binItems in enumerate(bestSolution, start=1):
            binCapacityUsed = sum(binItems)
            binCapacityTotal = self.binCapacity 
            barlength = 20
            filled = int(fillRate * barlength)
            empty = barlength - filled
            bar = f"Bin {binNumber} : "
            bar += "|" + ("█"*filled) + ("-"*empty) + "| " + f"{fillRate*100:.1f}%"
            self.binGraphRight.insert("end", bar + "\n")        
        self.binGraphRight.config(state="disabled")
        self.binGraphRight.see("end")
        return bar
'''