# 利用 `go-cqhttp` 和 `python3` 搭建 `QQ` 机器人

- 文件目录结构

```bash
.
├── go-cqhttp
│   ├── config.yml          # go-cqhttp 配置文件
│   ├── go-cqhttp           # go-cqhttp 主程序
│   └── middlewares.filter  # go-cqhttp 事件过滤器
├── func.py    # bot 功能函数
├── main.py    # bot 主函数
└── send.py    # bot 发送消息函数
```

## 1. 配置并运行 `go-cqhttp`

- [教程文档](https://docs.go-cqhttp.org/guide/)
- [我的配置文件](go-cqhttp)

## 2. 发送消息原理

- [发送私聊消息教程](https://docs.go-cqhttp.org/api/#发送私聊消息)
- 实现原理如下：

```text
http://127.0.0.1:5700/send_private_msg?user_id=QQ号&message=消息
```

## 3. 主要原理及函数

`Flask` 服务监控并处理 `go-cqhttp` 的上报信息

- 见 [main.py](main.py)

## 4. 运行有关程序

```bash
# 利用 screen 或者 systemctl 实现后台运行
python3 main.py

cd go-cqhttp
./go-cqhttp faststart
```

