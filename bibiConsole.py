import models
import tools
import tensorflow as tf
import gc
import numpy
from pluginFactory import PluginFactory

def analyse(sentence):
    subjects, types, stopwords, dictionnary = tools.defaultValues()
    modelSubjects= models.getModelSubjects(dictionnary, subjects)
    modelSubjects.load("data/modelSubjects.tflearn")
    resultS= modelSubjects.predict([tools.bagOfWords(sentence, dictionnary, stopwords)])
    tf.keras.backend.clear_session()
    del modelSubjects
    gc.collect()

    modelTypes= models.getModelTypes(dictionnary, types)
    modelTypes.load("data/modelTypes.tflearn")
    resultT= modelTypes.predict([tools.bagOfWords(sentence, dictionnary, stopwords)])
    tf.keras.backend.clear_session()
    del modelTypes
    gc.collect()

    modelValues= models.getModelValues(dictionnary)
    modelValues.load("data/modelValues.tflearn")
    resultV= modelValues.predict([tools.bagOfWords(sentence, dictionnary, stopwords)])
    tf.keras.backend.clear_session()
    del modelValues
    gc.collect()
    return resultS[0], resultT[0], resultV[0][0]

def searchAnswer(sentence, subject, typeS):
    plugin = PluginFactory.getPlugin(subject, typeS)
    return plugin.response(sentence)

def bibiQuestion(question):
    subjects, types, stopwords, dictionnary = tools.defaultValues()
    rSubject, rType, rValue = analyse(question)

    try:
        result = searchAnswer(question, subjects[numpy.argmax(rSubject)], types[numpy.argmax(rType)])
    except Exception as e:
        result = str(e)

    return result