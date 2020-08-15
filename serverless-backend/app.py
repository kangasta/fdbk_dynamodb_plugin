from chalice import Chalice, CognitoUserPoolAuthorizer, CORSConfig, NotFoundError

from os import getenv

from fdbk.utils import create_db_connection
from fdbk.server import ServerHandlers

app = Chalice(app_name='fdbk-lambda')
authorizer = CognitoUserPoolAuthorizer('FdbkPool', provider_arns=[getenv('USER_POOL_ARN')])
cors_config = CORSConfig(
    allow_origin=getenv('CLIENT_URL'),
    allow_credentials=True,
)

db_connection = create_db_connection('fdbk_dynamodb_plugin', [])
handlers = ServerHandlers(db_connection)

@app.route('/overview', authorizer=authorizer, cors=cors_config, methods=['GET'])
def overview():
    data, code = handlers.get_overview(query_args=app.current_request.query_params)
    if code == 404:
        raise NotFoundError(data.get('error'))
    return data
