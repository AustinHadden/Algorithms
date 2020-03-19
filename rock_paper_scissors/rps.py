#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  total_plays = []

  def rps_plays(total_plays, plays, n):
    if len(plays) == n:
      total_plays.append(plays)
    else:
      for x in ['rock', 'paper', 'scissors']:
        new_plays = plays.copy()
        new_plays.append(x)
        rps_plays(total_plays, new_plays, n)

  rps_plays(total_plays, [], n)
  return total_plays


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')