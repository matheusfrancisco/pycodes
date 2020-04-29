"""
Stric

- Statements evaluated when reached
- Variables assigned results immediately
- Pay up front
- Strict evaluation can be costly
- Can be cheaper on average in multithreaded applications
- Set backordered items stricts

Lazy

- Evaluation delayed until results needed
- Variables assigned when needed
- Pay as you go
- Lazy evaluation can save resources
- Might cos more overall in multithreaded app
- Set backoredered items lazy:
- Every thread can update but will block on others updating the collections

"""

"""
Demo:
  Want to know the total value of all items
  Use a property in the Order class
  Computation may be expensive
  Grand total costs even more!
  Recalculate when the collections changes
"""
