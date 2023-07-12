import pandas as pd
import matplotlib.pyplot as plt

class Graph():
    data = pd.DataFrame()
    graph = None
    name_x = ''
    name_y = ''
    data_x = data[name_x]
    data_y = data[name_y]
    title = "Relation between {} and {}".format(name_x, name_y)

    def __init__(self, graph, title, data, name_x, name_y, data_x, data_y):
        self.data = data
        self.graph = graph
        self.name_x = name_x
        self.name_y = name_y
        self.data_x = data_x
        self.data_y = data_y
        self.title = title

    def printGraph():
        pass