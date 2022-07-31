### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # 1. Missing '==' instead of just '=' before 1:
    if card.value = 1:
      return True
      #2.  Missing ':' to else
    else
      return False
   
# 1. Typo error, def instead of dif before highest_card() method.
# 2. Between card1 and card2 we need to insert a coma ','.
  dif highest_card(self, card1 card2):
  # Bad indentation in if else statement
  if card1.value > card2.value:
    # 3. card is not declared in this function.
    # 4. The most logical is return card1 variable.
    return card
  else:
    return card2
  

# 1. Bad indentation of this method.
def cards_total(self, cards):
  # 2. total is not initialised. 
  total
  for card in cards:
    total += card.value
    # 3. The return statement is placed in wrong place,
    # because it is not going to count the total number,
    # it will store only the first value of the array.
    # 4. We can not link one string with a number 'total'.
    return "You have a total of" + total
  
```
