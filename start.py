import os
import sys
import subprocess
from dotenv import load_dotenv

load_dotenv()

port = os.getenv("PORT", "8000")

print(f"Northstar backend starting on port {port}")
print(f"  http://localhost:{port}/        -> frontend")
print(f"  http://localhost:{port}/docs    -> swagger")
print(f"  http://localhost:{port}/api     -> api")
print()

subprocess.run([
    sys.executable, "-m", "uvicorn", "app.main:app",
    "--reload", "--host", "0.0.0.0", "--port", port,
])
