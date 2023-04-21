from ..models import Actor, Movie
from rest_framework import serializers

class ActorSerializer(serializers.ModelSerializer):
  
  def __init__(self, instance=None, flag=0, **kwargs):
    self.instance = instance
    self.flag = flag
    if not self.flag:
      super().__init__(**kwargs)
    
  class MovieSerializerForDetail(serializers.ModelSerializer):
    class Meta:
      model = Movie
      fields = ("title",)
      
  movies = MovieSerializerForDetail(many=True, read_only=True)
  class Meta:
    model = Actor
    fields = "__all__"
  
  def to_representation(self, instance):
    rep = super().to_representation(instance)
    if not self.flag:
      rep.pop('movies')
    return rep