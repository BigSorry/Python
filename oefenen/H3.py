def do_twice(function, value):
    function(value)
    function(value)

def print_spam(value):
    print(value)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(function, value):
    print_twice(value)
    print_twice(value)

spam = 'spam'
do_four(print, spam)