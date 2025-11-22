from train import pipeline
def test_model():
 m=pipeline().fit(["football goal team","basketball team score","orbit moon space","rocket space launch"],[0,0,1,1]);assert m.predict(["space rocket"])[0]==1;assert abs(sum(m.predict_proba(["team"])[0])-1)<1e-9
