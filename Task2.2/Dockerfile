# Installing python:alpine
FROM python:alpine3.19
# Installing requests lib
RUN pip3 install requests
# Setting the working dir
WORKDIR /app/nasaResults
# Copying my python script to the workdir
COPY get_data.py /app/nasaResults
# As entrypoint, executing my python script
ENTRYPOINT ["python","get_data.py"]
