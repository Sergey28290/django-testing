import pytest
from django.contrib.auth.models import User
from students.models import Course, Student
from model_bakery import baker

@pytest.mark.django_db #
def test_first_courses():
    customer = baker.make('students.Course') # создаем тестовую запись
    queryset = Course.objects.all()[0] # получаем ее из бд
    assert queryset == customer # проверяем на то, что это именно та запись


@pytest.mark.django_db #
def test_list_courses():
    customers = []
    for i in range(3):
        customer = baker.make('students.Course')
        customers.append(customer)

    queryset = Course.objects.all() # получаем queryset, после мы его преобразовываем в список для сравнения
    assert list(queryset) == customers


@pytest.mark.django_db
def test_id_courses():
    customer = baker.make('students.Course') # создаем одну запись
    queryset = Course.objects.filter(id=customer.id) # получаем по id
    assert list(queryset)[0] == customer # проверка первого, т.к. запись одна

@pytest.mark.django_db
def test_name_courses():
    customer = baker.make('students.Course')
    queryset = Course.objects.filter(name=customer.name)
    assert list(queryset)[0] == customer

@pytest.mark.django_db
def test_create_courses():
    user = Student.objects.create(name='Alex') # создаем пользователя
    customer = Course.objects.create(name='stepone') # создаем курс
    assert customer # проверяем что просто запустился


@pytest.mark.django_db
def test_update_courses():
    customer = baker.make('students.Course') # создаем запись
    customer.name = 'Sergey' # меняем его значения
    customer.save() # сохраняем
    assert customer


@pytest.mark.django_db
def test_delete_courses():
    customer = baker.make('students.Course') # создаем запись
    customer.delete() # удаляем
    assert customer
