# UserApp for Tornado (Python)

This library adds [UserApp](https://www.userapp.io/) support for the Python [Tornado web framework](http://www.tornadoweb.org/en/stable/). By simple decorators you can easily tap into the power of UserApp. Authenticate your users in just one line of code!

*UserApp is a cloud-based user management API for web apps with the purpose to relieve developers from having to program logic for user authentication, sign-up, invoicing, feature/property/permission management, OAuth, and more.*

## Getting started

### Installing and loading the library

Install using pip:

    $ pip install userapp.tornado --pre

Load the library:

    import userapp.tornado
    
## Decorators

#### config(string app_id, string cookie_name)

All handlers should always be decorated with this. Go [here](https://help.userapp.io/customer/portal/articles/1322336-how-do-i-find-my-app-id-) to find your App Id.

#### authorized()

Require that a request is authorized with UserApp. Once authenticated, use `self.user_id` to retrieve the identity of your user.

#### has_permission(mixed permission)

Assert that an authorized user has a specific permission. Can either be a single string or an array of strings.

## Example

    import userapp.tornado

    @userapp.tornado.config(app_id='YOUR_APP_ID')
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

For a full demo app, see [Tempbox](https://github.com/userapp-io/tempbox-python-angularjs) − A temporary file storage demo app powered by UserApp, Python (Tornado) and AngularJS.

## Dependencies

* [UserApp for Python](https://github.com/userapp-io/userapp-python) (userapp)

## Help

Contact us via email at support@userapp.io or visit our [support center](https://help.userapp.io).

## License

MIT
