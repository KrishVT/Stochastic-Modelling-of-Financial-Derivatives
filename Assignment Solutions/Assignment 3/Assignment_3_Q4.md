# Q4

From the definition of Wiener process we know that the increment will be a normal distribution

Now our aim remains to find it's mean and variance

Let two time instants be t and s such that t > s >= 0

Then E[ W<sub>t</sub> - W<sub>s</sub> ] = E[ W<sub>t</sub> ] - E[ W<sub>s</sub> ]

Now we know that for any time instant m, E[ W<sub>m</sub> ] = 0 ( because it is a normal distribution around zero )

Therefore E[ W<sub>t</sub> - W<sub>s</sub> ] = 0

Var( W<sub>t</sub> - W<sub>s</sub> ) = Var( W<sub>t</sub> ) + Var( W<sub>s</sub> ) - 2 * Cov( W<sub>t</sub> , W<sub>s</sub> )

Cov( X , Y ) = E[ ( X - E[X] ) ( Y - E[Y] ) ]

Therefore in our case Cov( W<sub>t</sub> , W<sub>s</sub> ) = E[ ( W<sub>t</sub> - E[ W<sub>t</sub> ] ) ( W<sub>s</sub> - E[ W<sub>s</sub> ] ) ]

Cov( W<sub>t</sub> , W<sub>s</sub> ) = E[ W<sub>t</sub> * W<sub>s</sub> ]

As we proved in Q3 that the value of E[ W<sub>t</sub> * W<sub>s</sub> ] = min( s , t ) = s

Var( W<sub>t</sub> - W<sub>s</sub> ) = t + s - 2 * s

Var( W<sub>t</sub> - W<sub>s</sub> ) = t - s

Hence proved that mean is zero and variance is t - s

Now proving the other part of the question that for non-overlapping intervals the increments will be independent

Let the points be t<sub>2</sub> > s<sub>2</sub> >= t<sub>1</sub> > s<sub>1</sub> >= 0

Cov( W<sub>t<sub>2</sub></sub> - W<sub>s<sub>2</sub></sub> , W<sub>t<sub>1</sub></sub> - W<sub>s<sub>1</sub></sub> ) = E[ ( W<sub>t<sub>2</sub></sub> - W<sub>s<sub>2</sub></sub> ) * ( W<sub>t<sub>1</sub></sub> - W<sub>s<sub>1</sub></sub> ) ]

Now E[ ( W<sub>t<sub>2</sub></sub> - W<sub>s<sub>2</sub></sub> ) * ( W<sub>t<sub>1</sub></sub> - W<sub>s<sub>1</sub></sub> ) ] = E[ W<sub>t<sub>2</sub></sub> * W<sub>t<sub>1</sub></sub> - W<sub>t<sub>2</sub></sub> * W<sub>s<sub>1</sub></sub> - W<sub>s<sub>2</sub></sub> * W<sub>t<sub>1</sub></sub> + W<sub>s<sub>2</sub></sub> * W<sub>s<sub>1</sub></sub> ]

E[ ( W<sub>t<sub>2</sub></sub> - W<sub>s<sub>2</sub></sub> ) * ( W<sub>t<sub>1</sub></sub> - W<sub>s<sub>1</sub></sub> ) ] = E[ W<sub>t<sub>2</sub></sub> * W<sub>t<sub>1</sub></sub> ] - E[ W<sub>t<sub>2</sub></sub> * W<sub>s<sub>1</sub></sub> ] - E[  W<sub>s<sub>2</sub></sub> * W<sub>t<sub>1</sub></sub> ] + E[ W<sub>s<sub>2</sub></sub> * W<sub>s<sub>1</sub></sub> ]

Now using knowledge from Q3,

E[ ( W<sub>t<sub>2</sub></sub> - W<sub>s<sub>2</sub></sub> ) * ( W<sub>t<sub>1</sub></sub> - W<sub>s<sub>1</sub></sub> ) ] = t<sub>1</sub> - s<sub>1</sub> - t<sub>1</sub> + s<sub>1</sub> = 0

Therefore Cov( W<sub>t<sub>2</sub></sub> - W<sub>s<sub>2</sub></sub> , W<sub>t<sub>1</sub></sub> - W<sub>s<sub>1</sub></sub> ) = 0

Hence we can say that they are independent
