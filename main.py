"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
  if n == 1:
    return 1
  else:
    return a * simple_work_calc(n // b, a, b) + n


def work_calc(n, a, b, f):
  if n == 1:
    return 1 + f(1)
  else:
    return a * work_calc(n // b, a, b, f) + f(n)





def span_calc(n, a, b, f):
  if n <= 1:
    return f(n)
  else:
    return max(span_calc(n // b, a, b, f) for _ in range(a)) + f(n)



def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))



def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			span_fn1(n),
			span_fn2(n)
			))
	return result
	

span1 = lambda n: span_calc(n, 2, 2, lambda n: 1)
span2 = lambda n: span_calc(n, 2, 2, lambda n: n)
span3 = lambda n: span_calc(n, 2, 2, lambda n: math.log(n))

print(compare_span(span1,span2))
print(compare_span(span1,span3))
