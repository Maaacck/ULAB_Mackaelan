# File: twoDimensionalMotion.py 

import numpy as np

g = -9.80665
# Gravity value.

def findTime(initialPosition, initialVelocity):
    """
    Calculates the time it takes to travel vertically. 

    Input: 
    initalPosition - Inital vertical height of bird. 
    initialVelocity - Initial vertical velocity of bird. 
    
    Output:
    time - Time it takes for bird's dropping to reach person. 
    """
    rootedSection = np.sqrt(((initialVelocity**2) - (4*1/2*g*initialPosition)))
    denominator = g
    time = ((initialVelocity - rootedSection) / denominator)
    return time

def distanceToHit(initialPosition, initialVelocity, horizontalVelocity):
    """
    Calculate the distance to hit a person.

    Input:
    initalPosition - Inital vertical height of bird. 
    initialVelocity - Initial vertical velocity of bird. 
    horizontalVelocity - Velocity bird is traveling horizontally. 
    
    Output:
    distance - Distance to hit person. 
    """
    time = findTime(initialPosition, initialVelocity)
    distance = horizontalVelocity * time
    return distance
 
def birdStatus(initialPosition, initialVelocity, horizontalVelocity, distanceBirdsCanTravel):
    """
    Determines if bird will hit person and then make it home (100 meters from person). Assumes they take break after hitting person with droppings. 

    Input:
    initalPosition - Inital vertical height of bird. 
    initialVelocity - Initial vertical velocity of bird. 
    horizontalVelocity - Velocity bird is traveling horizontally. 
    distanceBirdsCanTravel - multi-dimensional array showing distance bird can travel when hitting person and then distance they can travel after taking a break then going home. 

    Output:
    statuses - Shows status of each bird. 
    """
    distance = distanceToHit(initialPosition, initialVelocity, horizontalVelocity)
    statuses = [] 
    for i in range(0, len(distanceBirdsCanTravel)):
        if distanceBirdsCanTravel[i][0] >= distance:
            if distanceBirdsCanTravel[i][1] >= 100:
                statement = "Bird lets out droppings and makes it home."
            else: 
                statement = "Bird lets out droppings but collapses before making it home."
        elif distanceBirdsCanTravel[i][0] == 0: 
            statement = "Bird is asleep."
        else: 
            statement = "Bird does not let out droppings."
        statuses.append(statement)
    return statuses

        