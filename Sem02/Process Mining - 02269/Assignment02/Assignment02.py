import csv
from io import StringIO
import xml.etree.ElementTree as ElementTree
from datetime import datetime
from numbers import Number


def log_as_dictionary(csv_str):
    logs = {}
    csv_str = csv_str.strip()
    csv_file = StringIO(csv_str)
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        if row == []:
            continue
        task = row[0]
        case = row[1]
        user = row[2]
        timestamp = row[3]
        if case not in logs:
            logs[case] = {}
        logs[case][task] = {'case': case, 'user': user, 'timestamp': datetime.fromisoformat(timestamp), 'task': task}
    return logs

def dependency_graph_inline(logs):
    dependencies = {}
    for case in logs:
        previous_task = None
        tasks = logs[case]
        for task in tasks:
            if previous_task is None:
                previous_task = task
                continue
            if previous_task not in dependencies:
                dependencies[previous_task] = {}
            if task not in dependencies[previous_task]:
                dependencies[previous_task][task] = 0
            dependencies[previous_task][task] += 1
            previous_task = task
    return dependencies


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

def dependency_graph_file(logs):
    dependencies = {}
    for case in logs:
        previous_task_name = None
        tasks = logs[case]
        for task in tasks:
            task_name = task["concept:name"]
            if previous_task_name is None:
                previous_task_name = task_name
                continue
            if previous_task_name not in dependencies:
                dependencies[previous_task_name] = {}
            if task_name not in dependencies[previous_task_name]:
                dependencies[previous_task_name][task_name] = 0
            dependencies[previous_task_name][task_name] += 1
            previous_task_name = task_name
    return dependencies


def main():
    log = read_from_file("extension-log.xes")
    for case_id in sorted(log):
        print((case_id, len(log[case_id])))
    case_id = "case_123"
    event_no = 0
    print((log[case_id][event_no]["concept:name"], log[case_id][event_no]["org:resource"], log[case_id][event_no]["time:timestamp"],  log[case_id][event_no]["cost"]))


if __name__ == "__main__":
    main()
