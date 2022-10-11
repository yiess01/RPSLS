from RPSLS_player import RPSLS_player

class P17964(RPSLS_player):
  def __init__(self):
    pass

  def shoot(self):
    import random
    a_shoot = ["rock", "paper", "scissors", "lizard", "spock"]
    shooting = a_shoot[random.randint(0, 4)]
    return shooting
  
  def update(self, result: str, competitor_shot: str):
    pass