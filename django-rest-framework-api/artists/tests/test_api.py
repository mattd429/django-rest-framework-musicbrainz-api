# Django
from django.urls import resolve
# Django rest
from rest_framework.test import APITestCase
# Local
from artists.models import Experiment, LANGUAGE_CHOICES, STYLE_CHOICES
from albums.models import Album, Record

class ArtistAPITestCase(APITestCase):
    
    def setUp(self):
        self.movement = Album.objects.create(name='Movement', slug='movement')
        self.dreams_never_end = Record.objects.create(name='Dreams Never End', slug='dreams-never-end', album=self.movement)

    def test_create_artist(self):
        """
        Test that we can create a artist
        """
        post_data = {'record': '/api/records/1/', 'creator': 'New Order', 'genre': 'electronic',
                     'start_time': '0:16', 'end_time': '3:15'}
        ''' Post the data into artists in the format of json '''
        response = self.client.post('/api/artists/', data=post_data, format='json')
        
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data, {
            'url': 'http://127.0.0.1:8000/api/artists/1/',
            'creator': 'New Order',
            'slug': 'new-order',
            'genre': 'electronic',
            'start_time': '0:16',
            'end_time': '3:15',
            'record':  'http://127.0.0.1:8000/api/tracks/1/'
        })
    
    def test_artist_list_route(self):
        ''' Test that we've got routing set up for artists '''
        route = resolve('/api/artists/')
        
        self.assertEqual(route.func.__name__, 'ArtistViewSet')
        
class ExperimentAPITestCase(APITestCase):
    
    def setUp(self):
        self.title_code = Experiment.objects.create(title='Experiment Title', code='var = 2'),
        self.language_style = Experiment.objects.create(language='Cucumber', style='autumn'),
    
    def test_create_experiment(self):
        ''' Test that we can create an Experiment '''
        post_data = {'url': 'http://127.0.0.1:8000/artists/1/', 'id': 1,
                     'highlighted': 'http://127.0.0.1:8000/artists/1/highlight/', 'owner': 'owner',
                     'title': 'Django Rest framework 3', 
                     'linenoe': False, 
                     'language': 'python3', 
                     'style': 'colorful'
                     }
        response = self.client.post('/api/artists/', data=post_data, format='html')
        
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data, {
            'url': 'http://127.0.0.1:8000/artists/1/',
            'id': 1,
            'highlight': 'http://127.0.0.1:8000/artists/1/highlight/',
            'owner': 'owner',
            'title': 'Django is cool',
            'linenos': False,
            'language': 'python3',
            'style': 'colorful'
        })
        
    def test_experiment_list_route(self):
        ''' Test that we've got routing setup for artists '''
        route = resolve('/api/artists/')
        
        self.assertEqual(route.func.__name__, 'ExperimentViewSet')

class UserAPITestCase(APITestCase):
    pass