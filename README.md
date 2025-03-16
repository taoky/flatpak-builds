Build Flatpak single-file bundles for some certain packages not on Flathub, with GitHub Actions & GitHub Releases.

List:

- com.todesk.ToDesk from <https://github.com/chenyuanrun/flathub/tree/com.todesk.ToDesk> (Modified from <https://github.com/flathub/flathub/pull/5109>)
- io.github.vito0912.abs_flutter (from upstream pre-built release)
- dev.filimonov.klogg (from upstream appimage)

"COPYING" files within dirs are the license of each manifest files (xxx.yaml*), not for original software.

Notes:

- Update to latest version URL & sha256sum:

   ```shell
   flatpak run org.flathub.flatpak-external-data-checker --edit-only xxx.yaml
   ```

- Shell function for `dev.filimonov.klogg`:

   bash:

   ```bash
   klogg() {
      if [[ -z "$1" ]]; then
         echo "Usage: klogg <filename>"
         return 1
      fi
      flatpak run --file-forwarding dev.filimonov.klogg @@ "$1" @@
   }
   ```

   fish:

   ```fish
   function klogg
      if test -z "$argv"
         echo "Usage: klogg <filename>"
         return 1
      end
      flatpak run --file-forwarding dev.filimonov.klogg @@ $argv[1] @@
   end
   ```
