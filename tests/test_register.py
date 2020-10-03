from tutor import app, db, bcrypt
from tutor.routes import home, course # noqa
from tutor.models.users import Users


def test_register_user():
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['TESTING'] = True
    with app.test_client() as c:
        assert Users.query.all() == []
        user = {
            'username': 'test',
            'email': 'test@email.com',
            'password': '123',
            'confirm_password': '123',
            'submit': 'Sign Up'
        }
        c.post('/register', data=user, follow_redirects=True)
        test_user = Users.query.first()
        assert test_user.username == 'test'
        assert test_user.email == 'test@email.com'
        assert bcrypt.check_password_hash(test_user.password, '123')
    Users.query.delete()
    db.session.commit()