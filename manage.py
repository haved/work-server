#!/usr/bin/env python3

from subprocess import Popen, PIPE
import sys

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

    print()
    print("What do you want to do?")
    print(" [deploy] Build a docker image on heroku's registry and release it")
    print(" [docker_build] Build a docker image locally")
    print(" [docker_run] Run the local docker image")
    print(" [run] Run the server, not in docker")
    print()
    print("Enter your choice: ", end="")
    command = input()

    if command == "deploy":
        run_command(["heroku", "container:push", "web", "-a", "work-server"])
        run_command(["heroku", "container:release", "web", "-a", "work-server"])
    elif command == "docker_build":
        run_command(["docker", "image", "build", "-t", IMAGE_NAME])
    elif command == "docker_run":
        run_command(["docker", "run", "-it", IMAGE_NAME])
    elif command == "run":
        run_command(["python3", "work-server.py"])
    else:
        error(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
