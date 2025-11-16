#!/usr/bin/python3
import subprocess
from pathlib import Path
import os

BUILD_LIST = [
    ("com.todesk.ToDesk", "com.todesk.ToDesk.yaml"),
    ("io.github.vito0912.abs_flutter", "io.github.vito0912.abs_flutter.yaml"),
    ("dev.filimonov.klogg", "dev.filimonov.klogg.yaml"),
    ("io.github.RSSNext.Folo", "io.github.RSSNext.Folo.yaml"),
    ("io.github.hmcl_dev.hmcl", "io.github.hmcl_dev.hmcl.yaml"),
    ("org.gnome.dfeet", "org.gnome.dfeet.yaml"),
    ("org.gnome.dspy", "org.gnome.dspy.yaml"),
    ("me.kavishdevar.librepods", "me.kavishdevar.librepods.yaml"),

    # https://github.com/taoky/Cider/releases
    # https://github.com/taoky/showimg/releases
]


def get_replacement(env: str, default: str):
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
            "--repo=repo",
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
            "repo",
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
