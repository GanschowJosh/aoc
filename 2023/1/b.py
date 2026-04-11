with open(input(), 'r') as f:
  lines=f.readlines()

word_map = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

def find_first(s):
  for i in range(len(s)):
    try:
      i=int(s[i])
      return i
    except:
      pass
    if i+3>=len(s):
      continue
    if s[i:i+3] in word_map:
      return word_map[s[i:i+3]]
    if i+4>=len(s):
      continue
    if s[i:i+4] in word_map:
      return word_map[s[i:i+4]]
    if i+5>=len(s):
      continue
    if s[i:i+5] in word_map:
      return word_map[s[i:i+5]]

def find_last(s):
  for i in range(len(s)-1,-1,-1):
    try:
      i=int(s[i])
      return i
    except:
      pass
    if i+3>=len(s):
      continue
    if s[i:i+3] in word_map:
      return word_map[s[i:i+3]]
    if i+4>=len(s):
      continue
    if s[i:i+4] in word_map:
      return word_map[s[i:i+4]]
    if i+5>=len(s):
      continue
    if s[i:i+5] in word_map:
      return word_map[s[i:i+5]]


s=0
for line in lines:
  s+=(find_first(line)*10)
  s+=find_last(line)
print(s)