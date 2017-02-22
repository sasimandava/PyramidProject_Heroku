import os
import sys
import transaction
import os

# added this import
from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )

# added these imports from mymodel
from ..models.mymodel import (
    DBSession,
    Base,
    User,
    password_context,
    )

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    if 'DATABASE_URL' in os.environ:
        settings['sqlalchemy.url'] = os.environ['DATABASE_URL']

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    # engine = engine_from_config(settings, 'sqlalchemy.')
    # session_factory = get_session_factory(engine)

with transaction.manager:
    password = os.environ.get('ADMIN_PASSWORD', 'admin')
    encrypted = password_context.encrypt(password)
    admin = User(name=u'admin', password=encrypted)
    DBSession.add(admin)
