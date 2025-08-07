# Problem-3: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5
#     5) input a = 5, then output : 1, 3, 5, 7, 9
#     6) input a = 6, then output : 1, 3, 5, 7, 9
#     .
#     .
#     7) input a = x, then output : 1, 3, 5, 7, .......


class Solutions:

  def __init__(self, a: int) -> int:
    self.a = a

  def generate_series_of_a(self):
    swap_val = self.a

    if self.a % 2 == 0:
      swap_val = self.a - 1

    n = self.a * 2
    out = [i for i in range(n) if i % 2 == 1]

    return out[:swap_val]

if __name__ == '__main__':
  a = int(input("value : "))
  solutions = Solutions(a)
  print(solutions.generate_series_of_a())