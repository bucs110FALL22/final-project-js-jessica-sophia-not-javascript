class SceneService:
  """
  This will be a singleton that controls
  what scene to play on the screen
  """

  def __init__(self):
    """
  	initializes 
    """
    self.activeScene = None
    self.classes = {}
    self.generatedScenes = {}

  def switchToScene(self, key, SceneClass=None, context=None, reset=False):
    """
    This method will switch to the scene based on the key
    If there is already a scene associated with the key,
    then the service will just use that scene.
    If a new scene is provided, it will use that instead
    """
    if reset:
      if key not in self.classes or context == None:
        raise Exception("SceneClass and context must be defined for a forced reset")
      self.activeScene = self.classes[key](context)
      return
    
    if SceneClass == None:
      if key in self.generatedScenes:
        self.activeScene = self.generatedScenes[key]
        return

      raise Exception(f"Scene associated with [{key}] not defined")

    newScene = SceneClass(context)
    self.classes[key] = SceneClass
    self.generatedScenes[key] = newScene
    self.activeScene = newScene
  
  def getCurrentScene(self):
    return self.activeScene
  """
	Returns state info (the current Scene)
  """ 
  def clearCurrentScene(self):
    self.activeScene = None
    """
  	Clears current scene
    """     
