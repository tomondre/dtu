from datetime import datetime
import xml.etree.ElementTree as ElementTree
import csv
from io import StringIO
from itertools import combinations
import copy

class Place:
    def __init__(self, name, tokens):
        self.name = name
        if tokens is None:
            tokens = 0
        self.tokens = tokens
        self.initial_tokens = tokens
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

    def remove_token(self, count=1):
        self.tokens -= count

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

    def reset_marking(self):
        for node in self.nodes.values():
            if isinstance(node, Place):
                node.tokens = node.initial_tokens


def log_as_dictionary(csv_str):
    logs = {}
    csv_str = csv_str.strip()
    csv_file = StringIO(csv_str)
    csv_reader = csv.reader(csv_file, delimiter=';')
    for index, row in enumerate(csv_reader):
        if not row:
            continue
        task = row[0]
        case = row[1]
        user = row[2]
        timestamp = row[3]
        if case not in logs:
            logs[case] = []
        logs[case].append({'case': case, 'user': user, 'timestamp': datetime.fromisoformat(timestamp), 'task': task, 'concept:name': task})
    return logs

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

def alpha(log):
    succession = set()
    for case in log:
        events = log[case]
        for i in range(len(events) - 1):
            current_event = events[i]
            next_event = events[i + 1]
            succession.add((current_event['concept:name'], next_event['concept:name']))

    all_activities = set()
    for a, b in succession:
        all_activities.add(a)
        all_activities.add(b)

    causality = set()
    parallelism = set()
    choice = set()

    for a, b in succession:
        if (b, a) not in succession:
            causality.add((a, b))

    for a, b in succession:
        if (b, a) in succession and (a, b) in succession:
            parallelism.add((a, b))

    for a in all_activities:
        for b in all_activities:
            if (a, b) not in causality and (b, a) not in causality and (a, b) not in parallelism and (
            b, a) not in parallelism:
                choice.add((a, b))

    relationship_table = {}

    # Fill the dictionary with relationships
    for a in all_activities:
        if a not in relationship_table:
            relationship_table[a] = {}
        for b in all_activities:
            if b not in relationship_table:
                relationship_table[b] = {}
            # Diagonals
            if (a, b) in causality:
                relationship_table[a][b] = '->'
                relationship_table[b][a] = '<-'
            elif (a, b) in parallelism:
                relationship_table[a][b] = '||'
            elif (a, b) in choice:
                relationship_table[a][b] = '#'
            else:
                # Is this ok?
                if b not in relationship_table[a]:
                    relationship_table[a][b] = '#'
                if a not in relationship_table[b]:
                    relationship_table[b][a] = '#'
    # Print the table

    def print_table():
        header = "                  " + " | ".join(sorted(all_activities))
        print(header)
        print("-" * len(header))

        for a in sorted(all_activities):
            row = f"{a: <27}" + "|        "+ "        |       ".join(relationship_table[a][b] for b in sorted(all_activities))
            print(row)

    # print_table()

    # Tw
    tw = all_activities

    # t1 first activities
    t1 = set()
    for case in log:
        events = log[case]
        t1.add(events[0]['concept:name'])

    # to last activities
    to = set()
    for case in log:
        events = log[case]
        to.add(events[-1]['concept:name'])

    # Generate all subsets of tw
    tw_list = list(tw)

    # tw subsets
    # Choice relation elements
    tw_subsets = []
    for i in range(1, len(tw_list) + 1):
        for subset in combinations(tw_list, i):
            tw_subsets.append(subset)

    choice_subsets = []

    for subset in tw_subsets:
        is_choice = True
        for a1, a2 in combinations(subset, 2):
            if relationship_table[a1][a2] != '#':
                is_choice = False
                break
        if is_choice:
            choice_subsets.append(subset)

    xw = set()

    for A in choice_subsets:
        for B in choice_subsets:
            if A and B:
                valid = True
                for a in A:
                    for b in B:
                        if (a, b) not in causality:
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    xw.add((frozenset(A), frozenset(B)))

    xw_list = list(xw)
    yw = set(xw_list)

    for (a, b) in xw_list:
        for (a_sub, b_sub) in xw_list:
            if (a, b) != (a_sub, b_sub):
                if a <= a_sub and b <= b_sub:
                    if (a, b) in yw:
                        yw.discard((a, b))
                    break

    def build_place_key(inputs, outputs):
        input_str = ','.join(sorted(inputs))
        output_str = ','.join(sorted(outputs))
        return f"p({input_str},{output_str})"

    pw = set()
    pw.add('iw')
    pw.add('ow')
    for (inputs, outputs) in yw:
        place_name = build_place_key(inputs, outputs)
        pw.add(place_name)

    fw = set()
    for (inputs, outputs) in yw:
        place_name = build_place_key(inputs, outputs)
        for a in inputs:
            fw.add((a, place_name))
        for b in outputs:
            fw.add((place_name, b))

    for t in t1:
        fw.add(('iw', t))

    for t in to:
        fw.add((t, 'ow'))

    pn = PetriNet()
    for p in pw:
        pn.add_place(p)
    for t in tw:
        pn.add_transition(t, t)
    for f in fw:
        source = f[0]
        target = f[1]
        pn.add_edge(source, target)
    pn.add_marking('iw')

    return pn

def apply_trace(petri_net, trace):
    m_i = 0  # missing
    c_i = 0  # consumed
    p_i = 0  # produced
    r_i = 0  # remaining

    p_i += 1  # produced by iw

    for task in trace:
        transition = petri_net.get_node(task)

        for place in transition.sources:
            if place.tokens <= 0:
                m_i += 1
                place.add_token()

        for place in transition.sources:
            place.remove_token()
            c_i += 1

        for place in transition.targets:
            place.add_token()
            p_i += 1

    ow_place = petri_net.get_node('ow')
    if ow_place.tokens == 0:
        petri_net.get_node('ow').add_token()
        m_i += 1

    c_i += 1
    ow_place.fire()

    for node in petri_net.nodes.values():
        if isinstance(node, Place):
            r_i += node.tokens

    return m_i, c_i, r_i, p_i

def fitness_token_replay(log, model):
    traces_dict = {}
    for case in log:
        events = log[case]
        trace = tuple(event['concept:name'] for event in events)
        if trace in traces_dict:
            traces_dict[trace] += 1
        else:
            traces_dict[trace] = 1

    total_m = 0
    total_c = 0
    total_r = 0
    total_p = 0

    for trace, n_i in traces_dict.items():
        petri_net_copy = copy.deepcopy(model)

        m_i, c_i, r_i, p_i = apply_trace(petri_net_copy, trace)

        total_m += n_i * m_i
        total_c += n_i * c_i
        total_r += n_i * r_i
        total_p += n_i * p_i

    if total_c == 0:
        fitness_consumed = 0
    else:
        fitness_consumed = 1 - (total_m / total_c)

    if total_p == 0:
        fitness_produced = 0
    else:
        fitness_produced = 1 - (total_r / total_p)

    fitness = 0.5 * fitness_consumed + 0.5 * fitness_produced
    return fitness


def main():
    log = read_from_file("extension-log.xes")
    log_noisy = read_from_file("extension-log-noisy.xes")

    mined_model = alpha(log)
    print(round(fitness_token_replay(log, mined_model), 5))
    print(round(fitness_token_replay(log_noisy, mined_model), 5))

if __name__ == "__main__":
    main()
