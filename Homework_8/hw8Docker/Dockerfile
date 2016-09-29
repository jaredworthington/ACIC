FROM ubuntu:latest
MAINTAINER Jared Worthington <jworthington@email.arizona.edu>
RUN apt-get update; 
RUN apt-get -y install python python-pip netcdf-bin libnetcdf-dev libhdf5-serial-dev
RUN pip install 
RUN pip install plotly
RUN pip install netCDF4
RUN install h5py
RUN HDF5_DIR=/user/local/hdf5
ADD hw8Edit.py

VOLUME /data



