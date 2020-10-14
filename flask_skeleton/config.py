import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = "KXPeA6Wb5rHEGb6Dzxsxkvv6MKdMs5e2DESQArRwFqLXstsB"
  SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "project/site.db")