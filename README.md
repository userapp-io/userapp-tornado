# userapp-tornado

UserApp support for the Tornado web framework.

## Getting started

### Installing and loading the library

Install using pip:

    $ pip install userapp.tornado --pre

Load the library:

    import userapp.tornado
    
## Decorators

#### userapp.tornado.config(string app_id, string cookie_name)

All handlers should always be decorated with this.

#### userapp.tornado.authorized()

Require that a request is authorized with UserApp. Once authenticated, use `self.user_id` to retrieve the identity of your user.

#### userapp.tornado.has_permission(mixed permission)

Assert that an authorized user has a specific permission. Can either be a single string or an array of strings.

## Example

    import userapp.tornado

    @userapp.tornado.config(app_id=config.APP_ID)
    class ForumThreadHandler(tornado.web.RequestHandler):
        def get(self):
            """Read all threads."""
            # Does not have self.user_id since it does not require authorization.
            
        @userapp.tornado.authorized()
        def post(self):
            """Add a new thread."""
            print(self.user_id) # Do something with the authorized user.
            
        @userapp.tornado.authorized()
        @userapp.tornado.has_permission('admin')
        def delete(self):
            """Delete an existing thread (admin only)."""
            print(self.user_id) # Do something with the authorized user.

## Dependencies

* [UserApp for Python](https://github.com/userapp-io/userapp-python) (userapp)

## License

MIT
