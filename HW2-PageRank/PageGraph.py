__author__ = 'callie'


class PageGraph:
    def __init__(self, file_path):
        self.file = file_path
        self.in_links = dict()
        self.out_links = dict()
        self.all_nodes = []
        self.sink_nodes = []

    def fetch_graph(self):
        f = file(self.file)
        while True:
            line = f.readline().strip('\n')
            if len(line) == 0:
                break
            nodes = line.split(" ")
            self.all_nodes.append(nodes[0])
            self.in_links[nodes[0]] = []
            for node in nodes[1:]:
                # self.all_nodes.append(nodes[i])

                if nodes[0] in self.in_links:
                    self.in_links[nodes[0]].append(node)
                else:
                    self.in_links[nodes[0]] = [node]

                if node in self.out_links:
                    self.out_links[node] += 1
                else:
                    self.out_links[node] = 1

        f.close()

        # nodes_set = set(self.all_nodes)
        # self.all_nodes = list(nodes_set)

        for k, v in self.in_links.items():
            if k not in self.out_links:
                self.sink_nodes.append(k)

    def test_graph(self):
        for n, p in self.out_links.items():
            print n, p