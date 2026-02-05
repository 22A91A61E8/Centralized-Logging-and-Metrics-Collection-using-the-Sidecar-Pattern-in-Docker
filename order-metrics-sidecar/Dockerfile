FROM python:3.11-slim
WORKDIR /metrics
COPY metrics_sidecar.py .
RUN pip install flask requests
CMD ["python", "metrics_sidecar.py"]

