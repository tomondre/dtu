**System Integration feedback**

  

# Requirements model 

Is the model syntactically correct? 
Perhaphs it is missing a higher-level components like Driver? The reasons for driver has been mentioned in the text, therefore it could be included to ensure higher-level information?
  

Is the model semantically correct? 
The text has mentioned `the process of acquiring a student id remains efficient and accessible to all`, which should be a requirement of the system
  

Is the model consistent with the description? 
Mostly, yes
  

# Enterprise Architecture models 

## Is the business perspective syntactically correct? 
Looks good :)

## Is the business perspective semantically correct? 
The student should also have ability to activate/deactivate the card, as this is mentioned in the observations. The process contains only activation part (although it is included in the module lower in the diagram).

## Is the business perspective consistent with the description and the requirements model? 
Many processes/entities have not been mentioned in the text. Overall, the business model seems to dive deeper into requirements model correctly, explaining more details. 

## Is the application perspective syntactically correct? 
Seems correct :)
## Is the application perspective semantically correct? 
Hard to tell, as I don't really now all the details required. However, it seems like this could be a legit implementation of the system. 

## Is the application perspective consistent with the description? 
Yes.
  

## Is the technology perspective syntactically correct? 
Seems correct.
  

## Is the technology perspective semantically correct? 
One thing that is maybe missing is the database of the CardAdmin and Auth Nodes, as I suspect the application requires it. 
  

## Is the technology perspective consistent with the description? 
Some details are missing in the description, however it's almost impossible to write all the granular information
  

## Are the different perspectives linked together? 
Yes
  

# Workflow models 

  

## Are the models syntactically correct? 
Yes

## Are the models consistent with the description? 
* It seems like the language switching can ocurr only before logging out, which does not seem to be correct
* There are some repetitions in the model: Pin change for example, which could be unified
* Logout seems to be bit redundant to me, as it can be done anytime throughout the process (this could be included in the description)
  

## Are models sound? 
Looks sound
  

## Can all transitions in the models be fired? 
Yes, it seems like so.

## Do the models contain deadlocks? 
Doesn't seem to, as all actions have a possible path to continue on. However, some deadlock may ocurr due to the user actions. 
  

# Interaction models (1) 

  

## Validity of the models 
The text mentiones: `Siyao develop a CCS calculus specification`, however the model used in the figure is  π-calculus/
  

# Interaction models (2) 

## On the type of model selected 
The model selected is 
  

## On recursion:  

## On non-determinism: 

  

## On restriction:  

## On deadlock:  

## On progress:  

  

# Overall 

## To which extent do the models capture the system/process description?
The models seem to capture the description very well. They look at the system from a different perspectives, ensuring comprehensive overview of the system