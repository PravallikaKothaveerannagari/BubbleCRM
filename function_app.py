import azure.functions as func
import logging
from src.funcmain import *

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="register-account",methods=['POST'])
async def account_registration(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f'Request received from {req.url}')

    try:
        return await register_account(req=req)
    
    except Exception as e:
        logging.error(f'Error processing request: {str(e)}')
        return func.HttpResponse(f"Internal server error :{str(e)}", status_code=500)
    
@app.route(route="contact",methods=['POST'])
async def contact(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f'Request received from {req.url}')

    try:
        if req.params.get('action') == 'update':
            return await update_contact(req=req)
        
        elif req.params.get('action') == 'create':
            return await register_contact(req=req)
        
        else:
            return func.HttpResponse(f"Invalid action: {req.params.get('action')}", status_code=400)
    
    except Exception as e:
        logging.error(f'Error processing request: {str(e)}')
        return func.HttpResponse(f"Internal server error :{str(e)}", status_code=500)

@app.route(route="lead", methods=['POST'])
async def lead_operation(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f'Request received from {req.url}')
    try:
        if req.params.get('action') == 'update':
            return await update_lead(req)
        elif req.params.get('action') == 'create':
            return await create_lead(req)
        else:
            return func.HttpResponse(f"Invalid action: {req.params.get('action')}", status_code=400)
    except Exception as e:
        logging.error(f'Error processing request: {str(e)}')
        return func.HttpResponse(f"Internal server error: {str(e)}", status_code=500)

@app.route(route="offer", methods=['POST'])
async def offer_operation(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f'Request received from {req.url}')
    try:
        if req.params.get('action') == 'create':
            return await create_offer(req)
        elif req.params.get('action') == 'update':
            return await update_offer(req)
        else:
            return func.HttpResponse(f"Invalid action: {req.params.get('action')}", status_code=400)
    except Exception as e:
        logging.error(f'Error processing request: {str(e)}')
        return func.HttpResponse(f"Internal server error: {str(e)}", status_code=500)

@app.route(route="watchlist", methods=['POST'])
async def watchlist_operation(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f'Request received from {req.url}')
    try:
        if req.params.get('action') == 'create':
            return await add_watchlist(req)
        elif req.params.get('action') == 'update':
            return await update_watchlist(req)
        else:
            return func.HttpResponse(f"Invalid action: {req.params.get('action')}", status_code=400)
    except Exception as e:
        logging.error(f'Error processing request: {str(e)}')
        return func.HttpResponse(f"Internal server error: {str(e)}", status_code=500)

@app.route(route="ping", methods=['GET'])
async def ping(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Ping request received.')
    return func.HttpResponse("Service is Up!", status_code=200)