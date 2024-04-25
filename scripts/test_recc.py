from user.models import User
from recommender import Recommender

user = User.objects.get(username="mentix02")
rec = Recommender()

rec.build_dataset()
rec.build_model()

print(rec.recommend(user.id))
