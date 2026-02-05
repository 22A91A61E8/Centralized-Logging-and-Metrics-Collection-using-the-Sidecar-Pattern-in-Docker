FROM python:3.11-slim
WORKDIR /sidecar
COPY logging_sidecar.py .
RUN pip install requests
CMD ["python", "logging_sidecar.py"]
