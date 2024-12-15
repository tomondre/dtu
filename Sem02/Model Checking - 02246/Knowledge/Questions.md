<details>
<summary>What is Non-Determinism?</summary>
<br>
Abstraction that represents internal decision of the system that are intentionally underspecified (if/else logic) or representation of uncertainty of the environment where the system will operate.
</details>

<details>
<summary>What is the formal definition of non-determinism?</summary>
<br>
|I| > 1  ||  | {s' | s -a> s'}| > 1
</details>

<details>
<summary>What are terminal states?</summary>
<br>
State that has no outgoing transition: Post(s) = {}. Usually represent final states or deadlock states.
</details>

<details>
<summary>What is the formal definition of a transition system?</summary>
<br>
&lt; S, A, ->, L, AP, I &gt;<br>
S is a set of states<br>
A is a set of Actions<br>
-> belongs to S x A x S is a set of transitions<br>
L : S -> 2^AP is a labeling function<br>
AP is a finite set of "Atomic Propositions"<br>
I is a set of initial states
</details>

<details>
<summary>What is forward and backward reachability of a transition system?</summary>
<br>
Post(s) = { s' | Ea.s -a> s'} = The set of direct successors of a state s is defined.<br>
Pre(s) = { s' | Ea.s' -a> s}
</details>

<details>
<summary>What is an execution?</summary>
<br>
Sequence of transitions.<br>
E.g., s0 -click> s1 -click> s0 -click>.<br>
Execution is finite/infinite if the sequence is finite/infinite.
</details>

<details>
<summary>What is Maximal execution?</summary>
<br>
It is one that cannot be extended: either it is finite and the last state is a terminal state, or it is infinite.
</details>

<details>
<summary>What is a trace?</summary>
<br>
It is an execution with replaced states for atomic propositions.
</details>

<details>
<summary>What benefits does Computation Trees have over Linear Traces?</summary>
<br>
- Computation trees represent non-deterministic behavior naturally.<br>
- Computation trees can model future possibilities.
</details>

<details>
<summary>What is State Space Explosion?</summary>
<br>
The size of the interleaving of n transition systems of m states is m^n.
</details>

<details>
<summary>What is system composition?</summary>
<br>
Can be obtained in two ways:<br>
- Build TS(S1) and TS(S2), then compose.<br>
- Build composed TS directly from S1, S2.
</details>

<details>
<summary>What are the main components of propositional logic?</summary>
<br>
- Propositional (or Boolean) variables<br>
- Truth constants<br>
- ¬ Negation (“not”)<br>
- ∨ Disjunction (“or”)<br>
- ∧ Conjunction (“and”)<br>
- → Implication (“if...then...”)<br>
- ↔ Bi-implication (“if and only if”)
</details>

<details>
<summary>What is CNF?</summary>
<br>
Conjunctive Normal Form.<br>
Consists of conjunction of clauses = constraints on formula variables.<br>
Uses only propositional variables p, negation, disjunction, and conjunction.<br>
Used in SAT solvers.
</details>

How do you translate implication and biimplication to CNF form?
a -> b = !a OR ~B
a <-> b = (!p OR q) AND (!q OR p)

What are the ascii alternative to CTL grammar?
- ◯ X
- ◊    F
- □  G

<details>
<summary>When is formula satisfiable?</summary>
<br>
If there exists a valuation v such that v(phi) = T.<br>
No models if unsatisfiable.<br>
E.g., (_x_ → _y_) → _y_.
</details>

<details>
<summary>When is formula unsatisfiable?</summary>
<br>
The formula is valid but no model can be constructed.<br>
E.g., x ∧ (x → y) ↔ y.
</details>

<details>
<summary>When is formula valid?</summary>
<br>
If for all valuations v, it holds that v(phi) = T.<br>
At least one v is not a model.<br>
E.g., _x_ ∧ (_x_ → _y_) ↔ _y_.
</details>

<details>
<summary>When is formula not valid (invalid)?</summary>
<br>
At least one model created is not a model.<br>
E.g., x ∧ ¬y ∧ (x → y).
</details>

<details>
<summary>When are formulas equivalent?</summary>
<br>
If v(phi) = v(gamma) for all valuations v.<br>
E.g., (to be elaborated).
</details>

<details>
<summary>What is propositional logic?</summary>
<br>
(To be elaborated)
</details>

<details>
<summary>What are the derived operators in propositional logic?</summary>
<br>
- true<br>
- false = !true<br>
- p<br>
- not(phi)<br>
- phi1 or phi2<br>
- phi1 and phi2 = not(not(phi) or not(phi2))<br>
- phi -> phi2 = not(phi1) or phi2
</details>

<details>
<summary>What does LTL stand for?</summary>
<br>
Linear Temporal Logic.
</details>

<details>
<summary>What are LTL operators?</summary>
<br>
- ◯ϕ = next = from the next state, the execution satisfies ϕ.<br>
- ◊ϕ = eventually or finally = some suffix of the execution satisfies ϕ.<br>
- □ϕ = always = all states in the execution satisfy ϕ.<br>
- ϕ1𝖴ϕ2 = until = ϕ1 holds in some state of the execution and until then all states satisfy ϕ1.
</details>

<details>
<summary>What is a witness?</summary>
<br>
Witness for a formula is an explanation of why it holds.
</details>

<details>
<summary>What is a Counterexample?</summary>
<br>
Explanation of why it does not hold.<br>
- Lasso: Finite initial path fragment ending in state s.<br>
- Loop starting and ending at s.
</details>

What is Lasso?

<details>
<summary>What is CTL?</summary>
<br>
Computational Tree Logic.
</details>

<details>
<summary>How is CTL different from LTL?</summary>
<br>
CTL adds two quantifiers on top of LTL: ∃ (some) and ∀ (all).
</details>

<details>
<summary>What is a satisfaction set?</summary>
<br>
Set of states that satisfy the formula.<br>
sat(phi) = { s | s |= phi}.
</details>

<details>
<summary>When does a transition system satisfy a formula in terms of initial states?</summary>
<br>
If all initial states satisfy the formula.<br>
_T_ ⊧ _ϕ_ iff ∀_s_ ∈ _I_. _s_ ⊧ _ϕ_.<br>
_T_ ⊧ _ϕ_ iff _I_ ⊆ _sat_(_ϕ_).
</details>

<details>
<summary>When are two formulas equivalent?</summary>
If their validity (hold/not-hold) is the same for all transition systems.<br>
_T_ ⊧ ϕ1 iff T ⊧ ϕ2.
</details>

What is the difference Temporal logic a Propositional Logic
* Temporal is Exetension of Propositional

What is the difference between state formulas and path formulas?

How is CTL different from CTL*?

What is bounded Model Checking?
Searches for counterexample in executions whose length is smaller or equal than k, called bounded witness

What is counterexample for AGφ in BMC?
EF!φ

What is counterexample for AFφ in BMC?
EG!φ

How are loops handled in BMC?

What is SMT?
Satisfiability Modulo Theories. Extends SAT solvers

How is SMT different from SAT?
SMT Supports domain-specific reasoning to determine satisfiability of formulas that involve theories. Instead of boolea, we can use contrastrints like functions, inequaliotyies, arithmetic,...

What is ψ in CTL?
A path formula

What is ϕ in CTL?
Path quanitifier

What is ECTL?
Existential normal form

How does bottom-up computation work?
1. Find satisfaction set (states where the property hold)
2. For each subformula, compute set of states where to formula holds
3. Combine the results from subformulas to evaluate the full formula

Algorithm for EF?


... More algorithms from lecture 6?
... Fixpoint computation?


What is a bisimulation?
Relation used for proving equivalence or refinement between systems and verification of properties

What are the comparisons in bisimulation?
1. Each initial state is realted to at least another initial staate
2. Related states have the same labels
3. If T and T' are in related states, then T' can mimic T
4. T can also mimic T'

What are the properties of bisimlarity?
It is reflective, symmetric, transitive

What is bisimulation quotient?

What does DMTC stand for?

What is Discrete Markov Chain?
Tuple
* S - finite, not empty set of states
* P : S X S -> [0,1] - probabilistic transition function, such that the sum of probabilities of moving from s to s' in one step is 1
* _ι_ - initial distribution, summed up to 1
* AP - set of atomic propositions
* L is a labeling function

What is transition distribution?
Probability distribution over the states at a specific time step n. Describes how the probabilities of being in each state evolve over time

What is a steady state?
When a probability distribution over the states remains unchanged

What is a cylinder set?
Subset of sample space that corresponds to paths that share the common finite prefix.

What is a rachable part in transition system?
Set of all states that can be reached from the initial states by following the transitions of the system

Alignments?

DPLL(T)?

How to choose k?

What is PCTL?

When are two systems bisimilar?
1. Each initial state is related to at least another initial state
2. Related states have the same label
3. If T and T' are in related states, then T' can mimic T
4. Vice versa, T can mimic T'

What is equivalence class?
Used in bisimilarity, two  classess are in the same equivalence class if they have the same labels and



Go through:
* Minimizing a given transition system