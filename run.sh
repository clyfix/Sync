#this executes required python script to run the app -- without it, the app will be stuck on loading
set -e
cd "$(dirname "$0")"

if [ -x ".venv/bin/python" ]; then
  exec ./.venv/bin/python calculatorv2.py
else
  exec python3 calculatorv2.py
fi
