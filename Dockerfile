FROM continuumio/miniconda3

ENV JOBLIB_TEMP_FOLDER /tmp

RUN pip install -U \
    matplotlib \
    pandas \
    numpy \
    scikit-learn \
    scikit-image \
    scipy

RUN pip install -U \
    jupyter \
    tensorflow \
    keras
