import pytest
from unittest.mock import patch, MagicMock
from src.funcmain import *


# Test for register account
@pytest.mark.asyncio
@patch("src.apis.token_manager.TokenManager.get_access_token")
@patch("src.apis.user.add_bubble_companies")
async def test_register_account(add_bubble_companies_mock, get_access_token_mock):
    add_bubble_companies_mock.return_value = {'data': [{'code': 'SUCCESS'}]}
    get_access_token_mock.return_value =  "mocked_access_token"
    form = {
        "Account_Name": "Test Account",
        "Dealer_License_Number": "123456789",
        "Dealer_Phone": "1234567890",
        "Dealership_Type": "Test Category",
        "Website": "https://www.test.com",
        "Address": "123 Test Street",
        "ExpiryDate": "2024-08-19T02:40:09-04:00",
        "Business_Number": "123456789",
        "CRA_HST_GST_Number": "123456789",
        "SK_PST_Number": "23435",
        "Company_Email": "company@email.ca",
        "BC_PST_Number": "123456789"
    }

    encoded_form_data = '&'.join(f'{key}={value}' for key, value in form.items())
    req = func.HttpRequest(
        body=encoded_form_data.encode('utf-8'),
        method='POST',
        url='/api/register_account',
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    response = await register_account(req)

    assert response.status_code == 200

# Test for adding a contact
@pytest.mark.asyncio
@patch("src.apis.token_manager.TokenManager.get_access_token")
@patch("src.apis.user.add_bubble_contact")
async def test_register_contact(add_bubble_contact_mock, get_access_token_mock):
    # Mocking a successful response
    add_bubble_contact_mock.return_value = {'data': [{'code': 'SUCCESS'}]}
    get_access_token_mock.return_value = "mocked_access_token"
    
    form = {
        "Account_ID": "123456789",
        "Contact_Name": "Test Last Name",
        "Contact_Email": "bVg5Q@example.com",
        "Contact_Phone": "1234567890",
        "Position_Role": "Test Position",
        "Note": "Test Note"
    }

    encoded_form_data = '&'.join(f'{key}={value}' for key, value in form.items())
    req = func.HttpRequest(
        body=encoded_form_data.encode('utf-8'),
        method='POST',
        url='/api/register_contact',
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    response = await register_contact(req)

    assert response.status_code == 200


# Test Update Contact
@pytest.mark.asyncio
@patch("src.apis.token_manager.TokenManager.get_access_token")
@patch("src.apis.user.update_contact")
async def test_update_lead(update_contact_mock, get_access_token_mock):
    update_contact_mock.return_value = {'data': [{'code': 'SUCCESS'}]}
    get_access_token_mock.return_value = "mocked_access_token"
    raw_data = {
        "data" : [
            {
            "id":"3384000001340151",
            "offer_amount":1000,
            "Buyer Text":"Buyer Name"
            # ...
            }
        ]
            }
    # Mock request with necessary form data
    req = func.HttpRequest(
        body=json.dumps(raw_data).encode('utf-8'),
        method='POST',
        url='/api/update_lead',
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    response = await update_lead(req)

    # Assert the response
    assert response.status_code == 200


# Test for adding a lead
@pytest.mark.asyncio
@patch("src.apis.token_manager.TokenManager.get_access_token")
@patch("src.apis.lead.add_solo_lead")
async def test_add_lead(add_solo_lead_mock, get_access_token_mock):
    add_solo_lead_mock.return_value = {'data': [{'code': 'SUCCESS'}]}
    get_access_token_mock.return_value = "mocked_access_token"

    form = {
        "Last_Name": "Test Last Name",
        "buyer_id": "123456789",
        "Lead_Score": "Test Score",
        "Vehicle_id": "123456789",
        "Buyer_Text": "Test Text",
        "offer_amount": "Test Amount",
        "Seller": "Test Seller",
        "Vehicle_State": "Test State",
        "Progress_Status": "Test Status"
    }

    # Mock request with necessary form data
    encoded_form_data = '&'.join(f'{key}={value}' for key, value in form.items())
    req = func.HttpRequest(
        body=encoded_form_data.encode('utf-8'),
        method='POST',
        url='/api/add_lead',
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    response = await create_lead(req)

    # Assert the response
    assert response.status_code == 200


# Test for updating a lead
@pytest.mark.asyncio
@patch("src.apis.token_manager.TokenManager.get_access_token")
@patch("src.apis.lead.update_lead")
async def test_update_lead(update_lead_mock, get_access_token_mock):
    update_lead_mock.return_value = {'data': [{'code': 'SUCCESS'}]}
    get_access_token_mock.return_value = "mocked_access_token"
    raw_data = {
        "data" : [
            {
            "id":"3384000001340151",
            "offer_amount":1000,
            "Buyer Text":"Buyer Name"
            # ...
            }
        ]
            }
    # Mock request with necessary form data
    req = func.HttpRequest(
        body=json.dumps(raw_data).encode('utf-8'),
        method='POST',
        url='/api/update_lead',
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    response = await update_lead(req)

    # Assert the response
    assert response.status_code == 200


# Test for updating an offer
@pytest.mark.asyncio
@patch("src.apis.token_manager.TokenManager.get_access_token")
@patch("src.apis.offer.update_Offer")
async def test_update_offer(update_offer_mock, get_access_token_mock):
    update_offer_mock.return_value = {'data': [{'code': 'SUCCESS'}]}
    get_access_token_mock.return_value = "mocked_access_token"
    raw_data = {
        "data" : [
            {
            "id":"3384000001340151",
            "Offer":1000,
            "Email":"test@gmail.com"
            # ...
            }
        ]
            }
    # Mock request with necessary form data
    req = func.HttpRequest(
        body=json.dumps(raw_data).encode('utf-8'),
        method='POST',
        url='/api/update_offer',
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    response = await update_offer(req)

    # Assert the response
    assert response.status_code == 200


# Test for adding an offer
@pytest.mark.asyncio
@patch("src.apis.token_manager.TokenManager.get_access_token")
@patch("src.apis.offer.add_offer")
async def test_add_offer(add_offer_mock, get_access_token_mock):
    add_offer_mock.return_value ={'data': [{'code': 'SUCCESS'}]}
    get_access_token_mock.return_value = "mocked_access_token"

    form = {
        "Vehicle_ID": "123456789",
        "Lead_ID": "123456789",
        "Account_ID": "123456789",
        "Offer_Amount": "Test Amount",
        "Name": "Test Name"
    }

    # Mock request with necessary form data
    encoded_form_data = '&'.join(f'{key}={value}' for key, value in form.items())

    req = func.HttpRequest(
        body=encoded_form_data.encode('utf-8'),
        method='POST',
        url='/api/add_offer',
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    response = await create_offer(req)

    # Assert the response
    assert response.status_code == 200

# Test for adding a watchlist
@pytest.mark.asyncio
@patch("src.apis.token_manager.TokenManager.get_access_token")
@patch("src.apis.watchlist.add_watchlist")
async def test_add_watchlist(add_watchlist_mock, get_access_token_mock):
    add_watchlist_mock.return_value ={'data': [{'code': 'SUCCESS'}]}
    get_access_token_mock.return_value = "mocked_access_token"

    form = {
        "Vehicle_ID": "123456789",
        "Account_ID": "123456789",
    }

    # Mock request with necessary form data
    encoded_form_data = '&'.join(f'{key}={value}' for key, value in form.items())

    req = func.HttpRequest(
        body=encoded_form_data.encode('utf-8'),
        method='POST',
        url='/api/add_offer',
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    response = await add_watchlist(req)

    # Assert the response
    assert response.status_code == 200


# Test for updating a watchlist
@pytest.mark.asyncio
@patch("src.apis.token_manager.TokenManager.get_access_token")
@patch("src.apis.watchlist.update_watchlist")
async def test_update_watchlist(update_watchlist_mock, get_access_token_mock):
    update_watchlist_mock.return_value ={'data': [{'code': 'SUCCESS'}]}
    get_access_token_mock.return_value = "mocked_access_token"

    raw_data = {
        "data" : [
            {
            "id":"3384000001340151",
            "Active":True,
            # ...
           
            }
        ]
            }

 
    req = func.HttpRequest(
        body=json.dumps(raw_data).encode('utf-8'),
        method='POST',
        url='/api/add_offer',
        headers={'Content-Type': 'application/json'}
    )

    response = await update_watchlist(req)

    # Assert the response
    assert response.status_code == 200