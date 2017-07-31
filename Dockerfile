FROM continuumio/miniconda3

RUN pip install -U \
    matplotlib \
    pandas \
    numpy \
    scikit-learn \
    scikit-image \
    scipy
