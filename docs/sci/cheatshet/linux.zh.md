

## 用户管理与用户权限

### 添加用户
```bash
sudo adduser 用户名
```

### 删除用户
```bash
sudo deluser 用户名
```

### 修改用户密码
```bash
sudo passwd 用户名
```

### 查看当前用户
```bash
whoami
```

### 切换用户
```bash
su 用户名
```

### 查看用户信息
```bash
id 用户名
```

### 添加用户到组
```bash
sudo usermod -aG 组名 用户名
```

### 删除用户组
```bash
sudo delgroup 组名
```

### 修改文件权限
```bash
chmod 权限 文件名
```

### 修改文件所有者
```bash
chown 用户名:组名 文件名
```

### 给用户添加超级权限
```bash
sudo usermod -aG sudo 用户名
```