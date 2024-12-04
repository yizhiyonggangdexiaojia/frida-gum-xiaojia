import sys; 
sys.path.insert(0, sys.argv[1]); 

from releng.meson_make import main; 

main()

# python3 main.py ~/value/frida-gum ./build all

# python3 main.py ~/value/frida-gum ./build all -Doption1=value1 -Doption2=value2

# option1=get_option("option1")

# ./configure --host=android-arm64 -- -Dfrida-gum:devkits=gum,gumjs -Dfrida-core:devkits=core
