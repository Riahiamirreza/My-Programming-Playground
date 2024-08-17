
def collatz_seq_count(start: int, counter=0) -> int:
    if start == 1:
        return counter + 1
    if not start % 2: 
        return collatz_seq_count(start/2, counter+1)
    else:
        return collatz_seq_count((3*start) + 1, counter+1)



print(
    max(((i, collatz_seq_count(i)) for i in range(1, 1000_000)), key=lambda x: x[1])
)