import os

# get root directory
root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# File Names
log_file = 'gender_predictor.log'
zip_file = 'names.zip'
name_pickle_file = 'name.pickle'
naive_bayes_train_pickle = 'nb_classifier_train.pkl'
class_pickle_file = 'class_gender.pickle'
features_pickle_file = 'features.pickle'

# directory configurations
data_path = os.path.join(root_dir, 'data')         # data
log_path = os.path.join(data_path, 'log')          # data/log
pickle_path = os.path.join(data_path, 'pickle')          # data/pickle
raw_data_path = os.path.join(data_path, 'raw_data')          # data/raw_data


# logger configurations
log_file = os.path.join(log_path, log_file)
zip_file = os.path.join(raw_data_path, zip_file)
name_pickle_file = os.path.join(pickle_path, name_pickle_file)
naive_bayes_train_pickle = os.path.join(pickle_path, naive_bayes_train_pickle)
class_pickle_file = os.path.join(pickle_path, class_pickle_file)
features_pickle_file = os.path.join(pickle_path, features_pickle_file)
