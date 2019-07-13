FROM continuumio/anaconda3
ADD src /src
RUN conda update sympy
WORKDIR /src
CMD [ "python3", "main.py" ]
