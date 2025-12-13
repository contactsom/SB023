text="Get Certified Get Ahead Get Simplilearn"
# 1. Find the occurance of each words

words=text.lower().split()
print(words) # ['get', 'certified', 'get', 'ahead', 'get', 'simplilearn']

frequency={}
for word in words:
    frequency[word]=frequency.get(word,0)+1

print("Find the occurance of each words :: ",frequency)
