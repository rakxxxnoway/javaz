#!/bin/bash
set -e

INSTALLPATH="/usr/local/lib/javaz"
SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

GREEN="\033[92m"
RESET="\033[0m"

sudo mkdir -p "$INSTALLPATH/std"
sudo chown -R "$USER":"$USER" "$INSTALLPATH"

ln -sf "$SCRIPTDIR/javaz.py" "$INSTALLPATH/"
cp "$SCRIPTDIR"/std/* "$INSTALLPATH/std/"


ALIAS_LINE="alias javaz='python3 $INSTALLPATH/javaz.py'"
BASHRC="$HOME/.bashrc"

if ! grep -q "alias javaz=" "$BASHRC" 2>/dev/null; then
    echo "" >> "$BASHRC"
    echo "# javaz alias" >> "$BASHRC"
    echo "$ALIAS_LINE" >> "$BASHRC"
    echo -e "[${GREEN}*${RESET}] Alias added to .bashrc"
else
    echo -e "[${GREEN}*${RESET}] Alias already exists in .bashrc"
fi

echo -e "[\033[92m*\033[0m] Installation completed successfully!"
