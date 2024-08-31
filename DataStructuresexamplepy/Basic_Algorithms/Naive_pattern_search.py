# Finds patterns and requested data within a larger body of text
# has a runtime of O(n^2) or O(nk), for k is one to onewith n being the length of the text

#######################Iterating_over_text#######################
###////////////////////////////////////////////////////////////###
# Define pattern_search
def pattern_search(text, pattern):
  print("Input Text:", text, "Input Pattern:", pattern)
  for index in range(len(text)):
    print("Text Index:", index)
    for char in range(len(pattern)):
      print("Pattern Index:", char)


text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
# Invoke pattern_search
pattern_search(text, pattern)

#####################Counting_Pattern_Matches#####################
###////////////////////////////////////////////////////////////###
def pattern_search(text, pattern):
  print("Input Text:", text, "Input Pattern:", pattern)
  for index in range(len(text)):
    print("Text Index:", index)
    match_count = 0
    for char in range(len(pattern)):
      print("Pattern Index:", char)
      if pattern[char] == text[index + char]:
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)


text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
pattern_search(text, pattern)

# New inputs to test
text2 = "SOMEMORERANDOMWORDSTOpatternSEARCHTHROUGH"
pattern2 = "pattern"
text3 = "This   still      works with    spaces"
pattern3 = "works"
text4 = "96"
pattern4 = "42"
