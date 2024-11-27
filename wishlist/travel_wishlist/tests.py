from django.test import TestCase
from django.urls import reverse
from.models import Place

class TestHomePage(TestCase):
    def test_home_page_shows_empty_list_message_for_empty_database(self):
        home_page_url = reverse('place_list')
#       turn the url path place_list into an actual url the request can be made to
        response = self.client.get(home_page_url)
#       self is the testcase, and it has a client that makes get requests to web app server
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
#       asserting the template used
        self.assertContains(response, 'You have no places in your wishlist')
        # checks if it contains response with that specific message

class TestWishList(TestCase):

    fixtures = ['test_places']
    # goes in the fixtures directory and gets the data from test_places
    def test_wishlist_contains_not_visited_places(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertContains(response, 'Tokyo')
        self.assertContains(response, 'New York')
        self.assertNotContains(response, 'San Francisco')
        self.assertNotContains(response, 'Moab')
        # should NOT contain these two places in the response

class TestVisitedPage(TestCase):
    def test_visited_page_shows_empty_list_message_for_empty_database(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
        self.assertContains(response, 'You have not visited anywhere yet')


class VisitedList(TestCase):
    fixtures = ['test_places']
    def test_visited_list_shows_visited_places(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
        self.assertContains(response, 'San Francisco')
        self.assertContains(response, 'Moab')
        self.assertNotContains(response, 'New York')
        self.assertNotContains(response, 'Tokyo')

class TestAddNewPlace(TestCase):
    def test_add_new_unvisited_place(self):
        add_place_url = reverse('place_list')
        new_place_data = {'name': 'Tokyo', 'visited': False}

        response = self.client.post(add_place_url, new_place_data, follow=True )
#         the data is saved then a redirect to reload the home page
#         follow=True means if a second request happens as a result of
#         the first one then it follows the redirect
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        response_places = response.context['places']
        self.assertEqual(1, len(response_places))
#         only checks one place
        tokyo_from_response = response_places[0]
        tokyo_from_database = Place.objects.get(name='Tokyo', visited=False)
        self.assertEqual(tokyo_from_database, tokyo_from_response)


class TestVisitedPlace(TestCase):
    def test_visit_place(self):
        visit_place_url = reverse('place_was_visited', args=(2, ))
#         reversing the url should generate the right path to make the request to
        response = self.client.post(visit_place_url, follow=True)

        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        self.assertNotContains(response, 'New York')
        self.assertContains(response, 'Tokyo')

        new_york = Place.objects.get(pk = 2)
        self.assertTrue(new_york.visited)


    def test_non_existent_place(self):
        visit_non_existent_place_url = reverse('place_was_visited', args=(12334, ))
        response = self.client.post(visit_non_existent_place_url, follow=True)
        self.assertEqual(404, response.status_code)
#         to return a 404 error






