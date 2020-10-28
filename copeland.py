import networkx as nx
import matplotlib.pyplot as plt


class Copeland:
    def __init__(self, file_name):
        self.file_name = file_name
        self.dg = nx.DiGraph()

    def createGraph(self):
        file = open(self.file_name, "r")
        try:
            lines = file.readlines()
            print("reading...")
            for line in lines:
                nodes = line.strip().split(" ")
                self.dg.add_edge(nodes[0], nodes[1])
            print("...done\n")
        finally:
            file.close()

    def getInfo(self):
        print(nx.info(self.dg))

    def getDegreeRatio(self):
        degree_ratios = {}
        for n in self.dg.nodes:
            degree_ratio = (self.dg.out_degree[n] + 1) / (self.dg.in_degree[n] + 1)
            degree_ratios.update({n: degree_ratio})
        return degree_ratios

    def getCopelandScore(self):
        copeland_scores = {}
        for n in self.dg.nodes:
            copeland_score = self.dg.out_degree[n] - self.dg.in_degree[n]
            copeland_scores.update({n: copeland_score})
        return copeland_scores

    def closenessCentrality(self):
        print(nx.closeness_centrality(self.dg))

    def betweennessCentrality(self):
        print(nx.betweenness_centrality(self.dg))