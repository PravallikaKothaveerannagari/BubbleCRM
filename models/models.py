from pydantic import BaseModel, Field
from typing import Optional


class Company(BaseModel):
    Account_Name : str 
    Dealer_License_Number : str
    Dealer_Phone : str
    Category : str
    Website : str
    Address : str
    ExpiryDate : Optional[str] = None
    Business_Number : str
    CRA_HST_GST_Number : str
    SK_PST_Number : str
    Email : str
    BC_PST_Number : str 



class Contact(BaseModel):
    Account_ID : str 
    Last_Name : str 
    Email : str 
    Phone :str 
    Position_Role : str 
    Note : str 




class Lead(BaseModel):
    Last_Name : str
    buyer_id : str
    Lead_Score : str
    Vehicle_id : str
    Buyer_Text : str
    offer_amount : str
    Seller : str
    Vehicle_State : str = 'Available'
    Progress_Status : str = 'To Be Connected'



class Offer(BaseModel):
    Vehicle_id : str
    lead_id : str
    Account_ID : str
    Offer : str
    Name : str



class Watchlist(BaseModel):
    Dealer_id : str
    Vehicle_id : str
    Active : bool = True




