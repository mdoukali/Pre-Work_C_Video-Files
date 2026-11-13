# Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and skipping any digit with a value of zero. There cannot be more than 3 identical symbols in a row.

# In Roman numerals:

# 1990 is rendered: 1000=M + 900=CM + 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII.
# 1666 uses each Roman symbol in descending order: MDCLXVI.
# Example:

#   1 -->       "I"
# 1000 -->       "M"
# 1666 --> "MDCLXVI"
# Help:

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

def solutions(n):

   n, ans  = thousands_roman(n)
   n, ans = hundreds_roman(n, ans)
   n, ans = tens_roman(n, ans)
   ans = ones_roman(n, ans)

   return ans

def thousands_roman(n):

   number_of_M = n // 1000

   Ms = number_of_M * "M"
   remainder = n - (number_of_M * 1000)

   return remainder, Ms

def hundreds_roman(n, ans):

   if n // 900 == 1:
      ans += "CM"
      n -= 900

   if n // 500 == 1:
      ans += "D"
      n -= 500

   if n // 400 == 1:
      ans += "CD"
      n -= 900

   Cs = n // 100

   n -= 100 * Cs

   ans += "C" * Cs

   return n, ans

def tens_roman(n, ans):

   if n // 90 == 1:
      ans += "XC"
      n -= 90

   if n // 50 == 1:
      ans += "L"
      n -= 50
      
   if n // 40 == 1:
      ans += "XL"
      n -= 40

   tens = n // 10 

   n -= tens * 10

   ans += tens * "X"

   return n, ans

def ones_roman(n, ans):

   if n // 9 == 1:
      ans += "IX"
      n -= 9

   if n // 5 == 1:
      ans += "V"
      n -= 5

   if n // 4 == 1:
      ans += "IV"
      n -= 4

   ans += n * "I"

   return ans

print(solutions(3999))
print(solutions(3888))
print(solutions(3555))
print(solutions(3444))
print(solutions(3111))