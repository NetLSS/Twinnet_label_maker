
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(P, A, B):
    area = abs ( (A.x - P.x) * (B.y - P.y) - (A.y - P.y) * (B.x - P.x) )
    AB = ( (A.x - B.x) ** 2 + (A.y - B.y) ** 2 ) ** 0.5
    print(f"area: {area/2}")
    print(f"AB: {AB}")
    return ( area / AB )

dist(Point(1.0, 5.0), Point(-4.0, -7.0), Point(5.0, 2.0))
dist(Point(1.0, 1.0), Point(2.0, 3.0), Point(5.0, 4.0))








"""
https://m.blog.naver.com/PostView.nhn?blogId=honeyeah&logNo=110155336328&proxyReferer=https:%2F%2Fwww.google.com%2F
https://gtska.tistory.com/21
"""