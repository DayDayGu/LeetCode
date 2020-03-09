class Solution:
    def fizzBuzz(self, n: int):
        gens_3 = []
        gens_5 = []

        i = 1
        j = 1
        while ( ( 3*i<=n ) ):
            gens_3.append( 3*i )
            i += 1

        while ( ( 5*j<=n ) ):
            gens_5.append( 5*j )
            j += 1
        
        res = [ str(i) for i in range(1, n + 1) ]
        for g_i in gens_3:
            res[g_i - 1] = 'Fizz'
        for g_i in gens_5:
            r = res[g_i - 1]
            if r == 'Fizz':
                res[g_i - 1] += 'Buzz'
            else:
                res[g_i - 1] = 'Buzz'
        return res
