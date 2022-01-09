<h1>Simple Genetic Algorithm</h1>
<p>A simple object-oriented implementation of a genetic algorithm to find a target string.</p>

<h2>Example Run:</h2>

```
g = Genetic(target='To be, or not to be: that is the question',
            population_size=10000, parent_pool=.03)
g.evolve()
Generation 0: ('H1O:M,z7iS=5d.;tF(eH g/Y>X>s?2@$U[:>*NIeo', 4)
Generation 1: ("('Ed6,X9m !d<4t1m.G_Hl19A7i:q?1e(H82s]pLD", 6)
Generation 2: ('TOs"e;%^r!n?%JW][Ne4Sth3tA%K(`u]/t`e8M"o9', 10)
Generation 3: ('7=x@epi*h noI uvduG(fohTG^iLuthe #%"@tioA', 14)
Generation 4: ('5oxbe,_7& ,otRt?sbe4Rttat _Hk]he gu0CH4o"', 19)
Generation 5: ('Te9W=960r noz coybh^Uthatyis t+e qu[@t;on', 23)
Generation 6: ('TJ beB >rD1ot 5T bi:t7j2g is the question', 28)
Generation 7: ('T+;We, +r noM"to<ne: tha18is theyquest;on', 29)
Generation 8: ("T` be,m1r 'ot to l0:hthat is=the queation", 32)
Generation 9: ('To beu or nKt to beQ that is +he qurstiov', 35)
Generation 10: ('To be, br not 9o be:+that is the ques%ion', 37)
Generation 11: ('To be, or not to be: that is the quzs$ion', 39)
Generation 12: ('To be, or not to be: that is the quIstion', 40)
Generation 13: ('To be, or no7 to be: that is the question', 40)
Generation 14: ('To be, or not to be: that is the question', 41)
```