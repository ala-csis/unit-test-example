#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 09:40:52 2022

@author: ala
"""

import pytest

from unittest.mock import Mock
from item_database import ItemDatabase
from shopping_cart import ShoppingCart

@pytest.fixture
def cart():
    """ All the setup for the cart goes here. """
    
    return ShoppingCart(20)

# Type of behaviour that is legit, but that fails under certain conditions.
def test_can_add_item_to_cart(cart):
    
    cart.add('apple')
    assert cart.size() == 1
    

def test_when_item_added_then_cart_contains_item(cart):
    
    cart.add('apple')
    assert 'apple' in cart.get_items()
    
# Type of behaviour we *want* to fail.
def test_when_add_more_than_max_items_should_fail(cart):
    
    for item in range(cart.max_size):
        cart.add(str(item))    
    with pytest.raises(OverflowError):
        cart.add(item)

def test_can_get_total_price(
        cart,
        price_map={'apple': 1.37, 'orange': 2.99},
        items = ['orange', 'apple'],
        ):
    
    for item in items:
        cart.add(item)

    item_database = ItemDatabase()

    def mock_get_item(item: str, price_map=price_map):
        return price_map.get(item)
        
    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == sum(
        [item_database.get(item) for item in items])    