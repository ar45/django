from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    iso_two_letter = models.CharField(max_length=2)


class ProxyCountry(Country):
    class Meta:
        proxy = True


class ProxyProxyCountry(ProxyCountry):
    class Meta:
        proxy = True


class ProxyMultiCountry(ProxyCountry):
    pass


class ProxyMultiProxyCountry(ProxyMultiCountry):
    class Meta:
        proxy = True


class Place(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Restaurant(Place):
    pass


class Pizzeria(Restaurant):
    pass


class State(models.Model):
    two_letter_code = models.CharField(max_length=2, primary_key=True)


class TwoFields(models.Model):
    f1 = models.IntegerField(unique=True)
    f2 = models.IntegerField(unique=True)


class NoFields(models.Model):
    pass


class Parent(models.Model):
    id = models.IntegerField(primary_key=True, default=lambda: models.IntegerField.creation_counter)


class Child(Parent):
    child_field = models.CharField(max_length=50)


class GrandChild(Child):
    grand_child_field = models.CharField(max_length=50)


class ProxyGrandChild(GrandChild):
    class Meta:
        proxy = True


class SiblingWithAutoField(models.Model):
    my_pk = models.AutoField(primary_key=True)
    sibling_with_auto_field = models.CharField(max_length=50)


class SiblingWithNoAutoField(models.Model):
    sibling_with_no_auto_field = models.CharField(max_length=50, primary_key=True)


class MultiInheritanceWithNoAutoField(ProxyGrandChild, SiblingWithNoAutoField):
    pass


class MultiInheritorWithAutoParent(SiblingWithAutoField, ProxyGrandChild):
    pass
