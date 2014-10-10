__author__ = 'callie'


class PageGraph:
    def __init__(self, file_path):
        self.file = file_path
        # in-link pages for each page
        self.in_links = dict()
        # number of out-link pages for each page
        self.out_links = dict()
        # all pages in the file
        self.all_nodes = []
        # page list that have no out links
        self.sink_nodes = []

    def fetch_graph(self):
        f = file(self.file)
        while True:
            line = f.readline().strip('\n')
            if len(line) == 0:
                break
            # split line by " " to pages
            nodes = line.split(" ")
            # add the first page of the line to all pages set
            self.all_nodes.append(nodes[0])
            self.in_links[nodes[0]] = []
            for node in nodes[1:]:
                # add the rest pages of the line to the in-links set
                if nodes[0] in self.in_links:
                    self.in_links[nodes[0]].append(node)
                else:
                    self.in_links[nodes[0]] = [node]
                # count out-links for rest pages of the line
                if node in self.out_links:
                    self.out_links[node] += 1
                else:
                    self.out_links[node] = 1

        f.close()
        # calculate the sink pages
        for k, v in self.in_links.items():
            if k not in self.out_links:
                self.sink_nodes.append(k)
