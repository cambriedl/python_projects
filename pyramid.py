def pyramid(n):
    for x in range(1, n + 1):
        print '#' * x

pyramid(4)

def right_pyramid(n):
    for x in range(1, n + 1):
        print  (n - x) * ' ' + '#' * x

right_pyramid(30)

# TODO
# Make a function which creates a right pyramid and a left pyramid separated by
# two spaces

   #  #
  ##  ##
 ###  ###
####  ####
