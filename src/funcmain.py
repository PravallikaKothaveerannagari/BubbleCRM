import logging
from src.apis import *
from models import *
from utils import *
import azure.functions as func
import json




global token_instance
token_instance = TokenManager()

async def register_account(req : func.HttpRequest):
    """ Register new account """
    try:
        # Get the access token
        access_token=token_instance.get_access_token()

        # Get the form data
        body = req.form
        logging.info(f"received form data: {body}")

        # Create a Company Instance
        company = Company(
            Account_Name=body.get('Account_Name'),
            Dealer_License_Number=body.get('Dealer_License_Number'),
            Dealer_Phone=body.get('Dealer_Phone'),
            Category=body.get('Dealership_Type'),
            Address=body.get('Address'),
            ExpiryDate=body.get('ExpiryDate'),
            Business_Number=body.get('Business_Number'),
            CRA_HST_GST_Number=body.get('CRA_HST_GST_Number'),
            SK_PST_Number=body.get('SK_PST_Number'),
            Email=body.get('Company_Email'),
            BC_PST_Number=body.get('BC_PST_Number'),
            Website = body.get('Website','')

        )

        # Add Company
        response = user.add_bubble_companies(access_token,dict(company))
        logging.info(f"Add Company response {response}")

        # Check if the Company Already Exist
        try:
            if response['data'][0]['code'] == 'DUPLICATE_DATA':
                return func.HttpResponse("Company already exist in zoho", status_code=409)
            
        except Exception as e:
            logging.warning(f"No duplicate found {e}")

    except Exception as e:
        logging.error(f"Error adding submitted company in zoho {e}")
        return func.HttpResponse(json.dumps({"error":str(e)}), status_code=500)
    
    return func.HttpResponse(json.dumps(response), status_code=200)

async def update_contact(req : func.HttpRequest):
    """ Update Contact in Zoho """
    try:
        # Get access token
        access_token=token_instance.get_access_token()

        # Get raw data
        body = req.get_json()

        response = user.update_contact(access_token,body)

    except Exception as e:
        logging.error(f"Error adding submitted contact in zoho {e}")

        return func.HttpResponse(json.dumps({"error":str(e)}), status_code=500)
    
    return func.HttpResponse(json.dumps(response), status_code=200)

async def register_contact(req : func.HttpRequest):
    """ Rgister Contact in Zoho """
    try:
        # Get access token
        access_token=token_instance.get_access_token()

        # Get form data
        body = req.form
        logging.info(f"received form data: {body}")

        # Create Contact Instance
        contact = Contact(
            Account_ID=body.get('Account_ID'),
            Last_Name=body.get('Contact_Name'),
            Email=body.get('Contact_Email'),
            Phone=body.get('Contact_Phone'),
            Position_Role=body.get('Position_Role'),
            Note=body.get('Note')
        )
        # Call Add Contact Api
        response = user.add_bubble_contact(access_token,dict(contact),contact.Account_ID)
        logging.info(f"Add Contact response {response} ")
        # Check if contact already exist
        try:
            if response['data'][0]['code'] == 'DUPLICATE_DATA':
                print("Duplicates")

                return func.HttpResponse("Contact already exist in zoho", status_code=409)
        except Exception as e:
            logging.warning(f"No duplicate found {e}")

    except Exception as e:
        logging.error(f"Error adding submitted contact in zoho {e}")

        return func.HttpResponse(json.dumps({"error":str(e)}), status_code=500)
    
    return func.HttpResponse(json.dumps(response), status_code=200)




async def update_lead(req : func.HttpRequest):
    """ Update a lead """
    try:
        # Get the access token 
        access_token=token_instance.get_access_token()

        # Get the form data
        body = req.get_json()
        logging.info(f"received form data: {body}")


        # Update the lead
        response = lead.update_lead(access_token,body)
        logging.info(f"Lead update response {response}")

    except Exception as e:
        logging.error(f"error updating the lead {str(e)}")

        return func.HttpResponse(json.dumps({"error":str(e)}), status_code=500)
    
    # Return the response
    return func.HttpResponse(json.dumps(response), status_code=200)
    


async def create_lead(req : func.HttpRequest):
    """ Create a lead """
    try:
        # Get the access token
        access_token=token_instance.get_access_token()

        # Get the form data
        body = req.form
        logging.info(f"received form data: {body}")

        # Create the lead Instance
        lead_instance = Lead(
            Last_Name=body.get('Vehicle_Name',''),
            buyer_id=body.get('User_ID',''),
            Lead_Score=body.get('Lead_Score',''),
            Buyer_Text=body.get('Buyer_Name',''),
            offer_amount=body.get('Offered_Amount',''),
            Seller=body.get('Seller_ID',''),
            Vehicle_id=body.get('Vehicle_ID','')
        )
        # Call the add Api
        response = lead.add_solo_lead(access_token,dict(lead_instance))
        logging.info(f"Lead create response {response}")

    except Exception as e:
        logging.error(f"error creating the lead {str(e)}")

        return func.HttpResponse(json.dumps({"error":str(e)}), status_code=500)
    
    # Return the response
    return func.HttpResponse(json.dumps(response), status_code=200)
    




async def create_offer(req : func.HttpRequest):
    """ Create an offer """
    try:
        # Get the access token
        access_token=token_instance.get_access_token()

        # Get the form data
        body = req.form
        logging.info(f"received form data: {body}")

        # Create the offer Instance
        offer_instance = Offer(
            Vehicle_id=body.get('Vehicle_ID'),
            lead_id=body.get('Lead_ID'),
            Account_ID=body.get('Account_ID'),
            Offer=body.get('Offer_Amount'),
            Name=f"{body.get('Account_ID')} - {body.get('Vehicle_ID')}"
        )

        # Call the add Api
        response = offer.add_offer(access_token,dict(offer_instance))
        logging.info(f"Lead create response {response}")

        # Return the response
        return func.HttpResponse(json.dumps(response), status_code=200)
    
    except Exception as e:
        
        logging.error(f"error creating the offer {str(e)}")

        return func.HttpResponse(json.dumps({"error":str(e)}), status_code=500)
    


async def update_offer(req : func.HttpRequest):
    """ Update an offer """
    try:
        # Get the access token
        access_token=token_instance.get_access_token()

        # Get the form data
        body = req.get_json()
        logging.info(f"received form data: {body}")

        # Call the Update Api
        response = offer.update_Offer(access_token,body)
        logging.info(f"Lead update response {response}")


    except Exception as e:
        logging.error(f"error while updating the offer {str(e)}")

        return func.HttpResponse(json.dumps({"error":str(e)}), status_code=500)
    
    # Return the response
    return func.HttpResponse(json.dumps(response), status_code=200)
    


async def add_watchlist(req : func.HttpRequest):
    """ Add a watchlist """
    try:
        # Get the access token
        access_token=token_instance.get_access_token()

        # Get the form data
        body = req.form
        logging.info(f"received form data: {body}")

        # Create the watchlist Instance
        watchlist_instance = Watchlist(
            Dealer_id=body.get('Account_ID'),
            Vehicle_id=body.get('Vehicle_ID'),
        )

        # Call the Add Api
        response = watchlist.add_watchlist(access_token,dict(watchlist_instance))
        logging.info(f"Lead update response {response}")

    except Exception as e:
        logging.error(f"error while updating the watchlist {str(e)}")

        return func.HttpResponse(json.dumps({"error":str(e)}), status_code=500)
    # Return the response
    return func.HttpResponse(json.dumps(response), status_code=200)
        


async def update_watchlist(req : func.HttpRequest ):
    """ Add a watchlist """
    try:
        # Get the access token
        access_token=token_instance.get_access_token()

        # Get the form data
        body = req.get_json()
        logging.info(f"received form data: {body}")


        # Call the Add Api
        response = watchlist.update_watchlist(access_token,body)
        logging.info(f"Lead update response {response}")

        # Return the response
        return func.HttpResponse(json.dumps(response), status_code=200)
    
    except Exception as e:
        logging.error(f"error while updating the watchlist {str(e)}")

        return func.HttpResponse(json.dumps({"error":str(e)}), status_code=500)