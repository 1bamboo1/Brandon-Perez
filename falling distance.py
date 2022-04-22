def falling_distance(t):
    d = (1 / 2) * 9.8 * (t ** 2)
    print(format(d, '6.2f'), 'meters')
    return d

for t in range(1, 11):
    falling_distance(t)
    
#     Python 3.7.9 (bundled)
# >>> %Run 'falling distance.py'
#   4.90 meters
#  19.60 meters
#  44.10 meters
#  78.40 meters
# 122.50 meters
# 176.40 meters
# 240.10 meters
# 313.60 meters
# 396.90 meters
# 490.00 meters
# >>> 