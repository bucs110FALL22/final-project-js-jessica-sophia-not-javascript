def getOrElse(someDict, key, defaultValue):
  if key in someDict:
    return someDict[key]
  return defaultValue