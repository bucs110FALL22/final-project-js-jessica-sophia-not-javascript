class SceneService:
  """
  This will be a singleton that controls
  what scene to play on the screen
  """

  def __init__(self):
    self.activeScene = None
    self.generatedScenes = {}

  def switchToScene(self, key, SceneClass=None, context=None):
    """
    This method will switch to the scene based on the key
    If there is already a scene associated with the key,
    then the service will just use that scene.
    If a new scene is provided, it will use that instead
    """
    if SceneClass== None:
      if key in self.generatedScenes:
        self.activeScene = self.generatedScenes[key]
        return

      raise Exception(f"Scene associated with [{key}] not defined")

    newScene = SceneClass(context)
    self.generatedScenes[key] = newScene
    self.activeScene = newScene

  def getCurrentScene(self):
    return self.activeScene

  def clearCurrentScene(self):
    self.activeScene = None
