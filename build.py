#!/usr/bin/python3
import subprocess

BUILD_LIST = [
    ("com.todesk.ToDesk", "com.todesk.ToDesk.yaml"),
]


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
            "--runtime-repo=https://flathub.org/repo/flathub.flatpakrepo",
        ],
        check=True,
        cwd=appname,
    )


def build_single(appname: str, manifest: str):
    flatpak_build(appname, manifest)


def build():
    for i in BUILD_LIST:
        appname = i[0]
        manifest = i[1]
        print(f"Building {appname}/{manifest} ...")
        build_single(appname, manifest)


if __name__ == "__main__":
    build()
