import pytest
import json
from django.contrib.auth.models import User
from students.models import Course, Student
from django.urls import reverse
from model_bakery import baker
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED


@pytest.mark.django_db
def test_first_courses(api_client, course_factory):
    # arrange
    course1 = course_factory(name="Mathematics")
    course2 = course_factory(name="Physics")
    url = reverse("courses-detail", args=(course1.id,))
    # act
    resp = api_client.get(url)
    # assert
    assert resp.status_code == HTTP_200_OK
    assert resp.json()['id'] == course1.id
    assert isinstance(course1, Course)


@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    url = reverse("courses-list")
    courses = course_factory(_quantity=3)
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 3


@pytest.mark.django_db
def test_id_courses1(api_client, course_factory):
    course1 = course_factory(name="Mathematics")
    course2 = course_factory(name="Physics")
    url = reverse("courses-detail", args=(course1.id,))
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    assert resp.json()['id'] == course1.id


@pytest.mark.django_db
def test_id_courses2(api_client, course_factory):
    # arrange
    url = reverse("courses-list")
    course1 = course_factory(name="Mathematics")
    course2 = course_factory(name="Physics")
    # act
    resp = api_client.get(url)
    # assert
    data = resp.json()
    assert ([item['name'] for item in data if item['name']
             == 'Physics'][0]) == 'Physics'


@pytest.mark.django_db
def test_name_courses(api_client):
    # arrange
    url = reverse("courses-list")
    post_params = {"name": "Mathematics", "students": []}
    # act
    resp = api_client.post(url, post_params, format='json')
    # assert
    assert resp.status_code == HTTP_201_CREATED


@pytest.mark.django_db
def test_put_courses(api_client, course_factory):

    course1 = course_factory()
    url = reverse("courses-detail", args=(course1.id,))
    resp1 = api_client.get(url)
    assert resp1.status_code == HTTP_200_OK

    put_params = {"name": "Mathematics", "students": []}
    resp2 = api_client.put(url, data=put_params, format='json')
    assert resp2.status_code == HTTP_201_CREATED
    assert resp2.json()["id"] == course1.id


@pytest.mark.django_db
def test_delete_courses():
    customer = baker.make('students.Course') 
    customer.delete()
    assert customer
