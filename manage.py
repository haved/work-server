from subprocess import Popen, PIPE, STDOUT
import sys

def error(message):
    print(f"error: {message}", file=sys.stderr)
    exit(1)

def run_command(cmd, store_output=False, **kwargs):
    p = Popen(cmd, stdout=PIPE if store_output else STDOUT, **kwargs)
    p.wait()
    if p.returncode != 0:
        error(f"Command gave return code {p.returncode}: {' '.join(cmd)}")
    if store_output:
        return p.stdout.read()

def main():
    print("Welcome to the work-server management script.")
