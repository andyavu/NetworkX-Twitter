from copeland import Copeland
from triad import Triad


c = Copeland("twitter_combined.txt")
# c = Copeland("doh.txt")
c.createGraph()


''' SECTION 1 - DEGREE RATIO '''
degree_ratio = c.degreeRatio()
# print("Degree Ratio:", c.degreeRatio())
c.saveToCSV("degree_ratio.csv", degree_ratio, ["Node", "Ratio"])
# c.degreeHistogram()


''' SECTION 2 - COPELAND SCORE '''
copeland_scores = c.copelandScores()
# print("Copeland Scores:", copeland_scores)
c.saveToCSV("copeland_scores.csv", copeland_scores, ["Node", "Score"])
# c.copelandHistogram()


''' SECTION 3 - CLOSENESS CENTRALITY '''
closeness_centrality = c.closenessCentrality()
# print("Closeness Centrality:", closeness_centrality)
c.saveToCSV("closeness_centrality.csv", closeness_centrality, ["Node", "Value"])
# c.closenessHistogram()


''' SECTION 4 - BETWEENNESS CENTRALITY '''
betweenness_centrality = c.betweennessCentrality()
# print("Betweenness Centrality:", betweenness_centrality)
c.saveToCSV("betweenness_centrality.csv", betweenness_centrality, ["Node", "Value"])
# c.betweennessHistogram()


''' SECTION 5 - STATISTICS '''
stats = c.getStats()
# print("\nStats:", stats)
c.saveToCSV("stats.csv", stats, ["Node", "Mean", "Median", "Standard Deviation"])


''' SECTION 6 - TRIADIC CENSUS '''
t = Triad("twitter_combined.txt")
# t = Triad("doh.txt")
t.createGraph()

triadic_census = t.triadicCensus()
# print("\nTriadic Census:", triadic_census)
t.saveToCSV("triadic_census.csv", triadic_census, ["Triad", "Count"])
