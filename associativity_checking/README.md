This code was based on the exercise 13.6.7 of Invitation to Discrete
Mathematics (Matousek and Nesetril), Miniature 27 of Thirty-Three
Miniatures (Matousek) and the paper Verification of Identities
(Rajagopalan and Schulman). In `associativity_checker.py` we implement a
O(n^2) randomized algorithm to check if an operation is a associative and
a O(n^2*lgn) deterministic algorithm to do the same when the operation is
cancellative. Note that checking if an operation is cancellative can be
done in O(n^2). Therefore, if A is a finite set and * an operation on A,
we have a O(n^2) randomized algorithm and a O(n^2*lgn) deterministic
algorithm to check if (A,\*) is a group.

Examples:

`python3 cyclic_group.py 10 | python3 tester_cancellative.py`
