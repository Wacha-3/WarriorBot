class Exercise:
  def __init__(self, name, minRep, maxRep, hpScale):
      self.name = name
      self.minRep = minRep #make a list of excerices then use the perams to scale enemy
      self.maxRep = maxRep
      self.hpScale = hpScale

  def Exercise_details(self):
    print(f'Exercise name:{self.name} \nExercise minRep: {self.minRep} \nExercise maxRep: {self.maxRep} \nExercise hpScale: {self.hpScale}')
