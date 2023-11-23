import contextlib
import contextmanager as ct

@contextlib.contextmanager
def db_handler():
    ct.stop_database()
    yield
    ct.start_database()
    
    
    

with db_handler():
    ct.db_backup()
    