1. First diagram is a deterministic automata, as the number of inputs is 1 for 
each. If the 

2. The diagram is non-deterministic, as two outputs for the same action results exists
* In a case of string "a", the result is the action on the left point, without success state
* In a case of string "a" ending with "b", the result may either be in left point, or in a 
success state (this decision is non-deterministic).
* In a case of string "b", the result is either success or not - again, non deterministic. 
The message can recursively recurse on the left and right point, resulting in either success or not.

3. 
* In a case of "b, c" the action would end in success state. 
* In a case of "a" and ending "c, a" the state would end up on a right action. 
* In a case of "a" and getting "b" at the end, the end up state is success state 
