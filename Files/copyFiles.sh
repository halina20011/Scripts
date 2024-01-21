i3=~/.config/i3
polybar=~/.config/polybar
neovim=~/.config/nvim
alacritty=~/.config/alacritty

firefox=~/.mozilla/firefox/oiz172e1.default-release/chrome/userContent.css

themeScheme=~/.themeScheme.json

configs=("$i3 $polybar $neovim $alacritty $firefox $themeScheme")

for con in $configs; do
    echo "Copying $con to $(pwd):"
    $(cp -rf $con ./Rice)
done
