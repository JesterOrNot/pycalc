FROM continuumio/anaconda3
ADD . /app
WORKDIR /app
RUN /bin/ls
RUN pip install -r requirements.txt
RUN conda update sympy
CMD [ "/opt/conda/bin/python3.7", "main.py" ]