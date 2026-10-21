# Redis 与 MongoDB

> 对应图片里的「Redis」「MongoDB」。
> 目标：知道各自适合什么场景，能写基本操作，能在面试里讲清区别。

---

## 先记住这几件事

1. MySQL 存业务主数据，Redis 做缓存/计数/会话，MongoDB 存结构灵活的文档。
2. Redis 是内存数据库，快，但内存贵，别当主库。
3. Redis 的键要统一命名，设置过期时间。
4. MongoDB 用文档存数据，适合日志、对话、工具调用记录。
5. 三者不是互相替代，是分工。

---

## 一、Redis 是什么

- 内存中的键值数据库
- 读写非常快（微秒级）
- 常用于：缓存、会话、计数器、排行榜、限流、分布式锁

### 常见数据类型

| 类型 | 结构 | 场景 |
| --- | --- | --- |
| string | 字符串 | 缓存 JSON、计数器 |
| hash | 字段-值 | 存对象 |
| list | 列表 | 队列、最新消息 |
| set | 集合 | 去重、共同好友 |
| sorted set | 带分数的集合 | 排行榜、延时队列 |

### 基本命令

```text
SET user:1:name "小明"
GET user:1:name

HSET user:1 name "小明" age 18
HGET user:1 name
HGETALL user:1

LPUSH queue task1
RPOP queue

SADD tags python backend
SMEMBERS tags

ZADD rank 100 user1
ZREVRANGE rank 0 9 WITHSCORES

EXPIRE user:1:name 60
TTL user:1:name
DEL user:1:name
```

### 键名规范

```text
业务:模块:标识
user:1:profile
task:2026-10-22:count
cache:skill:list
```

### 缓存模式

```text
读：
  1. 先查 Redis
  2. 没有 → 查 MySQL
  3. 写回 Redis，设置过期时间

写：
  1. 更新 MySQL
  2. 删除 Redis 缓存（不是更新）
```

### 缓存常见问题

| 问题 | 含义 | 处理 |
| --- | --- | --- |
| 缓存穿透 | 查不存在的数据，每次都打到 DB | 缓存空值 / 布隆过滤器 |
| 缓存击穿 | 热点 key 过期，大量请求打到 DB | 互斥锁 / 逻辑过期 |
| 缓存雪崩 | 大量 key 同时过期 | 过期时间加随机值 |

### 过期策略

- 惰性删除：访问时检查是否过期
- 定期删除：定期扫描一部分
- 内存淘汰：内存满时按策略淘汰（LRU、LFU 等）

---

## 二、MongoDB 是什么

- 文档数据库
- 数据以 BSON（类似 JSON）文档存储
- 适合：结构不固定、字段经常变、嵌套层级深的数据

### 概念对比

| MySQL | MongoDB |
| --- | --- |
| 数据库 database | 数据库 database |
| 表 table | 集合 collection |
| 行 row | 文档 document |
| 列 column | 字段 field |
| 主键 id | `_id` |

### 基本操作

```javascript
// 插入
db.conversations.insertOne({
  user_id: 1,
  title: "学习计划",
  created_at: new Date()
})

// 查询
db.conversations.find({ user_id: 1 })
db.conversations.findOne({ _id: ObjectId("...") })

// 更新
db.conversations.updateOne(
  { _id: ObjectId("...") },
  { $set: { title: "新标题" } }
)

// 删除
db.conversations.deleteOne({ _id: ObjectId("...") })
```

### 什么时候用 MongoDB

- 数据结构不固定
- 需要嵌套（一条对话里包含多条消息）
- 日志、事件、工具调用记录
- 快速迭代，字段经常加

### 什么时候不用

- 需要复杂事务
- 需要多表 JOIN
- 数据关系强、一致性要求高

---

## 三、三者怎么分工

| 数据 | 存哪 | 原因 |
| --- | --- | --- |
| 用户、任务、打卡 | MySQL | 关系强，需要事务 |
| 热点查询结果 | Redis | 读多写少，要求快 |
| 会话 / 验证码 | Redis | 有过期时间 |
| 对话消息、工具调用日志 | MongoDB | 结构灵活，量大 |
| 文件 | 对象存储 / 磁盘 | 不适合数据库 |

---

## 四、Python 操作示例

### Redis

```python
import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

r.set("user:1:name", "小明", ex=60)
print(r.get("user:1:name"))
print(r.ttl("user:1:name"))

r.hset("user:1", mapping={"name": "小明", "age": 18})
print(r.hgetall("user:1"))

r.incr("task:2026-10-22:count")
```

### MongoDB

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["study_assistant"]
messages = db["messages"]

messages.insert_one({
    "conversation_id": 1,
    "role": "user",
    "content": "今天该学什么？",
})

for msg in messages.find({"conversation_id": 1}):
    print(msg)
```

---

## 五、面试常问

1. Redis 为什么快？
2. Redis 的常见数据类型和场景？
3. 缓存穿透、击穿、雪崩的区别？
4. Redis 的过期策略和淘汰策略？
5. Redis 能当主数据库吗？为什么？
6. MySQL 和 MongoDB 的区别？
7. 什么时候用 MongoDB？
8. Redis 和 MySQL 数据不一致怎么办？
9. 如何用 Redis 实现排行榜？
10. 如何用 Redis 实现分布式锁？

---

## 六、动手实验

### 实验 1：Redis 缓存

1. 用 Redis 存一个 JSON 字符串，设置 30 秒过期
2. 读取，观察 `TTL`
3. 30 秒后再读，确认已过期
4. 用 `INCR` 做一个访问计数器

### 实验 2：MongoDB 文档

1. 插入 3 条对话，每条包含 `conversation_id`、`role`、`content`
2. 按 `conversation_id` 查询
3. 给其中一条加一个 `tool_calls` 数组
4. 观察文档结构可以不一样

### 实验 3：对比

写一页笔记：

```text
同一份「对话记录」，存 MySQL 要几张表？存 MongoDB 要几个文档？
各自的好处和坏处是什么？
```

---

## 七、自检

- [ ] 能说出 Redis 的 5 种数据类型和场景？
- [ ] 能解释缓存穿透/击穿/雪崩？
- [ ] 能说出 MongoDB 适合什么数据？
- [ ] 能说出 MySQL / Redis / MongoDB 的分工？
- [ ] 能写一个 Redis 缓存读取流程？
- [ ] 能写一个 MongoDB 插入和查询？
