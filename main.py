from copeland import Copeland


# c = Copeland("twitter_combined.txt")
# c = Copeland("doh.txt")
c = Copeland("test.txt")

c.createGraph()
# print(c.getInfo())
# print("Degree Ratio:", c.getDegreeRatio())
# print("Copeland Score:", c.getCopelandScore())
c.closenessCentrality()
c.betweennessCentrality()
