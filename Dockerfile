FROM debian:bookworm-slim

# Install flatpak and add flathub repository
RUN printf "Types: deb\nURIs: http://deb.debian.org/debian/\nSuites: bookworm-backports\nComponents: main\n" > /etc/apt/sources.list.d/bookworm-backports.sources && \
    apt-get update && apt-get install -y python3 flatpak && apt-get install -y -t bookworm-backports flatpak-builder && \
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
WORKDIR /workspace
