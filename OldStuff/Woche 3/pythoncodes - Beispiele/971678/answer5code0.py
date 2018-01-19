def iterThrough(lists):
  if not hasattr(lists[0], '__iter__'):
    for val in lists:
      yield val
  else:
    for l in lists:
      for val in iterThrough(l):
        yield val

for val in iterThrough(
  [[[111,112,113],[121,122,123],[131,132,133]],
   [[211,212,213],[221,222,223],[231,232,233]],
   [[311,312,313],[321,322,323],[331,332,333]]]):
  print(val)
  # 111
  # 112
  # 113
  # 121
  # ..
