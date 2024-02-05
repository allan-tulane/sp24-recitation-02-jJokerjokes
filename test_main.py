from main import *

def test_simple_work():
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(20, 2, 4) == 34
  assert simple_work_calc (10,5,2) == 210
  assert simple_work_calc(40, 5, 2) == 5390


def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 23
  assert work_calc(20, 1, 2, lambda n: n*n) == 531
  assert work_calc(30, 3, 2, lambda n: n) == 381
  assert work_calc(16, 3, 2, lambda n: n // 2) == 146
  assert work_calc(27, 1, 3, lambda n: 2*n) == 81
  assert work_calc(17, 2, 2, lambda n: n - 1) == 66




def test_compare_work():
	# curry work_calc to create multiple work
	# functions that can be passed to compare_work
	# create work_fn1
	# create work_fn2
  def work_fn1(n):
    return work_calc(n, 2, 2, lambda n: n)

  def work_fn2(n):
    return work_calc(n, 2, 2, lambda n: n*n)
  res = compare_work(work_fn1,work_fn2)
  print(res)


	
def test_compare_span():
  def span_fn1(n):
    return span_calc(n, 2, 2, lambda n: n)

  def span_fn2(n):
    return span_calc(n, 2, 2, lambda n: n*n)
  res = compare_work(span_fn1,span_fn2)
  print(res)
  
