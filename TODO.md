# Fix Auth Issues

## Tasks
- [x] Convert models/user.py to ORM class User
- [x] Update app/auth/auth_handler.py to use User class and ORM queries
- [x] Update routes/user.py to use ORM session instead of core
- [x] Update models/index.py to import User class
- [x] Downgrade bcrypt to 3.2.2 to fix version error (not needed after fixes)
- [x] Ensure database tables are created with Base.metadata.create_all()
- [x] Test auth APIs
