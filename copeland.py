import networkx as nx
import matplotlib.pyplot as plt
import csv

class Copeland:
    def __init__(self, file_name):
        self.file_name = file_name
        self.dg = nx.DiGraph()

    def createGraph(self):
        file = open(self.file_name, "r")
        try:
            lines = file.readlines()
            # print("reading...")
            for line in lines:
                nodes = line.strip().split(" ")
                self.dg.add_edge(int(nodes[0]), int(nodes[1]))
            # print("...done\n")
        finally:
            file.close()

    def getInfo(self):
        return nx.info(self.dg)

    def degreeRatio(self):
        degree_ratios = {}
        for n in self.dg.nodes:
            degree_ratio = (self.dg.out_degree[n] + 1) / (self.dg.in_degree[n] + 1)
            degree_ratios.update({n: degree_ratio})
        return degree_ratios

    def copelandScores(self):
        copeland_scores = {}
        for n in self.dg.nodes:
            copeland_score = self.dg.out_degree[n] - self.dg.in_degree[n]
            copeland_scores.update({n: copeland_score})
        return copeland_scores

    def degreeHistogram(self):
        plt.figure()
        plt.title("Degree Ratio")
        plt.xlabel("Ratio")
        plt.ylabel("Node Count")
        plt.hist(self.degreeRatio().values())
        plt.show()

    def copelandHistogram(self):
        plt.figure()
        plt.title("Copeland Score")
        plt.xlabel("Score")
        plt.ylabel("Node Count")
        plt.hist(self.copelandScores().values())
        plt.show()

    def closenessCentrality(self):
        return nx.closeness_centrality(self.dg)

    def closenessHistogram(self):
        plt.figure()
        plt.title("Closeness Centrality")
        plt.xlabel("Value")
        plt.ylabel("Node Count")
        plt.hist(self.closenessCentrality().values())
        plt.show()

    def betweennessCentrality(self):
        return nx.betweenness_centrality(self.dg)

    def betweennessHistogram(self):
        plt.figure()
        plt.title("Betweenness Centality")
        plt.xlabel("Value")
        plt.ylabel("Node Count")
        plt.hist(self.betweennessCentrality().values())
        plt.show()

    def getStats(self):
        highest_betweenness = max(self.betweennessCentrality().items(), key=lambda x: x[1])
        betweenness_list = []
        for key, value in self.betweennessCentrality().items():
            if value == highest_betweenness[1]:
                betweenness_list.append(key)
        stats = {}
        for n in betweenness_list:
            values = [self.degreeRatio()[n], self.copelandScores()[n], self.closenessCentrality()[n]]
            values.sort()
            mean = (values[0] + values[1] + values[2]) / 3
            median = values[1]
            total = 0
            for i in values:
                temp = i - mean
                temp = temp**2
                total += temp
            standard_deviation = (total / 3)**0.5
            stats.update({n: [mean, median, standard_deviation]})
        return stats

    def saveToCSV(self, file_name, data, csv_columns):
        try:
            this = False
            for k in data.keys():
                if str(type(data[k])) == "<class 'list'>":
                    this = True
                break
            # create CSV for stats
            if this:
                with open(file_name, "w") as f:
                    f.write("{0}, {1}, {2}, {3}\n".format(csv_columns[0], csv_columns[1], csv_columns[2], csv_columns[3]))
                    [f.write("{0}, {1}, {2}, {3}\n".format(key, value[0], value[1], value[2])) for key, value in data.items()]
            # create CSV for others
            else:
                with open(file_name, "w") as f:
                    f.write("{0}, {1}\n".format(csv_columns[0], csv_columns[1]))
                    [f.write("{0}, {1}\n".format(key, value)) for key, value in data.items()]
        except:
            print("error")
