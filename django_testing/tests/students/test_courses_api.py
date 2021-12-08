import pytest
from django.contrib.auth.models import User
from students.models import Course, Student
from model_bakery import baker

@pytest.mark.django_db #
def test_first_courses():
    customer = baker.make('students.Course') 
    queryset = Course.objects.all()[0] 
    assert queryset == customer 


@pytest.mark.django_db #
def test_list_courses():
    customers = []
    for i in range(3):
        customer = baker.make('students.Course')
        customers.append(customer)

    queryset = Course.objects.all() 
    assert list(queryset) == customers


@pytest.mark.django_db
def test_id_courses():
    customer = baker.make('students.Course')
    queryset = Course.objects.filter(id=customer.id) 
    assert list(queryset)[0] == customer

@pytest.mark.django_db
def test_name_courses():
    customer = baker.make('students.Course')
    queryset = Course.objects.filter(name=customer.name)
    assert list(queryset)[0] == customer

@pytest.mark.django_db
def test_create_courses():
    user = Student.objects.create(name='Alex') 
    customer = Course.objects.create(name='stepone')
    assert customer


@pytest.mark.django_db
def test_update_courses():
    customer = baker.make('students.Course') 
    customer.name = 'Sergey'
    customer.save() 
    assert customer


@pytest.mark.django_db
def test_delete_courses():
    customer = baker.make('students.Course') 
    customer.delete()
    assert customer
