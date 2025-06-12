# Sum of two numbers:
"""
y = lambda a, b: a + b
print(y(3,4))
"""
# Square of a number:
"""
sq = lambda a: a*a
print(sq(4))
"""

#Greater number:
"""
grt = lambda a, b : f"{a} is greater" if (a > b) else f"{b} is greater"
print(grt(90, 67))
"""

# Even number:
"""
even = lambda a : "Even" if (a % 2 == 0) else "Odd"
print(even(3))
"""

# Grades:
# Example: Grading system
grade = lambda score: 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'

# Test the lambda function
print(grade(95))  # Output: A
print(grade(85))  # Output: B
print(grade(75))  # Output: C
print(grade(65))  # Output: D
print(grade(55))  # Output: F
 
