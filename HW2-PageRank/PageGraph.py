__author__ = 'callie'


class PageGraph:
    def __init__(self, file_path):
        self.file = file_path
        # in-link pages for each page
        self.in_links = dict()
        # number of out-link pages for each page
        self.out_links_count = dict()
        # out-link pages for each page
        self.out_links = dict()
        # all pages in the file
        self.all_nodes = []
        # page list that have no out links
        self.sink_nodes = []

    def fetch_graph(self):
        f = open(self.file)
        while True:
            line = f.readline().strip('\n')
            if len(line) == 0:
                break
            # split line by " " to pages
            nodes = line.strip().split(' ')
            # add the first page of the line to all pages set
            self.all_nodes.append(nodes[0])
            if nodes[0] not in self.in_links:
                self.in_links[nodes[0]] = set()
            for node in nodes[1:]:
                # add the rest pages of the line to the in-links set
                self.in_links[nodes[0]].add(node)

                # count out-links for rest pages of the line
                if node in self.out_links:
                    self.out_links[node].add(nodes[0])
                else:
                    self.out_links[node] = set()
                    self.out_links[node].add(nodes[0])

        f.close()

        # calculate the out-link counts
        for k, v in self.out_links.items():
            self.out_links_count[k] = len(v)
        # calculate the sink pages
        for k, v in self.in_links.items():
            if k not in self.out_links:
                self.sink_nodes.append(k)
