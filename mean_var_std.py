import numpy as np

def calculate(list):
    if len(list) < 9:
        print("List must contain nine numbers.")
    else: 
        rshp = np.array(list).reshape(3, 3)
        calculations = {"mean": [], "variance": [], "standard deviation": [], "max": [], 
                    "min": [], "sum": []}
        calculations["mean"].append(np.mean(rshp, axis=0).tolist())
        calculations["mean"].append(np.mean(rshp, axis=1).tolist())
        calculations["mean"].append(np.mean(rshp)) 

        calculations["variance"].append(np.var(rshp, axis = 0).tolist())
        calculations["variance"].append(np.var(rshp, axis = 1).tolist()) 
        calculations["variance"].append(np.var(rshp).tolist())

        calculations["standard deviation"].append(np.std(rshp, axis = 0).tolist())
        calculations["standard deviation"].append(np.std(rshp, axis = 1).tolist()) 
        calculations["standard deviation"].append(np.std(rshp).tolist())

        calculations["max"].append(np.amax(rshp, axis = 0).tolist())
        calculations["max"].append(np.amax(rshp, axis = 1).tolist()) 
        calculations["max"].append(np.amax(rshp).tolist())

        calculations["min"].append(np.amin(rshp, axis = 0).tolist())
        calculations["min"].append(np.amin(rshp, axis = 1).tolist()) 
        calculations["min"].append(np.amin(rshp).tolist())

        calculations["sum"].append(np.sum(rshp, axis = 0).tolist())
        calculations["sum"].append(np.sum(rshp, axis = 1).tolist()) 
        calculations["sum"].append(np.sum(rshp).tolist())

        return calculations
