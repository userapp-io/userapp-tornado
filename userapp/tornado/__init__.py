import userapp

class Context(object):
    def __init__(self, api, cookie_name=None):
        self.api=api
        self.cookie_name=cookie_name

def config(app_id, cookie_name='ua_session_token'):
    """
    Configuration decorator.
    """
    def func(f):
        def wrapper(*args):
            request = args[1]

            request.userapp = Context(userapp.API(app_id=app_id), cookie_name)

            return f(*args)
        return wrapper
    return func

def authorized():
    """
    Check whether a user is authorized.
    """
    def func(f):
        def wrapper(*args):
            result = None
            self = args[0]
            context = self.request.userapp
            
            try:
                if context.cookie_name in self.cookies:
                    # A good idea would be to add caching here so we don't need to hit the UserApp API every time
                    context.api.set_option("token", self.get_cookie(context.cookie_name))
                    self.user_id = context.api.user.get(fields=['user_id'])[0].user_id
                else:
                    result = {'error_code':'USER_NOT_AUTHORIZED', 'message':'User not authorized. Please log in.'}
            except userapp.UserAppServiceException as e:
                result = {'error_code':e.error_code, 'message':e.message}

            if not result is None:
                self.finish(result)
                return None

            return f(*args)
        return wrapper
    return func

def has_permission(permission):
    """
    Check whether a user is authenticated and has certain permissions.
    """
    def func(f):
        def wrapper(*args):
            result = None
            self = args[0]
            context = self.request.userapp

            try:
                permission_result = context.api.user.hasPermission(user_id='self', permission=permission)

                if len(permission_result.missing_permissions) > 0:
                    result = {'error_code':'USER_NOT_AUTHORIZED', 'message':'User is not authorized to do this action.'}
            except userapp.UserAppServiceException as e:
                result = {'error_code':e.error_code, 'message':e.message}

            if not result is None:
                self.finish(result)
                return None

            return f(*args)
        return wrapper
    return func