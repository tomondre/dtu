# Lecture 1.2

#### **1. Introduction to Process Models and Modeling Languages**

- **Modeling Languages**:
    - Provide tools for expressing processes.
    - Vary in **expressiveness**, **notation syntax**, and **semantics**.
- **Key Concepts**:
    - Precise definition or understanding of **syntax** and **semantics** is crucial.
    - Models represent behaviors expressed through process executions.

---

#### **2. Understanding Process Model Behavior**

- **Trace Analysis**:
    - A **trace** is a valid sequence of activities described by the process model.
    - Traces can start at multiple points and may not necessarily have defined endpoints.
    - Example of **infinite traces**:
        - Processes with loops can repeat sequences indefinitely.
- **Process Example**:
    - Activities represented as yellow boxes.
    - Gateways (diamonds) introduce branching behavior.
        - **Forking behavior**: Execution may follow one of several edges.
    - **Notational Context**:
        - Example notation used: **BPMN**.
        - Activities are labeled (e.g., A to H) for clarity.

---

#### **3. Valid Executions and Repeated Activities**

- **Example Valid Executions**:
    1. **Execution 1**:
        - A → B → C → D → G → H
        - Start event to end event, passing through specific activities.
    2. **Execution 2**:
        - A → B (ends here as no defined endpoint is mandatory).
    3. **Execution 3**:
        - A → B → C → D → F → C → D → E → F → C
        - Loops allow repeating activities (e.g., "C" occurs multiple times).

---

#### **4. Transition Systems for Process Models**

- **Label Transition System (LTS)**:
    - **Components**:
        - States (including one initial state).
        - Labels (representing activities).
        - Transition relations (state-to-state transitions labeled with activities).
    - **Example LTS Construction**:
        1. Initial state allows execution of "A".
        2. From the initial state, sequences like A → B → C → D transition through states.
        3. Gateway branching leads to:
            - Path 1: D → G → H (end state).
            - Path 2: D → F → C (repeated).
        4. Compacts knowledge of possible transitions into a visualized system.

---

#### **5. Behavioral Equivalence of Process Models**

- **Importance**:
    - Behavioral equivalence defines when two processes exhibit the same execution behaviors.
    - Several equivalence notions exist depending on the focus (e.g., topology, semantics, or traces).

##### **a. Trace Equivalence**:

- **Definition**:
    - Two models, S₁ and S₂, are trace equivalent if their sets of traces (T₁ and T₂) are identical.
- **Example**:
    - Model S₁ generates traces: `{a, ab, ac}`.
    - Model S₂ generates traces: `{a, ab, ac}`.
    - Result: S₁ and S₂ are trace equivalent.
- **Implications**:
    - Models with different topologies can be trace equivalent if their behaviors produce the same traces.

##### **b. Complete Trace Equivalence**:

- **Definition**:
    - Focuses only on complete traces (sequences that reach a terminal state).
    - Two models are equivalent only if their complete trace sets match.
- **Example**:
    - Model S₁: Complete trace = `{ab}`.
    - Model S₂: Complete traces = `{a, ab}`.
    - Result: Not complete trace equivalent, despite being trace equivalent.

---

#### **6. Key Takeaways on Behavioral Equivalence**

- **Behavioral Equivalence Notions**:
    - Trace equivalence considers all trace possibilities (including partial ones).
    - Complete trace equivalence is stricter, focusing solely on terminal behaviors.
- **Applications**:
    - Helps determine the similarity of models in terms of execution behavior, despite structural differences.


# Lecture 1.3
#### **1. Introduction to Petri Nets**

- **Definition**:
    - A formal language for describing **concurrent systems**.
    - Created by **Carl Adam Petri** in the early 1960s.
- **Features**:
    - Includes both **formal modeling notation** and **graphical representation**, which are equivalent.
    - Allows both **graphical model definition** and **mathematical analysis**.
- **Applications**:
    - Widely used in process modeling and systems analysis.
    - Supports extensions and variations for different use cases.

---

#### **2. Graphical Representation of Petri Nets**

- **Structure**:
    - Represented as a **directed bipartite graph**.
    - Two types of nodes:
        - **Places**: Represented by **circles**.
        - **Transitions**: Represented by **squares**.
    - **Arcs**:
        - Connect **places to transitions** or **transitions to places**.
        - Direct connections between two places or two transitions are not allowed.
- **Example**:
    - Seven places (e.g., B1B_1B1​ to B7B_7B7​).
    - Five transitions (e.g., T1T_1T1​ to T5T_5T5​), each labeled with names like "receive order" or "process order."

---

#### **3. Mathematical Representation of Petri Nets**

- **Components**:
    - PPP: A finite set of **places**.
    - TTT: A finite set of **transitions**.
    - FFF: The **flow relation**, a subset of all possible connections between PPP and TTT.
- **Functional Definitions**:
    - **Incoming and Outgoing Nodes**:
        - **Incoming nodes** for a place/transition (∙P\bullet P∙P or ∙T\bullet T∙T).
        - **Outgoing nodes** for a place/transition (P∙P\bulletP∙ or T∙T\bulletT∙).

---

#### **4. Dynamic Behavior of Petri Nets**

- **Marking**:
    - Describes the **state** of the system.
    - **Tokens**:
        - Represented as dots in places.
        - The distribution of tokens across places defines the marking.
    - **Marking Function**:
        - M:P→NM: P \to \mathbb{N}M:P→N, maps each place to the number of tokens it contains.
- **Transition Firing**:
    - A **transition** is **enabled** if:
        - All its incoming places have at least one token.
    - **Effects of Firing**:
        - Consumes one token from each incoming place.
        - Produces one token in each outgoing place.
- **Reachability**:
    - A marking M′M'M′ is **reachable** from MMM if a sequence of transitions leads from MMM to M′M'M′.

#### **5. Key Properties of Transition Firing**

1. **Atomicity**:
    - Transition firing is instantaneous and indivisible.
2. **Non-Determinism**:
    - When multiple transitions are enabled, the Petri net does not specify which will fire.
3. **Token Conservation**:
    - Tokens can be created or consumed during transitions, causing the total number to vary.
4. **Static Topology**:
    - The structure of the Petri net does not change over time.

---

#### **6. Petri Net Systems**

- **Definition**:
    - A Petri net combined with an **initial marking**.
- **Example**:
    - Transition from M1M_1M1​ (e.g., one token in P1P_1P1​) to M3M_3M3​ (e.g., one token in P3P_3P3​) occurs via:
        - T1T_1T1​: Moves the token from P1P_1P1​ to P2P_2P2​.
        - T2T_2T2​: Moves the token from P2P_2P2​ to P3P_3P3​.

---

#### **7. Transition Systems Derived from Petri Nets**

- **Conversion**:
    - A Petri net system can be transformed into a **transition system**.
- **Components**:
    - **States**: Represent all possible markings.
    - **Transitions**: Defined by enabled transitions in the Petri net.
    - **Initial State**: The initial marking of the Petri net.
- **Reachability Graph**:
    - Captures all reachable states and transitions.

---

#### **8. Applications in Business Processes**

- **Mapping Elements**:
    - **Transitions**: Represent activities (e.g., "process order").
    - **Places**: Represent states or configurations of the process.
    - **Tokens**: Represent process instances or artifacts.
- **Workflow Nets**:
    - A specialized form of Petri nets for business processes.
    - Characteristics:
        - One **initial place** (no incoming edges).
        - One **final place** (no outgoing edges).
        - All elements lie on a path from the initial place to the final place.
    - **Example**:
        - Start place ("start") connects to end place ("end") through intermediate transitions and places.

---

#### **9. Extensions and Variations**

- **Silent Transitions**:
    - Transitions that do not correspond to specific activities but influence control flow.
- **Workflow Net Short-Circuiting**:
    - Adding a transition between the initial and final place ensures strong connectivity, useful for analysis.

# Lecture 2.1
#### **Introduction to Event Logs**

- **Definition**:
    - Event logs record the activities/events performed by software systems and store them for historical and analytical purposes.
- **Purpose**:
    - Answer questions such as:
        - When was a process instance executed?
        - How many instances were executed?
        - Are there patterns that allow process reconstruction?
    - Provide **evidence-based**, unbiased answers without relying on human perception or fragmented knowledge.
- **Importance**:
    - High-quality logs are essential ("garbage in, garbage out" principle).
    - Examples of log entries:
        - Invoice checks, function execution, or message sending with timestamps and parameters.

---

#### **2. Construction of Event Logs**

- **Data Sources**:
    - Logs can be extracted from diverse systems like databases, data warehouses, ERP systems, transaction logs, and even APIs.
- **General Workflow**:
    1. **Extract Data**:
        - Directly from data sources or via a data warehouse using ETL processes.
    2. **Unfiltered Event Log**:
        - Initial extraction containing raw information.
    3. **Filtering**:
        - Clean and refine logs for **process mining** activities.
- **Typical Event Log Structure**:
    - **Process**: Root element representing a collection of cases.
    - **Cases**:
        - Represent process instances, each consisting of a sequence of events.
    - **Events**:
        - Each event belongs to a single case and is characterized by attributes like timestamp, activity name, cost, or resource.

---

#### **3. Event Logs as Trees**

- **Hierarchy**:
    - **Process** → **Cases** → **Events** → **Attributes**.
- **Example Structure**:
    - Root: Process.
    - Children: Cases.
    - Grandchildren: Events within each case.
    - Leaves: Attributes of individual events (e.g., timestamp, activity, urgency).
- **Mapping Event Logs**:
    - Group events sharing the same **Case ID** into a process instance.
    - Sort events within a case using **timestamp**.

---

#### **4. Challenges in Event Log Construction**

- **Heterogeneous Sources**:
    - Logs may come from databases, APIs, or systems like hospital records, trading systems, ERP platforms, or social media interactions.
- **Data Mapping**:
    - Requires context understanding to determine how attributes like sender, timestamp, or subject translate into cases, events, or activities.
    - Example Scenarios:
        1. **Emails**:
            - Group by subject (case).
            - Sender as activity and resource.
        2. **Student Data**:
            - Student ID as case.
            - Exam/course as activity.

---

#### **5. Handling Non-Instantaneous Activities**

- **Multiple Events per Activity**:
    - Example: Start and complete timestamps for an activity.
- **Secondary Correlation**:
    - Necessary to match events to the correct activity instance (e.g., first-in-first-out or contextual clues).
- **Transactional Lifecycle**:
    - May include events like **schedule**, **assign**, **start**, **suspend**, **resume**, **abort**, and **complete**.

---

#### **6. Noise in Event Logs**

- **Types of Noise**:
    1. **Missing Data**:
        - Missing tail, head, or episodes of traces.
    2. **Perturbed Order**:
        - Events swapped due to synchronization delays or buffering issues.
    3. **Duplicated Events**:
        - Multiple recordings of the same event.
    4. **Alien Events**:
        - Extraneous events erroneously included in traces.
- **Impact**:
    - Noise affects process mining outcomes and must be addressed early.
- **Handling Noise**:
    - Assumptions:
        - Noise is rare, allowing filtering of infrequent traces or transitions.
    - Limitations:
        - If noise is not rare, filtering may discard critical rare behaviors.

---

#### **7. Event Logs and Process Mining**

- **Role of Event Logs**:
    - Support discovery, conformance checking, and enhancement of process models.
    - Serve as objective data sources to map real-world processes.
- **Decorating Process Models**:
    - Event log attributes can enrich models with:
        - **Frequency** of activities.
        - **Waiting Time**: Average delay before starting an activity.
        - **Service Time**: Duration of activities.
        - **Cost**: Associated expenses.

---

#### **8. Resource Analysis and Social Networks**

- **Resource Attribution**:
    - Identify roles (e.g., administration, manager) and analyze their activity distribution.
- **Social Network Analysis**:
    - Visualize interactions between resources, e.g., frequency and centrality of communication.

---

#### **9. Storing Event Logs**

- **XES Standard**:
    - XML-based standard for process mining logs.
    - Official IEEE standard.
- **Advantages**:
    - Supported by commercial and open-source tools.
    - Extensible to include domain-specific attributes.
- **Structure**:
    - Similar to tree hierarchy:
        - Logs → Traces → Events → Attributes.
- **Conversion Tools**:
    - Tools exist to convert CSV or other formats into XES.

---

#### **10. Best Practices for Event Log Construction**

- **Context Awareness**:
    - Understand the process and goals before defining mappings.
- **Attribute Richness**:
    - Collect sufficient data to support correlation and analysis.
- **Noise Mitigation**:
    - Use filtering and heuristics judiciously.
- **Leverage Standards**:
    - Use XES for interoperability with mining tools.

# Lecture 2.2
#### **1. Introduction to Control Flow Discovery**

- **Definition**:
    - Connects event logs to process models by **discovering the model** implied in the event log.
- **Input**:
    - **Event Log**: A recording of observed behavior.
- **Output**:
    - A **process model** that abstracts and synthesizes the behavior in the event log.
- **Challenges**:
    - Event logs often do not contain all possible behaviors, requiring discovery techniques to abstract and generalize.

---

#### **2. Quality Dimensions of Discovered Models**

- **Fitness**:
    - Measures how well the model reproduces the behavior observed in the log.
- **Precision**:
    - Ensures the model does not allow behavior not found in the log.
- **Generalization**:
    - The model should generalize behavior while avoiding overfitting.
- **Simplicity**:
    - The model should remain easy to understand and process, balancing complexity and coverage.

---

#### **3. Discovery Example**

- **Example Log L1L_1L1​**:
    - Contains three traces:
        1. ABCDABCDABCD (3 times).
        2. ACBDACBDACBD (2 times).
        3. AEDAEDAED (1 time).
- **Discovery Process**:
    - **Start and End Identification**:
        - All traces start with AAA → Model starts with AAA.
        - All traces end with DDD → Model ends with DDD.
    - **Parallelism and Alternatives**:
        - BBB and CCC occur together in arbitrary order (BCBCBC, CBCBCB).
        - EEE occurs as an alternative to BBB and CCC.
    - **Generated Model**:
        - Parallel paths for BBB and CCC (AND-split).
        - Optional path for EEE, which consumes tokens for BBB and CCC.

---

#### **4. The Alpha Algorithm: Overview**

- **Purpose**:
    - Extract a **workflow net** (Petri net) based on relationships in an event log.
- **Features**:
    - Detects concurrent activities and basic control flow patterns.
    - Provides theoretical insights into control flow discovery.
- **Limitations**:
    - **Noise Sensitivity**:
        - Not robust to noisy or incomplete logs.
    - **Practical Use**:
        - Rarely used directly; extensions like Alpha+ and Alpha++ address some issues.

---

#### **5. Workflow Log Preprocessing**

- **Definition**:
    - A **workflow log** abstracts an event log, recording only the distinct sequences of activity executions.
- **Simplifications**:
    - **No Cardinalities**: Ignores trace frequencies.
    - **No Case IDs**: Focuses on activity sequences.
- **Example**:
    - Event Log:
        - Case 1: ABCDABCDABCD
        - Case 3: ABCDABCDABCD
        - Case 5: AEDAEDAED
    - Workflow Log:
        - ABCD,ACBD,AEDABCD, ACBD, AEDABCD,ACBD,AED.

---

#### **6. Ordering Relationships in Logs**

- **Relationships**:
    1. **Direct Succession** (X→YX \rightarrow YX→Y):
        - XXX is directly followed by YYY in at least one trace.
    2. **Causality** (X↣YX \rightarrowtail YX↣Y):
        - XXX directly precedes YYY, but YYY does not directly precede XXX.
    3. **Parallelism** (X∥YX \parallel YX∥Y):
        - XXX and YYY occur together but in arbitrary order.
    4. **Choice** (X↛YX \nrightarrow YX↛Y and Y↛XY \nrightarrow XY↛X):
        - XXX and YYY do not follow each other in any order.
- **Example**:
    - Log: ABCD,ACBD,AEDABCD, ACBD, AEDABCD,ACBD,AED.
    - Relationships:
        - A↣B,A↣C,E↣FA \rightarrowtail B, A \rightarrowtail C, E \rightarrowtail FA↣B,A↣C,E↣F.
        - B∥CB \parallel CB∥C.

---

#### **7. Control Flow Patterns in Petri Nets**

- **Key Patterns**:
    1. **Sequence**:
        - A↣BA \rightarrowtail BA↣B: Transition from AAA to BBB.
    2. **XOR-Split**:
        - Choice between BBB and CCC after AAA.
    3. **XOR-Join**:
        - CCC enabled after either AAA or BBB.
    4. **AND-Split**:
        - Both BBB and CCC enabled after AAA.
    5. **AND-Join**:
        - CCC requires completion of both AAA and BBB.

---

#### **8. The Alpha Algorithm**

- **Input**:
    - Workflow log LLL.
- **Output**:
    - Workflow net N=(P,T,F)N = (P, T, F)N=(P,T,F) where:
        - PPP: Places.
        - TTT: Transitions.
        - FFF: Flow relations.
- **Steps**:
    1. **Extract Transitions**:
        - TTT: All activities from the workflow log.
    2. **Identify Initial/Final Transitions**:
        - TiT_{i}Ti​: First activity in each trace.
        - ToT_{o}To​: Last activity in each trace.
    3. **Determine Relationships**:
        - **Direct succession**, **causality**, **parallelism**, and **choice**.
    4. **Create Workflow Net**:
        - For each causal relationship A↣BA \rightarrowtail BA↣B, create places and transitions.
        - Add special **input place** and **output place** connected to TiT_{i}Ti​ and ToT_{o}To​.

---

#### **9. Example Execution**

- **Event Log**:
    - ABCD,ACBD,AEDABCD, ACBD, AEDABCD,ACBD,AED.
- **Workflow Log**:
    - ABCD,ACBD,AEDABCD, ACBD, AEDABCD,ACBD,AED.
- **Alpha Algorithm Steps**:
    1. Extract transitions: A,B,C,D,EA, B, C, D, EA,B,C,D,E.
    2. Identify initial/final transitions:
        - Ti={A}T_{i} = \{ A \}Ti​={A}, To={D}T_{o} = \{ D \}To​={D}.
    3. Establish relationships:
        - A↣B,A↣CA \rightarrowtail B, A \rightarrowtail CA↣B,A↣C.
        - B∥CB \parallel CB∥C, E↣FE \rightarrowtail FE↣F.
    4. Construct workflow net:
        - Input place PiP_iPi​, output place PoP_oPo​.
        - Connect transitions based on relationships:
            - Sequence (A→P→BA \to P \to BA→P→B).
            - Parallelism (B∥CB \parallel CB∥C).
            - Sequence (E→FE \to FE→F).

---

#### **10. Summary**

- **Alpha Algorithm**:
    - Provides foundational understanding of control flow discovery.
    - Effective for learning the principles of model synthesis.
- **Limitations**:
    - Sensitive to noise and incomplete logs.
- **Extensions**:
    - Alpha+, Alpha++, and others improve on its core limitations.
- **Relevance**:
    - Helps create **workflow nets** that capture relationships in event logs, laying the foundation for more robust discovery algorithms.


# Lecture 2.3
#### **1. Limitations of the Alpha Algorithm**

- **Completeness Requirement**:
    
    - Requires **workflow logs to be complete** with respect to direct succession relationships.
    - **Implication**:
        - If two tasks are meant to occur in direct succession, the log must include at least one trace reflecting this order.
        - Without completeness, causal relationships between tasks cannot be discovered.
- **Rediscovery Problem**:
    
    - Addresses which models can be rediscovered from workflow logs generated by those models.
    - **Goal**:
        - Identify a class of workflow nets where the discovered model is **structurally and behaviorally equivalent** to the original model.

---

#### **2. Rediscovery and Sound Structured Workflow Nets**

- **Class of Rediscoverable Models**:
    
    - The Alpha algorithm rediscover models that are:
        1. **Sound**.
        2. **Structured**.
        3. Free of **short loops** (loops of length 1 or 2).
    - Assumes the event log is complete regarding direct succession relationships.
- **Structural Limitation: Implicit Places**:
    
    - **Implicit places** (places not explicitly required for process behavior) cannot be discovered.
    - Example:
        - A model with an implicit place and its equivalent model without the place are behaviorally identical, so rediscovery is unaffected.

---

#### **3. Structured Workflow Nets**

- **Definition**:
    - A **structured workflow net**:
        1. Is a workflow net:
            - One **input place** and one **output place**.
            - All transitions lie on a path from the input to the output.
        2. Contains no implicit places.
        3. Satisfies two additional structural properties:
            - **Property 1**:
                - If a place has multiple outgoing connections, the transitions they connect to must have this place as their **only source**.
                - Example:
                    - A place PPP with outgoing transitions T1,T2T_1, T_2T1​,T2​ must be the sole source for both T1T_1T1​ and T2T_2T2​.
            - **Property 2**:
                - If a transition has multiple incoming connections, the places feeding this transition must connect **only to that transition**.
                - Example:
                    - Transition TTT with incoming places P1,P2P_1, P_2P1​,P2​ cannot have P1P_1P1​ or P2P_2P2​ feeding other transitions.

---

#### **4. Soundness of Workflow Nets**

- **Sound Workflow Systems**:
    - A workflow system is **sound** if:
        1. **Option to Complete**:
            - From any reachable state, a sequence of transitions exists to reach the final state.
        2. **Proper Completion**:
            - Once the final state is reached, it is the **only state** with tokens in the final place.
        3. **No Dead Transitions**:
            - Every transition is reachable from the initial state and contributes to some execution sequence.

---

#### **5. Short Loops and the Alpha Algorithm**

- **Problem with Short Loops**:
    - The Alpha algorithm cannot rediscover workflow nets with **short loops** of length 1 or 2.
    - **Examples**:
        1. **Length 1 Loop**:
            - A task repeats immediately (e.g., A→AA \to AA→A).
            - Rediscovery disconnects the looped task.
        2. **Length 2 Loop**:
            - Two tasks repeat in alternation (e.g., A→B→AA \to B \to AA→B→A).
            - Rediscovery fails to connect tasks correctly.
    - **Longer Loops**:
        - Loops longer than 2 tasks can be rediscovered successfully.

---

#### **6. Summary of Rediscoverable Models**

- The Alpha algorithm successfully rediscover models that:
    1. Are **sound**:
        - Ensure process termination and proper completion.
    2. Are **structured**:
        - Adhere to strict structural properties.
    3. Do not contain **short loops**.
- **Assumption**:
    - The event log is complete regarding direct succession relationships.

---

#### **7. Practical Implications**

- **Benefits**:
    - Provides theoretical insights into the rediscovery of process models.
    - Establishes a foundation for understanding the limitations of control flow discovery.
- **Limitations**:
    - **Completeness Dependency**:
        - Relies on comprehensive logs for accurate rediscovery.
    - **Noise Sensitivity**:
        - Cannot handle noisy or incomplete logs.
    - **Short Loop Issue**:
        - Fails with loops of length 1 or 2.

---

#### **8. Extensions and Alternatives**

- **Improvements**:
    - Variants like Alpha+, Alpha++, and others enhance rediscovery capabilities.
    - Address structural and noise-related issues in specific contexts.
- **Future Directions**:
    - Algorithms robust to noise and incomplete logs provide more practical solutions for real-world data.


# Lecture 3.1: Overview of Noise in Event Logs and the Heuristic Miner Algorithm
#### **1. Noise in Event Logs**

- **Ideal Event Logs**:
    - Contain only valid events related to a single activity and process instance.
    - All traces represent valid execution sequences of the process.
- **Real-World Challenges**:
    - Event logs are often noisy, including:
        - **Incorrectly recorded events**.
        - **Missing entries**.
- **Impact of Noise**:
    - Affects process mining activities, including:
        - Control flow discovery.
        - Conformance checking.
        - Enhancement.
    - Noise is domain-specific and hard to characterize without domain knowledge.

---

#### **2. Example: Noise Impact on Process Models**

- **Two Models**:
    - **Model 1 (Top)**:
        - Restricts behavior by imposing dependencies between AAA and DDD and between BBB and EEE.
        - Example: DDD can only execute if AAA was executed earlier.
    - **Model 2 (Bottom)**:
        - Loosens restrictions, allowing DDD or EEE to execute freely after CCC.
- **Event Log Examples**:
    1. **Log 1**:
        - Traces ACDACDACD (99 times) and BCEBCEBCE (85 times).
        - **Ideal Model**: Top model aligns perfectly with the dominant behavior.
    2. **Log 2**:
        - All four possible executions occur equally.
        - **Ideal Model**: Bottom model captures the broader behavior.
    3. **Log 3**:
        - Mostly consistent with the top model, but 5% violates its restrictions.
        - **Ambiguity**: No clear best model due to noise.

---

#### **3. Noise Assumption in Process Mining**

- **Heuristic Approach**:
    - Assumes that infrequent behavior is noise.
    - Uses behavior frequency to filter out noise during model discovery.
- **Risks**:
    - Assumption may not hold if infrequent behavior is meaningful.
    - Requires careful domain understanding to determine validity of this approach.

---

#### **4. Spaghetti Models**

- **Definition**:
    - Models with excessive connections between activities.
    - Lack abstraction, making them difficult to interpret and analyze.
- **Example**:
    - Real spaghetti model with all activities nearly fully connected, rendering analysis impractical.

---

#### **5. The Heuristic Miner Algorithm**

- **Goal**:
    - Use a pragmatic approach to discover process models robust to noise.
- **Key Features**:
    - Exploits trace frequency to estimate probabilities of activity relations.
    - Builds on the dependency relations of the Alpha algorithm.

---

#### **6. Dependency Graph Construction**

- **Dependency Graph**:
    
    - Nodes represent activities.
    - Directed edges represent causal relationships between activities.
    - Special nodes for **start** and **end** may be included.
- **Example**:
    
    - Event Log:
        - ABCD,ACBD,AED,...ABCD, ACBD, AED, ...ABCD,ACBD,AED,...
    - Steps:
        1. Extract direct following relationships.
        2. Identify causal relationships.
        3. Build dependency graph with nodes and edges.

---

#### **7. Frequency and Dependency Measures**

- **Frequency Table**:
    
    - Records how often each direct following relationship occurs in the log.
    - Example:
        - A→BA \to BA→B: 11 times.
        - A→EA \to EA→E: 5 times.
- **Dependency Measure**:
    
    - Quantifies causal strength between activities.
    - Formula: Dependency(A,X)=Freq(A→X)−Freq(X→A)Freq(A→X)+Freq(X→A)+1\text{Dependency}(A, X) = \frac{\text{Freq}(A \to X) - \text{Freq}(X \to A)}{\text{Freq}(A \to X) + \text{Freq}(X \to A) + 1}Dependency(A,X)=Freq(A→X)+Freq(X→A)+1Freq(A→X)−Freq(X→A)​
    - **Interpretation**:
        - Near **1**: Strong causality (A→XA \to XA→X).
        - Near **0**: Parallelism (A∥XA \parallel XA∥X).
        - Near **-1**: Reverse causality (X→AX \to AX→A).

---

#### **8. Robustness Against Noise**

- **Thresholding**:
    - Apply thresholds to filter out low-frequency relations and weak dependencies.
    - Example:
        - Direct succession threshold: Minimum number of occurrences.
        - Dependency threshold: Minimum dependency strength.
    - Results:
        - Removes noisy relationships, simplifying the model.

---

#### **9. Example of Mining with Thresholds**

- **Event Log**:
    - ABCD,ACBD,AEDABCD, ACBD, AEDABCD,ACBD,AED with varying frequencies.
- **Thresholds**:
    - Direct succession threshold: 5.
    - Dependency threshold: 0.9.
- **Outcome**:
    - Weak connections (e.g., A→EA \to EA→E, D→DD \to DD→D) are removed.
    - Resulting graph is more readable and robust.

---

#### **10. Key Takeaways**

- **Strengths**:
    - Effective for noisy logs, assuming infrequent behavior is noise.
    - Provides meaningful insights into causal relationships through frequency analysis.
- **Limitations**:
    - Heavily depends on frequency assumptions.
    - May discard rare but meaningful behavior.
- **Domain Knowledge**:
    - Essential to validate assumptions and interpret results appropriately.

# Lecture 3.2 Overview of the Fuzzy Miner Algorithm for Process Mining
#### **1. Noise and Challenges in Process Mining**

- **Types of Noise**:
    - **Infrequent Behavior**:
        - Rare sequences of activities.
    - **Spaghetti Models**:
        - Highly varied logs producing overly complex models with excessive connections, making them unreadable and unmanageable.
- **Fuzzy Miner Solution**:
    - Addresses noise by creating **simplified views** of process models, balancing detail and abstraction through:
        1. **Significance**: Identifies important elements.
        2. **Correlation**: Groups related elements.

---

#### **2. Key Concepts in the Fuzzy Miner**

1. **Aggregation**:
    - Cluster similar elements in the process to simplify representation.
2. **Abstraction**:
    - Hide low-detail or insignificant information.
3. **Emphasis**:
    - Highlight highly significant elements for clarity.
4. **Customization**:
    - Enable interactive views, adaptable to different analysis contexts.

- **Metaphor**: The **map analogy**:
    - Just like a street map abstracts and highlights important roads (e.g., highways), the Fuzzy Miner creates simplified models for process analysis.

---

#### **3. Workflow of the Fuzzy Miner**

1. **Starting Point**:
    - Use **ordering relations** from the Alpha algorithm to create a **dependency graph**:
        - Nodes: Represent activities.
        - Edges: Represent causal relationships.
2. **Matrices**:
    - Use **Significance** and **Correlation** matrices to refine the dependency graph.
3. **Model Transformation**:
    - Iteratively simplify the graph by:
        1. **Filtering edges** based on significance.
        2. **Clustering and abstracting tasks** based on correlation.

---

#### **4. Matrices Used by the Fuzzy Miner**

- **Significance Matrices**:
    
    - Determine which tasks and relationships are important based on specific metrics.
    
    1. **Frequency Significance**:
        - Task importance is proportional to its occurrence frequency in the log.
        - Example: High-frequency housekeeping tasks (e.g., "send email") may not be significant in all contexts.
    2. **Routing Significance**:
        - Tasks guiding splits or synchronizations are more significant than those in simple sequences.
    3. **Relation Significance**:
        - Importance of direct succession relationships between task pairs.
- **Correlation Matrices**:
    
    - Assess how closely tasks are related:
    
    1. **Proximity Correlation**:
        - Average temporal distance between two tasks.
    2. **Originator Correlation**:
        - Whether tasks are performed by the same roles or resources.
    3. **Data Type Correlation**:
        - Whether tasks contribute to the same data objects.

---

#### **5. Simplifying the Dependency Graph**

- **Edge Filtering**:
    
    - Remove edges with low **significance** to simplify the model.
    - Avoid isolated clusters by introducing a **utility measure**:
        - Retain edges with the highest combined significance and correlation values.
    - Example:
        - From edge frequencies:
            - Filter out weak connections (e.g., H→FH \to FH→F).
        - Result: Simplified graph.
- **Task Aggregation and Abstraction**:
    
    - Identify **victim tasks** (low significance).
    - **Aggregation**:
        - Group victims with highly correlated neighbors.
        - Example: Combine infrequent tasks B,MB, MB,M into a cluster.
    - **Abstraction**:
        - Hide isolated clusters or tasks with no strong correlations.

---

#### **6. Example Process Transformation**

- **Initial Dependency Graph**:
    - All tasks and relationships are included, forming a complex "spaghetti model."
- **Iteration 1**:
    - Use task frequency as a significance measure.
    - Identify clusters of low-significance tasks (e.g., B,MB, MB,M).
- **Final Graph**:
    - Simplified model with:
        - Significant tasks and edges highlighted.
        - Insignificant or uncorrelated tasks aggregated or removed.

---

#### **7. Customization and Interactivity**

- **Interactive Views**:
    - Fuzzy Miner models are customizable for different analysis needs.
    - Example Tool: **ProM**:
        - Allows filtering and adjusting significance thresholds.
        - Dynamic views adapt to user preferences.
        - Extreme abstraction clusters all tasks, reducing the model to start and end points.

---

#### **8. Strengths and Limitations**

- **Strengths**:
    - Handles noisy logs effectively.
    - Flexible through multiple significance and correlation matrices.
    - Interactive and customizable for tailored analysis.
- **Limitations**:
    - Relies on selected thresholds and metrics, which may vary by context.
    - Risk of oversimplification in highly abstracted views.

---

#### **9. Key Takeaways**

- **Noise Robustness**:
    - Combines significance and correlation to identify and handle noise.
- **Interactive Process Discovery**:
    - Enables analysts to create process views that fit their analysis goals.
- **Practical Use**:
    - Effective for real-world noisy logs, provided domain knowledge is applied to guide matrix selection and threshold settings.

# Lecture 3.3 Inductive Miner Algorithm for Process Discovery

---

#### **1. Introduction to Representational Bias in Process Discovery**

- **Significance of Representational Bias**:
    - The formalism used to describe discovered models defines the boundaries of what a discovery algorithm can achieve.
    - Algorithms like the **Heuristic Miner** or **Fuzzy Miner**:
        - Focus on practicality, with limited guarantees about model properties.
    - Algorithms like the **Alpha Miner**:
        - Provide precise characterizations but are limited in flexibility.
- **Inductive Miner**:
    - Produces models as **process trees**, ensuring models are **sound** by construction.
    - Represents a **family of techniques** with implementations tailored for different scenarios, such as handling noise.

---

#### **2. Process Trees: The Formalism of the Inductive Miner**

- **Definition**:
    
    - A hierarchical structure with:
        - **Root node**: Represents the overall process.
        - **Leaves**: Represent process activities.
        - **Inner nodes**: Represent operators that define control flow.
- **Key Operators**:
    
    1. **Sequence**:
        - Activities execute in a defined order.
    2. **Exclusive Choice**:
        - Only one branch is executed.
    3. **Parallel Composition**:
        - Branches execute concurrently.
    4. **Redo Loop**:
        - Allows repetition of a process segment.
- **Mapping Process Trees to Workflow Nets**:
    
    - Leaves (activities) → Transitions.
    - Operators → Patterns:
        - **Sequence**: Sequential transitions.
        - **Exclusive Choice**: XOR-split and XOR-join constructs.
        - **Parallel Composition**: AND-split and AND-join using silent transitions.
        - **Redo Loop**: Loopback constructs.

---

#### **3. Workflow of the Inductive Miner**

- **Divide and Conquer**:
    - Splits event logs iteratively, identifying patterns to build the process tree recursively.

1. **Start with an Event Log**:
    
    - Identify shared patterns or characteristics, such as:
        - A common starting activity.
        - Parallel or exclusive branches.
2. **Dependency Graph**:
    
    - Construct a directed graph representing:
        - Nodes: Activities.
        - Edges: Causal relationships between activities.
3. **Identify Cuts**:
    
    - **Cuts** divide the graph into subcomponents based on control flow patterns.
    - Types of cuts:
        1. **Sequential**: One-way edges crossing the cut.
        2. **Exclusive Choice**: Disconnected components.
        3. **Parallel**: Fully connected components.
        4. **Loop**: Identifiable loopback structures.
4. **Build Process Tree**:
    
    - For each cut, create a corresponding operator in the process tree.
    - Apply recursion to subcomponents to refine the model further.
5. **Generate Workflow Net**:
    
    - Convert the completed process tree into a Petri net representation.

---

#### **4. Example of Process Tree Construction**

- **Event Log**:
    
    - Four traces: ABCD,ABCD,AFCD,AFCDABCD, ABCD, AFCD, AFCDABCD,ABCD,AFCD,AFCD.
- **Steps**:
    
    1. **Identify Shared Behavior**:
        - All traces start with AAA.
        - Construct a sequence node with AAA as the first child.
    2. **Refine Remaining Traces**:
        - Compute the dependency graph for traces after AAA.
        - Identify cuts:
            - **Exclusive Choice**: BCBCBC or FCFCFC.
        - Add an XOR node as the second child of the sequence operator.
    3. **Resolve Loop Structure**:
        - Analyze the dependency graph for traces with FCFCFC.
        - Identify a loop with CCC as the body and FFF as the loopback.
        - Add a loop node to the process tree.
- **Final Process Tree**:
    
    - Sequence AAA:
        - XOR:
            - Sequence BCBCBC.
            - Loop F→CF \to CF→C.

---

#### **5. Types of Cuts in Inductive Miner**

1. **Sequential Cuts**:
    - Edges cross in one direction only.
    - Indicate sequential flow.
2. **Exclusive Choice Cuts**:
    - Components are disconnected.
    - Represent XOR behavior.
3. **Parallel Cuts**:
    - All nodes are interconnected.
    - Indicate concurrent execution.
4. **Loop Cuts**:
    - Contain body and loopback components.
    - Represent iterative behavior.

---

#### **6. Ensuring Soundness**

- **Sound by Construction**:
    - Process trees inherently produce models with:
        - Valid termination.
        - Proper handling of concurrency and loops.
- **Mapping to Workflow Nets**:
    - Ensures the process model is always executable and consistent.

---

#### **7. Extensions of the Inductive Miner**

- **Handling Noise**:
    - Use thresholding to filter out infrequent behavior before constructing the dependency graph.
- **Advanced Operators**:
    - Expand the set of operators to capture more complex behaviors.
- **Specialized Variants**:
    - Variations tailored for specific requirements, such as noise robustness or handling incomplete logs.

---

#### **8. Key Takeaways**

- **Strengths**:
    - Guarantees soundness of discovered models.
    - Ensures models are block-structured and easy to interpret.
    - Flexible through recursive, modular construction.
- **Limitations**:
    - Relies on cuts for model structure, which may not capture all real-world nuances.
    - Requires sufficient event log completeness for effective discovery.


# Lecture 6.1 Overview of Conformance Checking Using Token Replay

---

#### **1. Introduction to Conformance Checking**

- **Definition**:
    - Compares a **reference process model** with **event logs** to identify **discrepancies** between the modeled behavior and observed executions.
- **Purpose**:
    - Detect violations of the reference model.
    - Pinpoint **specific parts** of:
        - The **log** that deviate from the model.
        - The **model** frequently violated by executions.
- **Applications**:
    - **Corporate Governance, Risk, and Compliance (GRC)**:
        - Ensures adherence to standards like ISO 9000.
    - **Process-IT Alignment**:
        - Ensures that information systems and real-world processes are aligned.
    - **Auditing**:
        - Provides **evidence-based validation** for organizational audits.
    - **Compliance with Legal Requirements**:
        - Verifies execution orders and activity constraints imposed by regulations.

---

#### **2. Fitness Measures in Conformance Checking**

- **Goal**:
    - Quantify how well event logs conform to the reference model.
- **Token Replay Fitness Measure**:
    - **Concept**:
        - Replay each trace from the event log on the process model.
        - Check if transitions in the model are **enabled** according to the trace.
    - **Key Indicators**:
        1. **Missing Tokens**:
            - Tokens required to fire a transition that is not enabled.
        2. **Remaining Tokens**:
            - Tokens left in the model after the trace has been fully replayed.

---

#### **3. Token Replay Mechanism**

- **Process**:
    
    1. Start with one token in the initial place of the model.
    2. Replay each trace step-by-step:
        - For each activity in the trace, check if the corresponding transition in the model is enabled.
    3. Detect deviations:
        - **Missing Tokens**:
            - Tokens must be added artificially for a transition to fire.
        - **Remaining Tokens**:
            - Tokens left unused after the replay ends.
- **Examples**:
    
    - **Trace Fully Conforming**:
        - All transitions are enabled when needed.
        - All tokens are consumed by the end.
        - **Fitness Score**: 111 (Perfect fitness).
    - **Trace Not Conforming**:
        - Some transitions are not enabled.
        - Tokens are left unconsumed.
        - **Fitness Score**: Below 111.

---

#### **4. Token Replay Example**

- **Model**:
    - Example process model with labeled transitions and places.
- **Event Log**:
    1. **Conforming Trace**:
        - A→B→D→E→AA \to B \to D \to E \to AA→B→D→E→A:
            - All transitions are enabled at the required time.
            - Ends with a single token in the final place.
            - **Fitness**: 111.
    2. **Non-Conforming Trace**:
        - A→C→H→T→F→AA \to C \to H \to T \to F \to AA→C→H→T→F→A:
            - Transition HHH requires a token in a place where none exist.
            - Transition CCC leaves a token unconsumed in another place.
            - **Fitness**: Below 111 (e.g., missing and remaining tokens affect the score).

---

#### **5. Fitness Calculation Formula**

- **Definition**:
    
    - Combines the proportion of missing tokens and remaining tokens into a normalized fitness score.
    
    Fitness=12(1−Missing TokensConsumed Tokens)+12(1−Remaining TokensProduced Tokens)\text{Fitness} = \frac{1}{2} \left( 1 - \frac{\text{Missing Tokens}}{\text{Consumed Tokens}} \right) + \frac{1}{2} \left( 1 - \frac{\text{Remaining Tokens}}{\text{Produced Tokens}} \right)Fitness=21​(1−Consumed TokensMissing Tokens​)+21​(1−Produced TokensRemaining Tokens​)
- **Components**:
    1. **Missing Tokens** (MiM_iMi​):
        - Tokens that had to be artificially added.
    2. **Remaining Tokens** (RiR_iRi​):
        - Tokens left unconsumed after the trace finishes.
    3. **Consumed Tokens** (CiC_iCi​):
        - Tokens consumed during the replay.
    4. **Produced Tokens** (PiP_iPi​):
        - Tokens produced during the replay.
- **Normalization**:
    - Ensures the fitness score ranges from 000 (no fitness) to 111 (perfect fitness).

---

#### **6. Example Fitness Calculation**

- **Conforming Trace**:
    - **Tokens Consumed**: 666, **Tokens Produced**: 666.
    - **Missing Tokens**: 000, **Remaining Tokens**: 000.
    - Fitness: Fitness=12(1−06)+12(1−06)=1\text{Fitness} = \frac{1}{2} \left( 1 - \frac{0}{6} \right) + \frac{1}{2} \left( 1 - \frac{0}{6} \right) = 1Fitness=21​(1−60​)+21​(1−60​)=1
- **Non-Conforming Trace**:
    - **Tokens Consumed**: 777, **Tokens Produced**: 777.
    - **Missing Tokens**: 111, **Remaining Tokens**: 111.
    - Fitness: Fitness=12(1−17)+12(1−17)≈0.857\text{Fitness} = \frac{1}{2} \left( 1 - \frac{1}{7} \right) + \frac{1}{2} \left( 1 - \frac{1}{7} \right) \approx 0.857Fitness=21​(1−71​)+21​(1−71​)≈0.857

---

#### **7. Feedback from Conformance Checking**

- **Global Feedback**:
    - Provides an overall fitness score for the event log.
    - Single numerical value summarizing conformance.
- **Local Feedback**:
    - Pinpoints:
        - **Transitions** fired without being enabled.
        - **Tokens** left unconsumed or added artificially.
    - Highlights specific hotspots of nonconformity in the model and log.

---

#### **8. Strengths and Limitations**

- **Strengths**:
    - **Granularity**:
        - Identifies both global and local deviations.
    - **Quantifiable**:
        - Produces a numerical fitness score for objective evaluation.
- **Limitations**:
    - **Interpretability**:
        - A single fitness score does not explain the root causes of deviations.
    - **Noise Sensitivity**:
        - May require additional techniques to filter out noise before analysis.

---

#### **9. Key Takeaways**

- Token Replay offers a robust method for conformance checking, ensuring that observed executions align with the reference process model.
- By combining global fitness scores with local feedback, organizations can identify and address both systemic and specific deviations, enhancing compliance, efficiency, and governance.

# Lecture 6.2 Overview of Conformance Checking Using Alignments

---

#### **1. Introduction to Conformance Checking with Alignments**

- **Definition**:
    - A method to assess the **conformance level** of an event log with a reference process model.
    - Focuses on finding **alignments** between:
        - **Traces in the event log**.
        - **Execution sequences** supported by the model.
- **Key Features**:
    - Alignments help detect discrepancies at both **local** (specific deviations) and **global** (overall conformance level) scales.
    - Provides insights into:
        - Activities that deviate in the trace.
        - Areas in the model where violations frequently occur.

---

#### **2. Concept of Alignments**

- **Core Idea**:
    
    - Treat the process model and event log as **sequences of symbols**:
        - **Model execution sequences** and **log traces** become comparable strings of symbols.
    - Align these sequences while preserving the **order** of symbols.
- **Applications**:
    
    - Quantify **conformance** between the log and model.
    - Identify specific points of **nonconformity**.

---

#### **3. Alignments as an Edit Distance Problem**

- **Definition**:
    
    - Alignments compare two sequences by linking their symbols step-by-step.
    - Each **alignment step** connects:
        - A symbol from the **trace**.
        - A symbol from the **model**.
    - **Unaligned symbols** are marked with a **no-move (⊥)** symbol.
- **Real-Life Example**:
    
    1. **Conforming Trace**:
        - A trace perfectly aligns with one of the model's execution sequences.
        - All symbols match.
    2. **Non-Conforming Trace**:
        - Deviations arise when:
            - A symbol in the trace does not exist in the model.
            - The model requires a symbol not found in the trace.

---

#### **4. Steps for Alignment-Based Conformance Checking**

1. **Define Alignments**:
    
    - Establish what constitutes an alignment.
    - Specify the types of moves allowed in an alignment step.
2. **Construct Optimal Alignments**:
    
    - Find the alignment with the **least deviations** between the trace and model execution.
3. **Quantify Conformance**:
    
    - Use the alignment to calculate a conformance score or measure deviations.

---

#### **5. Types of Moves in Alignments**

- **Four Possible Move Types**:
    
    1. **Move in Log**:
        - Progress in the trace but not the model.
        - Example: Trace contains an activity that the model does not support.
    2. **Move in Model**:
        - Progress in the model but not the trace.
        - Example: The model requires an activity not present in the trace.
    3. **Synchronous Move**:
        - Progress simultaneously in both the model and the trace.
        - Indicates a conforming behavior.
    4. **Illegal Move**:
        - Neither trace nor model progresses.
        - Disallowed in alignments.
- **Symbol Notation**:
    
    - ⊥\text{⊥}⊥: Indicates a **no-move**.

---

#### **6. Formal Definition of an Alignment**

- **Alignment**:
    
    - A sequence of **steps** where each step (x,y)(x, y)(x,y) pairs:
        - xxx: A symbol from the trace or ⊥\text{⊥}⊥.
        - yyy: A symbol from the model or ⊥\text{⊥}⊥.
- **Properties**:
    
    - Projection of xxx values reconstructs the original trace.
    - Projection of yyy values reconstructs the model's execution sequence.
- **Example Alignment**:
    
    |Trace (xxx)|Model (yyy)|
    |---|---|
    |AAA|AAA|
    |BBB|BBB|
    |FFF|⊥\text{⊥}⊥|
    |⊥\text{⊥}⊥|EEE|
    |DDD|DDD|
    
- **Interpretation**:
    
    - FFF: Exists in the trace but not in the model.
    - EEE: Required by the model but not in the trace.
    - Synchronous moves (e.g., AAA, BBB, DDD) indicate conforming behavior.

---

#### **7. Spectrum of Alignments**

- **Alignment Possibilities**:
    - Alignments range from:
        1. **Perfect Synchronization**:
            - All moves are synchronous.
            - Fully conforming trace.
        2. **Extreme Deviation**:
            - All moves are either "move in log" or "move in model."
            - Non-conforming trace.
- **Finite Set**:
    - While multiple alignments may exist, the set is **finite** for any trace and model.

---

#### **8. Using Alignments for Conformance Analysis**

- **Conformance Measures**:
    
    - Use alignment results to compute conformance scores based on:
        - Number of synchronous moves.
        - Number of deviations (move in log, move in model).
- **Feedback**:
    
    - **Local Feedback**:
        - Highlights specific deviations in the trace and model.
    - **Global Feedback**:
        - Provides an overall score reflecting the degree of conformance.
- **Practical Example**:
    
    - **Trace**: A→B→F→DA \to B \to F \to DA→B→F→D.
    - **Optimal Alignment**:
        - AAA: Synchronous.
        - BBB: Synchronous.
        - FFF: Move in log.
        - EEE: Move in model.
        - DDD: Synchronous.
    - **Result**:
        - Local feedback pinpoints FFF and EEE as problematic.
        - Global feedback yields a reduced conformance score.

---

#### **9. Strengths and Limitations of Alignments**

- **Strengths**:
    - Precise identification of nonconforming behaviors.
    - Clear mapping of trace deviations to specific model components.
    - Can handle complex execution sequences and trace variants.
- **Limitations**:
    - Computationally intensive for large models and logs.
    - Requires optimal alignment search, which may be resource-heavy.

---

#### **10. Key Takeaways**

- Alignment-based conformance checking offers a systematic approach to evaluate how well event logs align with process models.
- By using moves and alignments, it provides both detailed local feedback and aggregated global insights into conformance.
- While computationally demanding, this method ensures a rigorous and precise analysis of process adherence and deviations.

# Lecture 6.3 Alignments, Costs, and Optimization in Conformance Checking

#### **1. Types of Alignments**

- **Ideal Alignment**:
    
    - All moves are **synchronous** (matching trace and model steps).
    - No "no move" symbols appear.
    - **Cost**: 0 (under standard cost function).
- **Imperfect Alignment**:
    
    - Contains **non-synchronous moves** (e.g., one component uses a "no move").
    - Example: A "no move" in the trace or model increases cost.
    - **Cost**: Based on the number of non-synchronous moves.
- **Non-Optimal Alignment**:
    
    - Contains redundant steps (e.g., a "move in log" followed by a "move in model").
    - These can be merged into one synchronous step.
    - Non-optimal due to inefficiency in representation.
- **Invalid Alignment**:
    
    - Contains **illegal steps** where both components are "no move."
    - Violates the definition of valid steps.

---

#### **2. Assigning Costs to Moves**

- **Delta Function (Δ\DeltaΔ)**:
    
    - Maps moves to costs based on their type:
        - **Synchronous Moves**: Cost = 0.
        - **Move in Log/Model**: Cost = 1.
        - **Other Moves** (e.g., mismatched transitions): Cost = ∞\infty∞.
- **Custom Cost Functions**:
    
    - Reflect domain-specific importance:
        - Example: Skipping payment ≠ Skipping log entry.
    - Allows flexible adjustment for different scenarios.

---

#### **3. Examples of Costs for Alignments**

- **Alignment Example 1 (Ideal Alignment)**:
    
    - All moves are synchronous (e.g., A,A;C,C;D,DA, A; C, C; D, DA,A;C,C;D,D).
    - **Cost**: 0.
- **Alignment Example 2 (Imperfect Alignment)**:
    
    - Includes four non-synchronous moves (e.g., "no move" in log or model).
    - **Cost**: 4 (each non-synchronous move = 1).
- **Alignment Example 3 (Invalid Alignment)**:
    
    - Contains mismatched transitions (e.g., X,YX, YX,Y, A,BA, BA,B).
    - **Cost**: ∞\infty∞ (under standard cost function).

---

#### **4. Finding the Optimal Alignment**

- **Definition**:
    
    - Optimal alignment minimizes total cost (Δ\DeltaΔ) among all possible alignments.
- **Key Properties**:
    
    - **Always Exists**: An alignment can always be found, even in the worst case.
    - **Not Necessarily Unique**: Multiple alignments may have the same minimum cost.
    - **Computational Complexity**: Finding optimal alignment is computationally expensive.

---

#### **5. Search Space for Alignments**

- **Construction**:
    
    - Combine the state space of the **trace** and the **process model**.
    - Nodes: Pairs of states (model state, trace state).
    - Arcs: Represent possible moves (log, model, or synchronous).
- **Search Space Challenges**:
    
    - **Size**: The product of model and trace state spaces.
    - **Optimization Needed**: Techniques required to reduce size and improve efficiency.

---

#### **6. Optimizing the Search Space**

- **Silent Transition Pruning**:
    
    - Remove **silent transitions** (no labels) from consideration.
    - Focus on moves contributing to synchronous steps.
    - **Impact**:
        - Reduces states and transitions.
        - Example: From 45 states to 30; transitions reduced from 121 to 86.
- **Heuristic Search with A***:
    
    - Use heuristic functions to guide search:
        - **Heuristic**: Length of remaining trace.
    - **Properties**:
        - Must be **monotonic** (cost decreases as progress is made).
        - Cannot **overestimate** the remaining cost.
    - **Impact**:
        - Further reduces the search space.

---

#### **7. Practical Example of Search Space Reduction**

- **Initial Search Space**:
    
    - Contains all possible combinations of log and model moves.
    - Example: 45 states, 121 transitions.
- **After Silent Transition Pruning**:
    
    - Removes irrelevant states and transitions.
    - Result: 30 states, 86 transitions.
- **After Heuristic Search with A***:
    
    - Focuses search on promising paths.
    - Further reduction: 21 states, 32 transitions.

---

#### **8. Alignments in Petri Nets**

- **Process Net**:
    
    - Represents the **reference model**.
- **Event Net**:
    
    - Represents the **trace** as a sequential Petri net.
- **Combining Nets**:
    
    - Add transitions for **synchronous moves**:
        - Connect incoming and outgoing places in both nets.
- **Result**:
    
    - A unified **product net** that integrates the trace and model.
- **Shortest Path**:
    
    - The shortest path in the **product net's transition system** represents the optimal alignment.

---

#### **9. Key Takeaways**

- **Alignment-Based Conformance Checking**:
    
    - Enables precise evaluation of process compliance.
    - Resolves issues with silent and duplicate transitions.
- **Optimization Techniques**:
    
    - Reduce search space size significantly.
    - Make alignment computation feasible for large models and logs.
- **Flexible Cost Functions**:
    
    - Tailored cost functions enable domain-specific analysis.
- **Visualizing Alignments**:
    
    - Petri net-based representations clarify execution paths and violations.
- **Practical Use**:
    
    - Provides detailed local and global feedback on process deviations.



# Lecture 6.4 Alignment-Based Conformance Checking and Fitness Measures

---

#### **1. Introduction to the Scenario**

- **Objective**: Compute the **conformance** of a given trace with a reference process model using **alignment-based conformance checking**.
- **Key Example**:
    - A **process model** is given.
    - An **event log trace** (bottom-left) is analyzed for alignment with the model.

---

#### **2. Alignment and Cost in Conformance Checking**

- **Alignment Cost**:
    
    - The alignment is computed between the trace and the process model.
    - **Alignment cost** quantifies non-synchronous moves:
        - Example: An alignment with **3 non-synchronous moves** has a cost of 3.
- **Advantages of Alignment Over Token Replay**:
    
    - **Handles Silent Transitions**: Silent transitions (e.g., unrecorded activities) are seamlessly managed.
    - **Handles Duplicate Transitions**: Multiple transitions with the same label in the model are correctly processed.

---

#### **3. Fitness Measures in Alignment-Based Conformance Checking**

##### **Absolute Fitness of a Trace**:

- **Definition**:
    - Measures the conformity of a trace Σ\SigmaΣ with the process model.
    - Based on the **cost** (Δ\DeltaΔ) of the **optimal alignment** (γ∗\gamma^*γ∗) between Σ\SigmaΣ and the model.
- **Standard Cost Function**:
    - **Synchronous moves**: Cost = 0.
    - **Log/Model moves**: Cost = 1.
    - **Other moves** (mismatched activities): Cost = ∞.

##### **Absolute Fitness of an Event Log**:

- **Definition**:
    - Extends trace-level fitness to the entire event log.
    - Formula: Fabsolute=∑Σi∈Logni⋅Δ(γ∗)F_{\text{absolute}} = \sum_{\Sigma_i \in \text{Log}} n_i \cdot \Delta(\gamma^*)Fabsolute​=Σi​∈Log∑​ni​⋅Δ(γ∗)
        - Σi\Sigma_iΣi​: Trace.
        - nin_ini​: Frequency of Σi\Sigma_iΣi​ in the log.
        - Δ(γ∗)\Delta(\gamma^*)Δ(γ∗): Cost of the optimal alignment for Σi\Sigma_iΣi​.

##### **Normalized Fitness**:

- **Purpose**:
    
    - Normalize absolute fitness to a range of [0,1][0, 1][0,1] for comparability.
- **Worst-Case Alignment**:
    
    - Worst case involves:
        1. **Log moves only**: Aligning all events in the trace with no model moves.
        2. **Model moves only**: Aligning all transitions in the model with no log moves.
- **Formula**:
    
    Fnormalized=1−FabsoluteCS+CMF_{\text{normalized}} = 1 - \frac{F_{\text{absolute}}}{C_S + C_M}Fnormalized​=1−CS​+CM​Fabsolute​​
    - CSC_SCS​: Cost of log moves only.
    - CMC_MCM​: Cost of model moves only.

---

#### **4. Computing the Costs in the Fitness Formula**

##### **Log Moves Only** (CSC_SCS​):

- **Definition**:
    - Sum of costs for all events in the trace, repeated for each trace in the log.
- **Formula**: CS=∑Σi∈Logni⋅∣Σi∣C_S = \sum_{\Sigma_i \in \text{Log}} n_i \cdot |\Sigma_i|CS​=Σi​∈Log∑​ni​⋅∣Σi​∣

##### **Model Moves Only** (CMC_MCM​):

- **Definition**:
    - Cost of the shortest complete execution sequence in the model.

---

#### **5. Local and Global Feedback in Conformance Checking**

- **Local Feedback**:
    
    - Pinpoints **frequent violation pairs** (e.g., transition and move type).
    - Helps identify **hotspots of nonconformance** in the model or trace.
- **Global Feedback**:
    
    - Aggregates local feedback into overall measures:
        - **Violation Support**: Frequency of specific violations across traces.
        - **Violation Confidence**: Likelihood of certain violations co-occurring.

---

#### **6. Examples of Alignments and Costs**

##### **Examples of Alignments**:

1. **Ideal Alignment**:
    - All moves are synchronous.
    - Cost = 0.
2. **Imperfect Alignment**:
    - Contains non-synchronous moves (e.g., log or model moves).
    - Cost equals the count of non-synchronous moves.
3. **Non-Optimal Alignment**:
    - Includes redundant steps, such as separate log and model moves instead of a single synchronous move.
    - Results in unnecessary additional cost.
4. **Invalid Alignment**:
    - Contains illegal steps (e.g., no moves in both log and model simultaneously).

##### **Assigning Costs**:

- **Synchronous Moves**: Cost = 0.
- **Log or Model Moves**: Cost = 1 (standard cost).
- **Mismatched Moves**: Cost = ∞.
- **Custom Costs**:
    - Reflect business importance (e.g., skipping payment > skipping log entry).

---

#### **7. Optimizing Alignment Search**

##### **Search Space Construction**:

- Represented as the **state space** of the combined trace and model:
    - Each state = (M,T)(M, T)(M,T):
        - MMM: Model state.
        - TTT: Trace state.

##### **Challenges**:

- **Large Search Space**:
    - The product of the model and trace state spaces.

##### **Optimizations**:

1. **Silent Transition Pruning**:
    - Remove states associated with silent transitions (e.g., unobservable activities).
    - Reduces unnecessary states and transitions.
2. **Heuristic Search**:
    - Use algorithms like **A*** with admissible heuristics:
        - Example Heuristic: Remaining length of the trace.
    - Significantly reduces the search space while preserving optimality.

---

#### **8. Alignments in Petri Nets**

- **Process Net and Event Net**:
    - **Process Net**: Represents the reference model.
    - **Event Net**: Represents the sequence of events in the trace.
    - **Synchronous Moves**:
        - Combine transitions from the process and event nets.

##### **Combined State Space**:

- Construct a **product net** from the process and event nets.
- Generate a **reachability graph** to determine all valid alignments.

---

#### **9. Key Takeaways**

- **Alignment-Based Conformance Checking**:
    - Provides a rigorous framework for analyzing deviations.
    - Enables detailed **local** and **global feedback**.
- **Optimization Techniques**:
    - Efficient algorithms and state-space reductions make the approach feasible for larger models and logs.
- **Flexibility**:
    - Custom cost functions allow tailoring to business priorities.
- **Limitations**:
    - Computationally intensive for complex processes or large event logs.



# Lecture 7.1 Process Mining Projects and Use Cases

---

#### **1. Purpose of Process Mining Projects**

- **Process Mining as Use Case Collection**:
    
    - Process mining should focus on **specific goals** and **actionable outcomes**.
    - Each use case identifies:
        - **Key performance indicators (KPIs)** to improve.
        - **Actions** derived from insights to enhance processes.
- **Typical KPIs in Process Mining**:
    
    - **Time**: Minimize flow time, waiting time, or resource load.
    - **Cost**: Maintain costs within thresholds.
    - **Quality**: Increase high-quality product outputs.
    - **Risk**: Reduce execution and activity risks.

---

#### **2. Actionable Insights from Process Mining**

- **Actionable Results**:
    - Insights should lead to **improvements** in the process.
    - Examples of actionable outcomes:
        - **Process Redesign**:
            - Suggest structural changes based on deviations or bottlenecks.
            - Example: Remove unused process paths from a reference model to simplify execution.
        - **Adjust Resource Allocation**:
            - Example: Reallocate resources during high and low seasonal periods based on bottlenecks.
        - **Intervene on Process Instances**:
            - Address deviations at the instance level (e.g., using conformance checking insights).
        - **Operational Support**:
            - Use historical data to predict outcomes or suggest actions for ongoing process instances.
            - Example: Predict service level agreement fulfillment or process completion times.

---

#### **3. Examples of Process Mining Use Cases**

- **Improving Flow Time**:
    - Use bottleneck analysis to redesign the process and reduce flow time by a target percentage.
- **Ensuring Compliance**:
    - Use conformance checking to identify compliance violations.
    - Example: Adjust parameters for work distribution or trigger immediate interventions.
- **Merging Processes**:
    - Harmonize processes from merged entities to reduce costs (common in organizational mergers).
- **Predictive Analytics**:
    - Predict remaining flow time for better customer service.
    - Example: Mortgage application processing time prediction based on customer data.
- **Resource Allocation Optimization**:
    - Assign resources (human, equipment, etc.) to cases based on suitability and efficiency.
- **Handling Exceptional Cases**:
    - Isolate high-impact outliers to prevent disruptions in regular processes.
- **Risk Identification**:
    - Identify high-risk cases and take preventive measures.

---

#### **4. Process Mining as Part of a Lifecycle**

- **Action-Oriented Workflow**:
    
    - **Start with goals**: Define clear objectives for the project.
    - **Run process mining analyses**: Gather insights aligned with goals.
    - **Implement actions**: Use insights to trigger meaningful process improvements.
    - **Iterate and refine**: Continuously improve through iterative analysis.
- **Knowledge Discovery in Databases (KDD) Approach**:
    
    - **Steps**:
        1. Data selection and filtering.
        2. Preprocessing and transformation.
        3. Data mining to extract patterns.
        4. Evaluation and interpretation of results for actionable knowledge.
    - **Iterative nature**:
        - Revisit data and analysis steps to refine insights.

---

#### **5. Types of Processes: Lasagna vs. Spaghetti**

- **Lasagna Processes**:
    
    - **Characteristics**:
        - Structured, repetitive, regular, controllable.
        - Clear rules govern execution (e.g., car manufacturing).
    - **Use Cases**:
        - Detect bottlenecks and deviations.
        - Measure and improve performance.
        - Provide operational support for decision-making.
- **Spaghetti Processes**:
    
    - **Characteristics**:
        - Unstructured, flexible, variable, knowledge-intensive.
        - Execution often tailored to individual scenarios (e.g., surgeries).
    - **Use Cases**:
        - Highlight key problems in unstructured processes.
        - Provide evidence-based suggestions for improvements.
        - Shift management methodology from intuition (e.g., PowerPoint plans) to data-driven strategies.
- **Process Spectrum**:
    
    - Most processes fall between the extremes of **lasagna** and **spaghetti**.
    - Approach depends on process structure and complexity.

---

#### **6. Practical Examples of Lasagna and Spaghetti Processes**

- **Lasagna Example**:
    
    - **Car manufacturing**:
        - Highly repetitive and structured.
        - Every aspect is controlled and modeled for efficiency.
- **Spaghetti Example**:
    
    - **Surgery procedures**:
        - Flexible and situation-dependent.
        - Relies on expertise to adapt protocols to specific patient needs.

---

#### **7. Key Takeaways**

- **Focus on Goals**:
    
    - Define objectives and actionable insights for every process mining use case.
- **Tailor the Approach**:
    
    - Lasagna processes require performance-oriented optimization.
    - Spaghetti processes benefit from evidence-based methodologies and flexibility.
- **Iterative Process**:
    
    - Continuously refine insights through iterative analysis and action.
- **Evidence-Based Improvement**:
    
    - Use data-driven insights to replace intuition-based decisions for process enhancements.

# Lecture 7.2 Conducting a Process Mining Project on Lasagna Processes

---

#### **1. Characteristics of Lasagna Processes**

- **Definition**:
    
    - Processes where a simple process model can explain **~80% of the events** with minimal effort.
    - Stakeholders confirm that the discovered model accurately reflects the process.
    - Requires **domain expertise** to identify.
- **Indicators of Lasagna Processes**:
    
    - **Steady event flow**: Regular pace of incoming and outgoing events.
    - **Simple models**: Discovered process models tend to be well-structured with minimal complexity.
    - Example: A Dutch municipality’s event log for social support requests.
        - **Log statistics**: 500 process instances, ~5500 events.
        - **Discovered model**: Simple loop with one optional activity, reflecting the actual process with high fidelity.

---

#### **2. Stages of the L* Process Mining Lifecycle**

The **L*** lifecycle model provides a structured approach for conducting process mining projects.

---

### **Stage 0: Planning and Justification**

- **Activities**:
    - Define project type:
        - **Data-driven**: Explore the process structure and behavior.
        - **Question-driven**: Address specific behavioral questions.
        - **Goal-driven**: Target measurable KPIs for improvement.
    - **Justify**: Establish a clear business case with defined objectives and scope.
- **Key Outputs**:
    - Clear goals and actionable objectives (e.g., bottleneck reduction, compliance verification).

---

### **Stage 1: Data Extraction and Preparation**

- **Activities**:
    - Collect:
        - Event logs, process models, and artifacts (e.g., protocols, reference models).
        - Objectives and KPIs for evaluation.
    - Clean and prepare data:
        - Handle missing or incomplete information.
        - Ensure logs align with the project’s goals.
    - Consult with domain experts for context and validation.
- **Key Outputs**:
    - A prepared dataset and a clear understanding of the process environment.

---

### **Stage 2: Constructing the Control Flow Model**

- **Activities**:
    - Build a control flow model using:
        - Automated discovery techniques (e.g., inductive miner).
        - Stakeholder input and conformance checking.
    - Validate the model iteratively:
        - Compare against logs and adjust the model as needed.
    - Ensure the model is **sound**, structured, and representative.
- **Key Outputs**:
    - A well-validated control flow model serving as the **backbone** for further analysis.

---

### **Stage 3: Enhancement**

- **Activities**:
    - Enhance the control flow model with additional perspectives:
        - **Time**: Identify waiting times and activity durations.
        - **Costs**: Map costs to activities to locate high-cost areas.
        - **Resources**: Analyze resource utilization or bottlenecks.
    - Overlay event log data onto the model to uncover actionable insights:
        - Example: Identify the most time-consuming or costly activities.
    - Generate enhanced models for specific perspectives (e.g., time, cost, or performance).
- **Key Outputs**:
    - A comprehensive, enriched process model with actionable insights for improvement.

---

### **Stage 4: Operational Support**

- **Activities**:
    - Train models using historical data to provide real-time support:
        - Predict completion times for new process instances.
        - Recommend resource allocations for ongoing processes.
    - Tailor support systems for repetitive and stable lasagna processes.
- **Key Outputs**:
    - Predictive systems and interventions improving operational efficiency.

---

#### **3. Benefits of Process Mining for Lasagna Processes**

- **Ease of Analysis**:
    
    - Lasagna processes are typically straightforward to model due to their structured nature.
    - Simple models (e.g., loops or optional activities) often align closely with stakeholder expectations.
- **Examples of Insights**:
    
    - **Frequent Pathways**: Identify the most common execution paths.
    - **Performance Bottlenecks**:
        - Highlight activities with the longest waiting or sojourn times.
        - Identify high-cost activities for potential redesign.
    - **Compliance Monitoring**:
        - Ensure that actual executions match the reference model.

---

#### **4. Practical Use Cases for Lasagna Processes**

- **Redesign**:
    - Example: Simplify or remove loops that increase costs or time.
- **Adjustments**:
    - Temporal redistribution of resources during high- and low-demand periods.
- **Interventions**:
    - Address deviations in specific process instances (e.g., reallocate resources mid-process).
- **Operational Support**:
    - Predict process outcomes or allocate optimal resources in real-time.

---

#### **5. Key Insights from Lasagna Process Mining**

- **Data Insights Drive Actions**:
    - Data-driven discovery helps identify bottlenecks, high costs, and inefficiencies.
    - Example: Highlight long wait times or activities with excessive resource consumption.
- **Iterative Model Refinement**:
    - Start with stakeholder-provided models, refine them with process mining insights, and validate iteratively.
- **Combining Perspectives**:
    - Use enriched models to combine multiple dimensions (e.g., cost, time, compliance) for deeper analysis.

---

#### **6. Relationship to Process Mining Use Cases**

- **Goals**: Defined during the **planning stage** (Stage 0 and 1).
- **Actions**: Derived from **construction**, **enhancement**, and **operational support** stages (Stages 2-4).
    - Actions include process redesign, resource reallocation, or predictive support to improve customer experience.

---

#### **7. Comparison: Lasagna vs. Spaghetti Processes**

- **Lasagna Processes**:
    - Structured, repetitive, predictable.
    - Ideal for prediction and operational support (e.g., stable resource allocation).
- **Spaghetti Processes**:
    - Unstructured, flexible, highly variable.
    - Focuses more on highlighting key problems or methodological improvements.

---

#### **8. Key Takeaway**

For **lasagna processes**, process mining provides a robust framework to discover, enhance, and optimize structured workflows, transforming raw data into actionable insights that drive measurable improvements. The structured nature of these processes makes them particularly suited for predictive models and operational support.

# Lecture 7.3 Conducting Process Mining Projects on Spaghetti Processes

---

#### **1. Understanding Spaghetti Processes**

- **Definition**: Processes that do not meet the characteristics of lasagna processes.
    
    - Highly unstructured, irregular, and variable.
    - Lack of clear repeatable patterns or predictable behaviors.
- **Example**: Diagnosis and treatment process of 2700 patients in a Dutch hospital.
    
    - **Event log characteristics**:
        - ~115,000 events across 619 activities.
        - Involves 266 resources (e.g., doctors, nurses, clerks).
    - **Outcome of Process Discovery**:
        - Resulting model is complex and lacks clear structure.
        - Indicates that each patient is treated uniquely, with only partial structural components.

---

#### **2. Challenges of Mining Spaghetti Processes**

- **Operational Support**:
    - Not feasible due to lack of stability and repeatability.
    - Unpredictable, knowledge-intensive domains like healthcare make real-time predictions unreliable.
- **Control Flow Discovery**:
    - Produces "spaghetti models" that are difficult to analyze or act upon.
- **Stages 2 and 3 of the **L*** lifecycle (construction and enhancement) are harder to achieve for spaghetti processes.

---

#### **3. Strategies for Handling Spaghetti Processes**

- **Narrow the Scope**: Focus the analysis to make it manageable and meaningful.
    
    1. **Subset of Activities**:
        - Analyze only the most frequent or manually selected activities.
        - Example: Focus on back-office tasks.
    2. **Subset of Cases**:
        - Cluster process instances into groups based on shared characteristics (e.g., natural subclasses like "gold customers").
        - Example: Separate analysis for long-haul vs. domestic flights in airline operations.
    3. **Subset of Paths**:
        - Filter the process model to include only frequent or meaningful paths.
        - Example: Consider only cases where specific pairs of activities are executed in sequence.
    4. **Combination**:
        - Combine activity, case, and path filtering to achieve a simplified and structured view.
- **Iterative Filtering**:
    
    - Tools like **Disco** allow interactive filtering:
        - Filter activities to show only the most frequent ones.
        - Filter paths to highlight significant relationships.
        - Result: More structured and interpretable models.

---

#### **4. Lifecycle Model for Spaghetti Processes: PM²**

- PM² is a tailored lifecycle model designed for the iterative and exploratory nature of spaghetti process mining.

---

### **PM² Lifecycle Overview**

#### **Stage 0: Planning**

- **Goal**:
    - Set up the project, define objectives, and assemble the team.
- **Key Activities**:
    - Identify target processes and research questions.
    - Select the scope of the analysis.
- **Output**:
    - Clear project plan and research goals.

---

#### **Stage 1: Extraction**

- **Goal**:
    - Collect event data and process models.
- **Key Activities**:
    - Identify relevant information systems for data extraction.
    - Define the scope and abstraction level for the analysis.
- **Output**:
    - Prepared event logs and process models.

---

#### **Stage 2: Data Processing**

- **Goal**:
    - Prepare data for analysis.
- **Key Activities**:
    - Define key concepts:
        - **Activities**: Determine what constitutes an activity (e.g., email sender, subject).
        - **Use Cases**: Define process instances or cases (e.g., customer types, project IDs).
    - Enrich data:
        - Add attributes such as cost, time, or resource information.
    - Filter data:
        - Focus on specific activities, cases, or paths.
- **Output**:
    - Refined event logs ready for process discovery.

---

#### **Stage 3: Mining and Analysis**

- **Goal**:
    - Discover insights from the event logs.
- **Key Activities**:
    - **Process Discovery**:
        - Generate control flow models using discovery algorithms.
    - **Model Enhancement**:
        - Add perspectives such as time, cost, or quality.
    - **Conformance Checking**:
        - Compare discovered models with reference models to assess compliance.
    - **Analytical Models**:
        - Use data mining techniques for additional insights.
- **Output**:
    - Findings and enhanced models for further evaluation.

---

#### **Stage 4: Evaluation**

- **Goal**:
    - Interpret findings to generate actionable insights.
- **Key Activities**:
    - **Diagnosis**:
        - Relate findings to research questions and identify improvement opportunities.
    - **Replication and Validation**:
        - Verify the accuracy and relevance of findings.
- **Output**:
    - Validated results linked to research objectives.

---

#### **Stage 5: Process Improvement**

- **Goal**:
    - Apply insights to improve the process.
- **Key Activities**:
    - Suggest process modifications.
    - Implement and monitor changes.
- **Output**:
    - Improved process models and operations.

---

### **5. Practical Applications for Spaghetti Processes**

- **Iterative Analysis**:
    - Apply PM² in agile "sprints," conducting multiple analysis iterations to refine findings.
- **Exploratory Focus**:
    - Use filtering and clustering to narrow scope and improve interpretability.
- **Process Improvement**:
    - Generate actionable insights despite initial complexity.

---

### **6. Key Insights for Spaghetti Processes**

- **Exploratory Nature**:
    - Spaghetti process mining is less about predicting behavior and more about understanding and highlighting key issues.
- **Incremental Approach**:
    - Iterative filtering and focused analysis help tackle the inherent complexity of spaghetti processes.
- **Flexible Insights**:
    - Insights often stem from clustering, segmentation, and data enrichment rather than direct process discovery.

---

### **7. Comparison: PM² vs. L***

- **PM²**:
    - Designed for spaghetti processes.
    - Focuses on agile iterations, exploratory analysis, and incremental improvements.
- **L***:
    - Better suited for structured, repetitive lasagna processes.
    - Emphasizes operational support and predictive capabilities.

---

### **8. Conclusion**

For **spaghetti processes**, process mining requires a flexible and iterative approach, as captured by the **PM² lifecycle**. By focusing on subsets of activities, cases, or paths, and leveraging iterative filtering techniques, organizations can derive actionable insights even in highly unstructured and variable environments.

# Lecture 8.1 Evaluating the Quality of Discovered Process Models

---

#### **1. Introduction to Model Evaluation in Process Mining**

- **Goal**: To assess the quality of discovered process models by comparing them with event logs.
- **Purpose**:
    - Different process discovery algorithms produce varying models.
    - Evaluation helps identify the best algorithm or model for a given scenario.
    - Facilitates a structured comparison of models based on pros and cons.

---

#### **2. Overfitting vs. Underfitting in Process Models**

- **Overfitting**:
    - The model replicates the event log exactly but generalizes poorly.
    - Example: A "log representation" model with separate sequences for each trace—high fitness but no generalization.
- **Underfitting**:
    - The model is overly general and allows excessive behavior.
    - Example: The "flower model," which permits any sequence of activities without constraints—poor precision.

---

#### **3. Dimensions of Process Model Quality**

The quality of a discovered process model is assessed across four dimensions:

1. **Fitness**:
    
    - Measures how well the model replicates the behavior observed in the event log.
    - A model with high fitness covers most or all of the observed traces.
2. **Precision**:
    
    - Assesses whether the model allows for unnecessary or unrelated behavior.
    - High precision implies the model closely follows the event log's observed patterns without allowing extraneous behaviors.
3. **Generalization**:
    
    - Evaluates whether the model can account for unseen but plausible behavior.
    - High generalization means the model accommodates reasonable process variations beyond the observed log.
4. **Simplicity**:
    
    - Ensures the model is easy to understand and interpret.
    - A simple model avoids excessive complexity while still being accurate.

---

#### **4. Visualizing the Dimensions**

- **Event Log Behavior**: Represents the finite set of traces captured in the event log.
- **Discovered Model Behavior**: Includes the set of behaviors the discovered model permits.
- **Process Behavior** (Ground Truth): The actual behavior of the underlying process, typically a superset of the event log.

**Relationships**:

- **Fitness**: Measured by the overlap between event log and model behavior.
- **Precision**: Refers to the extent of extraneous behavior allowed by the model beyond the event log.
- **Generalization**: Measures how well the model captures unseen but likely behaviors of the process.
- **Simplicity**: A characteristic of the model’s structure itself.

---

#### **5. Examples of Model Quality**

- **Balanced Model**:
    
    - Covers observed behavior with limited additional behavior.
    - Example: A model with constrained paths based on event log patterns.
- **Underfitted Model (Flower Model)**:
    
    - High fitness (can replicate all traces).
    - Poor precision (allows all behaviors involving the listed activities).
- **Overfitted Model (Sequence Model)**:
    
    - High precision (replicates only observed traces).
    - Poor generalization (ignores plausible behaviors outside the log).
- **Log Representation Model**:
    
    - Perfect fitness (covers all traces).
    - High precision (doesn’t allow unseen behavior).
    - Poor generalization and simplicity.

---

#### **6. Challenges in Generalization**

- Generalization remains the least understood and most complex dimension.
- The research community has well-established methods for fitness and precision.
- Generalization requires further investigation to effectively measure and quantify.

---

#### **7. Practical Considerations**

- **Trade-offs**:
    
    - Fitness, precision, generalization, and simplicity often conflict.
    - Discovery algorithms aim to balance these dimensions for optimal models.
- **Model Examples**:
    
    - **Good Model**:
        - Balanced fitness, precision, and generalization.
    - **Sequence Model**:
        - High precision, low generalization.
    - **Log Representation Model**:
        - High fitness and precision, poor simplicity and generalization.
    - **Flower Model**:
        - High fitness, poor precision.

---

#### **8. Conclusion**

- **Importance of Evaluation**:
    
    - Process discovery algorithms should optimize across all four dimensions.
    - A well-evaluated model ensures effective decision-making and process improvement.
- **Objective**:
    
    - Use the four dimensions as benchmarks to assess and compare discovered models.
    - Strive for a balanced model that meets the needs of the specific process mining project.


# Lecture 8.2 Evaluating Precision in Process Models

---

#### **1. Understanding Precision in Conformance Checking**

- **Definition**: Precision measures how closely the behavior allowed by a process model aligns with the behavior observed in an event log.
- **Goal**: Quantify the excess behavior permitted by a model that is not present in the event log.
- **Key Insight**:
    - Higher precision implies that most of the behavior supported by the model is observed in the log.
    - Lower precision indicates that the model allows for many behaviors not seen in the log.

---

#### **2. Measuring Precision: Techniques**

##### **2.1. Simple Behavioral Appropriateness**

- **Concept**:
    - Calculates the average number of transitions enabled during the replay of a trace on a model.
    - More enabled transitions suggest the model supports additional, unobserved behavior (lower precision).
- **Formula**: SBA=1−Sum of enabled transitions during replayTotal transitions in the model\text{SBA} = 1 - \frac{\text{Sum of enabled transitions during replay}}{\text{Total transitions in the model}}SBA=1−Total transitions in the modelSum of enabled transitions during replay​ Normalized across all traces in the log, weighted by trace frequency.
- **Output**:
    - **Value Range**: [0, 1]
        - **0**: All transitions are always enabled (low precision).
        - **1**: Exactly one transition is enabled at any time (high precision).
- **Examples**:
    - **Flower Model**: All transitions always enabled, leading to precision close to 0.
    - **Sequential Model**: Only one transition enabled at each step, precision = 1.
- **Limitations**:
    - Precision = 1 only for sequential models, making it unsuitable for parallel or complex models.
    - Assumes perfect fitness (i.e., all traces can be replayed on the model).

---

##### **2.2. Advanced Behavioral Appropriateness**

- **Concept**:
    
    - Focuses on the relationships between activities rather than exact transitions during replay.
    - Uses **indirect relations** such as "follows" and "precedes" (e.g., Activity Y happens before Activity X in some traces).
- **Key Steps**:
    
    1. **Compute Relations**:
        - Identify "follows" and "precedes" relationships in both the model and the log.
        - Categorize relationships as:
            - **Always**: Relation holds in all traces.
            - **Sometimes**: Relation holds in some traces.
            - **Never**: Relation never holds.
    2. **Compare Matrices**:
        - Create matrices for both the model and the log based on "follows" and "precedes" relations.
        - Compare intersections of the matrices for both relationships.
- **Formula**:
    
    ABA=Intersection size (follows: model ∩ log)Model size (follows)+Intersection size (precedes: model ∩ log)Model size (precedes)\text{ABA} = \frac{\text{Intersection size (follows: model $\cap$ log)}}{\text{Model size (follows)}} + \frac{\text{Intersection size (precedes: model $\cap$ log)}}{\text{Model size (precedes)}}ABA=Model size (follows)Intersection size (follows: model ∩ log)​+Model size (precedes)Intersection size (precedes: model ∩ log)​
    - Computes how much of the model’s behavior overlaps with the log’s behavior.
- **Example**:
    
    - Given a process model and its corresponding event log, follows/precedes matrices are constructed and compared:
        - **Model**: "Activity B always follows Activity A."
        - **Log**: "Activity B sometimes follows Activity A."
    - The overlap between these relations is quantified to compute precision.

---

#### **3. Comparison of Simple vs. Advanced Approaches**

|**Feature**|**Simple Behavioral Appropriateness**|**Advanced Behavioral Appropriateness**|
|---|---|---|
|**Focus**|Number of enabled transitions during replay|Activity relations (follows/precedes)|
|**Strengths**|Simple to calculate|Captures more complex behaviors|
|**Weaknesses**|Biased toward sequential models|Computationally intensive|
|**Assumption**|Perfect fitness required|Broader, not reliant on perfect fitness|

---

#### **4. Applications and Use Cases**

- **Evaluating Model Quality**:
    - Use precision metrics to compare different process discovery algorithms.
- **Balancing Fitness and Precision**:
    - A highly fit model (covering all observed traces) might lack precision if it allows excessive behavior.
    - Combining fitness and precision helps in assessing a model's overall conformance.

---

#### **5. Conclusion**

- **Precision Metrics**:
    - Provide insights into how closely a model matches the observed log behavior.
    - Identify and quantify unnecessary or extraneous behaviors supported by the model.
- **Choosing the Right Metric**:
    - **Simple Behavioral Appropriateness** is suitable for straightforward comparisons.
    - **Advanced Behavioral Appropriateness** is ideal for complex or parallel models, capturing nuanced relationships.


# Lecture 8.3 Evaluating Simplicity in Process Models

---

#### **1. What is Simplicity in Process Models?**

- **Definition**: Simplicity measures the structural complexity of a process model, aiming for a model that is as simple as possible while maintaining other quality dimensions like fitness, precision, and generalization.
- **Guiding Principle**: Follows **Occam's Razor**, prioritizing simpler models when multiple candidates satisfy conformance criteria.

---

#### **2. Why is Simplicity Important?**

- **Understandability**:
    - Simpler models are easier for stakeholders to comprehend and use.
    - Improves communication between domain experts and technical analysts.
- **Efficiency**:
    - Simple models are easier to analyze, simulate, and enhance.
- **Target Audience**:
    - Simplicity considerations often depend on the **intended audience**, such as domain experts, analysts, or system implementers.

---

#### **3. Simplicity Measures**

##### **3.1. Baseline Measure: Number of Elements**

- **Definition**: Counts the total number of elements in the model (e.g., nodes, transitions, edges).
- **Rationale**: A smaller number of elements generally indicates a simpler model.
- **Limitation**: Does not account for the complexity of relationships or constructs between elements.

---

##### **3.2. Structural Measures**

- Evaluate structural properties of the model. Examples include:

1. **Average Node Degree**:
    
    - Measures the average number of connections per node.
    - Lower values indicate simpler structures.
2. **Diameter**:
    
    - Length of the shortest path from the start node to the end node.
    - Shorter diameters suggest more compact and streamlined models.
3. **Coefficient of Connectivity**:
    
    - Assesses how well-connected the elements are.
    - Lower connectivity often reflects simpler and more understandable models.
4. **Sequentiality**:
    
    - Measures the extent to which the model is sequential versus parallel or looping.
    - High sequentiality values suggest a simpler, more linear process.

---

##### **3.3. Language-Specific Simplicity Measures**

Tailored to specific modeling languages, considering unique constructs or syntax:

1. **Edge Complexity**:
    
    - Counts the number of edges fulfilling specific conditions, such as specific splits or joins.
2. **Nesting Depth**:
    
    - Evaluates how deeply nodes are nested within splits and joins.
    - Excessive nesting often increases complexity and reduces understandability.

---

#### **4. Key Considerations for Simplicity**

- **Modeling Language**:
    
    - The definition of simplicity varies by language (e.g., BPMN, Petri nets).
    - Each language has unique features that influence simplicity metrics.
- **Contextual Use**:
    
    - Simplicity must align with the purpose of the analysis.
    - For example:
        - A high-level strategic view might prioritize extreme simplicity.
        - Detailed operational analyses might require more nuanced structures.
- **Structural vs. Semantic Simplicity**:
    
    - Most simplicity measures focus on **structural properties** (e.g., connections, size) rather than **semantics** (e.g., process meaning).

---

#### **5. Examples of Simplicity Applications**

- **Flower Model**:
    - Low simplicity due to excessive flexibility and lack of structure.
- **Sequence Model**:
    - High simplicity as it has minimal elements and follows a linear flow.

---

#### **6. Balancing Simplicity with Other Dimensions**

- Simplicity must not come at the cost of other quality dimensions:
    - **Fitness**: A simple model should still explain the observed log behavior.
    - **Precision**: Avoid oversimplifying to the point where the model allows too much unobserved behavior.
    - **Generalization**: Ensure the model abstracts enough to represent future process behavior.

---

#### **7. Conclusion**

- **Simplicity Metrics**:
    - Provide insights into the structural complexity of process models.
    - Serve as a baseline for comparing different models.
- **Key Takeaways**:
    - Simplicity is essential for creating models that are not only accurate but also usable and interpretable.
    - A good simplicity measure begins with the model's size and extends to more nuanced structural properties.
    - Striking the right balance between simplicity and other quality dimensions is crucial for effective process mining outcomes.


# Lecture 11.1 Analyzing Event Logs Beyond the Control Flow Perspective

---

#### **1. Event Logs Contain Rich Data**

- **Typical Contents**:
    - **Data Objects**: E.g., invoice or order numbers linked to activities.
    - **Roles and Resources**: E.g., people or systems involved in executing activities.
    - **Timing Information**: Absolute or relative timestamps.
- **Beyond Control Flow**:
    - Event logs often capture more than sequence data, enabling analysis of other perspectives, such as time, resources, and social interactions.

---

#### **2. Importance of Multi-Perspective Analysis**

- **Compliance and Workflow Insights**:
    - Example: Enforcing the **Four-Eyes Principle**.
        - Ensures two individuals verify critical tasks, promoting accountability.
- **Operational Efficiency**:
    - Identifying **bottlenecks** or inefficiencies in execution time to improve process flow and quality.
- **Predictive Analysis**:
    - Leveraging additional dimensions like data attributes (e.g., property value, income) to predict outcomes such as process duration or likelihood of success.

---

#### **3. Techniques for Multi-Perspective Analysis**

##### **3.1. Dotted Charts**

- **Definition**: A scatter plot representation of events with:
    
    - **Horizontal Axis**: Time (absolute or relative).
    - **Vertical Axis**: Classes such as case IDs, resources, or activities.
    - **Color Coding**: Represents a third dimension (e.g., activity name or resource).
- **Use Cases**:
    
    - **Absolute Time Analysis**:
        - Visualize event generation patterns, e.g., weekend impact on processes.
        - Example: New process instances unaffected by weekends, but ongoing processes show delays.
    - **Relative Time Analysis**:
        - Understand case durations and bottlenecks.
        - Example: Half of cases completed within 3 days; others exhibit delays up to 90 days.

##### **3.2. Social Network Analysis**

- **Purpose**:
    - Explore interactions and handovers between individuals or roles involved in activities.
- **Example**:
    - Trace: Activities (A, B, D, H) assigned to individuals (Pete, Zod, Mike).
    - Insights:
        - Identify collaboration patterns or imbalances.
        - Highlight bottlenecks caused by specific individuals or roles.

##### **3.3. Prediction Models**

- **Approach**:
    - Train models on historical event logs for:
        - **Remaining Time Predictions**: Estimate when a process instance will complete.
        - **Outcome Predictions**: Forecast process success or failure based on attributes (e.g., customer data, product details).
- **Applications**:
    - Real-time support for decision-making during ongoing processes.
    - Example: Predicting mortgage approval times based on applicant details.

---

#### **4. Practical Examples**

1. **Time Dimension Analysis**:
    
    - Highlight weekends as factors causing inactivity in ongoing cases.
    - Detect patterns of long wait times followed by burst activity.
2. **Social Interactions**:
    
    - Understand workload distribution among team members or departments.
    - Identify roles critical to process execution and their interdependencies.
3. **Bottleneck Discovery**:
    
    - Use time data to pinpoint slow stages and focus on process redesign.

---

#### **5. Key Takeaways**

- **Rich Event Logs Enable Advanced Insights**:
    - Beyond control flow, exploring time, resources, and interactions reveals deeper process dynamics.
- **Actionable Outcomes**:
    - Insights from dotted charts and social networks guide compliance checks, resource allocation, and process optimization.
- **Strategic Decision-Making**:
    - Multi-dimensional analysis supports predictive capabilities and operational improvements.


# Lecture 11.2 Decision Mining in Process Mining

---

#### **1. What is Decision Mining?**

- **Definition**:
    - Decision mining is part of the **extension/enhancement dimension** of process mining.
    - It uses **data contained in event logs** to augment process models with decision-related insights.
- **Purpose**:
    - Identify **decision points** in a process model and understand the **data-driven conditions** influencing decisions.
    - Complement control flow discovery with actionable decision-making insights.

---

#### **2. Why is Decision Mining Important?**

- **Limits of Control Flow Discovery**:
    - Control flow models focus on the sequence of activities, often ignoring the decision logic behind branching.
- **Benefits of Decision Mining**:
    - Enables **data-aware verification** to detect deadlocks or dead activities based on data conditions.
    - Validates decision procedures to ensure **compliance**.
    - Improves **predictive accuracy** for process outcomes and performance.
    - Resolves **non-determinism** in Petri nets by identifying what data influences branching.

---

#### **3. Decision Mining Workflow**

##### **Step 1: Identify Decision Points**

- Detect **splits** (e.g., XOR splits) in the process model.
- Example:
    - A decision point after activity A may lead to either activity B or activity C based on certain conditions.

##### **Step 2: Frame the Problem as Classification**

- **Classes**:
    - Each branch in a decision point represents a classification label.
- **Prediction Variables**:
    - Attributes from the event log are used to predict which branch is taken.
- **Classification Type**:
    - Binary or multi-class depending on the number of branches.

##### **Step 3: Build Decision Models**

- Use classification techniques to generate decision models:
    - **Decision Trees** (most common).
    - Other options: SVMs, Neural Networks, etc.
- Decision trees split data into branches using attributes that best discriminate between classes.

---

#### **4. Examples of Decision Trees**

1. **Customer Loan Example**:
    
    - Decision point: Branch after activity A (leading to B or C).
    - Data conditions:
        - Amount > 500 and policy type = "Normal" → Activity B.
        - Amount ≤ 500 or policy type = "Premium" → Activity C.
2. **Student Exams Example**:
    
    - Predict if a student will pass or fail based on exam results.
3. **Coffee Shop Orders Example**:
    
    - Predict if a customer will buy a muffin based on other purchases.

---

#### **5. Challenges in Decision Mining**

##### **1. Noisy Event Logs**

- **Issue**:
    - Noise in event logs can reduce the reliability of classification.
- **Solution**:
    - Use robust classification techniques or pre-process data to handle noise.

##### **2. Silent Transitions**

- **Issue**:
    - Silent transitions in process models lack observable events, making labeling challenging.
- **Solution**:
    - Forward the search to the next observable activity.
    - Stop search at joins to avoid overly greedy progression.

##### **3. Duplicate Activities**

- **Issue**:
    - Multiple transitions with the same label make distinguishing branches difficult.
- **Solution**:
    - Forward the search to uniquely identifiable transitions.

##### **4. Loops**

- **Issue**:
    - Loops can create ambiguous conditions for decision mining.
- **Solution**:
    - Identify exit conditions of loops and their corresponding decision logic.

---

#### **6. Applications of Decision Mining**

1. **Compliance Verification**:
    - Check if decisions adhere to organizational rules and regulations.
2. **Outcome Prediction**:
    - Use decision logic to predict process outcomes (e.g., approval or rejection of a loan).
3. **Process Optimization**:
    - Identify data conditions that drive inefficiencies, enabling targeted improvements.

---

#### **7. Key Takeaways**

- Decision mining extends process mining by uncovering **data-driven decision logic**.
- By combining control flow models with decision trees or other classification techniques, it provides deeper insights into how and why processes branch.
- Effective decision mining requires addressing challenges like noise, silent transitions, and duplicate activities to ensure robust and actionable insights.

# Lecture 11.3 Social Network Analysis in Process Mining

---

#### **1. Overview of Social Network Analysis in Process Mining**

- **Context**:
    - Event logs often include **resource-related data** (e.g., person or department executing an activity).
    - This enables the construction of **social networks** to analyze relationships between resources or organizational entities.

---

#### **2. Event Logs with Resources**

- **Structure**:
    - Event logs include attributes for **activity name**, **case ID**, and the **resource** performing the activity.
- **Resource-Activity Matrix**:
    - A table summarizing the **average number of times** a resource performs an activity per case.
    - **Insights from the Matrix**:
        - Activity frequency (e.g., Activity A is performed once per case on average).
        - Resource involvement percentages (e.g., Pete performs 30% of Activity A).
        - Exclusive resource allocations (e.g., Sarah exclusively performs Activities E and F).

---

#### **3. What is a Social Network?**

- **Definition**:
    
    - A graph where **nodes** represent entities (e.g., people, departments), and **edges** represent relationships (e.g., handovers of work).
    - **Edge Weights**:
        - Indicate the **strength of the relationship** (e.g., frequency of interactions).
- **Applications**:
    
    - **Analysis**:
        - Identify central resources or roles (e.g., centrality, closeness).
        - Detect cliques or strong collaboration clusters.
    - **Optimization**:
        - Improve work allocation or streamline interactions between departments.

---

#### **4. Constructing Social Networks in Process Mining**

##### **Step 1: Define a Metric for Relationships**

- **Common Metrics**:
    1. **Handover of Work**:
        - Measures how often work is handed over from one resource to another within a case.
        - Example: Sarah hands over work to Mike an average of 1.47 times per case.
    2. **Similar Tasks**:
        - Groups resources performing similar activities.
    3. **Working Together**:
        - Groups resources working on the same cases simultaneously.

##### **Step 2: Build the Adjacency Matrix**

- Use the selected metric (e.g., handover of work) to compute relationships between resources.
- Adjust for **parallel activities**:
    - Sequential event logs may linearize parallel activities.
    - Ensure resources performing parallel tasks are **not incorrectly linked** in handover relationships.

##### **Step 3: Construct the Graph**

- **Nodes**: Represent individual resources or aggregated groups (e.g., roles or departments).
- **Edges**: Weighted by the strength of relationships (e.g., handover frequency).

---

#### **5. Insights from Social Networks**

##### **1. Individual Resource View**

- **Example**:
    - Pete, Mike, and Ellen are involved in similar tasks (e.g., Activity A).
    - Sarah exclusively performs managerial tasks (e.g., Activities E and F).

##### **2. Aggregated Role View**

- Resources grouped by roles (e.g., assistants, experts, managers).
- **Example**:
    - Managers and assistants frequently hand work over to each other.
    - Experts work independently, handing over work only to managers.

##### **3. Process Execution View**

- Analyze interactions across roles and resources to identify bottlenecks or inefficiencies.
- **Example**:
    - Experts rarely interact with assistants, suggesting potential silos in the workflow.

---

#### **6. Visualizing Social Networks**

- Nodes and edges are visually represented to show:
    - **Node size**: Importance of the resource (e.g., frequency of involvement).
    - **Edge weight**: Strength of the relationship (e.g., frequency of handovers).
- **Example**:
    - A thicker edge between managers and assistants indicates frequent handovers.
    - Lack of self-loops for experts shows they do not delegate tasks to other experts.

---

#### **7. Applications of Social Network Analysis**

1. **Identify Bottlenecks**:
    
    - Detect resource or role bottlenecks through centrality measures.
2. **Optimize Workflows**:
    
    - Use insights to balance workloads or improve collaboration between roles.
3. **Enforce Compliance**:
    
    - Check adherence to rules like the "Four-Eyes Principle" (ensuring tasks are reviewed by two individuals).
4. **Streamline Interactions**:
    
    - Reduce redundant handovers or improve communication between departments.

---

#### **8. Conclusion**

- Social network analysis in process mining enhances understanding of **resource interactions**.
- By leveraging metrics like **handover of work**, organizations can identify inefficiencies, enforce compliance, and improve collaboration.
- Aggregating insights across individual resources and roles helps drive **data-informed process improvements**.
