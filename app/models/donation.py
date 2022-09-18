from sqlalchemy import Column, ForeignKey, Integer, Text

from .abstract_base import AbstractBase


class Donation(AbstractBase):
    '''Модель пожертвований таблицы donation.'''
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)