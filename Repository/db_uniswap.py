# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Asset(Base):
    __tablename__ = 'asset'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    symbol = Column(String(50))
    load_prices = Column(Boolean)


class Blockchain(Base):
    __tablename__ = 'blockchain'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class AssetHourUsdPrice(Base):
    __tablename__ = 'asset_hour_usd_price'

    id = Column(Integer, primary_key=True)
    asset_id = Column(ForeignKey('asset.id'))
    price = Column(Numeric)
    ts = Column(DateTime)

    asset = relationship('Asset')


class AssetDailyUsdPrice(Base):
    __tablename__ = 'asset_daily_usd_price'

    id = Column(Integer, primary_key=True)
    asset_id = Column(ForeignKey('asset.id'))
    price = Column(Numeric)
    ts = Column(DateTime)

    asset = relationship('Asset')


class AssetDailyWethPrice(Base):
    __tablename__ = 'asset_daily_weth_price'

    id = Column(Integer, primary_key=True)
    asset_id = Column(ForeignKey('asset.id'))
    price = Column(Numeric)
    ts = Column(DateTime)

    asset = relationship('Asset')


class AssetPriceProvider(Base):
    __tablename__ = 'asset_price_provider'

    id = Column(Integer, primary_key=True)
    asset_id = Column(ForeignKey('asset.id'))
    price_provider = Column(String(50))
    token_address = Column(String(50))
    blockchain_id = Column(ForeignKey('blockchain.id'))

    asset = relationship('Asset')
    blockchain = relationship('Blockchain')

