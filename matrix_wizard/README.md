This is an implementation of the "Matrix Wizard", a probabilistic
algorithm invented by Rusins Freivalds that checks if a matrix C equals
the product of two matrices A and B. The name "Matrix Wizard" comes from
the presentation of the algorithm which Matousek gives in his book
Thirty-Tree Miniatures. Our code was inspired in the latter.

The program generates two random matrices A and B, calculates their
product C and checks if a perturbation of C is the product of A and B. As
expected, the frequency of a wrong answer increases as the "density of
perturbation" of the matrix C decreases. However, this frequency never
surpasses 0.5, as the theoretical analysis foresaw.
