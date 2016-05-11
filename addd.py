'''
Must have a return value,else it will return None
'''
def addd(n):
     sum = 0
     if n > 0:
             sum = n + addd(n - 1)
             return sum
     else:
             return n


