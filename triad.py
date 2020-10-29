import networkx as nx
import matplotlib.pyplot as plt

class Triad:
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

    def triadicCensus(self):
        return nx.triadic_census(self.dg)

    def saveToCSV(self, file_name, data, csv_columns):
        try:
            with open(file_name, "w") as f:
                f.write("{0}, {1}\n".format(csv_columns[0], csv_columns[1]))
                [f.write("{0},{1}\n".format(key, value)) for key, value in data.items()]
        except:
            print("error")
