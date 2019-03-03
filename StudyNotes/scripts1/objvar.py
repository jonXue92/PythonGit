#!/usr/bin/python
#Filename : objvar.py

class Person:
  '''Represents a person.'''
  population = 0

  def __init__(self,name):
    '''Initializes the person's data.'''
    self.name = name
    print '(Initializing %s)' % self.name

    # When this person is created, he/she
    # adds to the population
    Person.population += 1

  def __del__(self):
    '''I am dying.'''
    print '%s says bye.' % self.name
    
    Person.population -= 1

    if Person.population == 0:
      print 'I am the last one.'
    else:
      print 'There are still %d people left.' % Person.population

  def sayHi(self):
    '''Greeting by the person.

    Really, that's all it does.'''
    print 'Hi, my name is %s.' % self.name

  def howMany(self):
    '''Prints the current population.'''
    if Person.population == 1:
      print 'I am the only person here.'
    else:
      print 'We have %d persons here.' % Person.population

print Person.__doc__

print Person.__init__.__doc__
swaroop = Person('Swaroop')
print Person.sayHi.__doc__
swaroop.sayHi()
print Person.howMany.__doc__
swaroop.howMany()

print Person.__init__.__doc__
kalam = Person('Abdul Kalam')
print Person.sayHi.__doc__
kalam.sayHi()
print Person.howMany.__doc__
kalam.howMany()

print Person.sayHi.__doc__
swaroop.sayHi()
print Person.howMany.__doc__
swaroop.howMany()

print Person.__del__.__doc__
