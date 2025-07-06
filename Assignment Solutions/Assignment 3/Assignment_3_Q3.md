# Q3
Let us assume that t > s

We can write W<sub>t</sub> = W<sub>s</sub> + ( W<sub>t</sub> - W<sub>s</sub> )

E[ W<sub>s</sub> * W<sub>t</sub> ] = E[ W<sub>s</sub> * { W<sub>s</sub> + ( W<sub>t</sub> - W<sub>s</sub> ) } ]

E[ W<sub>s</sub> * W<sub>t</sub> ] = E[ W<sub>s</sub> * W<sub>s</sub> ] + E[ W<sub>s</sub> * ( W<sub>t</sub> - W<sub>s</sub> ) ]

We know that W<sub>s</sub> - W<sub>0</sub> ∼ N(0,s) but as this is standard Brownian motion W<sub>0</sub> = 0

Therefore, W<sub>s</sub> ∼ N(0,s)

E[ W<sub>s</sub> * W<sub>s</sub> ] = s ( because E[ X<sup>2</sup> ] = Var( X ) + E[ X ]<sup>2</sup> )

And as increment in any region is independent of the previous values, we can write E[ W<sub>s</sub> * ( W<sub>t</sub> - W<sub>s</sub> ) ] = E[ W<sub>s</sub> ] * E[ W<sub>t</sub> - W<sub>s</sub> ]

We know that W<sub>t</sub> - W<sub>s</sub> ∼ N(0,t - s) and therefore E[ W<sub>t</sub> - W<sub>s</sub> ] = 0

Therefore E[ W<sub>s</sub> ] * E[ W<sub>t</sub> - W<sub>s</sub> ] = 0

Therefore E[ W<sub>s</sub> * W<sub>t</sub> ] = s

Hence E[ W<sub>s</sub> * W<sub>t</sub> ] = min( s,t )
