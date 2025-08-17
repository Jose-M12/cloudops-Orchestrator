import json, os, subprocess, tempfile
from typing import Dict, Literal

def run_terraform(cmd: Literal["plan","apply","destroy"], stack_path: str, vars_: Dict, workspace: str):
    env = {**os.environ, "TF_IN_AUTOMATION": "1", "TF_INPUT": "0"}
    with tempfile.TemporaryDirectory() as tmp:
        cwd = stack_path
        subprocess.run(["terraform", "init", "-input=false", "-upgrade"], cwd=cwd, check=True, env=env)
        subprocess.run(["terraform", "workspace", "select", workspace], cwd=cwd, env=env, check=False)
        subprocess.run(["terraform", "workspace", "new", workspace], cwd=cwd, env=env, check=False)
        var_args = sum([["-var", f"{k}={json.dumps(v)}"] for k, v in vars_.items()], [])
        if cmd == "plan":
            out = os.path.join(tmp, "tfplan")
            subprocess.run(["terraform", "plan", "-input=false", "-out", out, *var_args], cwd=cwd, check=True, env=env)
            return {"plan_path": out}
        elif cmd == "apply":
            subprocess.run(["terraform", "apply", "-input=false", "-auto-approve", *var_args], cwd=cwd, check=True, env=env)
            return {"status": "applied"}
        else:
            subprocess.run(["terraform", "destroy", "-input=false", "-auto-approve", *var_args], cwd=cwd, check=True, env=env)
            return {"status": "destroyed"}
