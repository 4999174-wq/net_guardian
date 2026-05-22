#!/bin/bash

python src/train_model.py

python src/modbus_client.py &

streamlit run src/streamlit_app.py