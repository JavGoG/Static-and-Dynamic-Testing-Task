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
    # 1. missing == instead of just = before 1:
    if card.value = 1:
      return True
      #2.  missing : to else
    else
      return False
   
# 1. typo error, def instead of dif before highest_card() method.
# 2. between card1 and card2 we need to insert a coma ','

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    # 3. card is not declared
    return card
  else:
    return card2
  


def cards_total(self, cards):
  total
  for card in cards:
    # 1. there is nothing called 'value' in a dictionary, 
    # but a values() method yes.
    total += card.value
    # 2. total is a number and can not be linked to a string and:
    # 3. the return statement is placed in wrong place,
    # because it is not going to count the total number,
    # it will store only the first value of the array.
    return "You have a total of" + total
  
```
