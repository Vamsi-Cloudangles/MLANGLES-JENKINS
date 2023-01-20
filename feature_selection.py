from feature_engineering import feature_engineering

def feature_selection():
    dataset = feature_engineering()
    # Drop the unnecesssary columns
    dataset.drop(["SEX","PREGNANT","COPD","ASTHMA","INMSUPR","OTHER_DISEASE","CARDIOVASCULAR","OBESITY","TOBACCO"],inplace=True)
    return dataset