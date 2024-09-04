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

def main():
    p = PetriNet()

    p.add_place(1)  # add place with id 1
    p.add_place(2)
    p.add_place(3)
    p.add_place(4)
    p.add_transition("A", -1)  # add transition "A" with id -1
    p.add_transition("B", -2)
    p.add_transition("C", -3)
    p.add_transition("D", -4)

    p.add_edge(1, -1)
    p.add_edge(-1, 2)
    p.add_edge(2, -2).add_edge(-2, 3)
    p.add_edge(2, -3).add_edge(-3, 3)
    p.add_edge(3, -4)
    p.add_edge(-4, 4)

    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.add_marking(1)  # add one token to place id 1
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.fire_transition(-1)  # fire transition A
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.fire_transition(-3)  # fire transition C
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.fire_transition(-4)  # fire transition D
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.add_marking(2)  # add one token to place id 2
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.fire_transition(-2)  # fire transition B
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.fire_transition(-4)  # fire transition D
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    # by the end of the execution there should be 2 tokens on the final place
    print(p.get_tokens(4))

if __name__=="__main__":
    main()

