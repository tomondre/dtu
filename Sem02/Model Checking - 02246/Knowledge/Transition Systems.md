Parent: [[Models]]

Transition system is a formal model used to describe the dynamics of system in terms of states and transitions between those states
< S, A, ->, L, AP, I >
* S is a set of states
* A is a set of Actions
* ->  belongs to S x A x S is a set of transitions
* L : S -> 2 ^AP is a labelling function
* AP is a finiste state of "Atomic Proposition"
* I is a set of initial states


Atomic proposition is a statement that is indivisible and is either true or false.

![[Pasted image 20241209090931.png]]
S = {ON, OFF}
A = {click}
L = L{ S0 -> {on}, S1 -> {OFF} }
T = {S0 -> click -> S1, S1 -> click -> S0}

Forward and backward reachability
Post(s) = { s' | Ea.s -a> s'} = The set of direct successors of a state s is defined
Pre(s) = { s' | Ea.s' -a> s}

# Determinisim
The model is action-determinisitc if:
* There is no more than 1 initial state |I| <= 1
* For every state s and every action a, there is only one outgoing transition from s labelled with a

# Terminal States
State is terminal state if it has no outgoing transition
Formally 
Post(s) = empty set

**Systems with no terminals**: Just put self-loop at the end

# Semantics
## Executions
An execution fragment is a sequence of transitions
s0 -click> s1 -click> s0 -click> ...

An execution is fininte/infinite if the sequence is finite/infinite
s0 -> s1 -> s0

Execution is initial if the first state in the sequence is in i

Execution is maximal if it cannot be extended: Either it is finite and the last state is terminal state

## Traces

Replacing every stat in an execution by its atomic properties yields a trace
Even the transitions can be dropped

# Computation Trees
* Executions and traces are not appropriate if we want to se how the system make choices
* Tree whose nodes are states or atomic propositions
* Each state has each immediate successor as a successor

# Model Properties
* Safety properties: Reponsible for checking whether something "bad" happens
	* 
* Liveness properties: Checking the progress of the system
	* Something good will happen in the future