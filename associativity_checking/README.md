This code was based on the exercise 13.6.7 of Invitation to Discrete
Mathematics (Matousek and Nesetril), Miniature 27 of Thirty-Three
Miniatures (Matousek) and the paper Verification of Identities
(Rajagopalan and Schulman). In `associativity_checker.py` we implement a
O(n^2) randomized algorithm to check if an operation is associative and
a O(n^2\*lgn) deterministic algorithm to do the same when the operation is
cancellative. Note that checking if an operation is cancellative can be
done in O(n^2). Therefore, if A is a finite set and \* an operation on A,
we have a O(n^2) randomized algorithm and a O(n^2\*lgn) deterministic
algorithm to check if (A,\*) is a group.

### Examples

#### Randomized algorithm

`time python3 not_associative.py 1000 | python3 tester_random.py 50`

>Is it cancellative? False  
Is it associative? False  
Is it a group? False  
>
>real	0m32.602s  
user	0m33.772s  
sys	0m0.376s  

`time python3 cyclic_group.py 1000 | python3 tester_random.py 5`

>Is it cancellative? True  
Is it associative? True  
Is it a group? True  
>
>real	0m50.882s  
user	0m51.600s  
sys	0m0.404s  


#### Cancellative case
 
`time python3 cyclic_group.py 1000 | python3 tester_cancellative.py`

##### Output

> Is it cancellative? True  
Is it associative? True  
Is it a group? True  
>
>real	0m5.168s  
user	0m5.992s  
sys	0m0.372s  

As the operation created in `not_associative.py` is not cancellative, we cannot guarantee a O(n^2\*lgn) bound for this case and the code takes way too much time to run.

#### Probabilities

`python3 not_associative.py 10 | python3 probabilities.py 1000`

Number of randomized checkings | Frequency of wrong answers
--- | ---
t =  1  |  0.352
t =  2  |  0.134
t =  3  |  0.044
t =  4  |  0.014
t =  5  |  0.007
t =  6  |  0.002
t =  7  |  0.002
t =  8  |  0.0
t =  9  |  0.0
t =  10  |  0.0
