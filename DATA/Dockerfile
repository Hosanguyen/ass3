# Use official Python image
FROM python:3.9
# Set working directory
WORKDIR /app
# Copy files
COPY server.py LSTM_model.h5 tokenizer.pickle /app/
# Install dependencies
RUN pip install flask tensorflow numpy
# Expose port
EXPOSE 5000
# Run server
CMD ["python", "server.py"]