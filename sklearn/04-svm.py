from sklearn import svm

x = [[0, 0], [1, 1]]
y = [0, 1]
z = [2., 2.]

# --- Parameters --- #

# Kernal parameters
# These shape the linear line by fitting the data in higher dimensional planes
if False:
    # There are several SVM's besides SVC
    clf = svm.SVC(kernel="linear")
    clf.fit(x, y)
    print   clf.predict([[2., 2.]])

# Gamma parameter
# These make the line for wiggly in an attempt to fit the data tighter
if False:
    clf = svm.SVC(gamma=1.0)
    clf.fit(x, y)
    print clf.predict(z)

# C parameter
# Controls trade off between smoothness and fit. A larger value means more wiggle
if False\
        :
    # There are several SVM's besides SVC
    clf = svm.SVC(C=30)
    clf.fit(x, y)
    print clf.predict(z)
