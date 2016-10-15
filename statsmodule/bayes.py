# Resources
# - http://blog.yhathq.com/posts/naive-bayes-in-python.html



'''
A) I watched The Lego Movie today
B) I sat on the couch today

P(A) = P(I watched The Lego Movie today) = 10 / 60, or ~0.17
P(B) = P(I sat on the couch today) = (60 - 14) / 60, or ~0.76

P(B|A) = P(I sat on the couch given that I watched The Lego Movie) = 6 / 10 = 0.60
P(A|B)=P(B|A)*P(A)/P(B) = (0.60 * 0.17) / 0.76

P(I watched The Lego Movie given that I sat on the couch) = 0.13

