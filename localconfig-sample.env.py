import os

# Flask config
DEBUG=False
IP=os.environ.get('GALLERY_IP', 'localhost')
PORT=os.environ.get('GALLERY_PORT', '6969')
SERVER_NAME = os.environ.get('GALLERY_SERVER_NAME', 'localhost:6969')
SECRET_KEY = os.environ.get('GALLERY_SECRET_KEY', 'dummy key')

# LDAP config -- UIDs can be entered as a comma separated list e.g `mom,matted`, and are optional
EBOARD_UIDS = os.environ.get('EBOARD_UIDS', '')
RTP_UIDS = os.environ.get('RTP_UIDS', '')
ALUMNI_UIDS = os.environ.get('ALUMNI_UIDS', '')

# OpenID Connect SSO config
OIDC_ISSUER = os.environ.get('GALLERY_OIDC_ISSUER', 'https://sso.csh.rit.edu/auth/realms/csh')
OIDC_CLIENT_ID = os.environ.get('GALLERY_OIDC_CLIENT_ID', 'gallery-dev')
OIDC_CLIENT_SECRET = os.environ.get('GALLERY_OIDC_CLIENT_SECRET', '')

# DB config
SQLALCHEMY_DATABASE_URI = os.environ.get(
        'GALLERY_DATABASE_URI',
        'sqlite:///{}'.format(os.path.join(os.getcwd(), 'data.db')))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Storage config
LOCAL_STORAGE_PATH = './storage'
