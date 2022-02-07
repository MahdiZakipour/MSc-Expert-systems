#!/usr/bin/env python
# coding: utf-8

# In[1]:


from experta import *

class mahdi(Parent_mahdi):
    def mahdi2():
        pass
    


# In[6]:


### FACTS

# 1st way to define facts
class Alert(Fact):
    """The alert level."""
    pass

class Status(Fact):
    """The system status."""
    pass


f1 = Alert('red')
f2 = Status('critical')

print(f1)
print(f2)
#print(help(Fact))


# In[54]:


### RULES
# The LHS describes (using patterns) the conditions on which the rule * should be executed (or fired).
# The RHS is the set of actions to perform when the rule is fired.

class my_fact():
    pass

# Procedure:   MIND THE DECORATION !
@Rule(my_fact())  # This is the LHS  -- if section
def match_with_every_myfact():
  print("""This rule will match with every instance of `MyFact`.""")
  # This is the RHS  -- action
  pass

# an EXAMPLE :
@Rule(Fact( family='felinae'))
def match_with_cats():
  """
  Match with every `Fact` which:

    * f[0] == 'animal'
    * f['family'] == 'felinae'

  """
  print("Meow!")


# In[56]:


traffic_light_fact = Fact(color = 'red')

# equals to : IF the color is red THEN you must stop.
@Rule(Fact(color = 'red'))
def car_action():
    print('You must stop')


# In[5]:





# In[13]:


### KnowledgeEngine   /   Inference Engine :

# The first step is to make a subclass of it and use Rule to decorate its methods.
# After that, you can instantiate it, populate it with facts, and finally run it.


# complete Example
class Light(Fact):
  """Info about the traffic light."""
  pass


class RobotCrossStreet(KnowledgeEngine):
  @Rule(Light(color='green'))
  def green_light(self):
      print("Walk")

  @Rule(Light(color='red'))
  def red_light(self):
      print("Don't walk")

  @Rule(AS.light << Light(color=L('yellow') | L('blinking-yellow')))
  def cautious(self, light):
      print("Be cautious because light is", light["color"])
      print('have a nice day')

    
# consider it as our user interface 
engine = RobotCrossStreet()
engine.reset()
engine.declare(Light(color=input('what is the color? ')))  # .declare  == assert in CLIPS 
engine.run()

engine.facts


# In[18]:


class Animal(Fact):
  """Info about the traffic light."""
  pass


class AnimalKE(KnowledgeEngine):
  @Rule(Animal(animal_type = 'cat'))
  def cat_sound(self):
      print("mew")

  @Rule(Animal(animal_type = 'duck'))
  def duck_sound(self):
      print("quack")


engine = AnimalKE()
engine.reset()
engine.declare(Animal(animal_type = input('which one ? cat or duck or HORSE ? ')))
engine.run()

#engine.facts


# In[5]:


# Animal gussing /// multiople Conditions in LHS : IF (... AND ...) then (...)
class Animal(Fact):
  """Info about the traffic light."""
  pass


class AnimalKE2(KnowledgeEngine):
  @Rule(AND ( Animal(has=('feathers')), Animal(has2=('webbed-feet'))))
  def guess_animal(self):
    print("Animal is duck")
    print("Sound is quack")


engine = AnimalKE2()
engine.reset()
engine.declare(Animal(has=input('feathers or no feathers ? ')), Animal(has2=input('webbed-feet or no webbed-feet? ')))
engine.run()

#engine.facts


# In[19]:


# conclude a fact  (production system) :
# IF (...) THEN (animal is 'duck')
# IF (animal is 'duck') THEN (sound is 'quack')

class Animal(Fact):
  """Info about the traffic light."""
  pass


class AnimalKE3(KnowledgeEngine):
  @Rule(AND( Animal(has=('feathers')), Animal(has=('webbed-feet'))))
  def guess_animal(self):
    self.declare(Animal('duck'))
    print(self.facts)
  
  @Rule(Animal('duck'))
  def it_is_duck(self):
    print("Animal is duck")
    print("Sound is quack")

engine = AnimalKE3()
engine.reset()
engine.declare(Animal(has='feathers'), Animal(has='webbed-feet'))
engine.run()
engine.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




