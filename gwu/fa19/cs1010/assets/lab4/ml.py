from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Variable Initialization

# n_gram max min
ngram_min = 1
ngram_max = 1

print("Reading the tab delimited files ...")
dataset_x = []
dataset_y = []
trainfile = './movie_reviews_train.txt'
testfile = './movie_reviews_test.txt'

train = open(trainfile, encoding="utf8")
test = open(testfile, encoding="utf8")

# to keep the count of training set
index = 0
print("Get the lines from the tab delimited file & split the line to its parts, tweet text is the 2nd part")
for line in train:
    parts = line.split('\t')
    dataset_x.append(parts[0].replace('\n', ''))
    dataset_y.append(parts[1].replace('\n', ''))
    index += 1

for line in test:
    parts = line.split('\t')
    dataset_x.append(parts[0].replace('\n', ''))
    dataset_y.append(parts[1].replace('\n', ''))


print("Vectorizing Corpus ...")
vectorizer = CountVectorizer(ngram_range=(ngram_min, ngram_max), token_pattern=r'\b\w+\b', min_df=1)
X_fit = vectorizer.fit_transform(dataset_x)
dataset_matrix = vectorizer.transform(dataset_x).toarray()

# Separate train set from test
x_train = dataset_matrix[:index-1]
y_train = dataset_y[:index-1]

x_test = dataset_matrix[index:]
y_test = dataset_y[index:]

print("Training models ... \n")
model = MultinomialNB().fit(x_train, y_train)
#model = SVC(gamma='auto').fit(x_train, y_train)
print('Mean Accuracy: ' + str(float("{0:.3f}".format(model.score(x_test, y_test)))))

filename = 'finalized_model.sav'
joblib.dump(model, filename)

# some time later...

# load the model from disk

loaded_model = joblib.load(filename)
result = loaded_model.score(x_test, y_test)
print('Mean Accuracy from loaded_model: ' + str(float("{0:.3f}".format(result))))

xt = x_test[0:15]
plt.figure()
plt.plot(model.predict(xt), 'gd')
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.ylabel('predicted')
plt.xlabel('training samples')
plt.legend(loc="best")
plt.title('Comparison of individual predictions with averaged')
plt.show()