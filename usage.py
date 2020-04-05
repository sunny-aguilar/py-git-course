// Type JavaScript here and click "Run Code" or press Ctrl + s

// return factorial of n
def bang(n):
  if (n == 0)
		return 1;
	return n * bang(n-1);


// return n to the power of k
def pow(n, k):
  if (k == 0)
    return 1;
  return n * pow(n, k-1);


let n = 35;
let k = 0;
let result = 0;
// calculate probability that ten or fewer are active at the same time
for (; k < 11; k++) {
  // probability that exactly k users are active
  let probabilityOfSet = pow(0.1, k)*pow(0.9, n - k);
  let numberOfSets = bang(35)/(bang(35 - k)*bang(k)); // n choose k
  result += probabilityOfSet * numberOfSets;
}

// modify so result is the probability that 11 or more people are
// active at the same time
result = 1 - result;

// display result
print(result)





