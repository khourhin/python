def nice_print(f):
    def print1(string):
        return "#"* 5 + f(string) + "#" * 5
    return print1

class TalkToMe():

    greeting = "Hi"
    
    @nice_print
    def sayHi(self):
        return "Hi"

def currency(f):
    def wrapper(*args, **kwargs):
        return '$' + str(f(*args, **kwargs))
    
    return wrapper

class Product():

    name = 'test1'
    price = 12

    @currency
    def price_with_tax(self, tax_rate_percentage):
        """Return the price with *tax_rate_percentage* applied.
        *tax_rate_percentage* is the tax rate expressed as a float, like "7.0"
        for a 7% tax rate."""
        return self.price * (1 + (tax_rate_percentage * .01))


def logging(f):
    def inner(*args, **kargs):
        print "Arguments are: %s, %s" % (args, kargs)
        return f(*args, **kargs)
    return inner

@logging
def do_nothing(*args, **kargs):
    return None
    

    
print(TalkToMe().sayHi())
print(Product().price_with_tax(100))
do_nothing("abc", 1, 4, a=12, b=113)
