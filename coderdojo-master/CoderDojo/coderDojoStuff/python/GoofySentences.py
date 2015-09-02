# goofy sentence generator

import random

def make_sentence(n, *parts):
   """return n random sentences"""
   for _ in range(n):
      yield ' '.join(random.choice(p) for p in parts).capitalize() + '.'

# break a typical sentence into 3 parts
# first part of a sentence (subject)

subject_ = """\
a furry rabbit
a giggling goose
the meowing cat
the goofy ostrich
this mean mouse
the angry bird""".splitlines()

# middle part of a sentence (action)
action_ = """\
jumps over
flies over
runs across
loudly burps
twice tastes
vomits on""".splitlines()

# ending part of a sentence (object)
object_ = """\
a chain saw
the laughing cow
the stinky trash can
the timid trucker
the rotten cheese
the smelly socks""".splitlines()

print ('-'*60)

for item in make_sentence(3, subject_, action_, object_):
    print (item)
print ('-'*60)


