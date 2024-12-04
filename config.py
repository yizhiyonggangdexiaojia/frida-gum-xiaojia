import sys; 
sys.path.insert(0, sys.argv[1]); 
from releng.meson_configure import main; 

main()

# python3 config.py ~/value/frida-gum -- -Ddevkits=gum,gumjs

# python3 config.py ~/value/frida-gum -- -Dfrida-gum:devkits=gum,gumjs
