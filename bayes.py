import math
from scipy.stats import norm

# ほしい分位点の情報
want = [0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95]

fujii_results = [
    # 公式戦
    (1233, 1), (1430, 1), (1340, 1), (1336, 1), (1650, 1), (1536, 1), (1412, 1), (1547, 1), (1322, 1),
    (1539, 1), (1585, 1), (1520, 1), (1780, 1), (1498, 1), (1502, 1)

    # 非公式戦
      , (1858, 1), (1803, -1), (1802, 1), (1768, 1), (1741, 1), (1723, 1), (1695, 1), (1858, -1), (1556, 1)

    #                , (1442, -1)
    #                , (1536, 1)
    #                , (1551, 1)
    #                , (1699, 1)
    #                , (1755, 1)
    #                , (1591, 1)
    #                , (1689, 1)
]

kondou_results = [
    (1246, 1)
    , (1366, 1)
    , (1184, -1)
    , (1393, 1)
    , (1596, -1)
    , (1601, 1)
    , (1472, 1)
    , (1615, 1)
    , (1506, 1)
    , (1502, 1)
    , (1708, -1)
    , (1719, 1)
    , (1476, 1)
    , (1647, 1)
    , (1545, 1)

# 追加
#    , (1542, 1), (1724, 1), (1424, -1), (1458, 1), (1447, 1), (1462, 1), (1823, -1), (1724, 1), (1652, 1), (1628, -1)

]

takano_results = [
    (1636, -1)
    , (1184, -1)
    , (1310, 1)
    , (1558, 1)
    , (1543, -1)
    , (1655, -1)
    , (1594, 1)
    , (1306, 1)
    , (1747, 1)
    , (1583, -1)
    , (1571, 1)
    , (1557, 1)
    , (1684, -1)
    , (1415, -1)
    , (1375, -1)
    #    ,(1642, 1)
]
sasaki_results = [
    (1500, 1)
    , (1536, 1)
    , (1407, 1)
    , (1635, 1)
    , (1743, -1)
    , (1536, -1)
    , (1576, -1)
    , (1458, 1)
    , (1544, -1)
    , (1577, -1)
    , (1250, 1)
    , (1423, 1)
    , (1552, 1)
    , (1667, 1)
    , (1466, 1)
];

kishi_rating = [
    1863,
    1858,
    1856,
    1851,
    1838,
    1836,
    1809,
    1809,
    1803,
    1799,
    1786,
    1784,
    1781,
    1768,
    1767,
    1766,
    1755,
    1752,
    1749,
    1745,
    1745,
    1744,
    1741,
    1741,
    1737,
    1727,
    1724,
    1723,
    1721,
    1707,
    1706,
    1702,
    1699,
    1695,
    1690,
    1688,
    1686,
    1672,
    1667,
    1663,
    1657,
    1656,
    1656,
    1646,
    1643,
    1643,
    1639,
    1638,
    1619,
    1617,
    1616,
    1615,
    1613,
    1611,
    1602,
    1602,
    1602,
    1601,
    1599,
    1597,
    1595,
    1595,
    1591,
    1589,
    1586,
    1586,
    1585,
    1580,
    1579,
    1578,
    1574,
    1573,
    1571,
    1568,
    1566,
    1562,
    1558,
    1556,
    1555,
    1553,
    1553,
    1551,
    1550,
    1549,
    1546,
    1536,
    1536,
    1533,
    1532,
    1531,
    1524,
    1521,
    1520,
    1512,
    1511,
    1509,
    1507,
    1502,
    1501,
    1498,
    1498,
    1498,
    1496,
    1495,
    1494,
    1493,
    1492,
    1490,
    1489,
    1488,
    1485,
    1484,
    1481,
    1479,
    1479,
    1478,
    1478,
    1476,
    1475,
    1474,
    1473,
    1473,
    1470,
    1468,
    1450,
    1446,
    1444,
    1440,
    1436,
    1432,
    1428,
    1420,
    1417,
    1413,
    1407,
    1405,
    1398,
    1395,
    1394,
    1394,
    1393,
    1390,
    1389,
    1387,
    1385,
    1375,
    1373,
    1370,
    1370,
    1365,
    1363,
    1359,
    1332,
    1330,
    1329,
    1329,
    1320,
    1319,
    1280,
    1276,
    1273,
    1271,
    1253,
    1232,
    1218,
    1206
];

param = norm.fit(kishi_rating)
print(param)

# 使用するデータの決定
results = fujii_results

mu = param[0]
sigma = param[1] * param[1]


sigma = 15000

def prob(diff):
    bunbo = 1 + 10 ** (- diff / 400)
    return 1 / bunbo


def normal_distribution(x):
    base = math.exp(- ((x - mu) ** 2) / 2.0 / sigma)
    return base / (math.sqrt(2 * math.pi * sigma))


def prob_dist(x):
    score = (normal_distribution(x + 1) + normal_distribution(x)) / 2
    return score


probs = []
maxp = 0
cand = 1
sum = 0

for rating in range(500, 2500):
    p = 1
    for data in results:
        win_prob = prob(rating - data[0])
        p *= (win_prob if data[1] == 1 else 1 - win_prob)
    p *= prob_dist(rating)
    if maxp < p:
        maxp = p
        cand = len(probs)
    probs.append([rating, p])
    output = [rating, p]
    sum += p
# print(output)
#for i in range(cand - 10, cand + 10):
#    print(probs[i])
print(sum)
for res in probs:
    res[1] = res[1] / sum
sum = 0

for i in range(len(probs)):
    sum += probs[i][1]
    probs[i].append(sum)
# print(probs[i])

w_res = []
for w in want:
    minim = 1000
    cand = []
    for i in range(len(probs)):
        cond = abs(w - probs[i][2])
        if minim > cond:
            minim = cond
            cand = probs[i]
    print(w, end="")
    print(" ", end="")
    print(cand)
    w_res.append(cand[0])
print(w_res)



# print(normal_distribution(1500))
# print(normal_distribution(1600))
# print(normal_distribution(1700))
# print(normal_distribution(1800))
# print(normal_distribution(1900))
# print(normal_distribution(2000))
