import re,traceback

class O:
  y=n=0
  @staticmethod
  def report():
    print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))
  @staticmethod
  def k(f):
    try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      O.y += 1
    except:
      O.n += 1
      print(traceback.format_exc()) 
    return f

DATA1 ="""
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,25,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""

DATA2 ="""
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,

                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,25,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""


def lines(s):
    "Return contents, one line at a time."
    return s.splitlines()

def rows(src):
    """Kill bad characters. If line ends in ',' 
   then join to next. Skip blank lines."""
    #Skip blank lines and blank space
    i = 0
    delete_list = []
    for i in range(len(src)):
        if '#' in src[i]:
            index = src[i].index("#")
            #print(index)
            src[i] = src[i][:index]
        src[i] = src[i].strip()
        # print(src[i])
        if src[i] == '':
            # print(i)
            delete_list.append(i)
    for index in reversed(delete_list):
        del src[index]
    
    #If line ends in ',' then join to next
    i = 0
    while i < len(src):
        if src[i].endswith(','):
            src[i] = src[i] + src[i + 1]
            del src[i + 1]
            i -= 1
        i += 1

    return src



def cols(src):
    """ If a column name on row1 contains '?', then skip over that column."""
    for i in range(len(src)):
        src[i] = src[i].split(",")

    delete_item = []
    for i, item in enumerate(src[0]):
        if item[0] == '?':
            delete_item.append(i)
    for row in src:
        for delete_index in delete_item:
            del row[delete_index]

    return src


def prep(src):
    """ If a column name on row1 contains '$', 
  coerce strings in that column to a float."""
    float_item = []
    for i, item in enumerate(src[0]):
        if item[0] == '$':
            float_item.append(i)
    for row in src[1:]:
        for float_index in float_item:
            row[float_index] = float(row[float_index])
    return src

def ok0(s):

    for row in prep(cols(rows(lines(s)))):
        print(row)

@O.k
def ok1(): ok0(DATA1)

@O.k
def ok2(): ok0(DATA2)

if __name__== "__main__":
    O.report()