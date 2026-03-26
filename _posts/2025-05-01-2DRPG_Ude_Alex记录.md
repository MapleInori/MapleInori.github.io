---
layout: article
title: 2DRPG_Ude_Alex记录
tags: ["Unity", "游戏开发"]
key: 202505012DRPG_Ude_Alex
aside:
  toc: true
---
### 开发流程大纲

问DS的时候不用反复重开对话，太久远的他会自己忘记，项目太大，还是需要一些关联性的，如果每部分完成就新开对话，可能会有遗漏

## 碰到的问题

### 分层状态机

### 攻击动画对比

如果exit time 0，动画最后设置trigger，可能播放第二遍动画的第一帧，虽然会被打断

如果exit time 1，动画开始设置trigger，一定无法播放第二遍，但是对其他会不会有影响，比如必须等攻击动画完毕才能干其他

### 保存下落攻击时的冲刺预输入，优化下落攻击到冲刺的手感。

#### 限制冲刺

```csharp
        if (Input.GetKeyDown(KeyCode.LeftShift) && dashUsageTimer == 0f)
        {
            // 确定冲刺方向
            dashDir = Input.GetAxisRaw("Horizontal");
            if (dashDir == 0)
                dashDir = faceDir;
            // 当下落攻击时不允许冲刺，落地后才允许冲刺，怎么改都感觉落地后立刻冲刺的操作很僵硬，索性不再限制。
            // 添加预输入处理，优化了点手感，还是限制一下罢，不然看起来太怪了。
            if (isDropAttacking) return;
            // 你就冲吧。————阿杰如是说
            dashUsageTimer = dashCoolDown;
            stateMachine.ChangeState(dashState);
        }
```

下落攻击状态机部分逻辑

```csharp
        if(player.IsGroundDetected())
        {
            // 预输入再切换冲刺
            if(dashPreInput && player.dashUsageTimer ==0f)
            {
                stateMachine.ChangeState(player.dashState);
                return;
            }
            player.anim.SetBool("DropAttackAtGround", true);
            if (triggerCalled)
            {
                stateMachine.ChangeState(player.idleState);
            }
        }
```

状态基类预输入处理

```csharp
        if(Input.GetKeyDown(KeyCode.LeftShift))
        {
            dashPreInput = true;
            player.dashDir = Input.GetAxisRaw("Horizontal");
            if (player.dashDir == 0)
                player.dashDir = player.faceDir;
        }
```

### 在tilemap制作的地面上停下来瞬间会有一个极小的向左的力，导致停下来永远向左，并且在上边移动时也会有极小的向上的速度，在普通2Dsprite上没事

经测试发现，当Composite collider 2d  的 OffsetDistance设置为0（或者极小）时恢复正常。

> deepseek总结：`Offset Distance`通过修改碰撞体形状间接影响物理力的计算。你的问题本质是 **碰撞体形状的微小偏移导致法线方向计算异常** 。保持Offset Distance=0可确保碰撞体与视觉一致，是多数2D平台游戏的推荐设置。若必须使用非零值，需配合细致的碰撞体调试和物理材质优化。

还有一种改法，将FlipController从Update中移动到SetVelocity中，不用刚体的速度判断，而是当对角色设置速度时判断转向，这样就只有玩家控制时转向，而不会滑动时转向。

```csharp
    public void SetVelocity(float _xVelocity, float _yVelocity)
    {
        rb.velocity = new Vector2(_xVelocity, _yVelocity);
        FlipController(_xVelocity);
    }
```

扔剑技能细写逻辑。瞄准，调整角度，扔出去收回来。

存档就是开始的时候该读档的所有位置读取数据，结束或者存档的时候，所以需要保存的位置都保存数据，保存和读取的过程就是将需要保存的数据保存到自定义的存档数据类中GameData，比如保存为Json，需要将各种数据存到GameData类中之后，将该类序列化为Json文件，读档时将这个Json文件反序列化为GameData类，然后所有需要读取数据的地方从GameData类中读取各自的数据，GameData是个可实例化的类，每个存档都可以是一个GameData。大概





## 计划？

搜索TODO修改问题

慎用DontDestroyOnLoad。

加载顺序很容易出问题。

全是玄学，MD

计划扩展：

- [ ] 游戏开发文档

  - [ ] 类似UGUI文档格式
  - [ ] 整体开发流程大纲
  - [ ] 360度抛物线投掷逻辑
  - [ ] SO详解以及示例，自定义物品
  - [ ] 背包系统的逻辑实现，无限格子，鼠标放上去显示物品信息的悬浮窗
  - [ ] 对比唐UGUI的UI逻辑实现，性能对比分析
  - [ ] 存档系统，多个存档如何实现
  - [ ] 技能树逻辑
  - [ ] 中英双语切换
  - [ ] 以下扩展内容文档导航
- [ ] 键位管理

  - [ ] GameKeyboard.cs设置各种键位，其他地方从这里使用方便管理有哪些按键以及修改按键
  - [ ] 设置面板自定义键位
- [ ] 数值表格管理，

  - [ ] 通过excel统一管理所有数值，方便修改和查看，
  - [ ] 通过脚本读取数据并设置数值，
  - [ ] 物品Excel
  - [ ] 打包后隐藏excel数据？
  - [ ] 每个部位十个不同装备，材料二十种。
- [ ] 测试相关

  - [ ] 一键测试填写数据，
  - [ ] 重置默认数据，
  - [ ] 本次数据与上次数据对比，
  - [ ] 差异数据高亮
  - [ ] 日志系统，记录游戏中发生的所有事情以及玩家的行为
- [ ] 某种敌人的状态应该继承Enemystate，构造函数中添加敌人自身的类，节省每次生成构造函数时需要手动添加自身敌人类
- [ ] 技能和操作和功能详细介绍文档
- [ ] 伤害数字显示
- [ ] 新手操作引导
- [ ] 任务剧情：序章
- [ ] 商店
- [ ] AI队友
- [ ] 能否用技能类型直接区分同一技能不同类型的各种信息，只需要传入技能类型即可
- [ ] Editor扩展，简化键位观察和设置
- [ ] 更多的敌人和Boss.
- [ ] 还能扩展啥？



111
