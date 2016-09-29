FROM ubuntu:latest
MAINTAINER Jared Worthington <jworthington@email.arizona.edu>
RUN apt-get update 
RUN apt-get -y install python 
RUN apt-get -y install python-pip 
RUN apt-get -y install netcdf-bin 
RUN apt-get -y install libnetcdf-dev 
RUN apt-get -y install libhdf5-serial-dev
RUN pip install --upgrade pip
RUN HDF5_DIR=/usr/local/hdf5
RUN pip install h5py
RUN pip install plotly
RUN pip install netCDF4
ADD hw8Edit.py

VOLUME /data



