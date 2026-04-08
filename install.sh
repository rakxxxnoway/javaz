#!/bin/bash
set -e

SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SHAREPATH="/usr/local/share/javaz"

GREEN="\033[92m"
RESET="\033[0m"

ok() { echo -e "[${GREEN}*${RESET}] $1"; }

sudo mkdir -p "$SHAREPATH/std"
sudo chown "$USER":"$USER" "$SHAREPATH"

if [ -d "$SCRIPTDIR/std" ]; then
    cp "$SCRIPTDIR"/std/* "$SHAREPATH/std/"
fi

sudo ln -sf "$SCRIPTDIR/javaz.py" /usr/local/bin/javaz
sudo chmod +x "$SCRIPTDIR/javaz.py"

ok "Done! Run: javaz --help"