# Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1, 3
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5, 7
#     .
#     .
#     5) input a = x, then output : 1, 3, 5, 7, .......


class Solutions:
  def __init__(self, a: int) -> int:
    self.a = a*2
  def generate_series_of_a(self):
    out = [i for i in range(self.a) if i % 2 == 1]
    return out

if __name__ == '__main__':
  a = int(input("value : "))
  solution = Solutions(a)
  print(solution.generate_series_of_a())
