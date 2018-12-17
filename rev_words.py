s = "Hey there my friend"

#reverse string and then reverse characters of each individual word
words = s[::-1].split()
print ' '.join([w[::-1] for w in words])
#pythonic way
print ' '.join([w[::-1] for w in s[::-1].split()])

#reverse characters of each individual word and then reverse string
rev_words = [w[::-1] for w in s.split()]
print ' '.join(rev_words)[::-1]

#split string and reverse words
words = s.split()
rev_words = [w for w in words[::-1]]
print ' '.join(rev_words)
#pythonic way
print ' '.join(s.split()[::-1])
