import os
import numpy as np
import nltk
import docx
import math
from nltk.corpus import stopwords


#Doc file input!!
def main(myfile):
    def getText(filename):
        doc = docx.Document(filename)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)

    #Input filepath in listdir where all the file exists!!

    docFiles = []
    for filename in os.listdir():
        if filename.endswith(".docx"):
            filename = getText(filename)
            docFiles.append(filename)
    #docFiles.sort(key=str.lower)
    #print(len(docFiles))

    #Vocabulary of documents

    def built_lexicon(corpus):
        lexicon = set()
        for doc in corpus:
            
            word_token=[word for word in doc.split()]
            lower_word_list = [i.lower() for i in word_token]
            
            porter = nltk.PorterStemmer()
            stemmed_word = [porter.stem(t) for t in lower_word_list]
            
            stop_words = set(stopwords.words('english'))
            filtered_bag_of_word = [ w for w in stemmed_word if not w in stop_words]
            lexicon.update(filtered_bag_of_word)
        return lexicon

    vocabulary=built_lexicon(docFiles)

    def tf(term,document):
        return freq(term,document)

    def freq(term,document):
        return document.split().count(term)

    doc_term_matrix=[]
    #print('\n Our Vocabulary vector is ['+','.join(list(vocabulary))+']')

    for doc in docFiles:
        tf_vector=[tf(word,doc) for word in vocabulary]
        tf_vector_strings=','.join(format(freq,'d') for freq in tf_vector)
        #print('\n The tf vector for document %d is [%s]' % ((docFiles.index(doc)+1),tf_vector_strings))
        doc_term_matrix.append(tf_vector)

    #print('\n All combined here is our master document term matrix:')
    #print(doc_term_matrix)


    #Now every document is in the same feature space
    #Normalizing vectors to l2 norm
    #12 norm of each vector is one

    def l2_normalizer(vec):
        demon=np.sum([e1**2 for e1 in vec])
        return [(e1) for e1 in vec]

    doc_term_matrix_l2=[]
    for vec in doc_term_matrix:
        doc_term_matrix_l2.append(l2_normalizer(vec))

    #print('\n A regular old document term matrix: ')
    #print(np.matrix(doc_term_matrix))
    #print('\n A document term matrix with row wise l2 norms of 1')
    #print(np.matrix(doc_term_matrix_l2))


    def numDocsContaining(word,doclist):
        doccount=0
        for doc in doclist:
            if freq(word,doc)>0:
                doccount+=1
        return doccount

    def idf(word,doclist):
        n_samples=len(doclist)
        df=numDocsContaining(word,doclist)
        return np.log(n_samples/1+df)


    my_idf_vector=[idf(word,docFiles) for word in vocabulary]

    #print('Our vocabulary vector is ['+','.join(format(freq,'f') for freq in my_idf_vector))

    def build_idf_matrix(idf_vector):
        idf_mat=np.zeros((len(idf_vector),len(idf_vector)))
        np.fill_diagonal(idf_mat, idf_vector)
        return idf_mat

    my_idf_matrix=build_idf_matrix(my_idf_vector)

    #print('\n Idf matrix is:')
    #print(my_idf_matrix)

    doc_term_matrix_tfidf=[]

    #performing tfidf matrix multiplication 

    for tf_vector in doc_term_matrix:
        doc_term_matrix_tfidf.append(np.dot(tf_vector, my_idf_matrix))

    #Normalising

    doc_term_matrix_tfidf_l2=[]

    for tf_vector in doc_term_matrix_tfidf:
        doc_term_matrix_tfidf_l2.append(l2_normalizer(tf_vector))

    #print(vocabulary)
    #print(np.matrix(doc_term_matrix_tfidf_l2))

    #Cosine distance and angle between all the documents pairwisely
    temp=[]

    current_file=-1

    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".docx"):
            temp.append(filename)


    for filename in os.listdir(os.getcwd()):
        
        if filename.endswith(".docx"):
            #print(filename==str(myfile))
            #print(filename)
            #print(myfile)  
            current_file+=1  
            if filename==str(myfile):
                break

 
    
    #print(current_file)
    result={}
    for i in range(len(docFiles)):

        result_nltk = nltk.cluster.util.cosine_distance(doc_term_matrix_tfidf_l2[i], doc_term_matrix_tfidf_l2[current_file])
        #print('\n Cosine Distance btw %d and doc %d:' %(i,0))
        #print(result_nltk)
        cos_sin=1-result_nltk
        
        plagiarism=(cos_sin*100)


        variable ={
            "file" : temp[i].lower(),
            "value" : int(plagiarism)           
        }
        result.update({"data"+str(i) : variable})
        #print('\n Plagiarism =%s' %plagiarism)
    #print(result)
    return result


#print(r)
