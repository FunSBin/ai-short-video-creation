# 模块与依赖

唯一需要安装的目录是 `skills/ai-short-video-creation/`。其 `SKILL.md` 按相对路径读取内置模块，不依赖另一位用户机器上的技能目录。

| 内置模块 | 用途 | 读取条件 |
| --- | --- | --- |
| ai-short-video-assets | 视觉资产、状态和场景覆盖 | 制作／修复资源图 |
| ai-short-video-storyboard | 分镜、机位和空间 | 写分镜或修复连续性 |
| ai-short-video-seedance | 逐段提示与模板 | 为已定生成段写提示 |
| ai-short-video-combat | 连续攻防与物理接触 | 有战斗／追逐／连续动作 |
| ai-video-performance | 目标、刺激、反应与对白 | 人物表演 |
| ai-video-camera | 镜头任务与空间投影 | 机位设计 |
| ai-video-image-prompts | 图像提示与局部修改 | 需要生图或修图提示 |
| detail-expression-video-prompts | 面部与情绪连续变化 | 细节表演专项 |
| ai-video-provider | 平台适配与权限 | 配置画布、提交或取回媒体 |
| ai-video-finishing | 选片、剪辑和导出 | 已有生成媒体 |
| short-drama-factory | MIT编剧引擎、台账和校验 | 商业结构／长篇／剧本医生等 |
| ai-short-drama-storyboard-pipeline | 多宫格与连续动作导演卡 | 用户确实需要这些扩展产物 |

`references/`含主入口的项目接手、轻量剧本、媒体QA及封面文案规则。`templates/`含不带凭据的设置模板。编剧引擎的参考文件只按模式读取，不整库塞入上下文。

复制来源的相对目录与源文件哈希记录在 [source-manifest.json](source-manifest.json)，不含本地绝对路径。发布安装包的内容哈希在包内 `bundle-manifest.json`。哈希证明内容对应关系，不证明质量、版权所有权或模型能力。
