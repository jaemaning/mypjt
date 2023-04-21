from ..models import Movie, Review
from rest_framework import serializers
from rest_framework.fields import empty

class ReviewSerializer(serializers.ModelSerializer):
      
  def __init__(self, instance=None, data=empty, flag=0, read_only=False, **kwargs):
    self.instance = instance
    if data is not empty:
        self.initial_data = data
    self.partial = kwargs.pop('partial', False)
    self._context = kwargs.pop('context', {})
    kwargs.pop('many', None)
    self.flag = flag
    self.read_only = read_only
    if not self.flag:
      super().__init__(**kwargs)
      
  class MovieSerializerForDetail(serializers.ModelSerializer):
    class Meta:
      model = Movie
      fields = ("title",)
      
  movie = MovieSerializerForDetail(read_only=True)
  class Meta:
    model = Review
    fields = ("id", "movie", "title", "content", )
    read_only_fields = ("movie",)
    
  def to_representation(self, instance):
    rep = super().to_representation(instance)
    if not self.flag:
      rep.pop('id')
      rep.pop('movie')
    return rep