from asyncio.unix_events import can_use_pidfd
from datetime import datetime
import xml.etree.ElementTree as ElementTree

class Place:
    def __init__(self, id, tokens):
        self.id = id
        self.tokens = tokens
        self.sources = list()
        self.targets = list()

    def has_token(self):
        return self.tokens > 0

    def add_source(self, place):
        self.sources.append(place)

    def add_target(self, place):
        self.targets.append(place)

    def add_token(self):
        self.tokens += 1

    def fire(self):
        self.tokens -= 1

class Transition:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.sources = list()
        self.targets = list()

    def add_source(self, place):
        self.sources.append(place)

    def add_target(self, place):
        self.targets.append(place)

    def is_enabled(self):
        if len(self.sources) == 0:
            return False
        enabled = True
        for source in self.sources:
            if not source.has_token():
                enabled = False
        return enabled

    def fire(self):
        for source in self.sources:
            source.fire()
        for target in self.targets:
            target.add_token()

class PetriNet():

    def __init__(self):
        self.nodes = {}

    def add_place(self, name):
        self.set_node(name, Place(name, 0))

    def add_transition(self, name, id):
        self.set_node(id, Transition(name, id))
        return self

    def add_edge(self, source, target):
        source_node = self.get_node(source)
        target_node = self.get_node(target)

        self.get_node(source).add_target(target_node)
        self.get_node(target).add_source(source_node)
        return self

    def get_tokens(self, place):
        return self.get_node(place).tokens

    def is_enabled(self, transition):
        return self.get_node(transition).is_enabled()

    def add_marking(self, place):
        node = self.get_node(place)
        node.tokens = node.tokens + 1

    def fire_transition(self, transition):
        self.get_node(transition).fire()

    def get_node(self, name):
        return self.nodes[str(name)]

    def set_node(self, name, node):
        self.nodes[str(name)] = node

    def transition_name_to_id(self, name):
        return self.nodes[str(name)].id

def read_from_file(filename):
    try:
        tree = ElementTree.parse(filename)
        root = tree.getroot()
    except Exception as e:
        print(f"Error")
        return None
    ns = {'xes': 'http://www.xes-standard.org/'}
    event_log_dict = {}
    for trace in root.findall('xes:trace', ns):
        case_id = None
        events = []
        for attr in trace.findall('xes:string', ns):
            if attr.get('key') == 'concept:name':
                case_id = attr.get('value')
                break
        for event in trace.findall('xes:event', ns):
            event_data = {}
            for attr in event:
                key = attr.get('key')
                value = attr.get('value')
                if key == "time:timestamp":
                    value = datetime.fromisoformat(value)
                    value = value.replace(tzinfo=None)
                elif key == "cost":
                    value = int(value)
                event_data[key] = value
            events.append(event_data)
        if case_id:
            event_log_dict[case_id] = events
    return event_log_dict

# 1. Create set of traces
# * Find direct succession relations (be aware of choice/parallel relations). These will need to occur in the specific order
# * Find causal relations
# * Find parallel relations
# * Find choice (be aware of parallel relations). Also could be checked by checking whether the relation already exists in other relations
# ^^^^^ Result from relations will be 4 sets ^^^^^

# 2. Create map of traces with the given relations type from the result previous step. Fill out the empty places with choices

# 3. Algorithm
#   1. Create set with all traces
#   2. Set with first trace
#   3. Set with last trace
#   4. Check causal relation, if both traces are choices between them, add them to the set
#   5. Create set simplifications based on the relations from previous set. If no relations could be simplified, just copy the set
#   6. Create place for each set from previous step and two additional places iw and ow.
#   7. Create set of transitions with based on the previous answer. Make sure to create transitions for each input and output place + create transtions for iw and ow. iw is input place and ow is output place. iw connects to first place, ow connects to last place
#   8. Output set of places, transitions and relations

# Legend
# Tw = transitions (A, B, C..)
# Pw = places (p(A, B), p(B, C),...)
# Fw = transitions ([A, p(A, B)], [p(B, C), C],...)

def alpha(log):
    traces = set()
    for case in log:
        events = log[case]
        for i in range(len(events) - 1):
            current_event = events[i]
            next_event = events[i + 1]
            traces.add((current_event['concept:name'], next_event['concept:name']))
    # Find causal relations
    causal_relations = set()
    for trace in traces:
        for trace2 in traces:
            if trace[1] == trace2[0]:
                causal_relations.add((trace[0], trace2[1]))

    # Find parallel relations
    parallel_relations = set()
    for trace in traces:
        for trace2 in traces:
            if trace[0] == trace2[0] and trace[1] != trace2[1]:
                parallel_relations.add((trace[1], trace2[1]))
    print(parallel_relations)



#     return PetriNet()

def main():
    mined_model = alpha(read_from_file("extension-log.xes"))

    def check_enabled(pn):
        ts = ["record issue", "inspection", "intervention authorization", "action not required", "work mandate",
              "no concession", "work completion", "issue completion"]
        for t in ts:
            print(pn.is_enabled(pn.transition_name_to_id(t)))
        print("")

    trace = ["record issue", "inspection", "intervention authorization", "work mandate", "work completion",
             "issue completion"]
    for a in trace:
        check_enabled(mined_model)
        mined_model.fire_transition(mined_model.transition_name_to_id(a))


if __name__ == "__main__":
    main()