def solution(N):
  """
  Generates a string with as many distinct lowercase letters as possible.

  Args:
      N: The length of the desired string.

  Returns:
      A string containing distinct lowercase letters with equal occurrences.
  """

  # Special case: N = 1 (return 'a')
  if N == 1:
    return 'a'

  # Find prime factors of N (including 2)
  prime_factors = []
  i = 2
  while i * i <= N:
    while N % i == 0:
      prime_factors.append(i)
      N //= i
    i += 1
  if N > 1:
    prime_factors.append(N)

  # Count the maximum number of letters based on prime factors
  max_letters = 0
  for factor in prime_factors:
    if factor > 2:  # Consider only factors greater than 2
      max_letters += 1

  # Create a pattern of letters and repeat it
  pattern = ''
  for i in range(max_letters):
    pattern += chr(ord('a') + i)  # Add lowercase letters sequentially

  return (pattern * (N // max_letters))[:N]  # Repeat the pattern
