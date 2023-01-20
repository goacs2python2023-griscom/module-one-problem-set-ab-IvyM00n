def casinochance():
    values = input()
    v1, v2 = values.split( )
    faces = input()
    count_v1 = faces.count(v1)
    count_v2 = faces.count(v2)
    percent = (count_v1/6)*(count_v2/6)
    print(percent)

casinochance()
