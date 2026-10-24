# 代码阅读：/student/

- URL：`/student/`
  - 来源：`apps/accounts/urls.py` 第 43 行
    `path("student/", views.student_home, name="student_home")`

- 对应函数：`student_home(request)`
  - 位置：`apps/accounts/views.py` 第 64 行

- 函数做了什么：
  1. `@role_required("student")` 检查访问者是不是学生
  2. 算出今天、本周一、下周一的日期
  3. 查询这个学生的任务，筛出今天的任务
  4. 统计待审核数、本周完成数、预计分钟数，放进 `context`

- 用了哪个模板：`student/home.html`
  - 来源：`views.py` 第 111 行
    `return render(request, "student/home.html", context)`
