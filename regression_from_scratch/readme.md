The goal of this project is to write a somewhat eficcient linear regression algorythm that can solve least
squares problems somewhat eficciently and avoid large roundoff errors.

When finding the least squares solution of an overdetermined system of equations, it is commonly taught in
statistics and linear algebra classes that the solution to the matrix equation $A^TA\vec{x}=A^T\vec{b}$ is the least squares
solution to the equation $A\vec{x}=\vec{b}+\vec{r}$.  However when solving this kind of problem on a computer, this leads to 
roundoff errors since $A^T A$ is near singular, ie the row/column space of $A^T A$ is nearly linearly dependent 
leading to subtraction of near equal numbers during row reduction, resulting in roundoff errors.  
Instead, most modern statistical software uses some indirect
method of finding the QR factorization of the matrix A to find the least squares solution.

By performing a QR factorization, we end up with an orthogonal matrix Q, which has an inverse equal to its 
transpose, and an upper triangular matrix R.

This means that $Ax = b+r$ becomes $QR\vec{x}=\vec{b}+\vec{r}$ which can be solved as follows.
$R\vec{x} = Q^T\vec{b} +Q^T \vec{r}$.  $Q^t \vec{r} =0$ since $\vec{r}$ is orthogonal to the column space of $Q$
so this equation becomes $R\vec{x} = Q^T \vec{b}$ which can be solved using backsubstitution.
