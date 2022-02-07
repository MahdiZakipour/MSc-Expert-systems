#!/usr/bin/env python
# coding: utf-8

# In[9]:



from experta import *
"""
    Expert system for detecting if an enfant is diabetic
    @author: Fortas Abdeldjalil.
    Helpful Ressources:
        * http://www.nospetitsmangeurs.org/quoi-faire-si-mon-enfant-a-le-diabete/
        * http://www.nospetitsmangeurs.org/les-hauts-et-les-bas-du-taux-de-sucre/
        * http://www.childrenshospital.org/conditions-and-treatments/conditions/hypoglycemia-and-low-blood-sugar/symptoms-and-causes
        * https://www.mayoclinic.org/diseases-conditions/hyperglycemia/symptoms-causes/syc-20373631
"""


class Personne(Fact):
    """Info about the patient"""
    pass


def SUMFIELDS(p, *fields):
    return sum([p.get(x, 0) for x in fields])


class InreferenceEngine(KnowledgeEngine):
    @Rule(Personne(age=P(lambda x: x <= 5)))
    def concerned_person(self):
        self.declare(Fact(concerned=True))

    @Rule(Fact(concerned=True),
          Personne(glycemie=MATCH.glycemie))
    def hyper_glycemy(self, glycemie):
        if glycemie > 10:
            self.declare(Fact(hyperglycemic_risk=True))
            print("Warning! High blood sugar")
        else:
            self.declare(Fact(hyperglycemic_risk=False))

    @Rule(Fact(concerned=True),
          Personne(glycemie=MATCH.glycemie))
    def hypo_glycemy(self, glycemie):
        if glycemie < 4:
            print("Warning! Low blood sugar")
            self.declare(Fact(hypoglycemic_risk=True))
        else:
            self.declare(Fact(hypoglycemic_risk=False))

    @Rule(Fact(concerned=True),
          AS.p << Personne(),
          TEST(lambda p: SUMFIELDS(p,
                                   'shakiness',
                                   'hunger',
                                   'sweating',
                                   'headach',
                                   'pale') > 2))
    def has_signs_low_sugar(self, p):
        self.declare(Fact(has_signs_low_sugar=True))


    # If the patient is a child and has one or many signes or his blood sugar level is low
    @Rule(Fact(concerned=True),
          Fact(has_diabetic_parents=True),
          Fact(has_signs_low_sugar=True))
    def protocole_risk_low(self):
        print("Warning! Child could be diabetic")

    # If the patient is a child and has one or many signes, and his blood sugar level is low and passed the test
    @Rule(Fact(concerned=True),
          Fact(hypoglycemic_risk=True),
          Fact(has_signs_low_sugar=True))
    def protocole_alert_low(self):
        print("Alert! High risk of diabetes, you must see a doctor")


    #If the patient is child and has at least one of his parents diabetic
    @Rule(Fact(concerned=True),
          Personne(diabetic_parents=True))
    def has_diabetic_parents(self):
        self.declare(Fact(has_diabetic_parents=True))


    @Rule(Fact(concerned=True),
          AS.p << Personne(),
          TEST(lambda p: SUMFIELDS(p,
                                   'urination',
                                   'thirst',
                                   'blurred_vision',
                                   'headach',
                                   'dry_mouth',
                                   'smelling_breath',
                                   'shortness_of_breath') > 2)
    )
    def has_signs_high_sugar(self, **_):
        self.declare(Fact(has_signs_high_sugar=True))

    @Rule(Fact(concerned=True),
          Fact(has_diabetic_parents=True),
          Fact(has_signs_high_sugar=True))
    def protocole_risk_high(self):
        print("Warning! Child could be diabetic")

    @Rule(Fact(concerned=True),
          Fact(hyperglycemic_risk=True),
          Fact(has_signs_high_sugar=True))
    def protocole_alert_high(self):
        print("Alert! High risk of diabetes, you must see a doctor")


engine = InreferenceEngine()
engine.reset()

# Initial facts

# Sick high
#engine.declare(Personne(age= 3,
#                        glycemie=1,
#                        shakiness= True,
#                        hunger= True,
#                        sweating= True,
#                        headach= False,
#                        diabetic_parents = True,
#                        pale= True,
#                        urination = False,
#                        thirst = True,
#                        blurred_vision = True,
#                        dry_mouth = False,
#                        smelling_breath = True,
#                        shortness_of_breath = True,
#                        ))

engine.declare(Personne(age=2,
                        glycemie=12,
                        shakiness= False,
                        hunger= True,
                        sweating= True,
                        headach= False,
                        diabetic_parents = True,
                        pale= False,
                        urination = False,
                        thirst = False,
                        blurred_vision = True,
                        dry_mouth = True,
                        smelling_breath = False,
                        shortness_of_breath = True,
                        ))
engine.run()

#engine.facts


# In[ ]:




