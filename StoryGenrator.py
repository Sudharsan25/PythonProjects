import random
when=['On 25 Dec','On Nov 24','A long time ago','Once upon a time','Today']
who = ['Sudharsan','Krish','Vishnu','Geetha']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['On a walk','Cycling','To a book fair','Curlinary Fair','Shopping']
happened = ['Fell down','proposed her girlfriend','Ate lunch','Enjoyed a lot','Spent a lot of money']
print(random.choice(when) + ',' + random.choice(who) + ' who lived in ' + random.choice(residence) + ',went ' + random.choice(went) + ' and ' + random.choice(happened))