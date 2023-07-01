# take in a string array like racecar (palindrome)
# or abcabc (not a palindrome)
# or A
# using an O(n) time complexity and O(n) space complexity
def is_palindrome(s):
  # turn string into list (array)
  ra = list(s)
  # set left array pointer to start
  left = 0

  # set right array pointer to end
  right = len(ra) - 1

  # if size is 1 simply return True
  if len(ra)==1:
    return True

  # while the left pointer has not crossed over the right pointer (no comparisons left to make)
  while left < right:
    # check if the values are equivalent, if NOT then the string is not a palindrome
    if ra[left] != ra[right]:
      return False
    # otherwise if that check is passed, advance the left pointer by one, the right pointer by one (decrement)
    left = left + 1
    right = right -1
  # if you made it here it is a palindrome
  return True
