from knowrob_semantic_map_tools.prolog.IRI import *
from knowrob_semantic_map_tools.prolog.queries.Compound import *

class ActionProperty(Compound):
  def __init__(self, property, action = "Action", object = "Object"):
    Compound.__init__(self, "action_property",
      [str(action), str(property), str(object)])
    
    self._action = action
    self._property = property
    self._object = object
    
  def getAction(self):
    solution = self.solution
    
    if solution:
      return IRI(solution[self._action])
  
  action = property(getAction)

  def getActions(self):
    for solution in self.solutions:
      yield IRI(solution[self._action])
  
  actions = property(getActions)

  def getObject(self):
    solution = self.solution
    
    if solution:
      return IRI(solution[self._object])
  
  object = property(getObject)

  def getObjects(self):
    for solution in self.solutions:
      yield IRI(solution[self._object])
  
  objects = property(getObjects)
  