from haystack import indexes
from borme.models import Company, Person


class CompanyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, model_attr='name')
    #name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Company

    def get_updated_field(self):
        return "date_updated"


class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, model_attr='name')
    #name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Person

    def get_updated_field(self):
        return "date_updated"
