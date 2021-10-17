import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="techconfdb.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="MrBen@techconfdb" #TODO: Update value
    POSTGRES_PW="tech$conf1"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://bennotifiersb.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=Vwn2MYe2azMvaaLa7UhPovitQW1bR9fm8u8mypaSwPc=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = "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"
    OLD_SENDGRID_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False