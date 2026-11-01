# AI Short Video Creation｜AI短剧创作技能包

从一句创意到剧本、视觉资产、分镜、逐段视频提示词、样片复核、剪辑交回和发布包装。中文工作流优先，也可按用户要求换语言。

**安装一个主技能，相关制作模块随包提供。** 不需要逐个寻找表演、镜头或分镜依赖；按任务阶段读取，避免一次加载全部资料。

本项目是 Agent 的工作方法、提示模板与检查工具，**不是视频生成模型或免费算力服务**。真正的生图、生视频和剪辑由用户已有工具／账号执行；没有连接时仍能获得手动执行材料。不得把提示词完成、任务生成成功和用户审片通过混为一谈。

## 安装

### 在 Codex 中直接安装

把下面这句话发给支持 `skill-installer` 的 Codex：

> 请从 GitHub 仓库 FunSBin/ai-short-video-creation 安装 skills/ai-short-video-creation。这个目录包含完整模块，请完整保留子目录。

如果使用 Codex 自带安装脚本，其参数是：

```text
--repo FunSBin/ai-short-video-creation --path skills/ai-short-video-creation
```

### 克隆后安装（Windows／macOS／Linux）

需要 Python 3.10+ 和 Git；脚本本身仅使用Python标准库。

```bash
git clone https://github.com/FunSBin/ai-short-video-creation.git
cd ai-short-video-creation
python scripts/validate_bundle.py
python scripts/install.py --dry-run
python scripts/install.py
```

默认安装到 `$CODEX_HOME/skills/ai-short-video-creation`；未设置时为 `~/.codex/skills/ai-short-video-creation`。执行后在下一轮对话使用技能；若宿主没有重新发现技能，刷新或重新开启会话。

其他支持目录式SKILL的Agent可手动复制完整 `skills/ai-short-video-creation` 目录，或用 `--dest` 指定该宿主的技能根目录。**不要只复制 SKILL.md**，也不要把 `modules/` 移出去。

已有同名目录时默认拒绝覆盖；明确更新时加 `--force`，旧目录会备份在技能根目录旁的 `skill-backups/`，不混进自动发现目录。只想查看操作用 `--dry-run`。

## 开始创作

```text
使用 $ai-short-video-creation 帮我做一部5集的原创AI短剧。
题材：现代悬疑；每集约90秒；写实横屏；先完成大纲和第一集剧本。
已有材料在……。视频由我手动生成，先不要提交。
```

也可以从中间阶段接手：

```text
使用 $ai-short-video-creation 读取我的源剧本和资产台账，
为第二场设计正反打、人物站位和可提交视频提示词。
保留已通过片段，检查实际引用，不触发生成。
```

仅需封面与文案：

```text
参考现有封面风格，给本次合辑做横竖封面设计和标题正文。
对外集数写第二集，核心冲突是远古封妖；先核对源稿设定。
```

首次项目配置参考[项目设置模板](skills/ai-short-video-creation/templates/project-settings.example.json)。模板不含凭据，生成权限默认 `manual`。媒体执行需要用户真实授权，平台上限与可用模型在执行时核验。

## 包含什么

| 环节 | 随包内容 |
| --- | --- |
| 创意／剧本 | 轻量立项与分集交接；MIT许可的Short-Drama Factory编剧、台账、示例和检查脚本 |
| 资产 | 人物设定、场景覆盖与反打、道具、状态变体、唯一资源库和验收 |
| 分镜 | 世界站位、机位投影、尺度、镜头任务、关键帧与生成段映射 |
| 表演／动作 | 反应时序、对白口型、承重、连续攻防、接触与后果 |
| 视频提示 | 自足首帧、逐拍动作与机位、引用职责、声音和连续性 |
| 平台执行 | 工具发现、参数核验、画布回读、异步结果、生成权限与手动工作流 |
| 选片／剪辑 | 实际媒体复核、版本选定、入出点、音字幕检查与导出交回 |
| 发布 | 横竖封面、局部修图、标题钩子、剧情承诺与发布文案 |

宿主需要具备文件读写能力；图像观察、生图、生视频、音轨试听和剪辑能力按实际工具决定。没有进行的检查必须标明，不能由静态校验替代。详情见[完整流程](docs/workflow.md)与[模块清单和来源](docs/components.md)。

## 开发与检查

```bash
python scripts/validate_bundle.py
python -m unittest discover -s tests -v
```

检查覆盖包内路径、模块名称、内容完整性和私有信息模式，以及安装的冲突处理和备份。它不验证模型生成效果，也不保证播放量、推荐或商业收益。

MIT许可见[LICENSE](LICENSE)。第三方编剧模块保留原作者与MIT许可，见[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。未附再分发许可的外部技能原文、任何商业CLI程序、项目剧本和媒体素材均未打包。
