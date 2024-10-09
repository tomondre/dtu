
* Token needs to be created in case the transition is not active. This will set m to m++
* Last token is also consumed in the petri net. Increase c++
* The algorithm checks for the discrepancy between consumed and produced tokens
* Include produce and consume in the start of the petri net
* When a token is left in petrinet after full execution, r (remaining) needs to be incremented. This is done at the end of the algorithm
* Only tokens produced by transition are counted for p (produced)
