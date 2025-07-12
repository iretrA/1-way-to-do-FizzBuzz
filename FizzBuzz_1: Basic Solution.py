class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzbuzzed = list(range(1, n + 1))
      #goes through each and every single element in the list to see if is applicable to the conditions provided
        for i in fizzbuzzed:
            if i % 3 == 0 and i % 5 == 0:
                fizzbuzzed[fizzbuzzed.index(i)] = "FizzBuzz"
            elif i % 3 == 0:
                fizzbuzzed[fizzbuzzed.index(i)] = "Fizz"
            elif i % 5 == 0:
                fizzbuzzed[fizzbuzzed.index(i)] = "Buzz"
            else:
                continue
        #list comprehension because the soltuions require the elements to be strngs.
        return [str(x) for x in fizzbuzzed]
