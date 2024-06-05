from sklearn.manifold import MDS
from agent import Agent
from solution import checkSubtour, Combination, optimizer, Combination2
from model1ormoreSEC import moreThan1SEC
from model1SEC import only1SEC
import csv

V = 17
L = 4

q = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]
Q = 15

d = [
[99999, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354, 468, 776, 662],
      [548, 99999, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674, 1016, 868, 1210],
      [776, 684, 99999, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164, 1130, 788, 1552, 754],
      [696, 308, 992, 99999, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822, 1164, 560, 1358],
      [582, 194, 878, 114, 99999, 536, 764, 388, 730, 776, 1118, 400, 514, 708, 1050, 674, 1244],
      [274, 502, 502, 650, 536, 99999, 228, 308, 194, 240, 582, 776, 662, 628, 514, 1050, 708],
      [502, 730, 274, 878, 764, 228, 99999, 536, 194, 468, 354, 1004, 890, 856, 514, 1278, 480],
      [194, 354, 810, 502, 388, 308, 536, 99999, 342, 388, 730, 468, 354, 320, 662, 742, 856],
      [308, 696, 468, 844, 730, 194, 194, 342, 99999, 274, 388, 810, 696, 662, 320, 1084, 514],
      [194, 742, 742, 890, 776, 240, 468, 388, 274, 99999, 342, 536, 422, 388, 274, 810, 468],
      [536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 99999, 878, 764, 730, 388, 1152, 354],
      [502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 99999, 114, 308, 650, 274, 844],
      [388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 99999, 194, 536, 388, 730],
      [354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 99999, 342, 422, 536],
      [468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536, 342, 99999, 764, 194],
      [776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274, 388, 422, 764, 99999, 798],
      [662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730, 536, 194, 798, 99999],
]

mapper = MDS(n_components=2)
map = mapper.fit_transform(d)

testCases = [
            #  [0.65, 0.65], [0.75, 0.65], [0.55, 0.65], [0.45, 0.65],
             [0.65, 0.55], [0.75, 0.55], [0.55, 0.55], [0.45, 0.55],
             [0.65, 0.45], [0.75, 0.45], [0.55, 0.45], [0.45, 0.45],
             [0.65, 0.35], [0.75, 0.35], [0.55, 0.35], [0.45, 0.35]
             ]

# SEC = [[1, 3, 4], [2, 6], [10, 14, 16], [11, 15], [2, 6, 10], [11, 12], [3, 4], [11, 12, 15], [14, 16]]
# # SEC = []
# solution = optimizer(SEC, V, L, map, d, q, Q)
# # print(solution)
# # print(solution)
# # check if new subtours are created after applying the SEC
# orphans = checkSubtour(V, L, solution[1], solution[2])
# print(orphans)

# obj = 6208

file1 = open("1orMore.csv", mode='w', newline='')
writer = csv.writer(file1)
writer.writerow(["gamma", "epsilon_decay", "iterations", "execution_time", "solution_gap"])

file2 = open("1only.csv", mode='w', newline='')
writer = csv.writer(file2)
writer.writerow(["gamma", "epsilon_decay", "iterations", "execution_time", "solution_gap"])

res = optimizer([], V, L, map, d, q, Q)
    
for case in testCases:
    for i in range(5):
        moreThan1SEC(V, L, d, q, Q, map, case[0], case[1], file1)

for case in testCases:
    for i in range(5):
        only1SEC(V, L, d, q, Q, map, case[0], case[1], file2)
    