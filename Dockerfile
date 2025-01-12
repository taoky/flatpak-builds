FROM debian:bookworm-slim

# Install flatpak and add flathub repository
RUN apt-get update && apt-get install -y flatpak flatpak-builder python3 && \
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
WORKDIR /workspace
