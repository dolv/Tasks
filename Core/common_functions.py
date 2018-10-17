import os
import shlex
import subprocess
from Core.Logger import logger

def call_subprocess(cmd, args, env_vars={}):
    child = subprocess.Popen(shlex.split(cmd), env=env_vars, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cmd_result = {"stdout":[],"stderr":[]}
    while child.poll() is None:
        for line in iter(child.stdout.readline, b''):
            formated_string=line.decode().replace(line[:-1] if line[-1] == os.linesep else '\n', '')
            cmd_result["stdout"].append(formated_string)
            if args.debug:
                logger.info(message=formated_string)
        for line in iter(child.stderr.readline, b''):
            formated_string = line.decode().replace(line[:-1] if line[-1] == os.linesep else '\n', '')
            cmd_result["stderr"].append(formated_string)
            if args.debug:
                logger.error(message=formated_string)
    child.terminate()
    return cmd_result
