from fastapi import FastAPI, Response, Request, status
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel
from users_table_helpers import read_user_by_id, auth_user_by_creds
from products_table_helpers import read_products_table
import constants as const

# This is what we expect on login request. BaseModel takes care of other items
class Credentials(BaseModel):
    username: str
    password: str

app = FastAPI()

# adding a session. keep this line here to properly init middleware
app.add_middleware(SessionMiddleware, secret_key="SECRET_KEY")

@app.get("/")
async def read_root():
    '''
    Test URL. Check Postman or where-ever to get JSON Payload which is returned below
    '''
    return {"Hello":"World"}

# Test URL to check DB access is ok
@app.get("/users/{id}")
async def get_users(id):
    print(id, type(id))
    data = read_user_by_id(id)
    return {"name":data}

@app.post("/login", status_code= status.HTTP_200_OK)
async def authenticate_user(user: Credentials, req_header: Request, resp_header: Response):
    print(user.dict())
    resp_data = dict()
    data = auth_user_by_creds(user.dict())
    if(data == const.NOT_FOUND):
        resp_data['message'] = "UserId not Found!"
        req_header.session['token'] = None
        resp_header.status_code = status.HTTP_404_NOT_FOUND
    else:
        resp_data["message"] = data.username
        req_header.session['token'] = data.username
        print(req_header.session)
    return resp_data

@app.get('/products')
async def get_products_list(req: Request, res: Response):
    '''
    Access might be denied just because there's no session token initialized
    At UI, it must redirect to 
    '''
    if (req.session['token'] != None):
        print("TOKEN:", req.session['token'])
        print("Fetching Records.....")
        data = read_products_table()
        res.status_code = status.HTTP_200_OK
        return data
    else:
        res.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message":"Unauthorized Access"}