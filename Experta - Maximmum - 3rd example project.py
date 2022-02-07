#!/usr/bin/env python
# coding: utf-8

# In[1]:


from experta import *


# In[2]:


class Maximum(KnowledgeEngine):
    @Rule(NOT(Fact(max=W())))
    def init(self):
        self.declare(Fact(max=0))
    
    @Rule(Fact(val=MATCH.val),
          AS.m << Fact(max=MATCH.max),
          TEST(lambda max, val: val > max))
    def compute_max(self, m, val):
        self.modify(m, max=val)
    
    @Rule(AS.v << Fact(val=MATCH.val),
          Fact(max=MATCH.max),
          TEST(lambda max, val: val <= max))
    def remove_val(self, v):
        self.retract(v)
            
    @Rule(AS.v << Fact(max=W()),
          NOT(Fact(val=W())))
    def print_max(self, v):
        print("Max:", v['max'])


# In[5]:


m = Maximum()
m.reset()
m.declare(*[Fact(val=x) for x in (12, 33, 155, 99, 55, 11, 75)])


# In[4]:


m.run()


# In[ ]:




