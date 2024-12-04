### clone

递归clone

```
git clone --recurse-submodules https://github.com/yizhiyonggangdexiaojia/frida-gum-xiaojia.git
```



### build

```sh
./configcure --host=anrdoid-arm64

devkits编译
./configure --host=android-arm64 -- -Ddevkits=gum,gumjs -Dgumjs=enabled

make
```

### 修补
```
去除默认libc下的hook
去除Java的api，需要请自行编译_agent.js进行使用
去除gum-js-loop改为xiaojia
```

