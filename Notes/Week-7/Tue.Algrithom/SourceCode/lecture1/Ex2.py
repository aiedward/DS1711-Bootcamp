def reverse(S, start, stop):
    if (start<stop):
        S[start], S[stop] = S[stop], S[start]
        reverse(S, start+1, stop-1)
        
S = [1,2,3,4,5]
reverse(S, 0, len(S)-1)

print(S)

