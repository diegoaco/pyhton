# Finds the number of ways to climb n stairs by climbing a determined number of steps at a time 

def main(steps, t):
    path = []       # Empty list that will contain the different combinations
    
    # Subroutine
    def sub(chain):
        for i in steps:
            s = sum(chain+[i])
            if s < t:
                sub(chain + [i])  # Revursive function
            elif s == t:   # If the sum reaches the number of steps in the stairs the chain is appended to path list
                path.append(chain + [i])
    sub([])
    return len(path), path
    
# Note that the subroutine may produce the combinations that exceeds the number of steps in the stairs. These are not taken into account though

print(main([1,2],6))
