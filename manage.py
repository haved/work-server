#!/usr/bin/env python3

from subprocess import Popen, PIPE
import sys

HEROKU_NAME = "haved-work"
IMAGE_NAME = "work-server-local:1.0"

def error(message):
    print(f"error: {message}", file=sys.stderr)
    exit(1)

def run_command(cmd, store_output=False, **kwargs):
    if not store_output:
        print(f" $ {' '.join(cmd)}")
    p = Popen(cmd, stdout=PIPE if store_output else sys.stdout, **kwargs)
    p.wait()
    if p.returncode != 0:
        error(f"Command gave return code {p.returncode}")
    if store_output:
        return p.stdout.read().decode('utf-8')

def ask_command():
    print()
    print("What do you want to do?")
    print(f" [deploy] Build a docker image on heroku's registry and release it as '{HEROKU_NAME}'")
    print(f" [logs] See heroku logs")
    print(f" [docker_build] Build a docker image locally as '{IMAGE_NAME}'")
    print(f" [docker_run] Run the local docker image")
    print(f" [run] Run the server, not in docker")
    print(f" [<nothing>] quit")
    print()
    print("Enter your choice: ", end="")
    return input()

def main():
    print("Welcome to the work-server management script.")

    changes = run_command(["git", "status", "-sb", "--porcelain"], store_output=True)
    remote, *files = changes.strip().split('\n')
    if len(files) != 0:
        print("You have uncommited changes:")
        for f in files:
            print(f"\t{f}")
    if "ahead" in remote or "behind" in remote:
        print("You are not up to date with github:")
        print(f"\t{remote}")

    args = sys.argv[1:]
    if len(args) == 0:
        command = ask_command()
    elif len(args) == 1:
        command = args[0]
    else:
        error("Too many arguments!")

    if command == "deploy":
        run_command(["heroku", "container:push", "web", "-a", HEROKU_NAME])
        run_command(["heroku", "container:release", "web", "-a", HEROKU_NAME])
    elif command == "logs":
        run_command(["heroku", "logs", "-a", HEROKU_NAME])
    elif command == "open":
        run_command(["heroku", "open", "-a", HEROKU_NAME])
    elif command == "docker_build":
        run_command(["docker", "build", ".", "-t", IMAGE_NAME])
    elif command == "docker_run":
        run_command(["docker", "run", "-it", "-p", "8000:8000", IMAGE_NAME])
    elif command == "run":
        run_command(["python3", "work-server.py"])
    elif command.strip() == "":
        exit(0)
    else:
        error(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
