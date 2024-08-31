def polynomial_hash(s):
  hash_value = 0
  for i in range(len(s)):
    hash_value += (ord(s[i])*(26**(len(s) - i - 1)))
  return hash_value

def polynomial_rolling_hash(s, H, c):
  return (H - ord(s[0]) * 26**(len(s) - 1)) * 26 + ord(c)

def rabin_karp_algorithm(pattern, text):
  pattern_length = len(pattern)
  text_length = len(text)
  occurrences = 0
  substring = text[: pattern_length]
  substring_hash = polynomial_hash(substring)
  pattern_hash = polynomial_hash(pattern)
  # Checkpoint 1
  if (pattern_hash == substring_hash):
    occurrences += 1
  for c in text[pattern_length:]:
    substring_hash = polynomial_rolling_hash(substring, substring_hash, c)
    substring = substring[1:] + c
    if (pattern_hash == substring_hash):
        occurrences += 1
  return occurrences

# Checkpoint 2 and 3
pattern = 1000*'A'
text = 1000000*'A'
print(rabin_karp_algorithm(pattern, text))