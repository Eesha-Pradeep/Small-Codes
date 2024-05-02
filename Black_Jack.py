def blackjack_hand_greater_than(hand_1, hand_2):
  def calculate_score(hand):
    p = dict.fromkeys(["K","Q","J"],10)
    p["A"] = 11
    score = sum([int(i) if i.isdigit() else p[i] for i in hand])
    if "A" in hand and score>21:
      c = hand.count("A")
      while score>21 and c!=0:
        score-=10
        c-=1
    return score

  h1_score = calculate_score(hand_1)
  h2_score = calculate_score(hand_2)

  if (h2_score>21 or h1_score>h2_score) and h1_score<=21:
    return True
  else:
    return False