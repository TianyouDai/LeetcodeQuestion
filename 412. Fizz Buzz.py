class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzbuzz_list = []
        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:
                fizzbuzz_list.append('FizzBuzz')
            elif i % 3 == 0:
                fizzbuzz_list.append('Fizz')
            elif i % 5 == 0:
                fizzbuzz_list.append('Buzz')
            else:
                print(i)
                fizzbuzz_list.append(str(i))
        return fizzbuzz_list
        
