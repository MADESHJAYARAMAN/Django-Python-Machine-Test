from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class ClientTests(TestCase):
    def setUp(self):
        self.client = Client.objects.create(name='Test Client')

    def test_client_str(self):
        client = Client.objects.get(id=1)
        self.assertEqual(str(client), client.name)

    def test_get_client_list(self):
        response = self.client.get(reverse('client-list-create'))
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests as needed for Client operations

class ProjectTests(TestCase):
    def setUp(self):
        self.client = Client.objects.create(name='Test Client')
        self.project = Project.objects.create(client=self.client, name='Test Project')

    def test_project_str(self):
        project = Project.objects.get(id=1)
        self.assertEqual(str(project), project.name)

    def test_get_project_list(self):
        response = self.client.get(reverse('project-list-create'))
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests as needed for Project operations
