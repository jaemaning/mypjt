from ..models import Actor, Movie, Review
from rest_framework import serializers
class MovieSerializer(serializers.ModelSerializer):
  def __init__(self, instance=None, flag=0, **kwargs):
    self.instance = instance
    self.flag = flag
    if not self.flag:
      super().__init__(**kwargs)
    
  class ActorSerializerForDetail(serializers.ModelSerializer):
    class Meta:
      model = Actor
      fields = ("name",)
      
  class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
      model = Review
      fields = ("title", "content")
      
  actors = ActorSerializerForDetail(many=True, read_only=True)
  review_set = ReviewSerializer(many=True, read_only=True)
  
  class Meta:
    model = Movie
    fields = "__all__"
    
  def to_representation(self, instance):
    rep = super().to_representation(instance)
    if not self.flag:
      rep.pop('id')
      rep.pop('actors')
      rep.pop('review_set')
      rep.pop('release_date')
      rep.pop('poster_path')
    return rep
