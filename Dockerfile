FROM python
WORKDIR /Rest_api_tests/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=Rest_api_tests/tests/allure-results