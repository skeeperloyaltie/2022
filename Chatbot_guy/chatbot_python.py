#!/usr/bin/env python
# coding: utf-8

# ### Description 

#     # A python chatbot that uses django, numpy, mysql and pandas to elaborate more about a business structure. 
#     # For this we are going to use a simple business model for our project

#     # []: Business Model: Medical Symptoms
#     # []: Language        Python
#     # []: Model functions: 
#             - Tell user what the medical center is about
#             - explain if the user wants to know if there are certain diseases that can be treated by the medical center
#             - Types of drugs to be givn to some diseases
#             - Preventive methods to be taken on some diseases
#             - Close the chat -->

# ### Import neccessary imports

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import django
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import _tree


# ### Read the datasets

# In[3]:


# Importing the dataset
training_dataset = pd.read_csv('Training.csv')
test_dataset = pd.read_csv('Testing.csv')
df1 = pd.read_csv('Mental_Health_FAQ.csv')


# ### Ask questions about the medical structure and other questions
# 

# #### Classify the data using slicing and dicing

# In[4]:


X = df1.iloc[:, :-1].values
y = df1.iloc[:, -1].values


# #### remove redundancy

# In[5]:


dimension = df1.groupby('Questions').size()


# ### Classify the questionare as required

# #### Slice and Dice the datasets for the separate features for our prediction

# In[6]:


X = training_dataset.iloc[:, 0:132].values
y = training_dataset.iloc[:, -1].values


# #### Remove redundancy using dimensionality reduction
# 

# In[7]:


dimensionality_reduction = training_dataset.groupby(training_dataset['prognosis']).max()


# #### Encode the string values to integers

# In[8]:


labelencoder = LabelEncoder()
y = labelencoder.fit_transform(y)


# ### Splitting the dataset into training set and test set

# In[9]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


# ### Implementing the Decision Tree Classifier

# In[10]:


classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)


# ### Saving the information of columns

# In[11]:


cols = training_dataset.columns
cols = cols[:-1]


# ### Checking the Important features

# In[12]:


importances = classifier.feature_importances_
indices = np.argsort(importances)[::-1]
features = cols


# ## Implementing the Visual Tree

# ### Method to simulate the working of a Chatbot by extracting and formulating questions

# ### Questionare 

# In[13]:


def execute_bot():
    
    print("Please reply with yes/Yes or no/No for the following symptoms") 
    print()
    def print_disease(node):
        #print(node)
        node = node[0]
        #print(len(node))
        val  = node.nonzero() 
        #print(val)
        disease = labelencoder.inverse_transform(val[0])
        return disease
    def tree_to_code(tree, feature_names):
        tree_ = tree.tree_
        #print(tree_)
        feature_name = [
            feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
            for i in tree_.feature
        ]
        #print("def tree({}):".format(", ".join(feature_names)))
        symptoms_present = []
        def recurse(node, depth):
            indent = "  " * depth
            if tree_.feature[node] != _tree.TREE_UNDEFINED:
                name = feature_name[node]
                threshold = tree_.threshold[node]
                print(name + " ?")
                ans = input()
                ans = ans.lower()
                if ans == 'yes':
                    val = 1
                    
                else:
                    val = 0
                if  val <= threshold:
                    recurse(tree_.children_left[node], depth + 1)
                else:
                    symptoms_present.append(name)
                    recurse(tree_.children_right[node], depth + 1)
            else:
                present_disease = print_disease(tree_.value[node])
                print( "You may have " +  present_disease )
                red_cols = dimensionality_reduction.columns 
                symptoms_given = red_cols[dimensionality_reduction.loc[present_disease].values[0].nonzero()]
                print()
                print("symptoms present  " + str(list(symptoms_present)))
                print()
                print("symptoms given "  +  str(list(symptoms_given)) )  
                confidence_level = (1.0*len(symptoms_present))/len(symptoms_given)
                print()
                print("confidence level is " + str(confidence_level))
    
        recurse(0, 1)
    
    tree_to_code(classifier,cols)
    
# execute_bot()


# In[14]:


# create a menu that will ask the user to enter the symptoms and then print the disease and the confidence level
def menu():
    print("Please reply with yes/Yes or no/No for the following symptoms") 
    print()
    def print_disease(node):
        #print(node)
        node = node[0]
        #print(len(node))
        val  = node.nonzero() 
        #print(val)
        disease = labelencoder.inverse_transform(val[0])
        return disease
    def tree_to_code(tree, feature_names):
        tree_ = tree.tree_
        #print(tree_)
        feature_name = [
            feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!" for i in tree_.feature ]
        print("def tree({}):".format(", ".join(feature_names)))
        
        symptoms_present = []
        def recurse(node, depth):
            indent = "  " * depth
            if tree_.feature[node] != _tree.TREE_UNDEFINED:
                name = feature_name[node]
                threshold = tree_.threshold[node]
                print(name + " ?")
                ans = input()
                ans = ans.lower()
                if ans == 'yes':
                    val = 1
                    
                else:
                    val = 0
                if  val <= threshold:
                    recurse(tree_.children_left[node], depth + 1)
                else:
                    symptoms_present.append(name)
                    recurse(tree_.children_right[node], depth + 1)
            else:
                present_disease = print_disease(tree_.value[node])
                print()
                print( "You may have " +  present_disease )
                print()
                red_cols = dimensionality_reduction.columns 
                symptoms_given = red_cols[dimensionality_reduction.loc[present_disease].values[0].nonzero()]
                print()
                print("symptoms present  " + str(list(symptoms_present)))
                print()
                print("symptoms given "  +  str(list(symptoms_given)) )  
                confidence_level = (1.0*len(symptoms_present))/len(symptoms_given)
                print()
                print("confidence level is " + str(confidence_level))
    
        recurse(0, 1)
        
    tree_to_code(classifier,cols)
    execute_bot()
    
    
menu()


# In[ ]:




