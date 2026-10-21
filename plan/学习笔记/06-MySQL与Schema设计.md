# MySQL 与 Schema 设计

> 对应图片里的「MySQL」「Schema design」。
> 目标：能设计 8–10 张表的项目库，会写 CRUD、JOIN、索引、事务。

---

## 先记住这几件事

1. 表 = 一类数据，行 = 一条记录，列 = 字段。
2. 主键唯一标识一行，外键关联另一张表。
3. 先画 ER 图，再建表。
4. 索引能加速查询，但会拖慢写入，不是越多越好。
5. 事务保证「要么全成功，要么全失败」。

---

## 一、SQL 基础

### 建表

```sql
CREATE TABLE student (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### 插入

```sql
INSERT INTO student (name, age) VALUES ('小明', 18);
INSERT INTO student (name, age) VALUES ('小红', 19), ('小刚', 20);
```

### 查询

```sql
SELECT * FROM student;
SELECT name, age FROM student WHERE age >= 18;
SELECT * FROM student ORDER BY age DESC LIMIT 10;
```

### 更新

```sql
UPDATE student SET age = 19 WHERE name = '小明';
```

### 删除

```sql
DELETE FROM student WHERE id = 1;
```

> 真实项目一般不物理删除，用 `is_deleted` 软删除。

---

## 二、JOIN

### 内连接

只返回两边都匹配的行。

```sql
SELECT s.name, c.title
FROM student s
JOIN course c ON s.id = c.student_id;
```

### 左连接

返回左表所有行，右表没有的显示 NULL。

```sql
SELECT s.name, c.title
FROM student s
LEFT JOIN course c ON s.id = c.student_id;
```

### 右连接

返回右表所有行。

```sql
SELECT s.name, c.title
FROM student s
RIGHT JOIN course c ON s.id = c.student_id;
```

### 对比

| 类型 | 结果 |
| --- | --- |
| INNER JOIN | 两边都匹配 |
| LEFT JOIN | 左表全要 |
| RIGHT JOIN | 右表全要 |
| FULL JOIN | 两边全要（MySQL 不直接支持，用 UNION） |

---

## 三、聚合与分组

```sql
SELECT student_id, COUNT(*) AS total
FROM task
GROUP BY student_id;

SELECT student_id, AVG(score) AS avg_score
FROM exam
GROUP BY student_id
HAVING avg_score > 80;
```

> `WHERE` 在分组前过滤，`HAVING` 在分组后过滤。

---

## 四、索引

### 为什么需要

没有索引，查一行要扫描全表；有索引，像查字典一样快。

### 建索引

```sql
CREATE INDEX idx_task_user_date ON task (user_id, task_date);
```

### 什么时候该加

- 经常出现在 `WHERE`、`JOIN`、`ORDER BY` 的字段
- 区分度高的字段（比如用户 ID）
- 组合索引注意顺序：最左前缀

### 什么时候会失效

- 在索引列上做运算：`WHERE YEAR(created_at) = 2026`
- 用 `LIKE '%xxx'` 前置通配
- 类型不匹配：字符串列传数字
- 使用 `OR` 但两边没有都走索引
- 数据量很小，优化器可能直接全表扫描

### 常见面试题

- 索引为什么能加速？
- B+ 树和 B 树的区别？
- 聚簇索引和非聚簇索引？
- 什么是最左前缀原则？
- 索引失效的常见情况？

---

## 五、事务

### ACID

| 特性 | 含义 |
| --- | --- |
| 原子性 Atomicity | 要么全成功，要么全失败 |
| 一致性 Consistency | 从一种合法状态到另一种合法状态 |
| 隔离性 Isolation | 并发事务互不干扰 |
| 持久性 Durability | 提交后不会丢 |

### 隔离级别

| 级别 | 脏读 | 不可重复读 | 幻读 |
| --- | --- | --- | --- |
| 读未提交 | 可能 | 可能 | 可能 |
| 读已提交 | 不会 | 可能 | 可能 |
| 可重复读（MySQL 默认） | 不会 | 不会 | 可能（InnoDB 很大程度避免） |
| 串行化 | 不会 | 不会 | 不会 |

### 示例

```sql
START TRANSACTION;
UPDATE account SET balance = balance - 100 WHERE id = 1;
UPDATE account SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

出错时：

```sql
ROLLBACK;
```

---

## 六、Schema 设计原则

1. **一张表只存一类东西。**
2. **每张表有主键。**
3. **能拆的重复数据拆出去**（比如科目字典）。
4. **不要存计算得出的冗余数据**，除非有性能需要。
5. **字段尽量 `NOT NULL` + 默认值。**
6. **时间用 `DATETIME`，统一时区。**
7. **软删除用 `is_deleted` + `deleted_at`。**
8. **命名统一**：表名小写下划线，字段名小写下划线。

---

## 七、项目 Schema：AI 学习助手

### ER 关系

```text
user 1 ── n goal
user 1 ── n skill
user 1 ── n task
task 1 ── n checkin
skill 1 ── n task
user 1 ── n conversation
conversation 1 ── n message
message 1 ── n tool_call
```

### 建表 SQL（简化版）

```sql
CREATE TABLE app_user (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE goal (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    target_role VARCHAR(100) NOT NULL,
    target_company VARCHAR(100),
    start_date DATE,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_goal_user FOREIGN KEY (user_id) REFERENCES app_user(id)
);

CREATE TABLE skill (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    current_level TINYINT NOT NULL DEFAULT 0,
    target_level TINYINT NOT NULL DEFAULT 3,
    notes TEXT,
    CONSTRAINT fk_skill_user FOREIGN KEY (user_id) REFERENCES app_user(id)
);

CREATE TABLE task (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    skill_id BIGINT,
    title VARCHAR(200) NOT NULL,
    task_date DATE NOT NULL,
    estimated_minutes INT DEFAULT 30,
    actual_minutes INT DEFAULT 0,
    status VARCHAR(20) NOT NULL DEFAULT 'todo',
    evidence_url VARCHAR(500),
    notes TEXT,
    is_deleted TINYINT NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_task_user FOREIGN KEY (user_id) REFERENCES app_user(id),
    CONSTRAINT fk_task_skill FOREIGN KEY (skill_id) REFERENCES skill(id),
    INDEX idx_task_user_date (user_id, task_date)
);

CREATE TABLE checkin (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    task_id BIGINT NOT NULL,
    user_id BIGINT NOT NULL,
    minutes INT NOT NULL,
    note TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_checkin_task FOREIGN KEY (task_id) REFERENCES task(id),
    CONSTRAINT fk_checkin_user FOREIGN KEY (user_id) REFERENCES app_user(id)
);

CREATE TABLE resource (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    skill_id BIGINT,
    title VARCHAR(200) NOT NULL,
    url VARCHAR(500),
    resource_type VARCHAR(50),
    CONSTRAINT fk_resource_skill FOREIGN KEY (skill_id) REFERENCES skill(id)
);

CREATE TABLE conversation (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    title VARCHAR(200),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_conv_user FOREIGN KEY (user_id) REFERENCES app_user(id)
);

CREATE TABLE message (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    conversation_id BIGINT NOT NULL,
    role VARCHAR(20) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_msg_conv FOREIGN KEY (conversation_id) REFERENCES conversation(id),
    INDEX idx_msg_conv (conversation_id)
);

CREATE TABLE tool_call (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    message_id BIGINT NOT NULL,
    tool_name VARCHAR(100) NOT NULL,
    arguments JSON,
    result TEXT,
    duration_ms INT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_tool_msg FOREIGN KEY (message_id) REFERENCES message(id)
);
```

### 设计说明

- `task.status` 用字符串枚举：`todo / done / skipped`，不用 0/1/2。
- `task` 加 `(user_id, task_date)` 组合索引，因为最常按用户+日期查。
- `message` 加 `conversation_id` 索引，因为最常按会话查。
- `tool_call` 存 `arguments` 和 `result`，方便排查 Agent 问题。
- 软删除只加在业务表 `task` 上，日志表不删。

---

## 八、练习题

1. 查出某用户本周完成的任务数。
2. 查出每个能力项的平均当前分。
3. 查出最近 10 条工具调用，带工具名和耗时。
4. 查出连续打卡天数（可以先简化）。
5. 查出每个任务类型花的总时间。
6. 给 `task` 表加一个索引，并解释为什么。
7. 写一个事务：完成任务 + 写打卡记录，要么都成功，要么都失败。

---

## 九、面试常问

1. 索引为什么能加速？
2. 什么是最左前缀原则？
3. 索引什么时候失效？
4. 事务的 ACID？
5. 脏读、不可重复读、幻读的区别？
6. INNER JOIN 和 LEFT JOIN 的区别？
7. `WHERE` 和 `HAVING` 的区别？
8. 慢查询怎么排查？
9. 为什么要软删除？
10. 一对多、多对多怎么设计表？

---

## 十、自检

- [ ] 能独立写出建表 SQL？
- [ ] 能解释主键和外键？
- [ ] 能写出带 JOIN 的查询？
- [ ] 能说出索引的利弊？
- [ ] 能解释事务的四个特性？
- [ ] 能为自己项目设计 8 张表？
