# mod
创建一个模块存放的位置，供学习使用，大家一起借鉴和给意见

#mysql遇到的坑
- mysql中%s的参数中不要传数字值，会引起mysql warning；
  mysql Warning | 1292 | Truncated incorrect DOUBLE value: '25a3c516a4c15eda917963e48a254'  |
  可能造成的原因：on running a MySQL query, it could be caused by using a numeric value against a CHAR/VARCHAR column.
- executemany使用时，传的参数必须是元祖
- fetchone返回的是dict
- fetchall返回是元祖。所以取值时，需要先fd[0]["information"]