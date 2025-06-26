from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from products.models import Product, Kategorie
import json

User = get_user_model()


class BasketViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Create a category
        self.category = Kategorie.objects.create(nazev='Test Category')
        
        # Create test products
        self.product1 = Product.objects.create(
            name='Test Product 1',
            description='Test Description 1',
            category=self.category,
            price=10.00,
            is_discounted=False,
            type='food',
            available=True,
            author=self.user
        )
        
        self.product2 = Product.objects.create(
            name='Test Product 2',
            description='Test Description 2',
            category=self.category,
            price=20.00,
            is_discounted=True,
            discount_price=15.00,
            type='drink',
            available=True,
            author=self.user
        )

    def test_view_basket_empty(self):
        """Test viewing an empty basket"""
        response = self.client.get(reverse('basket:basket'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Váš košík je prázdny')
        self.assertEqual(len(response.context['basket_items']), 0)
        self.assertEqual(response.context['total_price'], 0)

    def test_add_to_basket(self):
        """Test adding a product to the basket"""
        # Add one product
        response = self.client.post(
            reverse('basket:add_to_basket', args=[self.product1.id]),
            {'quantity': 2},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['quantity'], 2)
        self.assertEqual(data['basket_count'], 1)
        
        # Check if basket is updated in session
        session = self.client.session
        self.assertEqual(session['basket'].get(str(self.product1.id)), 2)

    def test_add_to_basket_invalid_quantity(self):
        """Test adding with invalid quantity"""
        response = self.client.post(
            reverse('basket:add_to_basket', args=[self.product1.id]),
            {'quantity': 'invalid'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])  # Should default to quantity 1
        self.assertEqual(data['quantity'], 1)

    def test_update_quantity_increase(self):
        """Test increasing item quantity in basket"""
        # First add to basket
        self.client.post(
            reverse('basket:add_to_basket', args=[self.product1.id]),
            {'quantity': 1},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        
        # Then increase quantity
        response = self.client.post(
            reverse('basket:update_quantity'),
            {'produkt_id': str(self.product1.id), 'action': 'inc'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['new_qty'], 2)
        
        # Check session
        session = self.client.session
        self.assertEqual(session['basket'].get(str(self.product1.id)), 2)

    def test_update_quantity_decrease(self):
        """Test decreasing item quantity in basket"""
        # First add to basket with quantity 2
        self.client.post(
            reverse('basket:add_to_basket', args=[self.product1.id]),
            {'quantity': 2},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        
        # Then decrease quantity
        response = self.client.post(
            reverse('basket:update_quantity'),
            {'produkt_id': str(self.product1.id), 'action': 'dec'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['new_qty'], 1)
        
        # Check session
        session = self.client.session
        self.assertEqual(session['basket'].get(str(self.product1.id)), 1)

    def test_remove_item_from_basket(self):
        """Test removing an item from the basket"""
        # First add to basket
        self.client.post(
            reverse('basket:add_to_basket', args=[self.product1.id]),
            {'quantity': 1},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        
        # Then remove it
        response = self.client.post(
            reverse('basket:remove_from_basket'),
            {'produkt_id': str(self.product1.id)},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['basket_count'], 0)
        
        # Check session
        session = self.client.session
        self.assertNotIn(str(self.product1.id), session.get('basket', {}))

    def test_basket_total_price(self):
        """Test that basket calculates total price correctly"""
        # Add multiple products with different quantities
        self.client.post(
            reverse('basket:add_to_basket', args=[self.product1.id]),
            {'quantity': 2},  # 2 * 10.00 = 20.00
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.client.post(
            reverse('basket:add_to_basket', args=[self.product2.id]),
            {'quantity': 1},  # 1 * 15.00 (discounted) = 15.00
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        
        response = self.client.get(reverse('basket:basket'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['basket_items']), 2)
        self.assertEqual(response.context['total_price'], 35.00)  # 20.00 + 15.00

    def test_update_quantity_remove_when_zero(self):
        """Test that item is removed when quantity reaches zero"""
        # Add one item
        self.client.post(
            reverse('basket:add_to_basket', args=[self.product1.id]),
            {'quantity': 1},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        
        # Decrease to zero
        response = self.client.post(
            reverse('basket:update_quantity'),
            {'produkt_id': str(self.product1.id), 'action': 'dec'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['new_qty'], 0)
        self.assertEqual(data['basket_count'], 0)
        
        # Check session
        session = self.client.session
        self.assertNotIn(str(self.product1.id), session.get('basket', {}))
