### clone

递归clone

```
git clone --recurse-submodules https://github.com/yizhiyonggangdexiaojia/frida-gum-xiaojia.git
```



### build

```sh
./configure --host=android-arm64

devkits编译
./configure --host=android-arm64 -- -Ddevkits=gum,gumjs -Dgumjs=enabled

make
```

### 修补
```
frida-java-bridge修改为frida-java-bridge-xiaojia，默认为直接修改Artethod的方式
如果出现问题找到bindings/gumjs/runtime/frida-java-bridge-xiaojia，把里面的android.js替换为此项目中的branch的hookGetOatQuickMethodHeader_android.js
添加相关子项目等
```

