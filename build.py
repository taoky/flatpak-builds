#!/usr/bin/python3
import subprocess
from pathlib import Path
import os

BUILD_LIST = [
    ("com.todesk.ToDesk", "com.todesk.ToDesk.yaml"),
]


def get_replacement(env, default):
    res = os.environ.get(env, default)
    if not res:
        return default
    return res


REPLACEMENTS = {
    "😡TODESK_DOMAIN😡": get_replacement(
        "TODESK_DOMAIN", "dl.todesk.com"
    ),
    "😡TODESK_DIR😡": get_replacement(
        "TODESK_DIR", "linux"
    )
}


def flatpak_build(appname: str, manifest: str):
    subprocess.run(
        [
            "flatpak-builder",
            "--force-clean",
            "--install-deps-from=flathub",
            "--install",
            "build",
            manifest,
        ],
        check=True,
        cwd=appname,
    )
    subprocess.run(
        [
            "flatpak",
            "build-bundle",
            "/var/lib/flatpak/repo/",
            appname + ".flatpak",
            appname,
        ],
        check=True,
        cwd=appname,
    )


def build_single(appname: str, manifest: str):
    manifest_path = Path(appname) / manifest
    manifest_template_path = Path(appname) / (manifest + ".template")
    if manifest_template_path.exists():
        # Do template substitution
        with open(manifest_template_path, "r") as f:
            data = f.read()
        for k, v in REPLACEMENTS.items():
            data = data.replace(k, v)
        with open(manifest_path, "w") as f:
            f.write(data)
    flatpak_build(appname, manifest)


def build():
    for i in BUILD_LIST:
        appname = i[0]
        manifest = i[1]
        print(f"Building {appname}/{manifest} ...")
        build_single(appname, manifest)


if __name__ == "__main__":
    build()
