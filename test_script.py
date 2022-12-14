from zakar import*

def test_app(file=__file__):
    data = iText(file)
    assert data

def test_fetch():
    df = fetch_spambase()
    assert((4601, 58) == df.values.shape)

def test_basemodel():
    df = fetch_spambase()
    p = create_pipeline_spambase()
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1:].values.astype('int').ravel() 
    scores = cross_val_score(p, X, y, cv=10)   
    print(scores)
