FROM python:3.7

LABEL author="Chris Lee"
LABEL email="chrisklee93@gmail.com"

ARG EXTRAS="[test]"
ENV PATH=/asyncio-syringe/bin:/root/.poetry/bin:${PATH}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

COPY . /asyncio-syringe
WORKDIR /asyncio-syringe

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

CMD ["bash"]
